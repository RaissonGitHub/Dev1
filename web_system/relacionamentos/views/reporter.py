from relacionamentos.models.reporter import Reporter
from django.shortcuts import render


def exemplo_list(request):
    exemplos = Reporter.objects.all()

    context = {"exemplos":exemplos}

    return render(request, "reporter/list.html", context) 