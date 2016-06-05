from django.contrib.gis.db import models
from django.conf import settings
# Create your models here.

class Providers(models.Model):
	name = models.CharField(max_length=77,blank=True)
	email=models.EmailField()
	phone_no=models.CharField(max_length=17,blank=True)
	language=models.CharField(max_length=17,blank=True)
	Currency=models.CharField(max_length=132,blank=True)


	def __str__(self):
		return self.name



class ServiceArea(models.Model):

    name = models.CharField(max_length=80,blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    poly = models.MultiPolygonField()
    provider = models.ForeignKey(Providers, on_delete=models.CASCADE, related_name='service_areas')

    def __str__(self):
        return self.name
