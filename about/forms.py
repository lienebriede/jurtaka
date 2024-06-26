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
            'email': 'Your e-mail (optional):',
            'message': 'Write your message here:',
        }

    # checks if the user is authenticated, sets the users pk
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ContactForm, self).__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields['user'].initial = user

    # validates the user field and raises error if not valid
    def clean_user(self):
        user = self.cleaned_data.get('user')
        if user and not isinstance(user, User):
            raise forms.ValidationError("Invalid user.")
        return user