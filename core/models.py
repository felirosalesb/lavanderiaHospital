from django.db import models

# Create your models here.

class ropaLavanderiaHospital(models.Model):
    limpio = models.IntegerField()
    suciio = models.IntegerField()

    @property
    def cantidad(self):
        return self.limpio + self.suciio

class ropaLavanderiaExterna(models.Model):
    limpio = models.IntegerField()
    suciio = models.IntegerField()

    @property
    def cantidad(self):
        return self.limpio + self.suciio
