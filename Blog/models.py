from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    watch_count = models.IntegerField(default=0)
    publication_date = models.DateTimeField(auto_now_add=True)
