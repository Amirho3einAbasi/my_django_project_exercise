from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


# Create your views here.

class product_list(ListView):
    template_name = 'product_list.html'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.get_active_product()
    #.............................. detail view ...........................................

class product_detail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()

#................................. search view .............................................

class search_product_view(ListView):
    template_name = 'product_list.html'
    paginate_by = 2
    def get_queryset(self):
        request = self.request
        search_query = request.GET.get('q')
        if search_query is not None:
            return Product.objects.filter(title__icontains=search_query)

        return Product.objects.get_active_product()