from django.shortcuts import render
from blog_app.models import post_blog
# Create your views here.

def home_page(request):
     article=post_blog.objects.all()
     return render(request , 'home_page/index.html' , context={'article': article})
