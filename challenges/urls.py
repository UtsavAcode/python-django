# first import path from urls

from django.urls import path

# then import the views from your views.py that are the functions or classes that are to be sent when the client request it 
## then import the views from your views.py that are the functions or classes 
## then import the views from your views.py that are the functions or classes 
from . import views

urlpatterns =[
   
    path("<month>",views.monthly_challenge),
]