from django.db import models
from django.db.models import CharField, FloatField, DateTimeField, \
    ForeignKey, IntegerField, CASCADE, BooleanField
from django.contrib.auth.models import User

# Create your models here.
class Equipo(models.Model):
    nombre = CharField(max_length=30)
    precio = FloatField()
    url = CharField(max_length=255)
    creado = DateTimeField(auto_now_add=True)
    actualizado = DateTimeField(auto_now=True)
    active = BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} | {self.precio}'

class Status(models.TextChoices):
    PREPARACION = 'PRE', 'Preparación'
    ALQUILADO = 'ALQ', 'Alquilado'
    CANCELADO = 'CAN', 'Cancelado'
    REINTEGRADO = 'REI', 'Reintegrado'

class Alquiler(models.Model):
    usuario = ForeignKey(User, on_delete=CASCADE)
    direccion = CharField(max_length=255)
    inicia = DateTimeField()
    termina = DateTimeField()
    creado = DateTimeField(auto_now_add=True)
    actualizado = DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=3,
        choices=Status.choices,
        default=Status.PREPARACION,
    )

class EquipoAlquiler(models.Model):
    equipo = ForeignKey(Equipo, on_delete=CASCADE)
    alquiler = ForeignKey(Alquiler, on_delete=CASCADE)
    numero = IntegerField()
