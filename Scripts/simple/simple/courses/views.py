from django.shortcuts import render
from django.http import HttpResponse  # Add isso

from .models import Courses

def index(request):
    courses = Courses.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)
