from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def First(request):
    return HttpResponse('<h1>Hi this is You first Program</h1>')