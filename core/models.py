from django.db import models

# Create your models here.

class ropaLavanderiaHospital(models.Model):
    
    limpio = models.IntegerField()
    suciio = models.IntegerField()
    cantidad = models.IntegerField()

class ropaLavanderiaExterna(models.Model):
    
    limpio = models.IntegerField()
    suciio = models.IntegerField()
    cantidad = models.IntegerField()