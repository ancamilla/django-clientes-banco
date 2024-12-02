import csv
from django.core.management.base import BaseCommand
from api.models import Cliente

class Command(BaseCommand):
	help = 'Carga datos del archivo clientes_banco.csv en el modelo Cliente'

	def handle(self, *args, **kwargs):
		ruta_csv = '/var/www/django/djangoapi/clientes_banco.csv'

		with open(ruta_csv, newline='', encoding='utf-8') as archivo_csv:
			lector = csv.DictReader(archivo_csv)
			for fila in lector:
				if not Cliente.objects.filter(cliente_id=fila['Cliente_ID']).exists(): #Manejo de cliente_id duplicados.
					genero = fila['Genero'].capitalize() if fila['Genero'] else 'Otro'  # Normalizar género
					if genero not in ['Masculino', 'Femenino']:
						genero = 'Otro'
					Cliente.objects.create(
						cliente_id=fila['Cliente_ID'],
						edad=int(float(fila['Edad'])) if fila['Edad'] else 0, # Manejo de valores vacíos
						genero=genero,  # Normalización aplicada
						saldo=float(fila['Saldo']) if fila['Saldo'] else 0.0,  # Manejo de valores vacíos
						activo=bool(int(float(fila['Activo'])) if fila['Activo'] else 0),  # Manejo de valores vacíos
						nivel_satisfaccion=int(float(fila['Nivel_de_Satisfaccion'])) if fila['Nivel_de_Satisfaccion'] else 0
					)
		self.stdout.write(self.style.SUCCESS('Clientes cargados exitosamente.'))
