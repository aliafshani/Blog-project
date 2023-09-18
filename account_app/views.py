from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.


def account_app(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/login')

    return render (request , 'account_app/login.html')


def log_out(request):
    logout(request)
    return redirect('account:regester')


def regester(request):

    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect('/')
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'account_app/regester.html')
