from django.urls import path
from .views import product_list, product_detail, search_product_view,product_category_view,product_category_RenderPartial

urlpatterns = [
    path('products', product_list.as_view(), name='product_list'),
    path('products_detail/<pk>/<name>', product_detail.as_view(), name='product_detail'),
    path('product_search', search_product_view.as_view(), name='search_product'),
    path('products/<category_name>', product_category_view.as_view(), name='product_categories'),
    path('products_category', product_category_RenderPartial, name='product_category_render_partial')

]
