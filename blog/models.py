from django.db import models
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class BlogModel(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    # autor toma el valor del usuario que esta ingresado, importo libreria user
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
