# Generated by Django 3.1.7 on 2021-03-03 16:03

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('project_products', '0003_auto_20210303_1858'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]