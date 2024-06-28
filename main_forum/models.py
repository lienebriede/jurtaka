from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Variable for post status
STATUS = ((0, "Pending"), (1, "Approved"), (2, "Deleted"), (3, "Update Pending"))

class Category(models.Model):
    """
    Model for categories
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    Model for posts
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
        )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    post_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    has_been_edited = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name='posts')
    image1 = CloudinaryField('image', blank=True, null=True)
    image2 = CloudinaryField('image', blank=True, null=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # returns only two first lines of post text
    def get_content_preview(self):
        words = self.post_content.split()  
        first_20_words = words[:20]  
        return ' '.join(first_20_words)

    # generates a slug automatically (needed when users add a post )
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Like(models.Model):
    """
    Model for likes
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # user can like one post only once
    class Meta:
        unique_together = ('post', 'user')
    
    def __str__(self):
        return f"Like  by '{self.user}' on '{self.post}'"
        

class Comment(models.Model):
    """
    Model for comments
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"

