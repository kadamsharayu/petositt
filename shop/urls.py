from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('grooming/',views.pet_grooming,name='pet_grooming'),
    path('boarding/',views.pet_boarding,name='pet_boarding'),
    path('walking/',views.pet_walking,name='pet_walking'),
    # temp links
    path('',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('gallery/',views.gallery,name='gallery'),
    path('faqs/',views.faqs,name='faqs'),
    path('services/',views.services,name='services'),
]
