from django.urls import path, include
from . import views

urlpatterns=[
    path('detailess/<slug:slug>',views.Detailes),
    path('lists/',views.article_list,name='article_list')
]