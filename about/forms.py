from django import forms
from django.contrib.auth.models import User
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['user', 'email', 'message']
        widgets = {
            'user': forms.HiddenInput(),
            'email': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'message': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'height: 200px;',
            }),
        }
        labels = {
            'email': 'Your e-mail:',
            'message': 'Write your message here:',
        }

    # checks if the user is authenticated, sets the users pk
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ContactForm, self).__init__(*args, **kwargs)

        if self.request and self.request.user.is_authenticated:
            self.fields['user'].initial = self.request.user.pk
            self.fields['user'].widget = forms.HiddenInput()
            self.fields['email'].required = False

    # validates the user field and raises error if not valid
    def clean_user(self):
        user = self.cleaned_data.get('user')
        if user and not isinstance(user, User):
            raise forms.ValidationError("Invalid user.")
        return user

    # raises validation error if email field empty for non-authenticated users
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not self.request.user.is_authenticated and not email:
            raise forms.ValidationError("Please provide your e-mail or log in!")
        return email