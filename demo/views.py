import json
from demo.archetypes import archetypes
from django.http import HttpResponse
from django.shortcuts import render
from demo.forms import *
import datetime

# Create your views here.

def main(request):
    print(get_data())
    return render(request, 'main.html', {'form': MainForm()})

def get_results(request):
    pass
    """
    file = open('demo/oceny.json')
    data = json.loads(file.read())
    form = MainForm(request.GET)
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
    return render(request, 'archetype.html', archetypes[best_index].get_context_data())
    """

sql_query = """
SELECT * FROM OPENQUERY(DMServer,
'SELECT
  (Predict([Student].[ALG])) as [alg],
  PredictProbability([Student].[ALG])
From
  [Student]
NATURAL PREDICTION JOIN
(SELECT 10 AS [AKS],
  10 AS [Analiza1],
  10 AS [Analiza2],
  %s AS [ASD],
  10 AS [BD],
  10 AS [BSK],
  10 AS [GAL],
  10 AS [IO],
  10 AS [IPP],
  10 AS [JAO],
  10 AS [JNP1],
  10 AS [JNP2],
  10 AS [JNP3],
  10 AS [JPP],
  10 AS [MD],
  10 AS [MNUM],
  10 AS [Pmat],
  10 AS [PO],
  10 AS [R Pi S],
  10 AS [SIK],
  10 AS [SO],
  10 AS [SWP],
  10 AS [TINF],
  10 AS [WP],
  10 AS [WWW]) AS t');
"""

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
def get_data():
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute(sql_query, [[10,10]])
    list = dictfetchall(cursor)
    return list


