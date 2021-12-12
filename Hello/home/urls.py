from django.contrib import admin

from django.urls import path
from django.urls.conf import include
from django.db import models



from home import views

urlpatterns = [
    path("",views.index,name='Homepage'),
    path("about",views.about,name="about"),
    path("contact",views.contact,name='contact'),
    path("services",views.services,name='services'),
    path("triund",views.triund,name='triund'),
    path("kareri",views.kareri,name='kareri'),
    path("thatharana",views.thatharana,name='thatharana'),
    path("himani",views.himani,name='himani'),
    path("indra",views.indra,name='indra'),
    path("rising",views.rising,name='rising')
    
    ]