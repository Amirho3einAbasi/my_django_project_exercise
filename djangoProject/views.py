from django.shortcuts import render, redirect

def home_page(request):
    context ={
        'home' : 'home'
    }
    return render(request,'home_page.html',context)