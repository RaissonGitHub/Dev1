from django.http import HttpResponse, JsonResponse
from django.views import View
from ..models import Reporter
from django.core import serializers


class NomeView(View):
    @staticmethod
    def get(request,nome):
        if nome == "" or nome == "":
            exemplos = list(Reporter.objects.all())
        else:
            exemplos = Reporter.objects.find_by_name(nome)

        tipo = str(request.GET.get("type"))
        saida = ""
        
        match tipo.lower():
            case "http":
                for exemplo in exemplos:
                    saida += f"<p><b>ID: </b> {exemplo.id}</p>"
                    saida += f"<p><b>Email: </b> {exemplo.email}</p>"
                    saida += f"<p><b>CPF: </b> {exemplo.cpf}</p>"
        
                return HttpResponse(saida, status=200)
            
            case "json":
                objeto = serializers.serialize('python', exemplos)
                return JsonResponse(objeto, safe=False)
            
            case _:
                return HttpResponse("Bad request", status=400)
            