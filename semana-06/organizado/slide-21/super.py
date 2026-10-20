class Animal:                  # classe mãe
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} faz um som")

# Semana 6 | Slide 21 | Bloco 2
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # usa a mãe
        self.raca = raca        # e adiciona

rex = Cachorro("Rex", "Labrador")
print(rex.nome, rex.raca)  # Rex Labrador
