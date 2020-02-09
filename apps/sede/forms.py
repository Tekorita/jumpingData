from django import forms
from apps.sede.models import Sede

class SedeForm(forms.ModelForm):
	class Meta:
		model = Sede

		fields = [
			'campaña',
			'nombre',
            'departamento',
            'distrito',
            'direccion',
		]
		labels = {
			'campaña': 'Campaña',
			'nombre': 'Nombre',
            'departamento': 'Departamento',
            'distrito': 'Distrito',
            'direccion': 'Dirección',	
		}
		widgets = {
            'campaña': forms.Select(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'departamento': forms.Select(attrs={'class':'form-control'}),
            'distrito': forms.Select(attrs={'class':'form-control'}),
            'direccion': forms.Textarea(attrs={'class':'form-control'}),
        }
