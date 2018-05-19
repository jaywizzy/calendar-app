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

def edit_entry(request, id):
    entry = get_object_or_404(Entry, id=id)
    if request.method == 'POST':
        form = EntryForm(request.POST or None, instance = entry)
        if form.is_valid():                    
            form.save()
            return redirect('home')
    else:
        form = EntryForm(instance=entry)
    return render(request, 'edit.html', {'form': form, 'entry':entry})

    # product = Product.objects.get(id=id)
    # form = ProductForm(request.POST or None, instance=product)
    # if form.is_valid():
    #     form.save()
    #     return redirect('products_list')

    # return render(request, 'products_form.html', {'form': form, 'product': product})
    
def delete_entry(request, id):
    entry = get_object_or_404(Entry, id=id)
    if request.method == 'POST':
        entry.delete()
        return redirect('/')
    return render(request, 'delete.html', {'entry':entry})
