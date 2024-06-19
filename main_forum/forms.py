from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content',)
        widgets = {
            'comment_content': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Add a comment',
                'style': 'height: 80px;',
            }),
        }
        labels = {
            'comment_content': '',
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_content')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Add a title',
            }),
            'post_content': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Add text',
                'style': 'height: 200px;',
            }),
        }
        labels = {
            'title': '',
            'post_content': '',
        }

