from django.shortcuts import render
from django.http import JsonResponse
from analysis_backend.helpers.util import downloadPreview, extractFeatures



def show(previewUrl):
    downloadPreview(previewUrl)

    array = extractFeatures()

    return JsonResponse({ features: array })
