# Semana 6 | Slide 11
# Organização: Validadores exibidos no slide 5.
import re

def validar_email(email):
    """Valida formato de email."""
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))

def validar_cpf(cpf):
    """Valida formato de CPF (000.000.000-00)."""
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.match(padrao, cpf))
