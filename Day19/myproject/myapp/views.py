from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
    return render(request,'index.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Contact(name=name,email=email).save()
        
    return render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')