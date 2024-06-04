from django.shortcuts import render,redirect
from.models import *
#from django.contrib.auth.models import user,auth


def home(request):
    return render(request,'homepage.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def package(request):
    return render(request,'package.html')
def about(request):
    return render(request,'about.html')
