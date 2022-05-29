from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import Blog

class DateInput(forms.DateInput):
    input_type: 'date'

class BlogForm(forms.ModelForm):  
    class Meta:  
        model = Blog
        fields = "__all__"  
        widgets={
            'my_date':DateInput()
        }