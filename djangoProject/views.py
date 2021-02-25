from django.shortcuts import render


def home_page(request):
    context = {
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
# .............................................................................................................................................
