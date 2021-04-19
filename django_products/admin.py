from django.contrib import admin
from .models import Product, product_gallery


# Register your models here.
class admin_Manager(admin.ModelAdmin):
    list_display = ['title', 'active']


admin.site.register(Product, admin_Manager)

admin.site.register(product_gallery)
