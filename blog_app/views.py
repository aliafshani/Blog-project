from django.shortcuts import render,get_object_or_404
from .models import post_blog
# Create your views here.

def Detailes(request,slug):
    special=get_object_or_404(post_blog,slug=slug)
    return render(request , 'blog_app/article_deatails.html',context={'article':special})


def article_list(request):
    article = post_blog.objects.all()
    return render(request, 'blog_app/article_lists.html', context={'all_article': article})