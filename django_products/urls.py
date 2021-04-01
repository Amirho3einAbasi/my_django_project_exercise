from django.urls import path
from .views import product_list,product_detail,search_product_view

urlpatterns = [
    path('products',product_list.as_view(), name='product_list'),
    path('products_detail/<slug>/<name>',product_detail.as_view(),name='product_detail'),
    path('product_search' , search_product_view.as_view(),name='search_product')

]
