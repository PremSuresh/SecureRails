from django.db import models

# Create your models here.
class registersos(models.Model):
    phone = models.CharField(max_length=10)
    phone1 = models.CharField(max_length=10)
    phone2 = models.CharField(max_length=10)
    phone3 = models.CharField(max_length=10)
    def __str__(self):
        return self.phone
