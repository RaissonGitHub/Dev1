from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from relacionamentos.models.reporter import Reporter
from relacionamentos.forms.reporter import ReporterForm


class ReporterListView(View):
    @staticmethod
    def get(request):
        reporters = Reporter.objects.all()
        context = {"reporters":reporters}
        return render(request, "reporter/list.html", context) 
    
class ReporterDetailView(View):
    @staticmethod
    def get(request,pk):
        reporter = Reporter.objects.get(id=pk)
        context = {"reporter":reporter}
        return render(request, "reporter/read.html", context)
    
class ReporterCreateView(View):
    @staticmethod
    def get(request):
        form = ReporterForm()
        context = {
            'form':form
        }
        return render(request, 'reporter/create.html', context)
    def post(request):
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter_view_list')
        context = {
            'form':form
        }
        return render(request, 'reporter/create.html', context)

   