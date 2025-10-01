from django.db import models
from .base import Base
from django.utils.translation import gettext_lazy as _


class Magazine(Base):

    title = models.CharField(max_length=30,
                             help_text=_("Digite o título"),
                             verbose_name=_("Title"))
    
    def __str__(self):
        return self.title