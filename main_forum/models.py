from django.db import models
from django.contrib.auth.models import User

# Variable for post status
STATUS = ((0, "Pending"), (1, "Approved"), (2, "Deleted") )

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
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class Like(models.Model):
    """
    Model for likes
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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

