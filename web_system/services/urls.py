from django.urls import path
from services.views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
# from services.views.person import PersonService, PersonListService

app_name = 'services'

# router = routers.DefaultRouter()
urlpatterns = [
    path('', api_root, name="api-root"),
    path('saudacao', saudacao, name="saudacao"),
    path('saudacao/classe', ExemploSaudacao.as_view(), name="saudacao_classe"),
    path('calculo',calculo, name="calculo"),

]
