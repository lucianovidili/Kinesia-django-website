# Generated by Django 3.2.8 on 2021-10-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_category_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción'),
        ),
    ]
