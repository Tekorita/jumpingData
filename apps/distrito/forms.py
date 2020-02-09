from django import forms
from apps.distrito.models import Distrito

class DistritoForm(forms.ModelForm):
	class Meta:
		model = Distrito

		fields = [
			'nombre',
			'departamento',	
		]
		labels = {
			'nombre': 'Nombre',
			'departamento': 'Departamento',	
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'departamento': forms.Select(attrs={'class':'form-control'}),
		}
