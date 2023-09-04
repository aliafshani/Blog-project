import django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class category(models.Model):
    title=models.CharField(max_length=30)
    crerated=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class post_blog(models.Model):
    author=models.ForeignKey(User , on_delete=models.CASCADE)
    category=models.ManyToManyField(category)
    title=models.CharField(max_length=70)
    body=models.TextField()
    image=models.ImageField(upload_to='images/article')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.body[:30]}'
  