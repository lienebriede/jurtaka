from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import PostForm, CommentForm
from .models import Category, Post
from django.contrib.auth.models import User
import tempfile


class TestPostForm(TestCase):
    """
    Tests for Post form
    """

    # creates a test user
    def setUp(self):
        self.user = User.objects.create_user(username='tuser', email='test@test.com', password='p123')
        self.category1 = Category.objects.create(name='Category 1')
        self.category2 = Category.objects.create(name='Category 2')
        self.category3 = Category.objects.create(name='Category 3')

    # tests if has fields
    def test_post_form_has_fields(self):
        form = PostForm()
        expected_fields = ['title', 'post_content', 'categories', 'image1', 'image2']
        actual_fields = list(form.fields.keys())
        
        self.assertListEqual(expected_fields, actual_fields, msg="Form does not have the expected fields")

    # tests if valid with a non-empty content
    def test_post_form_is_valid(self):
        form_data = {
            'title': 'Test Post',
            'post_content': 'This is a test post.',
            'categories': [self.category1.id, self.category2.id, self.category3.id],
            'image1': None,
            'image2': None,
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid(), msg='Form is not valid')

    # tests if invalid with no title
    def test_post_form_is_invalid_no_title(self):
        form_data = {
            'title': '',
            'post_content': 'This is a test post.',
            'categories': [self.category1.id],
            'image1': None,
            'image2': None,
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid(), msg='Form is valid without title')

    # tests if invalid with no content
    def test_post_form_is_invalid_no_content(self):
        form_data = {
            'title': 'Test Post',
            'post_content': '',
            'categories': [self.category1.id],
            'image1': None,
            'image2': None,
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid(), msg='Form is valid without content')

    # tests if invalid with no categories
    def test_post_form_is_invalid_no_categories(self):
        form_data = {
            'title': 'Test Post',
            'post_content': 'This is a test post.',
            'categories': [],
            'image1': None,
            'image2': None,
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid(), msg='Form is valid without categories')

    # tests if invalid with invalid category id
    def test_post_form_is_invalid_with_invalid_category(self):
        form_data = {
            'title': 'Test Post',
            'post_content': 'This is a test post.',
            'categories': [10],
            'image1': None,
            'image2': None,
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid(), msg='Form is valid with invalid category')

    # tests if invalid with blank space in title
    def test_post_form_invalid_with_blank_space_title(self):
        form_data = {
            'title': '   ',
            'post_content': 'This is a test post.',
            'categories': [self.category1.id],
            'image1': None,
            'image2': None,
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid(), msg='Form is valid with only blank spaces in title')

    # tests if invalid with blank space in content
    def test_post_form_invalid_with_blank_space_content(self):
        form_data = {
            'title': 'Test Post',
            'post_content': '   ',
            'categories': [self.category1.id],
            'image1': None,
            'image2': None,
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid(), msg='Form is valid with only blank spaces in content')

    # tests if valid with one uploaded image
    def test_post_form_is_valid_with_one_image(self):

        # creates a temporary file to simulate image
        with tempfile.NamedTemporaryFile(suffix='.jpg') as img1:
            img1.write(b'\x00' * 1024)
            img1.seek(0)
            
            form_data = {
                'title': 'Test Post',
                'post_content': 'This is a test post.',
                'categories': [self.category1.id, self.category2.id],
            }
            
            # creates a file like object for testing uploads
            form_files = {
                'image1': SimpleUploadedFile(img1.name, img1.read(), content_type='image/jpeg'),
            }

            form = PostForm(data=form_data, files=form_files)
            self.assertTrue(form.is_valid(), msg='Form is not valid with one image')

    # tests if valid with two uploaded images
    def test_post_form_is_valid_with_two_images(self):
        with tempfile.NamedTemporaryFile(suffix='.jpg') as img1, tempfile.NamedTemporaryFile(suffix='.jpg') as img2:
            img1.write(b'\x00' * 1024)
            img1.seek(0)
            img2.write(b'\x00' * 1024)
            img2.seek(0)
            
            form_data = {
                'title': 'Test Post',
                'post_content': 'This is a test post.',
                'categories': [self.category1.id, self.category2.id],
            }
            form_files = {
                'image1': SimpleUploadedFile(img1.name, img1.read(), content_type='image/jpeg'),
                'image2': SimpleUploadedFile(img2.name, img2.read(), content_type='image/jpeg'),
            }
            form = PostForm(data=form_data, files=form_files)
            self.assertTrue(form.is_valid(), msg='Form is not valid with valid images')
    
    # tests if valid with no uploaded images
    def test_post_form_valid_with_no_images(self):
        form_data = {
            'title': 'Test Post',
            'post_content': 'This is a test post.',
            'categories': [self.category1.id],
            'image1': None,
            'image2': None,
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid(), msg='Form is not valid without images')

    # tests if has a placeholder for the title
    def test_post_form_title_placeholder(self):
        form = PostForm()
        self.assertEqual(form.fields['title'].widget.attrs['placeholder'], 'Add a title', msg='Title placeholder not found')

    # tests if has a placeholder for the post content
    def test_post_form_content_placeholder(self):
        form = PostForm()
        self.assertEqual(form.fields['post_content'].widget.attrs['placeholder'], 'Add text', msg='Post content placeholder not found')

    # tests if the title field has no label
    def test_post_form_title_no_label(self):
        form = PostForm()
        self.assertEqual(form.fields['title'].label, '', msg='Title field should have no label')

    # tests if the post content field has no label
    def test_post_form_content_no_label(self):
        form = PostForm()
        self.assertEqual(form.fields['post_content'].label, '', msg='Post content field should have no label')

    # tests if the categories field has a label
    def test_post_form_categories_label(self):
        form = PostForm()
        self.assertEqual(form.fields['categories'].label, 'Categories', msg='Categories field should have a label')

    # tests if the image1 field has a label
    def test_post_form_image1_label(self):
        form = PostForm()
        self.assertEqual(form.fields['image1'].label, 'Image', msg='Image1 field should have a label')

    # tests if the image2 field has a label
    def test_post_form_image2_label(self):
        form = PostForm()
        self.assertEqual(form.fields['image2'].label, 'Image', msg='Image2 field should have a label')

    # tests if valid with content max 10 000 characters
    def test_post_form_valid_with_max_length(self):
        max_length_content = 'a' * 10000
        form_data = {
            'title': 'Test Post',
            'post_content': max_length_content,
            'categories': [self.category1.id, self.category2.id],
            'image1': None,
            'image2': None,
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid(), msg='Form is not valid with content at max length')

    # tests if invalid with content exceeding 10 000 characters
    def test_post_form_invalid_with_max_length(self):
        exceeding_content = 'a' * 11000
        form_data = {
            'title': 'Test Post',
            'post_content': exceeding_content,
            'categories': [self.category1.id, self.category2.id],
            'image1': None,
            'image2': None,
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid(), msg='Form is valid with exceeding content')


class TestCommentForm(TestCase):
    """
    Tests for Comment form
    """

    # tests if valid with a non-empty content
    def test_comment_form_is_valid(self):
        comment_form = CommentForm({'comment_content': 'This is a test comment'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

    # tests if invalid with an empty content
    def test_comment_form_is_invalid(self):
        comment_form = CommentForm({'comment_content': ''})
        self.assertFalse(comment_form.is_valid(), msg='Form is valid with empty string')

    # tests if has comment_content field
    def test_comment_form_has_fields(self):
        form = CommentForm()
        self.assertIn('comment_content', form.fields, msg="Form should have a content field")

    # tests if is invalid with blank space in content
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