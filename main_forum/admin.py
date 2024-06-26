from django.contrib import admin
from .models import Post, Like, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'id', 'slug', 'author', 'status', 'updated_on',)
    search_fields = ['title', 'post_content']
    list_filter = ('status', 'categories',)
    summernote_fields = ('post_content',)
    filter_horizontal = ('categories',)

admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Category)