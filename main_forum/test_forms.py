from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    # tests if its valid with a non-empty content
    def test_comment_form_is_valid(self):
        comment_form = CommentForm({'comment_content': 'This is a test comment'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

    # tests if its invalid with an empty content
    def test_comment_form_is_invalid(self):
        comment_form = CommentForm({'comment_content': ''})
        self.assertFalse(comment_form.is_valid(), msg='Form is valid with empty string')

    # tests if the form has comment_content field
    def test_comment_form_has_fields(self):
        form = CommentForm()
        self.assertIn('comment_content', form.fields, msg="Form should have a content field")

    # tests if the form is invalid with blank space in content
    def test_comment_form_invalid_with_blank_space(self):
        comment_form = CommentForm({'comment_content': '   '})
        self.assertFalse(comment_form.is_valid(), msg='Form is valid with only blank spaces in content field')

    # tests if label is an empty string
    def test_comment_form_labels(self):
        form = CommentForm()
        self.assertEqual(form.fields['comment_content'].label, '', msg="Label for content should be an empty string")

    # tests if there is a placeholder text
    def test_comment_form_placeholder(self):
        form = CommentForm()
        self.assertEqual(form.fields['comment_content'].widget.attrs['placeholder'], 'Add a comment')
        rendered_form = form.as_p()
        self.assertIn('placeholder="Add a comment"', rendered_form, msg='Placeholder "Add a comment" not found')

    # tests if valid with content max 10 000 characters
    def test_comment_form_valid_with_max_length(self):
        valid_content = 'a' * 10000
        form_data = {'comment_content': valid_content}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid(), msg='Form is not valid with content at max length')

    # tests if invalid with content exceeding 10 000 characters
    def test_comment_form_invalid_with_max_length(self):
        exceeding_content = 'a' * 11000
        form_data = {'comment_content': exceeding_content}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid(), msg='Form is valid with exceeding content')