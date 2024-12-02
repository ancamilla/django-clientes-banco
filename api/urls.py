from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, listar_clientes, crear_cliente, actualizar_cliente, eliminar_cliente, estadisticas_clientes, filtrar_clientes

# Rutas para la API REST
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)

# Rutas para las vistas basadas en templates
urlpatterns = [
	path('listar/', listar_clientes, name='listar_clientes'),
	path('crear/', crear_cliente, name='crear_cliente'),
	path('filtrar/', filtrar_clientes, name='filtrar_clientes'),
	path('actualizar/<int:pk>/', actualizar_cliente, name='actualizar_cliente'),
	path('eliminar/<int:pk>/', eliminar_cliente, name='eliminar_cliente'),
	path('estadisticas/', estadisticas_clientes, name='estadisticas_clientes'),
	path('api/', include(router.urls)),  # Incluye las rutas de la API REST
]

