from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from django.utils.text import slugify
from .forms import CommentForm, PostForm
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
            status=1,
            slug=slugify("Test post"),
            )
        self.post.save()

        # creates a another test post
        self.post2 = Post(
            title="Second test post", 
            author=self.user,
            post_content="This is the second test post content", 
            status=1,
            slug=slugify("Second test post"),
            )
        self.post2.save()

        # adds category for testing
        self.post2.categories.add(self.category1)

        # creates test comments for the test post
        self.comment1 = Comment(
            author=self.user,
            post=self.post,
            comment_content="Test comment 1",
        )
        self.comment1.save()

        self.comment2 = Comment(
            author=self.user,
            post=self.post,
            comment_content="Test comment 2",
        )
        self.comment2.save()

        # creates a like for the test post
        self.like = Like(
            user=self.user,
            post=self.post
        )
        self.like.save()


    def test_render_post_detail_page(self):
        """
        Tests post detail page
        """

        # genrates a url
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        
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
        self.assertEqual(self.post.comments.count(),2, "Comment count not rendered properly.")
        
        # checks if add comment form is present
        self.assertIn('comment_form', response.context, "Add comment form is missing from the response context.")
        
        # checks if user has liked
        self.assertIn('is_liked', response.context, "Like status indicator 'is_liked' is missing from the response context.")
        
        # retrieves likers count
        likers_count = self.post.likes.count()
        
        # checks likes count
        self.assertEqual(self.post.likes.count(),1, "Like count not rendered properly.")

        # retrieves likers
        if likers_count > 0:
            likers_present = False

            # checks for likers username
            for like in self.post.likes.all():
                if like.user.username in response.content.decode('utf-8'):
                    likers_present = True
                    break
            self.assertTrue(likers_present, "Likers were not found in the response")


    def test_render_post_list_latest_view(self):
        """
        Tests 'Latest' page
        """

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200, "Failed to load post list page. Expected status code 200, but received {response.status_code}.")
        
        # Converts to string representation and compares to list in context
        expected_posts = [
            str(self.post2),
            str(self.post),
        ]
        actual_posts = [str(post) for post in response.context['posts']]
        self.assertEqual(actual_posts, expected_posts, f"Expected posts {expected_posts}, but got {actual_posts}")
    

    def test_render_post_list_category_filter(self):
        """
        Tests 'Browse by category1' page
        """

        # retrieves from setUp()
        category_id = self.category1.id
        response = self.client.get(reverse('home') + f'?category={category_id}')
        self.assertEqual(response.status_code, 200, "Failed to load browse by category1 page. Expected status code 200, but received {response.status_code}.")

        # checks if post matches the category
        expected_posts = [
            str(self.post2),
        ]
        actual_posts = [str(post) for post in response.context['posts']]
        self.assertEqual(actual_posts, expected_posts, f"Expected posts {expected_posts}, but got {actual_posts}")


    def test_render_post_create_view(self):
        """
        Tests 'New Post' page
        """

        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200, "Failed to load add post page. Expected status code 200, but received {response.status_code}.")
        self.assertIsInstance(response.context['post_form'], PostForm, "Post form is not correctly initialized.")


    def test_render_post_edit_view(self):
        """
        Tests 'Edit Post' page
        """

        response = self.client.get(reverse('post_edit', args=[self.post.slug, self.post.id]))
        self.assertEqual(response.status_code, 200, "Failed to load edit post page. Expected status code 200, but received {response.status_code}.")
        self.assertIsInstance(response.context['post_form'], PostForm, "Post form is not correctly initialized.")