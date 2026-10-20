# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 44

```python
def total(*precos, desc=0):
    s = sum(precos)
    return s * (1 - desc / 100)

print(total(10, 25.5, 7))
# 42.5

print(total(10, 25.5, 7, desc=10))
# 38.25
```
