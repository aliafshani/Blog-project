from django.urls import path
from . import views


app_name='account'

urlpatterns=[
    path('login/', views.account_app , name='account_app'),
    path('logout/', views.log_out, name='logout'),
    path('regester/', views.regester ,name='regester')
]