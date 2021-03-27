from django.urls import path
from .views import product_list

urlpatterns = [
    path('products',product_list.as_view(), name='product_list'),
    # path('products_detail/<pk>',Detail_view.as_view(),name='product_detail'),

]
