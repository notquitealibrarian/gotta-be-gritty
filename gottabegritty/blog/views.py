from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("The blog is up and running!  So much to do...")