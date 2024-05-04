from django.http import HttpResponse
from django.shortcuts import redirect, render

def index(request, *args, **kwargs):
    return render(request, "index.html")

def singlepet(request, *args, **kwargs):
    return render(request, "singlepet.html")