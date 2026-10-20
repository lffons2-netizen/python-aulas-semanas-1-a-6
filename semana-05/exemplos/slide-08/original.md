# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 8

```python
def adicionar(estoque, produto):
    if produto not in estoque:
        estoque.append(produto)
    return estoque
```

```python
def remover(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
    else:
        print("Produto não encontrado")
    return estoque
```

```python
from adicionar import adicionar
from remover import remover

estoque = ["mouse", "teclado"]
adicionar(estoque, "monitor")
remover(estoque, "mouse")
print(estoque)  # ['teclado', 'monitor']
```
