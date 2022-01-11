# Generated by Django 3.2.8 on 2022-01-10 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0014_auto_20220109_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnas',
            name='diseases',
        ),
        migrations.AddField(
            model_name='alumnas',
            name='affections',
            field=models.CharField(choices=[('anemia', 'Anemia'), ('asthma', 'Asma'), ('back_pain', 'Dolor de Espalda'), ('cancer', 'Cáncer'), ('diabetes', 'Diabetes'), ('stroke', 'Accidente Cerebro Vascular'), ('epilepsy', 'Epilepsia'), ('depression', 'Depresión'), ('arthritis', 'Artritis'), ('none', 'Ninguna'), ('others', 'Otras')], default='anemia', max_length=35, verbose_name='Afecciones'),
        ),
    ]