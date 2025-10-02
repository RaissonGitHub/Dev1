from django.shortcuts import render, redirect, HttpResponse
# from django.core import serializers
# from django.http import JsonResponse
# from django.core.serializers import serialize
# from datetime import datetime
# from django.views import View

def primeira_view(request):
    mensagem = "Bom dia"
    return HttpResponse(mensagem, status=200)