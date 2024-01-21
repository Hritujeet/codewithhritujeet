from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    concern = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)