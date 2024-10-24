from django.shortcuts import render
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib import messages
import random

import difflib

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea, label="Content")

class EditPageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label="Content")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entries": util.list_entries(),
        "content": util.get_entry(title)
    })

def search(request):
    query = request.GET.get('q')
    entries = util.list_entries()

    if query in entries:
        entry_url = reverse('entry', args=[query])
        return HttpResponseRedirect(entry_url)
    else:
        
        similar_entries = difflib.get_close_matches(query, entries)

        return render(request, "encyclopedia/not_found.html", {
            "query": query,
            "entries": entries,
            "similar_entries": similar_entries
        })

def new(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid() and form.cleaned_data["title"] not in util.list_entries():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", args=[title]))
        else:
            if form.cleaned_data["title"] in util.list_entries():
                messages.error(request, "An entry with this title already exists.")
            else:
                messages.error(request, "Invalid form submission.")
            return render(request, "encyclopedia/new.html", {
                "form": form
            })
    return render(request, "encyclopedia/new.html", {
        "form": NewPageForm()
    })

def edit(request, title):
    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", args=[title]))
    return render(request, "encyclopedia/edit.html", {
        "form": EditPageForm(),
        "title": title,
        "content": util.get_entry(title)
    })

def random_page(request):
    random_page = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("entry", args=[random_page]))