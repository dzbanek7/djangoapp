from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("Witaj w barze Pizza!")
    return render(request, 'pizza/index.html')

def news(request):
    return HttpResponse("<h1>Nowości w barze</h1>")

def lokal(request):
    return HttpResponse("<h1>Lokalizacja baru</h1>")