from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.admin.views.decorators import staff_member_required
from .models import Post, Comment
from .forms import CommentForm, PostForm

def post_list(request):
    """
    View to display all the posts (latest first)
    """
    queryset = Post.objects.filter(status=1).order_by('-created_on')

    # Adds comment count to each post
    for post in queryset:
        post.comment_count = post.comments.count()

        
    paginator = Paginator(queryset, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    is_paginated = page_obj.has_other_pages()

    context = {
        'posts': queryset,
        'page_obj': page_obj,
        'posts': page_obj.object_list,
        'is_paginated': is_paginated,
    }

    return render(request, "main_forum/index.html", context)

def post_detail(request, slug):
    """
    View to display an individual post
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.count()
    
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

    return render(
        request,
        "main_forum/post_detail.html",
        {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
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
    print(f"Post slug: {post.slug}")
    
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
        post.original_post_content = post.post_content
        post.status = 1
        post.save()
        messages.add_message(request, messages.SUCCESS, f'Your updated post "{post.title}" is approved!')

    return render(
        request, 
        "main_forum/approve_posts.html",
        {
            'pending_posts': pending_posts
        },
    )