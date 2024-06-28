from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title


class Contact(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Replied', 'Replied'),
        ('Closed', 'Closed'),
    )

    SUBJECT_CHOICES = (
    ('General Inquiry', 'General Inquiry'),
    ('Technical Issue', 'Technical Issue'),
    ('Give Feedback', 'Give Feedback'),
)
    # allows both registered and unregistered users to fill in the form
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
        )
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='General Inquiry')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    
    def __str__(self):
        if self.user:
            return f"Message from {self.user.username}"
        else:
            return f"Message from {self.email}"
