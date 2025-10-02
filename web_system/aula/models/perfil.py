from django.db import models
from .base import Base
from ..enumarations import Genero
from django.contrib import admin
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator, MinLengthValidator


class Perfil(Base):
    data_nascimento = models.DateField(verbose_name="Data de nascimento",
                                       help_text="Digite a data de nascimento")
    
    bio = models.TextField(help_text="Digite a biografia do perfil", 
                           max_length=255,
                           validators=[MaxLengthValidator(255)])

    passaporte = models.TextField(help_text="Digite o número do passaporte",
                                  max_length=10, 
                                  validators=[MaxLengthValidator(10)])
    
    genero = models.CharField(max_length=20,
                              choices=Genero,
                              default=Genero.NOT_SPECIFIED,
                              verbose_name="Gênero",
                              help_text="Selecione o gênero",
                              validators=[MaxLengthValidator(20)])

    cidade = models.TextField(max_length=255, 
                              help_text="Digite a cidade atual",
                              validators=[MaxLengthValidator(255), MinLengthValidator(3)])

    pais = models.CharField(max_length=20, 
                            help_text="Digite o país do perfil", 
                            verbose_name="País",
                            validators=[MaxLengthValidator(20), MinLengthValidator(3)])

    def __str__(self):
        return f"{self.id} " 


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id','data_nascimento','passaporte','cidade','pais')
    # readonly_fields = ('data_nascimento',)
    search_fields = ('passaporte',)
    list_filter = ('data_nascimento', 'cidade', 'pais')