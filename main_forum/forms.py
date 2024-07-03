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

    # Sets the max length of a comment text
    def clean_comment_content(self):
        comment_content = self.cleaned_data['comment_content']
        max_length = 10000

        if len(comment_content) > max_length:
            raise forms.ValidationError(
                f'Sorry, your comment is too long.'
                'Comments cannot exceed {max_length} characters.'
                )

        return comment_content


class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'custom-checkbox'}),
        required=True,
        label='Categories',
        error_messages={'required': 'Please select at least one category.'}
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

    # Sets the max length of a post text
    def clean_post_content(self):
        post_content = self.cleaned_data['post_content']
        max_length = 10000

        if len(post_content) > max_length:
            raise forms.ValidationError(
                f'Sorry, your post is too long.'
                'Posts cannot exceed {max_length} characters.'
            )

        return post_content
