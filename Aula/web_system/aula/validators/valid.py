from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def tem_coreia(endereco):
    try:
        if "Coreia Do Norte".lower() in endereco.lower():
            raise ValidationError(_("Não pode ter Coreia do Norte"),params={'endereco':endereco})
    except ValueError:
        pass
