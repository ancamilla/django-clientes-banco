import django_filters
from .models import Cliente

class ClienteFilter(django_filters.FilterSet):
    """
    Filtros para el modelo Cliente, incluyendo búsqueda por ID.
    """
    cliente_id = django_filters.CharFilter(lookup_expr='icontains', label='Cliente ID')

    class Meta:
        model = Cliente
        fields = {
            'genero': ['exact'],  # Filtra por género exacto
            'activo': ['exact'],  # Filtra por estado activo/inactivo
            'nivel_satisfaccion': ['exact'],  # Filtra por nivel de satisfacción
        }
        # Agregar cliente_id como un filtro manual adicional
        additional_filters = ['cliente_id']
