from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class sign(models.Model):
    # user   = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone  = models.CharField(primary_key=True,max_length=11)
    Age    = models.IntegerField()
    Gender = models.CharField(max_length=6)


class Reading(models.Model):
    na_level    = models.DecimalField(max_digits=5, decimal_places=2)
    intensity   = models.DecimalField(max_digits=5, decimal_places=2)
