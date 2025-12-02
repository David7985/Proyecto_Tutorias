from django.db import models
from django.contrib.auth.models import User  # <--- Importamos la tabla de Usuarios

class Tutoria(models.Model):
    # Opciones para el campo 'modalidad'
    MODALIDAD_CHOICES = [
        ('presencial', 'Presencial'),
        ('online', 'Online'),
    ]

    # Conectamos la Tutoría con un Usuario (el Tutor que la dicta).
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Tutor responsable")

    # Campos normales
    asignatura = models.CharField(max_length=100, verbose_name="Asignatura") 
    tema = models.CharField(max_length=200, verbose_name="Tema a tratar")    
    fecha = models.DateTimeField(verbose_name="Fecha y Hora")                
    modalidad = models.CharField(max_length=20, choices=MODALIDAD_CHOICES, default='presencial')
    cupos = models.IntegerField(default=5, verbose_name="Cupos Disponibles")
    
    def __str__(self):
        # Ahora mostramos también el nombre del tutor en el texto
        return f"{self.asignatura} - {self.tema} (Dictada por: {self.tutor.username})"