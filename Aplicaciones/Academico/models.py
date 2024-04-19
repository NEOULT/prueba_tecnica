from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=60)
    horas_creditos=models.PositiveSmallIntegerField()

    def __str__(self):
        text=  "{0} ({1} HC)"
        return text.format(self.nombre,self.horas_creditos)