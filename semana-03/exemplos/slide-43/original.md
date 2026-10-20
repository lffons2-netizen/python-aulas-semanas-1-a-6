# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 43

```python
def media(a, b, casas=2):
    m = (a + b) / 2
    return round(m, casas)

print(media(8, 6))
# 7.0

print(media(8, 5, 1))
# 6.5
```
