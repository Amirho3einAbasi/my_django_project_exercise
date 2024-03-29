# Generated by Django 3.1.7 on 2021-04-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_products', '0004_auto_20210413_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان')),
                ('slug', models.SlugField(verbose_name='slug/ عنوان در url ')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='تاریخچه')),
                ('active', models.BooleanField(verbose_name='فعال')),
                ('products', models.ManyToManyField(to='django_products.Product')),
            ],
        ),
    ]
