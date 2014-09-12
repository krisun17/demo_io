import json
import django
from demo.archetypes import archetypes
from django.http import HttpResponse
from django.shortcuts import render
from demo.forms import *
import datetime
from django.template import *;

# Create your views here.

def main(request):
    if request.method == 'POST'
        form = MainForm(request.POST) 
        if form.is_valid():
            print(get_data({
                'Analiza1' : form.cleaned_data['Analiza1'],
                'Pmat' : form.cleaned_data['PMAT'],
                'WPI' : form.cleaned_data['WP'],
                'GAL' : form.cleaned_data['GAL'],
                'Analiza2' : form.cleaned_data['AM2'],
                'MD' : form.cleaned_data['MD'],
                'IPP' : form.cleaned_data['IPP'],
                'PO' : form.cleaned_data['PO'],
                'AKS' : form.cleaned_data['AKS'],
                'JNP1' : form.cleaned_data['JNP1'],
                'ASD' : form.cleaned_data['ASD'],
                'RPiS' : form.cleaned_data['RPiS'],
                'BD' : form.cleaned_data['BD'],
                'SO' : form.cleaned_data['SO'],
                'SIK' : form.cleaned_data['SIK'],
                'JAO' : form.cleaned_data['JAO'],
                'WWW' : form.cleaned_data['WWW'],
                'IO' : form.cleaned_data['IO'],
                'JNP2' : form.cleaned_data['JNP2'],
                'Pmat' : form.cleaned_data['PMAT']
                #do tego slownika trzeba wrzucic wyniki formularza
            }))
            # return HttpResponseRedirect('/thanks/')
    else
        form = MainForm()
    
    return render(request, 'main.html', {'form': MainForm()})

def get_results(request):
    pass

sql_query = Template("""
SELECT * FROM OPENQUERY(DMServer,
'SELECT
  (Predict([Student].[ALG])) as [alg],
  PredictProbability([Student].[ALG])
From
  [Student]
NATURAL PREDICTION JOIN
(SELECT {{ AKS }} AS [AKS],
  {{ Analiza1 }} AS [Analiza1],
  {{ Analiza2 }} AS [Analiza2],
  {{ ASD }} AS [ASD],
  {{ BD }} AS [BD],
  {{ BSK }} AS [BSK],
  {{ GAL }} AS [GAL],
  {{ IO }} AS [IO],
  {{ IPP }} AS [IPP],
  {{ JAO }} AS [JAO],
  {{ JNP1 }} AS [JNP1],
  {{ JNP2 }} AS [JNP2],
  {{ JNP3 }} AS [JNP3],
  {{ JPP }} AS [JPP],
  {{ MD }} AS [MD],
  {{ MNUM }} AS [MNUM],
  {{ Pmat }} AS [Pmat],
  {{ PO }} AS [PO],
  {{ RPiS }} AS [RPiS],
  {{ SIK }} AS [SIK],
  {{ SO }} AS [SO],
  {{ SWP }} AS [SWP],
  {{ TINF }} AS [TINF],
  {{ WP }} AS [WP],
  {{ WWW }} AS [WWW]) AS t');
""")

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
def get_data(dict):
    from django.db import connection
    cursor = connection.cursor()
    c = Context(dict)
    cursor.execute(sql_query._render(c))
    list = dictfetchall(cursor)
    return list


