import django_filters
from .models import Cliente

class ClienteFilter(django_filters.FilterSet):
	"""
	Filtros para el modelo Cliente.
	"""
	class Meta:
		model = Cliente
		fields = {
			'genero': ['exact'],  # Filtra por género exacto (Masculino, Femenino, Otro)
			'activo': ['exact'],  # Filtra por estado exacto (True o False)
			'nivel_satisfaccion': ['exact'],  # Filtra por nivel de satisfacción exacto (1-5)
	}
