from django.contrib import admin
from .models import Pets,PetWalking,PetBoarding,PetGrooming
# Register your models here.
admin.site.register(Pets)
admin.site.register(PetGrooming)
admin.site.register(PetWalking)
admin.site.register(PetBoarding)
