# Generated by Django 3.1.7 on 2021-04-18 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_products', '0006_auto_20210415_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to='products_gallery/', verbose_name='عکس')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_products.product')),
            ],
        ),
    ]