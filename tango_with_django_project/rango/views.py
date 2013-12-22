from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world!<br><a href=\"about/\">About page</a>")

def about(request):
    return HttpResponse("Rango says: Here is the about page.<br><a href=\"..\">Main page</a>")

