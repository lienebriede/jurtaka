from django.test import TestCase
from django.urls import reverse
from .models import About, Contact
from .forms import ContactForm


class TestAboutView(TestCase):

    def setUp(self):
        """
        Sets a state for testing
        """

        self.about_content = About(
            title="About page", 
            content="This is about contact.",
        )
        self.about_content.save()

    def test_render_about_page(self):
        """
        Tests about page
        """

        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200, "Failed to load about page. Expected status code 200, but received {response.status_code}.")
        self.assertIn(b'About page', response.content, "Post title 'Test post' not found in the response content.")
        self.assertIn(b'This is about contact.', response.content, "Post content 'This is test post content' not found in the response content.")

    
class TestContactView(TestCase):

    def test_render_contact_page(self):
        """
        Tests contact page
        """

        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200, "Failed to load about page. Expected status code 200, but received {response.status_code}.")
        self.assertIsInstance(response.context['contact_form'], ContactForm, "Contact form is not correctly initialized.")
