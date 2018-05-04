from django import forms
from .models import *

class EntryForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    date = forms.DateTimeField()
    description = forms.CharField(widget = forms.Textarea())
    class Meta:
    	model = Entry
    	fields = ('__all__')