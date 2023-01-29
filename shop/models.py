from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pets(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='pets')
    pet_type = models.CharField(max_length=256)
    pet_age = models.IntegerField()
    pet_name = models.CharField(max_length=256)
    breed_name = models.CharField(max_length=256)
    pet_weight = models.CharField(max_length=256)



class PetGrooming(models.Model):
    pet_detail = models.ForeignKey(Pets,on_delete=models.CASCADE,related_name='pet_grooming')
    pet_service_type = models.CharField(max_length=256)

class PetBoarding(models.Model):
    pet_detail = models.ForeignKey(Pets,on_delete=models.CASCADE,related_name='pet_boarding')
    time = models.TimeField()
    meal = models.CharField(max_length=500)
    special_care = models.TextField()

class PetWalking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='pet_walking')
    pet_detail = models.ForeignKey(Pets,on_delete=models.CASCADE)

