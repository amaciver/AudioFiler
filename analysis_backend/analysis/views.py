from django.shortcuts import render
from django.http import JsonResponse
from analysis_backend.helpers.util import downloadPreview, extractFeatures



def show(previewUrl):
    downloadPreview(previewUrl)

    # perform analysis

    # format json response
    return JsonResponse({ 'working?': 'yes'})
