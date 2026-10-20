# Semana 6 | Slide 18 | Bloco 2
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):      # para o usuário
        return f"{self.nome} (R$ {self.preco:.2f})"

    def __repr__(self):     # para o dev
        return f"Produto({self.nome!r}, {self.preco!r})"

    def __eq__(self, outro):
        if not isinstance(outro, Produto):
            return False
        return (self.nome == outro.nome
               and self.preco == outro.preco)

    def __lt__(self, outro):
        return self.preco < outro.preco

p1, p2 = Produto("Notebook", 2500.0), Produto("Mouse", 45.9)
print(p1)                       # Notebook (R$ 2500.00)
print(repr(p1))                 # Produto('Notebook', 2500.0)
print(p1 == Produto("Notebook", 2500.0))   # True
print(p1 < p2)                  # False
