from django import forms
from apps.afiliador.models import Afiliador

class AfiliadorForm(forms.ModelForm):
	class Meta:
		model = Afiliador

		fields = [
			'id_afiliador',
			'nombre',
            'telefono',
            'sede',
		]
		labels = {
			'id_afiliador': 'Campaña',
			'nombre': 'Nombre',
            'telefono': 'Num de teléfono',
            'sede': 'Sede',
		}
		widgets = {
            'id_afiliador': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'sede': forms.Select(attrs={'class':'form-control'}),
        }
