from django.shortcuts import render
import requests
import pdb

from helpers import util

from django.http import JsonResponse, HttpResponse

GENRES = {
    0: 'Alternative',
    1: 'Blues',
    2: 'Classical',
    3: 'Country',
    4: 'D&B',
    5: 'Disco',
    6: 'Dubstep',
    7: 'Electronic',
    8: 'Folk',
    9: 'Funk',
    10: 'Hip-Hop',
    11: 'House',
    12: 'Indie',
    13: 'Jazz',
    14: 'Metal',
    15: 'Pop',
    16: 'Punk',
    17: 'R&B',
    18: 'Rap',
    19: 'Reggaeton',
    20: 'Reggae',
    21: 'Rock',
    22: 'Salsa',
    23: 'Ska',
    24: 'Soul',
    25: 'Trance'
}

def index(request):
    return render(request, 'index.html')

def show(request, preview_url):
    url = f"http://localhost:8001/analysis/{preview_url}"
    response = requests.get(url)
    classification = util.run_model([response.json()['features']]).tolist()
    # pdb.set_trace()
    genre_guesses = list(map(lambda x: GENRES[x], classification))
    return JsonResponse({"classification": genre_guesses})
    # return(classify(response))