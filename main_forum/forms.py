from .models import Comment
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