from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string


monthly_challenges = {
    "january" : "This is the monthly challenge for january",
    "february" : "This is the monthly challenge for february",
    "march" : "This is the monthly challenge for march",
    "april": "This is the monthly challenge for april",
    "may": "This is the monthly challenge for may",
    "june" : "This is the monthly challenge for june",
    "july" : "This is the monthly challenge fot july",
    "august" : "This is the mobthly challenge for august",
    "september" : "This is the monthly challenge for september",
    "october" : "This is the monthly challenge for october",
    "november": "This is the monthly challenge for november",
    "december" : "This is the monthly challenge for december",
    
    }

def monthly_challenge(request,months):
       months = list(monthly_challenges.keys())

       return render(request,"challenges/challenges.html",{
              "months" : months
       })
      
    
    