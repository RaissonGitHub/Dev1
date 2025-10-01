from django.contrib import admin
from aula.models import Atividade, AtividadeAdmin, Local, LocalAdmin, Avaliacao, AvaliacaoAdmin, Perfil, PerfilAdmin

# Register your models here.
admin.site.register(Atividade, AtividadeAdmin)
admin.site.register(Local,LocalAdmin)
admin.site.register(Avaliacao,AvaliacaoAdmin)
admin.site.register(Perfil,PerfilAdmin)

