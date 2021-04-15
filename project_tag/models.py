from django.db import models
from django.db.models.signals import pre_save

from django_products.models import Product

# Create your models here.
from project_tag.unique_slug import unique_slug_generator


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='slug/ عنوان در url ',blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخچه')
    active = models.BooleanField(verbose_name='فعال')
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name_plural = 'تگ ها'
        verbose_name = 'تگ'

    def __str__(self):
        return self.title

def Tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(Tag_pre_save_receiver, sender=Tag)
