from .base import Base
from django.db import models
from django.contrib import admin
from django.core.validators import MaxLengthValidator, MaxValueValidator, EmailValidator, MinValueValidator, MinLengthValidator, DecimalValidator
from django.core.exceptions import ValidationError
from aula.validators.valid import tem_coreia

class Local(Base):
    nome = models.CharField(max_length=100, 
                            help_text="Digite o nome do local",
                            validators=[MaxLengthValidator(100), MinLengthValidator(3)])
                            
    endereco = models.CharField(verbose_name="Endereço",
                                max_length=200, 
                                help_text="Digite o endereço do local",
                                validators=[MinLengthValidator(5), MaxLengthValidator(200), tem_coreia])
                                
    nota = models.FloatField(default=0.0, 
                             help_text="Deixe uma nota para o local",       
                             validators=[MaxValueValidator(5), MinValueValidator(1)])
                             
    horario_abertura = models.TimeField(help_text="Digite o horário de abertura do local",
                                        verbose_name="Horário de abertura")
    
    horario_fechamento = models.TimeField(help_text="Digite o horário de fechamento do local",
                                          verbose_name="Horário de fechamento")
    
    informacoes = models.TextField(max_length=100, 
                                   help_text="Digite o nome do local",
                                   verbose_name="Informações",
                                   validators=[MaxLengthValidator(200)])
                                   
    ingresso = models.BooleanField(default=False, 
                                   help_text="O local possui ingresso pago?")
                                   
    valor = models.DecimalField(max_digits=10, 
                                decimal_places=2, 
                                default=0.00, 
                                help_text="Digite o valor do local em reais. R$ ",
                                validators=[DecimalValidator(10,2), MinValueValidator(0)])
                                
    acessibilidade = models.BooleanField(default=False, 
                                         help_text="O local possui acessibilidade?")
                                         
    classificacao = models.IntegerField(default=0, 
                                        help_text="Digite a classificação do local",
                                        verbose_name="classificação")
                                        
    contato = models.EmailField(max_length=100, 
                                help_text="Digite o contato do local",
                                validators=[MaxLengthValidator(100),EmailValidator()])


    def __str__(self):
        return f"{self.id} - {self.nome}"   
    
    def clean(self):
        if self.ingresso == False and self.valor > 0:
            raise ValidationError(message={'valor': 'Não pode cobrar valor se não há ingresso'},code="error001")
        
       
        


class LocalAdmin(admin.ModelAdmin):
    list_display = ('id','nome','classificacao')
    search_fields = ('nome',)
    list_filter = ('nome', 'horario_abertura','horario_fechamento')