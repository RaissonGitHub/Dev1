from django.urls import path
from relacionamentos.views.funcoes import primeira_view, saudacao, calculo, exercicio, nome
from relacionamentos.views import PrimeiraView, NomeView

app_name = 'relacionamentos'

urlpatterns = [
    
    path('funcao/teste', primeira_view,
         name='primeira_view'),
    
    path('funcao/saudacao', saudacao,
         name="saudacao"),

    path('funcao/exercicio/calculo/<int:x>/<int:y>', calculo,
         name="calculo"),
    
    path('funcao/exercicio/<str:nome>', exercicio,
         name='exercicio'),

    # Qualquer coisa em string, deve sempre ser por ultimo para nao inutilizar as urls de cima que sao fixas
    # nome é a variavel que vai armazenar o que vem depois de funcao/
    path('funcao/<str:nome>', nome,
         name="nome"),

    path('classe/teste', PrimeiraView.as_view(), name="primeira_view_class"),

    path('classe/<str:nome>', NomeView.as_view(), name="nome_view_class" )
]