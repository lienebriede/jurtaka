from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from django.utils.text import slugify
from .forms import CommentForm
from .models import Post, Comment, Category, Like

class PostViews(TestCase):


    def setUp(self):
        """
        Sets a state for testing
        """

        # creates a superuser
        self.user = User.objects.create_superuser(
            username="tusername",
            password="tuserpass",
            email="test@test.com"
        )

        # creates categories for testing
        self.category1 = Category(name='Category 1')
        self.category1.save()

        self.category2 = Category(name='Category 2')
        self.category2.save()

        self.category3 = Category(name='Category 3')
        self.category3.save()

        # creates a test post
        self.post = Post(
            title="Test post", 
            author=self.user,
            post_content="This is test post content", 
            status=1
            )
        
        self.post.slug = slugify(self.post.title)
        self.post.save()

        # creates test comments for the test post
        self.comment1 = Comment(
            author=self.user,
            post=self.post,
            comment_content="Test comment 1"
        )
        self.comment1.save()

        self.comment2 = Comment(
            author=self.user,
            post=self.post,
            comment_content="Test comment 2"
        )
        self.comment2.save()

        # creates a like for the test post
        self.like = Like(
            user=self.user,
            post=self.post
        )
        self.like.save()

        # creates test images
        self.post.image1 = 'http://example.com/image1.jpg'
        self.post.image2 = 'http://example.com/image2.jpg'
        self.post.save()


    def test_render_post_detail_page_authenticated(self):
        """
        Renders post detail page for authenticated users
        """

        # simulates authenticated user
        self.client.force_login(self.user)

        # generates a URL  based on a slug which is automatically generated using slugify
        url = reverse('post_detail', args=[self.post.slug])
        response = self.client.get(url)
        
        # checks for a succesful request
        self.assertEqual(response.status_code, 200, "Failed to load post detail page. Expected status code 200, but received {response.status_code}.")

        # checks post title and content
        self.assertIn(b"Test post", response.content, "Post title 'Test post' not found in the response content.")
        self.assertIn(b"This is test post content", response.content, "Post content 'This is test post content' not found in the response content.")
        
        # checks if the comment form is correctly initialized
        self.assertIsInstance(response.context['comment_form'], CommentForm, "Comment form is not correctly initialized.")
        
        # checks comments
        self.assertIn(b"Test comment 1", response.content, "Comment 'Test comment 1' not found in the response content.")
        self.assertIn(b"Test comment 2", response.content, "Comment 'Test comment 2' not found in the response content.")
        
        # checks for the post author
        self.assertContains(response, self.user.username, msg_prefix="Post author not found in the response content.")

        # checks comment authors
        for comment in self.post.comments.all():
            self.assertContains(response, comment.author.username, msg_prefix="Comment author not found in the response content.")

        # checks comment count
        self.assertIn(f"{self.post.comments.count()} comments".encode(), response.content, "Comment count not rendered properly.")

        # checks likes count
        self.assertIn(f"{likers_count} likes".encode(), response.content, "Like count not rendered properly.")

        # checks if add comment form is present
        self.assertIn('comment_form', response.context, "Add comment form is missing from the response context.")
        
        # checks if user has liked
        self.assertIn('is_liked', response.context, "Like status indicator 'is_liked' is missing from the response context.")
        
        # retrieves likers count
        likers_count = self.post.likes.count()

        # retrieves likers
        if likers_count > 0:
            likers_present = False

            # checks for likers username
            for like in self.post.likes.all():
                if like.user.username in response.content.decode('utf-8'):
                    likers_present = True
                    break
            self.assertTrue(likers_present, "Likers were not found in the response")

        # checks images
        if self.post.image1:
            self.assertIn(self.post.image1.encode(), response.content, "First image not found in the response content.")
        if self.post.image2:
            self.assertIn(self.post.image2.encode(), response.content, "Second image not found in the response content.")

        # checks edit and delete btn
        self.assertIn(b"Edit Post", response.content, "Edit post button not found in the response content.")
        self.assertIn(b"Delete Post", response.content, "Delete post button not found in the response content.")