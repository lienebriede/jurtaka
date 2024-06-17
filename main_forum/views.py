from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    """
    Display all the posts (latest first)
    """
    queryset = Post.objects.all().order_by('-created_on')

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
