from django.shortcuts import render
from django.views.generic import ListView, DetailView

from project_product_category.models import Category
from .models import Product


# Create your views here.

class product_list(ListView):
    template_name = 'product_list.html'
    paginate_by = 3
    def get_queryset(self):
        return Product.objects.get_active_product()
    # .............................. detail view ...........................................


class product_detail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()


# ................................. search view .............................................

class search_product_view(ListView):
    template_name = 'product_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        search_query = request.GET.get('q')
        if search_query is not None:
            return Product.objects.search(search_query)

        return Product.objects.get_active_product()

    # ..............................  category view ............................................


class product_category_view(ListView):
    template_name = 'product_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name_in_url = self.kwargs['category_name']
        return Product.objects.get_products_by_category(category_name_in_url)
#.........................................................................................
def product_category_RenderPartial(request):
    category_query = Category.objects.all()
    context = {
        'categories' : category_query
    }
    return render(request,'component/product_category_render_partial.html',context)