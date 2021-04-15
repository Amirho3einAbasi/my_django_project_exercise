from django.db import models
from django.db.models.signals import pre_save
from django.db.models import Q

from project_product_category.models import Category
from .unique_slug import unique_slug_generator


# Create your models here
class Product_manager(models.Manager):
    def get_active_product(self):
        return self.get_queryset().filter(active=True)
    def search(self,query):
        lookup = Q(title__icontains=query) | Q(description__icontains=query) | Q(tag__title__icontains=query)
        return self.get_queryset().filter(lookup,active=True).distinct()
    def get_products_by_category(self,category_name_in_url):
        return Product.objects.filter(category__url_name__iexact=category_name_in_url,active=True)



class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(default='', blank=True, unique=True)
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=8, default=0, decimal_places=3, verbose_name='قیمت')
    image = models.ImageField(upload_to='django_product/', null=True, verbose_name='عکس')
    active = models.BooleanField(verbose_name='فعال')
    category = models.ManyToManyField(Category)
    objects = Product_manager()

    class Meta:
        verbose_name_plural = 'محصولات'
        verbose_name = 'محصول'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/products_detail/{self.slug}/{self.title.replace(" ","+")}'



def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver, sender=Product)

