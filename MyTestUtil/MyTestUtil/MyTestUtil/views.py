# i have created this file - jyoti

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    parameter = {'name': 'jyoti', 'place': 'adinathnagar'}
    return render(request, 'index.html',parameter)
    #return HttpResponse("<a href ='https://www.youtube.com/watch?v=4eeumqUH3uw'>youtube</a>")


def about(request):
    return HttpResponse("in ablut")


def pipe(request):
    return HttpResponse("<a href='about'>back</a>")
