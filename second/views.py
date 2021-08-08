from django.http.response import Http404, HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def display_time(request):
    return HttpResponse("current time "+datetime.now().strftime('%H:%M:%S'))


def index(request):
    return HttpResponse("second")
