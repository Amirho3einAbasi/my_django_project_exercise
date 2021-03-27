from django.db import models
from django.db.models.signals import pre_save
from .unique_slug import unique_slug_generator

# Create your models here
class Product_manager(models.Manager):
    def get_active_product(self):
        return self.get_queryset().filter(active=True)


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(default='', blank=True,unique=True)
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=8, default=0, decimal_places=3, verbose_name='قیمت')
    image = models.ImageField(upload_to='django_product/', null=True, verbose_name='عکس')
    active = models.BooleanField(verbose_name='فعال')
    object = Product_manager()

    def __str__(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
