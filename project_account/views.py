from django.shortcuts import render, redirect
from .forms import login_form, register_form
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    form_login = login_form(request.POST or None)
    if form_login.is_valid():
        user = authenticate(request, username=form_login.cleaned_data.get('user_name'),password=form_login.cleaned_data.get('user_password'))
        if user is not None:
            login(request, user)
            return redirect('/')
    context = {
        'login_form': form_login
    }
    return render(request, 'login_user.html', context)



def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    form_register = register_form(request.POST or None)
    if form_register.is_valid():
        username = form_register.cleaned_data.get('user_name')
        email = form_register.cleaned_data.get('user_email')
        password = form_register.cleaned_data.get('user_password')
        user = User.objects.create_user(username=username,email=email,password=password)
        login(request,user)
        return redirect('/')
    context = {
        'register_form': form_register
    }
    return render(request, 'register_user.html', context)
