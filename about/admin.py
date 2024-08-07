from django.contrib import admin
from .models import About, Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    list_display = ('user', 'email', 'subject', 'created_on', 'status')
    list_filter = ('status', 'subject', 'created_on',)
    search_fields = ('user__username', 'message')
