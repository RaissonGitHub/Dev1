import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def valida_cpf(cpf):
    """
    Valida um CPF.
    Remove caracteres não numéricos e verifica se o número
    é válido de acordo com os dígitos verificadores e
    se não é uma sequência de números repetidos.
    """
    # Remove pontos e traço
    cpf_limpo = re.sub(r'[^0-9]', '', cpf)
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf_limpo) != 11:
        raise ValidationError(_("O CPF deve conter 11 dígitos."))
    
    # Verifica se o CPF é uma sequência de números repetidos
    # como 111.111.111-11
    if len(set(cpf_limpo)) == 1:
        raise ValidationError(_("CPF com números repetidos é inválido."))
    
    # Calcula e valida o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf_limpo[i]) * (10 - i)
    
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
        
    if resto != int(cpf_limpo[9]):
        raise ValidationError(_("O CPF é inválido."))
        
    # Calcula e valida o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf_limpo[i]) * (11 - i)
        
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
        
    if resto != int(cpf_limpo[10]):
        raise ValidationError(_("O CPF é inválido."))