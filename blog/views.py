from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#----------------------------------------------------------------

def home(request):
    return HttpResponse('hoooo')

#----------------------------------------------------------------

def api(request):

    data={
        "article1":{ "title":"time",
        "slug":"wewr",
        "f":"b",
        "kjbdk":4,},
        "article11":{ "title":"hu",
        "dec":"wewr",
        "f":"b",
        "kjbdk":4,},
        "article12":{ "title":"hu",
        "dec":"wewr",
        "f":"b",
        "kjbdk":4,},
        "article13":{ "title":"hu",
        "df":"wewr",
        "f":"b",
        "kjbdk":4,},
        "article14":{ "title":"hu",
        "trrrrrrr":"wewr",
        "f":"b",
        "kjbdk":4,},
    }
    return JsonResponse(data)