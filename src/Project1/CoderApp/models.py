from django.db import models

class Teachers(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Teachers"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    
class Students(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Students"
        ordering = ["nombre"]

    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}"
    
class Courses(models.Model):
    nombre = models.CharField(max_length=20)
    comision = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Courses"
        ordering = ["nombre"]

    def __str__(self) -> str:
        return f"{self.nombre}, {self.comision}"
    
class Deliverables(models.Model):
    nombre = models.CharField(max_length=20)
    fechaDeEntrega = models.DateField(verbose_name="Fecha de entrega")
    entregado = models.BooleanField()

    class Meta:
        verbose_name_plural = "Deliverables"
        ordering = ["nombre"]

    def __str__(self) -> str:
        return f"{self.nombre}, {self.fechaDeEntrega}, {self.entregado}"