from django.db import models

class Teachers(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
