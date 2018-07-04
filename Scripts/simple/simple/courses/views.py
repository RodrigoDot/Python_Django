from django.shortcuts import render
from django.http import HttpResponse  # Add isso


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')
