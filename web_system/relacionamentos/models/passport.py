from django.db import models
from .base import Base
from django.utils.translation import gettext_lazy as _
from .person import Person
from datetime import date
from django.core.exceptions import ValidationError


class Passport(Base):

    number = models.CharField(max_length=100,
                              verbose_name=_("Number"),
                              help_text=_("Digite o número do passaporte"),
                              unique=True)
    
    issue_date = models.DateField(verbose_name=_("Issue Date"),
                                  help_text=_("Digite a data da emissão"))
    
    expiration_date = models.DateField(verbose_name=_("Expiration_date"),
                                       help_text=_("Digite a data de expiração"))
    
    owner = models.OneToOneField(Person, 
                                 on_delete=models.CASCADE,
                                 primary_key=True)
    
    def __str__(self):
        return self.number
    
    def clean(self):
        try:
            if self.issue_date > self.expiration_date:
                raise ValidationError(message={"expiration_date": _('Invalid date')}, code='error3')
        except ValueError:
            pass