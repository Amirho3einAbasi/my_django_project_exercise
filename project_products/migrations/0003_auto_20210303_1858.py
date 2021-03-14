# Generated by Django 3.1.7 on 2021-03-03 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_products', '0002_auto_20210303_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=8, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50, verbose_name='عنوان'),
        ),
    ]
