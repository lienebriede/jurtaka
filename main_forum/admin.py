from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Like, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'slug',
        'author',
        'image_preview1',
        'image_preview2',
        'status',
        'updated_on',
        )
    search_fields = ['title', 'post_content']
    list_filter = ('status', 'categories',)
    summernote_fields = ('post_content',)
    filter_horizontal = ('categories',)

    # Displays a small image in the admin panel if there is one
    def image_preview1(self, obj):
        if obj.image1:
            return format_html(
                '<img src="{}" width="50" height="50" />',
                obj.image1.url)
        else:
            return format_html('<p>No Image</p>')

    image_preview1.short_description = 'Image1'

    def image_preview2(self, obj):
        if obj.image2:
            return format_html(
                '<img src="{}" width="50" height="50" />',
                obj.image2.url)
        else:
            return format_html('<p>No Image</p>')

    image_preview2.short_description = 'Image2'


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('author', 'post', 'created_on',)


admin.site.register(Like)
admin.site.register(Category)
