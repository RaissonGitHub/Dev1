from django.urls import path
import relacionamentos.views as views

app_name = 'relacionamentos'

urlpatterns = [
    path('funcao/teste', views.primeira_view,
         name='primeira_view')
]