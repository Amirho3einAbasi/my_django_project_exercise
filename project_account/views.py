from django.shortcuts import render, redirect
from .forms import login_form
from django.contrib.auth import authenticate, login, get_user_model
# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    form_login = login_form(request.POST)
    if form_login .is_valid():
        user = authenticate(request,username=form_login.cleaned_data.get('user_name'),password=form_login.cleaned_data.get('user_password'))
        if user is not None:
            login(request,user)
            return redirect('/')
    context = {
        'login_form': form_login
    }
    return render(request, 'login_user.html', context)
