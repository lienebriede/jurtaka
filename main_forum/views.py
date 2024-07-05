from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q, Count
from django.utils.html import mark_safe, strip_tags
import re
from .models import Post, Comment, Like, Category
from .forms import CommentForm, PostForm


def search_results(request):
    """
    Display posts filtered by search query
    """
    query = request.GET.get('q')
    if query:
        queryset = Post.objects.filter(
            Q(title__icontains=query) | Q(post_content__icontains=query),
            status=1
        ).annotate(comment_count=Count('comments')).order_by('-created_on')

        # Highlights, case insensitive
        for post in queryset:
            highlighted_title = mark_safe(re.sub(
                re.escape(query),
                f'<span class="highlight">{query}</span>',
                post.title, flags=re.IGNORECASE))
            highlighted_content = mark_safe(re.sub(
                re.escape(query),
                f'<span class="highlight">{query}</span>',
                post.post_content, flags=re.IGNORECASE))

            post.highlighted_title = highlighted_title
            post.highlighted_content = highlighted_content
            post.sanitized_title = strip_tags(post.title)

    else:
        queryset = Post.objects.none()

    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.has_other_pages()

    context = {
        'query': query,
        'page_obj': page_obj,
        'posts': page_obj.object_list,
        'is_paginated': is_paginated,
    }

    return render(request, "main_forum/search_results.html", context)


def post_list(request):
    """
    View to display either latest, top posts or posts by category
    Displays latest first by default
    """

    view_type = request.GET.get('view_type', 'latest')
    category_id = request.GET.get('category')

    queryset = Post.objects.filter(status=1)

    if category_id:
        queryset = Post.objects.filter(categories__id=category_id, status=1).annotate(
            comment_count=Count('comments'))
        view_type = None

    if view_type == 'latest':
        queryset = Post.objects.filter(status=1).annotate(
            comment_count=Count('comments')).order_by('-created_on')

    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.has_other_pages()

    categories = Category.objects.all()

    context = {
        'page_obj': page_obj,
        'posts': page_obj.object_list,
        'is_paginated': is_paginated,
        'view_type': view_type,
        'current_category': category_id,
    }

    return render(request, "main_forum/index.html", context)


def post_detail(request, slug):
    """
    View to display an individual post
    """
    queryset = Post.objects.filter(slug=slug, status__in=[1, 3])
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.count()
    likers = post.likes.all()

    # brings backt to last visited site
    referer = request.META.get('HTTP_REFERER', None)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(
                request,
                "Thanks for commenting!"
            )

            comment_count = post.comments.count()
            return redirect('post_detail', slug=slug)
    else:
        comment_form = CommentForm()

    is_liked = False

    if request.user.is_authenticated:
        is_liked = Like.objects.filter(post=post, user=request.user).exists()

    return render(
        request,
        "main_forum/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "is_liked": is_liked,
            "likers": likers,
            "referer": referer,
        },
    )


def post_create(request):
    """
    View to display a form for creating posts
    """
    post_form = PostForm()

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            post_form.save_m2m()
            messages.success(
                request,
                "Thanks for posting! Your post will be visible shortly."
            )
            return redirect('home')
        else:
            print(post_form.errors)
            messages.add_message(request,
                                 messages.ERROR,
                                 'There was an error uploading your post!')
    else:
        post_form = PostForm()

    return render(
        request,
        "main_forum/post_create.html",
        {
            'post_form': post_form,
        },
    )


def post_edit(request, slug, post_id):
    """
    View to edit posts
    """
    post = get_object_or_404(Post, slug=slug, id=post_id)

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES, instance=post)

        if post_form.is_valid() and post.author == request.user:
            post = post_form.save(commit=False)
            post.status = 3
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your post update is awaiting approval!')
            return redirect('post_detail', slug=post.slug)
        else:
            messages.add_message(
                request, messages.ERROR,
                'There was an error updating your post!')
    else:
        post_form = PostForm(instance=post)

    return render(
        request,
        "main_forum/edit_post.html",
        {
            'post_form': post_form,
            'post': post
        },
    )


@staff_member_required
def approve_posts(request):
    """
    View to approve edited posts
    """
    pending_posts = Post.objects.filter(status=3)

    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)

        # Updates original post content with the edited content
        post.status = 1
        post.has_been_edited = True
        post.save()

    return render(
        request,
        "main_forum/approve_posts.html",
        {
            'pending_posts': pending_posts
        },
    )


def post_delete(request, slug, post_id):
    """
    View to " soft delete" posts
    """
    post = get_object_or_404(Post, slug=slug, id=post_id)

    if request.method == "POST" and post.author == request.user:
        post.status = 2
        post.save()
        messages.success(request, 'Your post has been deleted successfully!')
        return redirect('home')

    else:
        return redirect('post_detail', slug=post.slug)


def like_post(request, slug):
    if request.method == 'POST':
        post = get_object_or_404(Post, slug=slug)

        if Like.objects.filter(user=request.user, post=post).exists():
            Like.objects.filter(user=request.user, post=post).delete()
        else:
            Like.objects.create(user=request.user, post=post)

        return redirect('post_detail', slug=slug)
    else:
        return HttpResponse('Method not allowed', status=405)
