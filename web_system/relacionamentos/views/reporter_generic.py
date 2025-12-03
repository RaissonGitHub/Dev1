from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView, ListView, DetailView
from relacionamentos.models.reporter import Reporter
from relacionamentos.forms.reporter import ReporterForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ReporterGenericListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Reporter
    template_name = "reporter/list.html"
    permission_required = "relacionamentos.view_reporter"
    # Nome que é passado para o template Ex: usado no for
    context_object_name = "reporters"
    # A consulta normal seria Classe.objects.all()
    # Se quiser usar uma consulta nao tao generica
    queryset = Reporter.objects.find_by_name("Joao")

    # Outra implementação do queryset (vai sobrescrever a variavel se os dois existirem)
    def get_queryset(self):
        objetos = Reporter.objects.find_by_name("Joao")
        outros_objetos = Reporter.objects.find_by_name("Pedro")
        objetos = objetos.union(outros_objetos)
        return objetos

class ReporterGenericDetailView(DetailView):
    model = Reporter
    fields = "__all__"
    template_name = "reporter/read.html"
    # url para voltar
    success_url = reverse_lazy("relacionamentos:reporter_generic_class_list")

class ReporterGenericDeleteView(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    permission_required = "relacionamentos.delete_reporter"
    model = Reporter
    fields = "__all__"
    template_name = "reporter/delete.html"
    # url para voltar
    success_url = reverse_lazy("relacionamentos:reporter_generic_class_list")

class ReporterGenericCreateView(CreateView):
    model = Reporter
    form_class = ReporterForm
    template_name = "reporter/create.html"
    # url para voltar
    success_url = reverse_lazy("relacionamentos:reporter_generic_class_list")

class ReporterGenericUpdateView(UpdateView):
    model = Reporter
    form_class = ReporterForm
    template_name = "reporter/update.html"
    # url para voltar
    success_url = reverse_lazy("relacionamentos:reporter_generic_class_list")

