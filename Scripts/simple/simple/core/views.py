from django.shortcuts import render
from django.http import HttpResponse  # Add isso

from .forms import ContactForm


def hello(request):
    return render(request, 'home.html')


def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            print(form.cleaned_data)
            form = ContactForm()
    else:
        form = ContactForm()
        context['form'] = form
        context['is_valid'] = False
    return render(request, 'contact.html', context)
