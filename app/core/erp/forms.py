from django.forms import *

from core.erp.models import Alumnas


class AlumnasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        '''
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        '''
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Alumnas
        fields = '__all__'
        widgets = {
            'names': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Ingrese su correo elctrónico',
                }
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'phone': TextInput(
                attrs={
                    'placeholder': 'Ingrese su teléfono',
                }
            ),
            'e_name_contact': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de su contacto de emergencia',
                }
            ),
            'e_phone_contact': TextInput(
                attrs={
                    'placeholder': 'Ingrese el teléfono de su contacto de emergencia',
                }
            ),
            'observations': TextInput(
                attrs={
                    'placeholder': 'Ingrese aquí sus observaciones',
                }
            ),
            'goals_others': TextInput(
                attrs={
                    'placeholder': '¿Cuáles?',
                }
            )
        }
