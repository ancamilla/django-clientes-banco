from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Cliente
from .serializer import ClienteSerializer
from .forms import ClienteForm
from django.db.models import Avg, Count
from django.core.paginator import Paginator
from .filters import ClienteFilter

class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['genero', 'activo', 'nivel_satisfaccion']


def listar_clientes(request):
	"""
	Lista los clientes con paginación.
	Permite al usuario seleccionar la cantidad de registros por página.
	"""
	#Opciones de paginación
	opciones_registros = [10, 20, 50, 100]
	# Obtiene el número de registros por página desde el parámetro GET, por defecto 10
	registros_por_pagina = int(request.GET.get('registros', 10))

	# Obtiene todos los clientes y los pagina
	clientes = Cliente.objects.all()
	paginator = Paginator(clientes, registros_por_pagina)  # Configura la paginación
	pagina = request.GET.get('page')  # Obtiene el número de página actual desde los parámetros GET
	clientes_pagina = paginator.get_page(pagina)  # Obtiene la página actual
	# Renderiza la plantilla con la lista paginada
	return render(request, 'listar_clientes.html', {
		'clientes_pagina': clientes_pagina,
		'registros_por_pagina': registros_por_pagina,
		'opciones_registros': opciones_registros,
	})


def crear_cliente(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('listar_clientes')
	else:
		form = ClienteForm()
	return render(request, 'crear_cliente.html', {'form': form})

def actualizar_cliente(request, pk):
	cliente = get_object_or_404(Cliente, pk=pk)
	if request.method == 'POST':
		form = ClienteForm(request.POST, instance=cliente)
		if form.is_valid():
			form.save()
			return redirect('listar_clientes')
	else:
		form = ClienteForm(instance=cliente)
	return render(request, 'actualizar_cliente.html', {'form': form, 'cliente': cliente})

def eliminar_cliente(request, pk):
	cliente = get_object_or_404(Cliente, pk=pk)
	if request.method == 'POST':
		cliente.delete()
		return redirect('listar_clientes')
	return render(request, 'eliminar_cliente.html', {'cliente': cliente})



def estadisticas_clientes(request):
	"""
	Genera estadísticas básicas para los clientes.
	"""
	# Calcula el promedio del saldo
	promedio_saldo = Cliente.objects.aggregate(promedio=Avg('saldo'))['promedio']

	# Calcula la distribución de edades
	distribucion_edades = Cliente.objects.values('edad').annotate(total=Count('edad')).order_by('edad')

	# Renderiza las estadísticas en el template
	return render(request, 'estadisticas_clientes.html', {
		'promedio_saldo': promedio_saldo,
		'distribucion_edades': distribucion_edades,
	})

def filtrar_clientes(request):
	"""
	Filtra y pagina los clientes basándose en los parámetros GET.
	"""
	# Configurar filtros
	filtro = ClienteFilter(request.GET, queryset=Cliente.objects.all())

	# Paginar los resultados filtrados
	registros_por_pagina = int(request.GET.get('registros', 10))  # Por defecto 10
	paginator = Paginator(filtro.qs, registros_por_pagina)
	pagina = request.GET.get('page')
	clientes_pagina = paginator.get_page(pagina)

	# Renderizar la plantilla
	return render(request, 'filtrar_clientes.html', {
		'filter': filtro,  # Filtro para mostrar opciones
		'clientes_pagina': clientes_pagina,  # Resultados paginados
	'registros_por_pagina': registros_por_pagina,  # Registros por página seleccionados
	})
