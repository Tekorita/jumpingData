from django import forms
from apps.campaña.models import Campaña

class CampañaForm(forms.ModelForm):
	class Meta:
		model = Campaña

		fields = [
			'nombre',	
		]
		labels = {
			'nombre': 'Nombre',	
		}
		widgets = {
			'nombre': forms.TextInput(
				attrs={
					'class':'form-control',
				},
			),
		}
