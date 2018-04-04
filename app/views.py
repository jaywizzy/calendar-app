from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Entry
from .forms import EntryForm
# Create your views here.

def home(request):
    entries = Entry.objects.all()
    return render(request, 'index.html', {'entries': entries})

def details(request, id):
    entry = Entry.objects.get(id=id)
    return render(request, 'details.html', {'entry': entry})

def create(request):
	if request.method == 'POST':
		form = EntryForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			date = form.cleaned_data['date']
			desc = form.cleaned_data['description']
			Entry.objects.create(
				name = name, date = date, description = desc
			).save()
			return HttpResponseRedirect('/')
	else:
		form = EntryForm()
	return render(request, 'create.html', {'form': form})

def delete(request, pk):
	if request.method == 'DELETE':
		entry = get_object_or_404(Entry, pk=pk)
		entry.delete()
	return HttpResponseRedirect('/')

