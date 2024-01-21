from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=600)
    img = models.ImageField(upload_to='blog/images', default="")
    author = models.CharField(max_length=300)
    content = models.TextField()
    views = models.IntegerField()
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Post {self.title}"

class Comment(models.Model):
    user = models.CharField(max_length=500)
    content = models.TextField()
    post_id = models.IntegerField()
    comment_id = models.IntegerField(null=True)
    timestamp = models.DateField(auto_now_add=True)
