from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    task_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Új feladat felvétele...'}))
    class Meta:
        model= Task
        fields = '__all__'
