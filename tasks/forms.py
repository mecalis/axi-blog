from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    task_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Új feladat felvétele...'}))
    class Meta:
        model= Task
        fields = '__all__'

class TaskListModel3Form(forms.ModelForm):
    list_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Új feladatlista felvétele...'}))
    class Meta:
        model= TaskListModel3
        fields = '__all__'

class Task3Form(forms.ModelForm):
    task_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Új feladat felvétele...'}))
    class Meta:
        model= Task3
        fields = '__all__'
