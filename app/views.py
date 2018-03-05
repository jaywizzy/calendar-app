from django.shortcuts import render
from .models import Entry
# Create your views here.

def home(request):
    entries = Entry.objects.all()
    return render(request, 'index.html', {'entries': entries})

def details(request, id):
    entry = Entry.objects.get(id=id)
    return render(request, 'details.html', {'entry': entry})
