import django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


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
    slug=models.SlugField(null=True,unique=True,blank=True)

    class Meta:
        ordering=('-created',)
        verbose_name='postamota'
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug=slugify(self.title)
        super(post_blog,self).save()
    def __str__(self):
        return f'{self.title} - {self.body[:30]}'





