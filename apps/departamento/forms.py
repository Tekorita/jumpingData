from django import forms
from apps.departamento.models import Departamento

class DepartamentoForm(forms.ModelForm):
	class Meta:
		model = Departamento

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
