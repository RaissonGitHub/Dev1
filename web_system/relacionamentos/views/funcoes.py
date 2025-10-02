from django.shortcuts import render, redirect, HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers import serialize
from datetime import datetime
from django.views import View
from relacionamentos.models.reporter import Reporter

def primeira_view(request):
    mensagem = "Bom dia"
    return HttpResponse(mensagem, status=200)

def saudacao(request):
    agora = datetime.now()
    mensagem = "boa noite"
    if 12 > agora.hour > 6:
        mensagem ="bom dia"
    elif 0 < agora.hour <=6:
        mensagem = "boa madrugada"

    completo = f"<html><body><h1>{mensagem.capitalize()}  visitante!<br /> {agora}</h1>{request.META["REMOTE_ADDR"]}</body></html>"
    return HttpResponse(completo)

def nome(request, nome):
    reporter = Reporter.objects.find_by_name(nome)
    objeto = serializers.serialize('python', reporter)
    return JsonResponse(objeto, safe=False)
    #return HttpResponse(reporter, status=200)