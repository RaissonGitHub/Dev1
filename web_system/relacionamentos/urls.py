from django.urls import path
from relacionamentos.views.funcoes import primeira_view, saudacao, calculo, exercicio, nome
from relacionamentos.views import PrimeiraView, NomeView, SaudacaoView, ReporterListView, ReporterDetailView, ReporterCreateView, ReporterGenerateCode, ReporterUpdateView, ReporterDeletelView
from relacionamentos.views.reporter import reporter_list, reporter_detail, reporter_delete, reporter_code, reporter_create, reporter_update
from relacionamentos.views.reporter_generic import *

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
     path("reporter/generic_class/list", ReporterGenericListView.as_view(), name="reporter_generic_class_list"),

    # Como esta em generic use sempre pk
     path("reporter/generic_class/read/<int:pk>/", ReporterGenericDetailView.as_view(), name="reporter_generic_class_read"),

     path("reporter/generic_class/delete/<int:pk>/", ReporterGenericDeleteView.as_view(), name="reporter_generic_class_delete"),

     path("reporter/generic_class/update/<int:pk>/", ReporterGenericUpdateView.as_view(), name="reporter_generic_class_update"),

     path("reporter/generic_class/create", ReporterGenericCreateView.as_view(), name="reporter_generic_class_create"),

     path('reporter/function/read/<int:pk>', reporter_detail, name="reporter_read"), 
     
     path('reporter/function/create/', reporter_create, name="reporter_create"),
     
     path('reporter/function/delete/<int:pk>', reporter_delete, name="reporter_delete"), 

     path('reporter/function/update/<int:reporter_id>', reporter_update, name="reporter_update" ),

     path("reporter/function/gerar_codigo/<int:reporter_id>", reporter_code, name="reporter_generate_code"),

     path('reporter/function/', reporter_list, name="reporter"), 

     path('reporter/classe/', ReporterListView.as_view(), name="reporter_view_list" ),
     
     path('reporter/classe/create/', ReporterCreateView.as_view(), name="reporter_view_create"),

     path("reporter/classe/gerar_codigo/<int:pk>", ReporterGenerateCode.as_view(), name="reporter_view_generate_code"),
     
     path('reporter/classe/update/<int:pk>', ReporterUpdateView.as_view(), name="reporter_view_update" ),
          
     path('reporter/classe/read/<int:pk>', ReporterDetailView.as_view(), name="reporter_view_read"), 

     path('reporter/classe/delete/<int:pk>', ReporterDeletelView.as_view(), name="reporter_view_delete"), 

     path('classe/teste/', PrimeiraView.as_view(), name="primeira_view_class"),
     
     path('classe/saudacao/', SaudacaoView.as_view(), name="saudacao_view_class"),

     path('classe/<str:nome>', NomeView.as_view(), name="nome_view_class" ),



]