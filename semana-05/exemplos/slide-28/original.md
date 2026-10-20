# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 28

```python
class IdadeInvalidaError(Exception):
    """Exceção para idade menor que 18."""
    pass

def validar_idade(idade):
    if idade < 18:
        raise IdadeInvalidaError(f"Idade {idade} é menor que 18.")
    return True

try:
    validar_idade(15)
except IdadeInvalidaError as e:
    print(f"Erro: {e}")
else:
    print("Idade válida.")
```
