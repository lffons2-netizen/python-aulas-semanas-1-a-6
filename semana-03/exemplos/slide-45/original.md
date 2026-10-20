# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 45

```python
def reg(nota, boletim=None):
    """Nao altera a lista original."""
    if boletim is None:
        boletim = []
    novo = boletim[:]   # copia
    novo.append(nota)
    return novo

notas = [7]
print(reg(9, notas))  # [7, 9]
print(notas)          # [7]
```
