# Generated by Django 3.1.7 on 2021-03-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_products', '0005_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product/', verbose_name='عکس'),
        ),
    ]
