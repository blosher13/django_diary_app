from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

def index(request):
    entries = Entry.objects.order_by('-date_posted') # provides all the objects for Entry

    context = {'entries' : entries} # create a dictionary and make context available in templates

    return render(request, 'entries/index.html', context)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save() # save data to db
            return redirect('home') # send data to home
    else:
        form = EntryForm() #instatiate EntryForm object

    context = {'form': form}

    return render(request, 'entries/add.html', context)