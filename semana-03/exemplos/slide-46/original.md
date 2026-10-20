# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 46

```python
# script_desafio.py
from calculadora import somar, \
                       multiplicar

def orc(qtd, preco, frete=0):
    """Total do pedido."""
    s = multiplicar(qtd, preco)
    return somar(s, frete)

print(orc(3, 49.9, 15))  # 164.7
```
