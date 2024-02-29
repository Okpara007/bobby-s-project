# collect from listings urls.py p.s we are setting up the routes for the accounts app
from django.urls import path

from . import views

urlpatterns = [
    path('', views.forms, name="forms"), # first parameter(root path/home page), second parameter(mathod that we want to connect it to), final parameter(the name which would be used to easily access the path)
    
]