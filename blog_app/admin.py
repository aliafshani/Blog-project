from django.contrib import admin
from .models import post_blog
from .models import category
# Register your models here.

admin.site.register(post_blog)
admin.site.register(category)

