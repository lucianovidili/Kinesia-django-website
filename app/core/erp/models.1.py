from django.db import models
from datetime import datetime
from django.db.models import Choices
from django.forms import model_to_dict
from core.erp.choices import alumnas_goals_choices, alumnas_diseases_choices


class Alumnas(models.Model):
    names = models.CharField(max_length=100, verbose_name='Nombres', null=False, blank=False)
    surnames = models.CharField(max_length=100, verbose_name='Apellidos', null=False, blank=False)
    email = models.EmailField(max_length=250, verbose_name='Email', null=False, blank=False, unique=True)
    date_of_birth = models.DateField(verbose_name='Fecha de Nacimiento')
    address = models.CharField(max_length=250, verbose_name='Dirección', null=False, blank=False)
    phone = models.CharField(max_length=30, verbose_name='Teléfono', null=False, blank=False)
    e_name_contact = models.CharField(max_length=200, verbose_name='Contacto de Emergencia', null=False, blank=False)
    e_phone_contact = models.CharField(max_length=30, verbose_name='Teléfono de Emergencia', null=False, blank=False)
    goals = models.CharField(max_length=35, choices=alumnas_goals_choices, default='flexibility', verbose_name='Objetivos')
    goals_others = models.CharField(max_length=250, verbose_name='Otros', null=True, blank=True)
    #¿Padece alguna patología de columna? ¿Cuál? *
    back_pain = models.CharField(max_length=100, verbose_name='Patología de Columna', null=True, blank=True)
    #¿Padece alguna lesión (o dolor) ósea o muscular? ¿ Cuál? *
    pain = models.CharField(max_length=100, verbose_name='Dolor Óseo o Muscular', null=True, blank=True)
    #¿Padece alguna enfermedad cardiaca? Otorgar mayores detalles *
    heart_disease = models.CharField(max_length=150, verbose_name='Enfermedad Cardíaca', null=True, blank=True)
    #Marque las enfermedades que le han diagnosticado o por las que recibió tratamiento médico, u otros *
    affections = models.CharField(max_length=35, choices=alumnas_diseases_choices, default='anemia', verbose_name='Afecciones')
    #OTRAS OBSERVACIONES *
    observations = models.CharField(max_length=200, verbose_name='Observaciones', null=True, blank=True)
    '''
    NORMAS Y FUNCIONAMIENTO
    ¿Acepta las normas? *
    Sí
    No
    '''
    #DIAS Y HORARIO QUE CONCURRES A PILATES *

    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Ingreso')
    # dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')

    def __str__(self):
        return self.names

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Alumna'
        verbose_name_plural = 'Alumnas'
        ordering = ['id']