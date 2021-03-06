# Generated by Django 3.2.8 on 2022-01-03 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_alter_category_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=100, verbose_name='Nombres')),
                ('surnames', models.CharField(max_length=100, verbose_name='Apellidos')),
            ],
            options={
                'verbose_name': 'Alumna',
                'verbose_name_plural': 'Alumnas',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]
