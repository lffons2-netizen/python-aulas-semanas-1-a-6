# Semana 6 | Slide 9 | Bloco 3
class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar(self, preco, qtd):
        self.itens.append((preco, qtd))

    def total(self):
        return sum(p * q for p, q
                   in self.itens)

pedido = Pedido()
pedido.adicionar(45.90, 2)
pedido.adicionar(120.0, 1)
print(pedido.total())  # 211.8
