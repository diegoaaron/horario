from django import forms

from .models import Mascota

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
        ]

        label = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',
        }

        widget = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
        }