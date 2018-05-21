from django.db import models
from django.urls import reverse
from police.models import policeuser
from police.distancescript import haversine
import geocoder
# Create your models here.
def neareststation(latitude,longitude):
    policeforms = policeuser.objects.all()
    min=1000000
    for form in policeforms:
        plat = float(form.latitude)
        plong = float(form.longitude)
        dist = haversine(plong,plat,longitude,latitude)
        if min > dist:
            min = dist
            nearest = form.user
    return str(nearest)

class firstruc(models.Model):
    pnr = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    type = models.CharField(max_length=1000, null=True)
    complaint = models.CharField(max_length=10000)
    latitude = models.CharField(max_length=250, default=str(geocoder.ip('me').latlng[0]))
    longitude = models.CharField(max_length=250, default=str(geocoder.ip('me').latlng[1]))
    nearest = models.CharField(max_length=250, default=neareststation(float(geocoder.ip('me').latlng[0]),float(geocoder.ip('me').latlng[1])))
    status = models.CharField(max_length=10, default='Unresolved')
    def __str__(self):
        return self.pnr+ ' ' + str(self.phone)
def get_absolute_url(self):
    return reverse('/homepage/', kwargs={'pk': self.pk})
