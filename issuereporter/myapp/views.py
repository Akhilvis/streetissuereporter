from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return JsonResponse({"hai":33773})
