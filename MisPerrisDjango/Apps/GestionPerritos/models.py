from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Perritos(models.Model):
	codigo = models.PositiveIntegerField()
	nombre = models.CharField(max_length=15)
	tamano = models.FloatField(validators=[MinValueValidator(0.5), MaxValueValidator(2,5)],)
	peso = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(200)],)
	color = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=50)
	fechaRescate = models.DateTimeField()
	estadoRescate = (('R','Rescatado'),('D','Disponible'),('A','Adoptado'))
	estado = models.CharField(max_length=1, choices=estadoRescate,default='D')