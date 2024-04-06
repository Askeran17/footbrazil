from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_portal(request):
    return HttpResponse("Footbrazil Ole!")
