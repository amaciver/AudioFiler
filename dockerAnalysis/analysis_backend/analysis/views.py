from django.shortcuts import render
from django.http import JsonResponse
from helpers import util


def show(request, previewUrl):
    util.downloadPreview(previewUrl)
    array = util.extractFeatures()
    
    return JsonResponse({ 'features': array })
