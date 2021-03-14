from django.urls import path
from .views import product_list

urlpatterns = [
    path('products',product_list.as_view(), name='product_list'),

]
