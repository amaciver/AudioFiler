from django.shortcuts import render
import requests
import pdb


from helpers import util

from django.http import JsonResponse, HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def show(request, preview_url):
    url = f"http://localhost:8001/analysis/{preview_url}"
    response = requests.get(url)
    classification = util.run_model([response.json()['features']])
    # pdb.set_trace()
    return JsonResponse({"classification": classification.tolist()})
    # return(classify(response))
