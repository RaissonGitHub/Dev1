from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from relacionamentos.models.reporter import Reporter
from relacionamentos.forms.reporter import ReporterForm
import random
import string


class ReporterListView(View):
    @staticmethod
    def get(request):
        reporters = Reporter.objects.all()
        context = {"reporters":reporters}
        return render(request, "reporter_classe/list.html", context) 
    
class ReporterDetailView(View):
    @staticmethod
    def get(request,pk):
        reporter = Reporter.objects.get(id=pk)
        context = {"reporter":reporter}
        return render(request, "reporter_classe/read.html", context)
    
class ReporterCreateView(View):
    @staticmethod
    def get(request):
        form = ReporterForm()
        context = {
            'form':form
        }
        return render(request, 'reporter_classe/create.html', context)
    
    @staticmethod
    def post(request):
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter_view_list')
        context = {
            'form':form
        }
        return render(request, 'reporter_classe/create.html', context)


class ReporterGenerateCode(LoginRequiredMixin,  PermissionRequiredMixin, View ):
    login_url = 'accounts:login'
    permission_required = 'relacionamentos.generate_code_reporter'
    @staticmethod
    def get(request, pk):
        reporter = get_object_or_404(Reporter, pk=pk)
        try:
            letters = string.ascii_letters +string.digits
            reporter.cod = "".join(random.choice(letters) for i in range(10))
            reporter.save()
            return redirect('relacionamentos:reporter_view_generate_code')
        except:
            print(f"Erro ao gerar código para reporter {reporter}")
            return redirect('relacionamentos:reporter')
        
class ReporterUpdateView(View):
    @staticmethod
    def get(request, pk):
        reporter = get_object_or_404(Reporter, pk=pk)
        form = ReporterForm(instance=reporter)
        context = {
            'form': form,
            'reporter': reporter,
        }
        return render(request, 'reporter_classe/update.html', context)

    @staticmethod
    def post(request,pk):
        reporter = get_object_or_404(Reporter, pk=pk)
        form = ReporterForm(request.POST, instance=reporter)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter')

class ReporterDeletelView(View):
    @staticmethod
    def get(request, pk):
        reporter = get_object_or_404(Reporter, pk=pk)
        try:
            context ={'reporter': reporter}
            return render(request, 'reporter_classe/delete.html', context)
        except Exception as e:
            print(e)
            context = {}
            return render(request, "reporter_classe/list.html", context) 
    @staticmethod
    def post(request,pk):
        reporter = get_object_or_404(Reporter, pk=pk)
        try:
            v_reporter_id = request.POST.get("reporter_id",None)
            if int(v_reporter_id) == pk:
                reporter.delete()
                return redirect('relacionamentos:reporter_view_list')
        except Exception as e:
            print(e)
            context = {}
            return render(request, "reporter_classe/list.html", context) 


