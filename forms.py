from django import forms
from django.forms import ModelForm
from .models import Appointments

class SchedulingForm(ModelForm):
    class Meta:
        model = Appointments
        fiels = ['date', 'time', 'service']
        widgets = {
            'date' : forms.DateInput(attrs={'type': 'date'}),
            'time' : forms.TimeInput(attrs={'type': 'time'}),

        }