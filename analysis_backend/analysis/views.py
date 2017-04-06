from django.shortcuts import render
from django.http import JsonResponse
from helpers import util


def show(request, previewUrl):
    downloadPreview(previewUrl)

    array = extractFeatures()

    return JsonResponse({ features: array })
