import json
from demo.archetypes import archetypes
from django.http import HttpResponse
from django.shortcuts import render
from demo.forms import *
import datetime

# Create your views here.

def main(request):
    return render(request, 'main.html', {'form': MainForm()})

def get_results(request):
    file = open('demo/oceny.json')
    data = json.loads(file.read())
    form = MainForm(request.POST)
    form.is_valid()
    scores = {}
    for key in form.cleaned_data:
        res = form.cleaned_data[key]
        if (not res):
            res = '1'
        scores[key] = data[res][key]

    max_score = 0.0
    best_index = 0
    for i in range(len(archetypes)):
        score = archetypes[i].get_score(scores)
        if (score >= max_score):
            max_score = score
            best_index = i
    return HttpResponse(archetypes[i].desc())

