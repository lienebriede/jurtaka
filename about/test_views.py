from django.contrib.auth.models import User
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


    def setUp(self):
        """
        Sets a state for testing
        """

        # creates a superuser
        self.user = User.objects.create_superuser(
            username="tusername",
            password="tuserpass",
        )


    def test_successful_contact_submission(self):
        """
        Tests for submitting a contact form
        """

        post_data = {
            'email': 'test@test.com',
            'subject': 'General Inquiry',
            'message': 'This is a test message for inquiry.'
        }

        # use follow=True to ensure test client follows redirect after submission
        response = self.client.post(reverse('contact'), post_data, follow=True)

        self.assertEqual(response.status_code, 200, "Failed to load home page after contact submission.")

        # tests if created in the database
        self.assertTrue(Contact.objects.filter(email='test@test.com', subject='General Inquiry', message='This is a test message for inquiry.').exists(),
                        "Contact object not created in the database.")

        # tests the success message
        success_message = "Thanks for your inquiry! We will get back to you shortly."
        self.assertContains(response, success_message, msg_prefix="Expected success message not found.")


    
    def test_successful_contact_submission_registered_user(self):
        """
        Tests for submitting a contact form by a registered user
        """
        # ensures that user is logged in
        login_successful = self.client.login(username='tusername', password='tuserpass')
        self.assertTrue(login_successful, "User login failed.")

        post_data = {
            'user': self.user.pk,
            'subject': 'Give Feedback',
            'message': 'I want to give feedback'
        }

        response = self.client.post(reverse('contact'), post_data, follow=True)

        # Check if the Contact object is created in the database
        contact_exists = Contact.objects.filter(user=self.user, subject='Give Feedback', message='I want to give feedback').exists()
        self.assertTrue(contact_exists, "Contact object not created in the database.")
        
        self.assertEqual(response.status_code, 200, "Failed to load home page after contact submission.")

        # Check for the success message
        success_message = "Thanks for your inquiry! We will get back to you shortly."
        self.assertContains(response, success_message, msg_prefix="Expected success message not found.")