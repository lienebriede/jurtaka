from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, RequestFactory
from .forms import ContactForm
from .models import Contact


class TestContactForm(TestCase):

    # creates a test user
    def setUp(self):
        self.user = User.objects.create_user(
            username='tuser',
            email='test@test.com', password='p123'
        )

    # tests if valid with a valid user id and no email
    def test_contact_form_valid_with_user(self):

        # mocks an authenticated user
        request = RequestFactory().get('/')
        request.user = self.user

        # defines mock data and request
        form_data = {
            'user': self.user.id,
            'email': '',
            'subject': 'General Inquiry',
            'message': 'This is a test message.',
        }
        # gets contact form with mock data and request
        form = ContactForm(data=form_data, request=request)

        # asserts that form is valid
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    # tests if valid with an email but no user id
    def test_contact_form_valid_with_email(self):
        request = RequestFactory().get('/')
        request.user = self.user

        form_data = {
            'user': '',
            'email': 'test@test.com',
            'subject': 'General Inquiry',
            'message': 'This is a test message.',
        }
        form = ContactForm(data=form_data, request=request)
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    # tests if invalid with an empty content
    def test_contact_form_is_invalid(self):

        request = RequestFactory().get('/')
        request.user = self.user

        form_data = {
            'user': self.user.id,
            'email': '',
            'subject': '',
            'message': '',
        }
        form = ContactForm(data=form_data, request=request)
        self.assertFalse(
            form.is_valid(),
            msg='Form is valid with empty content')

    # tests if invalid with blank space in content
    def test_contact_form_invalid_with_blank_space(self):
        request = RequestFactory().get('/')
        request.user = self.user

        form_data = {
            'user': self.user.id,
            'email': 'test@test.com',
            'subject': 'General Inquiry',
            'message': '   ',
        }
        form = ContactForm(data=form_data, request=request)
        self.assertFalse(
            form.is_valid(),
            msg="Form is valid with only blank spaces in message field"
        )
