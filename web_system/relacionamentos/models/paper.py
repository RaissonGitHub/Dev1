from django.db import models
from .base import Base
from django.utils.translation import gettext_lazy as _
from .reporter import Reporter
from .magazine import Magazine
from ..validators.coreia import tem_coreia


class Paper(Base): 

    title = models.CharField(max_length=100,
                             help_text=_("Digite o título do artigo"),
                             verbose_name=_("Title"),
                             validators=[tem_coreia])
    
    pub_date = models.DateField(verbose_name='Publication Date',
                                help_text=_("Digite a data de publicação do artigo"))
    
    reporter = models.ForeignKey(Reporter, on_delete=models.RESTRICT)

    magazines = models.ManyToManyField(Magazine, 
                                       blank=True,
                                       through="Publication",
                                       through_fields=("paper","magazine"))

    def __str__(self):
        return f'{self.title} by {self.reporter.name}'
