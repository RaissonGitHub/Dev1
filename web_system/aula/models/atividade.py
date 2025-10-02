from .base import Base
from django.db import models
from django.contrib import admin
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator, MinLengthValidator, DecimalValidator
from django.core.exceptions import ValidationError



class Atividade(Base):
    # Salvar textos
    nome = models.CharField(max_length=100,
                            help_text="Digite o nome da atração")
    # Salvar valores monetários
    # verbose_name muda o nome
    # help_text é um texto que fica em baixo do campo como ajuda para o usuário
    # Null para valor nulo (banco), Blank para ser nulo (frontend)
    turno = models.CharField(max_length=8,
                             null=True,
                             blank=True,
                             help_text="Digite o turno em que a atração ocorre",
                             validators=[MaxLengthValidator(8)])
    
    nota = models.FloatField(default=0.0,
                             help_text="Deixe uma nota para a atração",
                             validators=[MaxValueValidator(5),MinValueValidator(1)])

    duracao = models.IntegerField(default=0,
                                  help_text="Digite a duração da atração em minutos",
                                  verbose_name="Duração",
                                  validators=[MinValueValidator(0)])
    
    ingresso = models.BooleanField(default=False,
                                   help_text="A atração possui ingresso pago?")
    
    valor = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                default=0.00,
                                help_text="Digite o valor da atração em reais. R$ ",
                                validators=[DecimalValidator(10,2)])
    
    informacoes = models.TextField(default='',max_length=500,
                                   help_text="Digite as informações sobre a atração",
                                   verbose_name="Informações",
                                   validators=[MaxLengthValidator(500)],
                                   )
    
    guia = models.BooleanField(default=False,
                               help_text="A atração possui guia?")
    
    endereco = models.CharField(default='',
                                max_length=200,
                                help_text="Digite o endereço da atração",
                                verbose_name="Endereço",
                                validators=[MaxLengthValidator(200), MinLengthValidator(5)])
    
    participantes = models.IntegerField(default=0,
                                        help_text="Digite o número de participantes da atração")


    def __str__(self):
        return f"{self.id} - {self.nome}"
    
    def save(self,*args, **kwargs):
        if self.informacoes is None or self.informacoes == '':
            self.informacoes = f'{self.nome} ainda não cadastrou informações.'
        super().save(*args,**kwargs)

    def clean(self):
        if self.ingresso == False and self.valor >0:
            raise ValidationError(message={"valor":'Não pode cobrar valor se não há ingresso'},code="error001")

 # def save(self, *args, **kwargs):
    #    if self.cod is None or self.cod == '':
    #        letters = string.ascii_letter + string.digits
    #        self.cod = ''.join(random.choice(letters) for i in range(10))
    # super().save(*args,**kwargs)

class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('id','nome','turno','nota')
    search_fields = ("nome",)
    list_filter = ('nome','nota')
