from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from web_system.views import estaticas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relacionamentos/', include('relacionamentos.urls')),
    path('', estaticas.index, name="index")
]
