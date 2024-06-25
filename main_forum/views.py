from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q, Count
from django.utils.html import mark_safe
import re
from .models import Post, Comment, Like
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
            post.title = mark_safe(re.sub(re.escape(query), f'<span class="highlight">{query}</span>', post.title, flags=re.IGNORECASE))
            post.post_content = mark_safe(re.sub(re.escape(query), f'<span class="highlight">{query}</span>', post.post_content, flags=re.IGNORECASE))

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
    View to display either latest or top posts
    based on view_type.
    Displays latest first by default
    """

    view_type = request.GET.get('view_type', 'latest')

    if view_type == 'latest':
        queryset = Post.objects.filter(status=1).annotate(
            comment_count=Count('comments')).order_by('-created_on')
    elif view_type == 'top': 
        queryset = Post.objects.filter(status=1).annotate(
            comment_count=Count('comments'), 
            popularity=Count('likes') + Count('comments')
        ).order_by('-popularity', '-created_on')
    else:
        queryset = Post.objects.filter(status=1).annotate(
            comment_count=Count('comments')).order_by('-created_on')

    paginator = Paginator(queryset, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.has_other_pages()

    context = {
        'page_obj': page_obj,
        'posts': page_obj.object_list,
        'is_paginated': is_paginated,
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

    comment_form = CommentForm()

    is_liked = False

    if request.user.is_authenticated:
        is_liked = Like.objects.filter(post=post, user=request.user).exists()

        if 'like' in request.POST:
            if is_liked:
                post.likes.filter(user=request.user).delete()
                is_liked = False
            else:
                Like.objects.create(post=post, user=request.user)
                is_liked = True

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
        },
    )


def post_create(request):
    """
    View to display a form for creating posts
    """
    post_form = PostForm() 

    if request.method == "POST":
        post_form = PostForm(request.POST)
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
        post_form = PostForm(request.POST, instance=post)

        if post_form.is_valid() and post.author == request.user:
            post = post_form.save(commit=False)
            post.status = 3
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Your post update is awaiting approval!')
            return redirect('post_detail', slug=post.slug)
        else:
            messages.add_message(request, messages.ERROR, 'There was an error updating your post!')
    
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
    View to delete posts
    """
    post = get_object_or_404(Post, slug=slug, id=post_id)
    
    if request.method == "POST" and post.author == request.user:
        post.delete()
        messages.success(request, 'Your post has been deleted successfully!')
        return redirect('home')
    
    return redirect('post_detail', slug=post.slug)


