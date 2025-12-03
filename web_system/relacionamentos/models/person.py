from django.db import models
from .base import Base
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.core.exceptions import ValidationError
from ..validators.validar_cpf import valida_cpf


class Person(Base):
    name = models.CharField(max_length=100,
                            validators=[MinLengthValidator(3)],
                            help_text=_('Digite o nome'),
                            verbose_name=_('Name'))
    
    birthdate = models.DateField(help_text=_('Digite a data de nascimento'),
                                 verbose_name=_('Birthdate'))

    cpf = models.CharField(max_length=11,
                           validators=[MinLengthValidator(11), valida_cpf],
                           help_text='Digite o CPF',
                           unique=True)
    
    def __str__(self):
        return self.name
    
    def clean(self):
        today = date.today()

        try:
            if self.birthdate > today.replace(year=today.year - 18):
                raise ValidationError({'birthdate': _("You must be 18 years old.")}, 
                                      code="error1")
            
        except ValueError:
            pass