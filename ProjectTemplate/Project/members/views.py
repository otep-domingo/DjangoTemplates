from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    # return HttpResponse("Weldome to Python and Django!")
    template = loader.get_template('myfirst.html')
    context={
        'FIRSTNAME':'Linus',
        'lastname':'Torvalds',
        'alias':'Linux',
    }
    return HttpResponse(template.render(context,request))

def name(request):
    return HttpResponse("My name is Juan dela Cruz")

def birthday(request):
    return HttpResponse("My birthday is on January")

def child(request):
    template=loader.get_template('child.html')
    return HttpResponse(template.render())

def subjects(request):
    template=loader.get_template('subjects.html')
    return HttpResponse(template.render())


def portfolio(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())