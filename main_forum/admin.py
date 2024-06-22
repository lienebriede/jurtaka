from django.contrib import admin
from .models import Post, Like, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'updated_on',)
    search_fields = ['title', 'post_content']
    list_filter = ('status', 'created_on',)
    summernote_fields = ('post_content',)


admin.site.register(Like)
admin.site.register(Comment)