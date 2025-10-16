from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
class PrimeiraView(View):
    @staticmethod
    def get(request):
        mensagem = request.META["REMOTE_ADDR"]
        #return HttpResponse(mensagem, status=200)
        return render(request, "primeira.html", {"mensagem":mensagem})  