from .base import Base
from django.db import models
from django.contrib import admin
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator, MinLengthValidator
from django.core.exceptions import ValidationError


class Avaliacao(Base):
    titulo = models.CharField(max_length=100, 
                              help_text='Digite o título da avaliação',
                              validators=[MaxLengthValidator(100)])
    
    data_avaliacao = models.DateField(verbose_name='Data da avaliação',
                                      help_text='Digite a data da avaliação')

    data_visita = models.DateField(verbose_name='Data da visita',
                                   help_text='Digite a data da visita')

    comentario = models.TextField(verbose_name='Comentário',
                                  help_text='Digite o comentário da avaliação')

    nota = models.IntegerField(help_text='Digite a nota da avaliação',
                               validators=[MinValueValidator(1),MaxValueValidator(5)] )

    acompanhantes = models.CharField(max_length=20, 
                                     help_text='Digite os acompanhantes da avaliação',
                                     validators=[MaxLengthValidator(20)])
    
    likes = models.IntegerField( help_text='Número de likes da avaliação',
                                validators=[MinValueValidator(0)])


    def __str__(self):
        return f'{self.id} - {self.titulo}'   
    
   

    def clean(self):
        if self.data_avaliacao < self.data_visita:
            raise ValidationError(message={'data_avaliacao':"A data de avaliacao deve ser posterior a data da visita"},code='error002')

# classe para interface do django admin
class AvaliacaoAdmin(admin.ModelAdmin):
    # colunas que aparecerao na tabela
    list_display = ('id','titulo', 'data_avaliacao','data_visita','likes','nota',)
    # campo usado para filtrar
    search_fields = ('titulo',)
    # campos para o menu lateral
    list_filter = ('data_avaliacao', 'data_visita', 'likes',)
    # campos imutaveis
    # readonly_fields = ('data_avaliacao','data_visita')
