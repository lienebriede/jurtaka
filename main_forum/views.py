from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def post_list(request):
    """
    Display all the posts
    """
    queryset = Post.objects.all()
    context = {
        'posts': queryset
    }

    return render(request, "main_forum/index.html", context)
