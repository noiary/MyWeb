from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<H2>Hi, this is Max and Elsa</H2> <H3>This's our first web-site :)</H3><H3>to be continued...</H3>")
