from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ['cliente_id', 'edad', 'genero', 'saldo', 'activo', 'nivel_satisfaccion']
