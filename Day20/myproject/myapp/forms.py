from .models import Registration
from django import forms

class ModelFormRegistration(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        