from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=200,verbose_name="Titulo")
    description=models.TextField(verbose_name="Descripcion")
    image=models.ImageField(upload_to="projects",verbose_name="Imagen")
    link = models.URLField(null=True, blank=True,verbose_name="Dirección Web")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="proyecto"
        verbose_name_plural="proyectos"
        ordering=["-created"] # Es una lista que permite ordenar con prioridades entre distintos campos.

    def __str__(self):
        return self.title    