from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def tem_coreia(titulo):
    try:
        if "Coreia Do Norte".lower() in titulo.lower():
            raise ValidationError(_("Não pode ter Coreia do Norte"),params={'endereco':titulo})
    except ValueError:
        pass
