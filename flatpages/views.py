from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django import template

# Create your views here.


def home(request):
    return render(request, 'templates/index.html')


def st_hndlr(request):
    return render(request, 'templates/static_heandler.html')
