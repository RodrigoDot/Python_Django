from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse  # Add isso

from .models import Courses


def index(request):
    courses = Courses.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)


def details(request, id):
    # course =  Courses.objects.get(id=id)
    course = get_object_or_404(Courses, id=id)
    template_name = 'courses/details.html'
    context = {
        'course': course
    }
    return render(request, template_name, context)
