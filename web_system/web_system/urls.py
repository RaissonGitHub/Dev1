from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from web_system import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relacionamentos/', include('relacionamentos.urls', namespace="relacionamentos")),
    path('', views.estaticas.index, name="index"),
    #path('funcao/contato/', views.contact, name="function_contact")
    #path('funcao/search/', , name="search_function"),

]
