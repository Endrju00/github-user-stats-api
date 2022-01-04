from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List of repositories': '/user-repositories/',
        'Sum of stars': '/stars-counter/',
        'The most popular programming languages': '/programming-languages/'
    }
    return Response(api_urls)
