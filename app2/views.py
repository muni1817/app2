from django.shortcuts import render
from django.http import HttpResponse

def phone(request):
    return HttpResponse('<h1>honor</h1>')
def fav(request):
    return HttpResponse('<marquee>viratkohli</marquee>')
