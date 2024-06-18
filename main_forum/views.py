from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment
from django.core.paginator import Paginator

def post_list(request):
    """
    Display all the posts (latest first)
    """
    queryset = Post.objects.all().order_by('-created_on')

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
    Display an individual post
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.count()

    return render(
        request,
        "main_forum/post_detail.html",
        {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        },
    )
