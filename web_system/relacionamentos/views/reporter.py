import random
import string
from ..models.reporter import Reporter
from django.shortcuts import get_object_or_404, render, redirect
from ..forms.reporter import ReporterForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import permission_required, login_required

@login_required
@permission_required("relacionamentos.view_reporter", raise_exception=True)
@require_http_methods(['GET',])
def reporter_list(request):
    reporters = Reporter.objects.all()
    context = {"reporters":reporters}
    return render(request, "reporter/list.html", context) 

@require_http_methods(['GET', 'POST'])
def reporter_detail(request,pk):    
    reporter = Reporter.objects.get(id=pk)
    context = {"reporter":reporter}
    return render(request, "reporter/read.html", context)


@require_http_methods(['GET', 'POST'])
def reporter_create(request):
    if request.method == "POST":
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter')
    else:
        form = ReporterForm()
    context = {
        'form':form
    }
    return render(request, 'reporter/create.html', context)

@require_http_methods(['GET', 'POST'])
def reporter_delete(request,pk):    
    reporter = get_object_or_404(Reporter, pk=pk)
    try:
        if request.method == "POST":
            v_reporter_id = request.POST.get("reporter_id",None)
            if int(v_reporter_id) == reporter.id:
                reporter.delete()
                return redirect('relacionamentos:reporter')
        else:
            context ={'reporter': reporter}
    except Exception as e:
        print(e)
        context = {}
        return render(request, "reporter/list.html", context) 

    return render(request, "reporter/delete.html", context)

@require_http_methods(['GET', 'POST'])
def reporter_code(request, reporter_id):
    reporter = get_object_or_404(Reporter, pk=reporter_id)
    try:
        letters = string.ascii_letters +string.digits
        reporter.cod = "".join(random.choice(letters) for i in range(10))
        reporter.save()
        return redirect('relacionamentos:reporter')
    except:
        print(f"Erro ao gerar código para reporter {reporter}")
        return redirect('relacionamentos:reporter')

@require_http_methods(['GET', 'POST'])
def reporter_update(request, reporter_id):
    reporter = get_object_or_404(Reporter, pk=reporter_id)
    if request.method == "POST":
        form = ReporterForm(request.POST, instance=reporter)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter')
    else:
        form = ReporterForm(instance=reporter)
    context = {
        'form': form,
        'reporter': reporter,
    }
    return render(request, 'reporter/update.html', context)
