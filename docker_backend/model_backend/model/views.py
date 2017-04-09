from django.shortcuts import render
from requests import Session
session = Session()

# import classify from util

# from django.http import JsonResponse, HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def show(request, preview_url):
    response = session.get(
    url=f"localhost:8001/analysis/{preview_url}")
    return("we hit the route")
    # return(classify(response))
