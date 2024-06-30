from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    # tests if its valid with a non-empty content
    def test_form_is_valid(self):
        comment_form = CommentForm({'comment_content': 'This is a test comment'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

    # tests if its invalid with an empty content
    def test_form_is_invalid(self):
        comment_form = CommentForm({'comment_content': ''})
        self.assertTrue(comment_form.is_valid(), msg='Form is valid')