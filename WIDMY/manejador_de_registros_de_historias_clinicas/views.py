from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_historia_clinica as lhc


@csrf_exempt

def historia_clinica_view(request):
    if request.method == 'POST':
        hc_dto = lhc.create_historia_clinica(json.loads(request.body))
        hc = serializers.serialize('json',[hc_dto])
        return HttpResponse(hc,'application/json')    
    
@csrf_exempt
#GET ONE
def historia_clinica_get_one(request, pk):
    if request.method == 'GET':
        hc = lhc.get_HU(pk)
        hc = serializers.serialize('json',[hc,])
        return HttpResponse(hc,'application/json')



@csrf_exempt
def historias_clinicas_list(request):
    hus = lhc.get_HUs()
    context = {
        'historias_clinicas_list': hus
    }
    return render(request, 'Historia_Clinica/historias_clinica.html', context)

@csrf_exempt
def historia_clinica_registro_create(request, pk):
    if request.method =='POST':
        hu_ret =serializers.serialize('json',[hu_ret])
        return HttpResponse(hu_ret,'application/json')


