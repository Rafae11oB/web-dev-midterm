from django import forms
from .models import Task
from django.forms.widgets import DateInput

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        widgets = {
            'due_date': DateInput(attrs={'type': 'date'})
        }
