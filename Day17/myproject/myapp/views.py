from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse(f'<h1> WELCOME </h1>')

def about(request):
    return HttpResponse(f'<h1> ABOUT </h1>')

def contact(request):
    return HttpResponse(f'<h1> CONTACT </h1>')