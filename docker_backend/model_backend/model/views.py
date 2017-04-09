from django.shortcuts import render
import requests


# import classify from util

from django.http import JsonResponse, HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def show(request, preview_url):
    url = f"http://localhost:8001/analysis/{preview_url}"
    response = requests.get(url)
    print(response)
    return JsonResponse({"key": response.text})
    # return(classify(response))
