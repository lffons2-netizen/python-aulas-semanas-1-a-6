# Semana 6 | Slide 29 | Bloco 1
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
