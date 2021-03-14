from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


# Create your views here.

class product_list(ListView):
    template_name = 'product_list.html'
    paginate_by = 1
    def get_queryset(self):
        return Product.object.get_active_product()
