from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "Pages/Homepage.html")

def product(request):
    return render(request,"Pages/Products.html")