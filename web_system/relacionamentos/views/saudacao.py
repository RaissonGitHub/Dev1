from datetime import datetime
from django.shortcuts import render
from django.views import View
class SaudacaoView(View):
    @staticmethod
    def get(request):
        agora = datetime.now()
        mensagem = "boa noite"
        if 12 > agora.hour > 6:
            mensagem ="bom dia"
        elif 0 < agora.hour <=6:
            mensagem = "boa madrugada"

        #completo = f"<html><body><h1>{mensagem.capitalize()}  visitante!<br /> {agora}</h1>{request.META["REMOTE_ADDR"]}</body></html>"
        return render(request, "saudacao.html", {"mensagem":f"{mensagem.capitalize()} visistante! ","agora":f"{agora}", "user":f"{request.META["REMOTE_ADDR"]}"})