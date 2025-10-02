from django.urls import path
import relacionamentos.views as views_funcoes

app_name = 'relacionamentos'

urlpatterns = [
    path('funcao/teste', views_funcoes.primeira_view,
         name='primeira_view'),
    
    path('funcao/saudacao', views_funcoes.saudacao,
         name="saudacao"),
    
    # Qualquer coisa em string, deve sempre ser por ultimo para nao inutilizar as urls de cima que sao fixas
    # nome é a variavel que vai armazenar o que vem depois de funcao/
    path('funcao/<str:nome>', views_funcoes.nome,
         name="nome")
]