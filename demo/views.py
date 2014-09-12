from django.shortcuts import render
from django.template import *

from demo.forms import *


# Create your views here.

def main(request):
    form = MainForm()
    return render(request, 'main.html', {'form': MainForm()})

def get_results(request):

    form = MainForm(request.GET)
    res = None
    if form.is_valid():
        res = get_data({
            'Analiza1' : form.cleaned_data['AM1'],
            'WP' : form.cleaned_data['WPI'],
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
        })
    return render(request, 'display.html', {'res': res[0]})
    #return render(request, 'archetype.html', archetypes[best_index].get_context_data())

sql_query = Template("""
SELECT * FROM OPENQUERY(DMServer,
'SELECT
 """
########################################
#tylko to zmieniamy
##################################
 """
  (Predict([Student].[ALG])) as [ALG],
  (Predict([Student].[ALT])) as [ALT],
  (Predict([Student].[BO])) as [BO],
  (Predict([Student].[PLO])) as [PLO],
  (Predict([Student].[SID])) as [SID],
  (Predict([Student].[SUS])) as [SUS],
  (Predict([Student].[TINF])) as [TINF],
  (Predict([Student].[WSS])) as [WSS],
  (Predict([Student].[WWK])) as [WWK],
  (Predict([Student].[ZBD])) as [ZBD],
  (Predict([Student].[ZSO])) as [ZSO]
"""
                     # ##########################
                     #dotad
                     ###########################
 """
From
  [Student]
NATURAL PREDICTION JOIN
(SELECT {{ AKS }} AS [AKS],
  {{ Analiza1 }} AS [Analiza1],
  {{ Analiza2 }} AS [Analiza2],
  {{ ASD }} AS [ASD],
  {{ BD }} AS [BD],
  {{ GAL }} AS [GAL],
  {{ IO }} AS [IO],
  {{ IPP }} AS [IPP],
  {{ JAO }} AS [JAO],
  {{ JNP1 }} AS [JNP1],
  {{ JNP2 }} AS [JNP2],
  {{ MD }} AS [MD],
  {{ Pmat }} AS [Pmat],
  {{ PO }} AS [PO],
  {{ RPiS }} AS [RPiS],
  {{ SIK }} AS [SIK],
  {{ SO }} AS [SO],
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


