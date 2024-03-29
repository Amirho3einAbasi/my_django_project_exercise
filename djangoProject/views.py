from django.shortcuts import render
from project_slider.models import Slider

def home_page(request):
    sliders = Slider.objects.all()
    context = {
        'sliders' : sliders,
        'home': 'home'
    }
    return render(request, 'home_page.html', context)


# .............................................. header and footer .........................................................
def header(request):
    context = {}
    return render(request, 'shared/header.html', context)


def footer(request):
    context = {
        'about_us': 'این سایت توسط امیرحسین عباسی و برای تمرین ایجاد شده است'
    }
    return render(request, 'shared/footer.html', context)


# ................................................. about us page ..................................................................
def about_us(request):
    context = {
        'about' : 'این سایت توسط امیرحسین عباسی برای تمرین ساخته شده است'
    }
    return render(request, 'about_us.html', context)
