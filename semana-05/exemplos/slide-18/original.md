# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 18

```python
import re

def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))

def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.match(padrao, cpf))

def validar_telefone(telefone):
    padrao = r"^\(\d{2}\)\s\d{4,5}-\d{4}$"
    return bool(re.match(padrao, telefone))

def validar_data(data):
    padrao = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(padrao, data))

# Testes
print(validar_email("ana@email.com"))       # True
print(validar_cpf("123.456.789-00"))        # True
print(validar_telefone("(11) 91234-5678"))  # True
print(validar_data("2026-08-30"))           # True
```
