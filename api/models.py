from django.db import models

# Create your models here.
class Cliente(models.Model):
	GENEROS = [
		('Masculino', 'M'),
		('Femenino', 'F'),
		('Otro', 'O'),
	]

	NIVELES_SATISFACCION = [
		(1, 'Muy insatisfecho'),
		(2, 'Insatisfecho'),
		(3, 'Neutral'),
		(4, 'Satisfecho'),
		(5, 'Muy satisfecho'),
	]

	cliente_id = models.CharField(max_length=50, unique=True)
	edad = models.IntegerField()
	genero = models.CharField(max_length=10, choices=GENEROS) #Uso de choices.
	saldo = models.FloatField()
	activo = models.BooleanField(default=True)
	nivel_satisfaccion = models.IntegerField(choices=NIVELES_SATISFACCION) #Uso de choices.
	def __str__(self):
		return self.cliente_id
