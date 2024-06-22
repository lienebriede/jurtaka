from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['user', 'email', 'message']
        widgets = {
            'user': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'email': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'message': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'height: 200px;',
            }),
        }
        labels = {
            'user': 'Your username:',
            'email': 'Your e-mail:',
            'message': 'Write your message here:',
        }
