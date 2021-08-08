from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def example(request):
    return HttpResponse("Hello, World!")


def name(request):
    return HttpResponse("My Name is Arnas")
