from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class Validar:
    def __init__(self, cod):
        self.cod = cod
       
   
    def __call__(self, valor):
        raise ValidationError(_(''),params={"valor":valor},code='invalid')
   
    def __eq__(self, value):
        return(
            isinstance(value, Validar) and self.cod == value.cod
        )


    