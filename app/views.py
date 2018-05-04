from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry
from .forms import EntryForm
# Create your views here.

def home(request):
    entries = Entry.objects.all()
    return render(request, 'index.html', {'entries': entries})

def details(request, id):
    entry = Entry.objects.get(id=id)
    return render(request, 'details.html', {'entry': entry})

def add_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            Entry.objects.create(
                name=name, date=date, description=description
            ).save
            return redirect('home')
    else:
        form = EntryForm()
    return render(request, 'entry_form.html', {'form': form})

def delete_entry(request, id):
    entry = get_object_or_404(Entry, id=id)
    if request.method == 'POST':
        entry.delete()
        return redirect('/')
    return render(request, 'delete.html', {'entry':entry})