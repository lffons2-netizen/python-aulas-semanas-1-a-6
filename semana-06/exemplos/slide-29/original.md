# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 29

```python
class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def emitir_som(self):
        return f"{self.nome} faz {self.som}"

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Au au!")
    def buscar(self):
        return f"{self.nome} está buscando a bolinha"

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Miau!")
    def arranhar(self):
        return f"{self.nome} arranhou o sofá"

rex, mimi = Cachorro("Rex"), Gato("Mimi")
print(rex.emitir_som())   # Rex faz Au au!
print(rex.buscar())       # Rex está buscando a bolinha
print(mimi.emitir_som())  # Mimi faz Miau!
print(mimi.arranhar())    # Mimi arranhou o sofá
```
