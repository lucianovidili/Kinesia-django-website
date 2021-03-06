# Generated by Django 3.2.8 on 2022-01-10 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0012_auto_20220109_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnas',
            name='address',
            field=models.CharField(default=0, max_length=250, verbose_name='Dirección'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnas',
            name='e_name_contact',
            field=models.CharField(default=0, max_length=200, verbose_name='Contacto de Emergencia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnas',
            name='e_phone_contact',
            field=models.CharField(default=0, max_length=30, verbose_name='Teléfono de Emergencia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnas',
            name='goals',
            field=models.CharField(choices=[('flexibility', 'Flexibilidad'), ('strength', 'Fuerza'), ('relax', 'Relajación'), ('posture', 'Postura disminución del estrés'), ('others', 'Otros')], default='flexibility', max_length=35, verbose_name='Objetivos'),
        ),
        migrations.AddField(
            model_name='alumnas',
            name='phone',
            field=models.CharField(default=0, max_length=30, verbose_name='Teléfono'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumnas',
            name='email',
            field=models.EmailField(max_length=250, unique=True, verbose_name='Email'),
        ),
    ]
