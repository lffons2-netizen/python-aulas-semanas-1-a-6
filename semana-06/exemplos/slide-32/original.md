# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 32

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_preco_final(self):
        return self.preco

    def __str__(self):
        return f"{self.nome}: R$ {self.calcular_preco_final():.2f}"

class ProdutoFisico(Produto):
    def __init__(self, nome, preco, frete):
        super().__init__(nome, preco)
        self.frete = frete

    def calcular_preco_final(self):
        return self.preco + self.frete

class ProdutoDigital(Produto):
    def calcular_preco_final(self):
        return self.preco * 0.9   # 10% de desconto
```

```python
produtos = [
    ProdutoFisico("Notebook", 2500, 50),
    ProdutoDigital("Curso Python", 200),
    ProdutoFisico("Mouse", 45.90, 15),
]
for p in produtos:
    print(p)
```
