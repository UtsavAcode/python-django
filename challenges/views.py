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

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenges.html")
        return HttpResponse(response_data)
    
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

    
    return HttpResponse(challenge_text)