from django.db import models


# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیخات')
    link = models.URLField(verbose_name='آدرس')
    image = models.ImageField(upload_to='slider/', null=True, verbose_name='عکس')

    class Meta:
        verbose_name_plural = 'اسلایدر ها'
        verbose_name = 'اسلایدر'
    def __str__(self):
        return self.title
