from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    url_name = models.CharField(max_length=120, verbose_name='عنوان در url')

    class Meta:
        verbose_name_plural = 'دسته بندی ها'
        verbose_name = 'دسته بندی'

    def __str__(self):
        return self.title
