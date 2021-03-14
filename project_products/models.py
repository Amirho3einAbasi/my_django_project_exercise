from django.db import models


# Create your models here.
class Product_manager(models.Manager):
    def get_active_product(self):
        return self.get_queryset().filter(active=True)

class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=8, default=0, decimal_places=3, verbose_name='قیمت')
    image = models.ImageField(upload_to='product/',null=True,verbose_name='عکس')
    active = models.BooleanField(verbose_name='فعال')
    object =  Product_manager()

    def __str__(self):
        return self.title
