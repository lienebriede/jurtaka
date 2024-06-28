from .models import Comment, Post, Category
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
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Categories'
    )
    
    class Meta:
        model = Post
        fields = ('title', 'post_content', 'categories', 'image1', 'image2')
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

