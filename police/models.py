from django.db import models

# Create your models here.
class policeuser(models.Model):
    user = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    latitude = models.CharField(max_length = 100, null=True)
    longitude = models.CharField(max_length = 100, null=True)
    def __str__(self):
        return self.user

class RPF(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    pnr = models.CharField(max_length = 100)
    def __str__(self):
        return self.pnr
