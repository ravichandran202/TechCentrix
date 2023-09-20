from django.shortcuts import render
from django.http import HttpResponse
from .forms import ModelFormRegistration
from .models import Registration
# Create your views here.

def home(request):
    form = ModelFormRegistration()
    if request.method == 'POST':
        form = ModelFormRegistration(data=request.POST)
        if form.is_valid():
            form.save()
    
    
    return render(request,'index.html',{
        'form':form,
        'reg_data' : Registration.objects.all()
    })
