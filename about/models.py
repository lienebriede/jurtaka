from django.db import models
from django.contrib.auth.models import User

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title


class Contact(models.Model):
    # allows both registered and unregistered users to fill in the form
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
        )
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)