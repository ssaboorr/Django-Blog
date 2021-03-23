from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    timestamp = models.TimeField(auto_now_add=True)
