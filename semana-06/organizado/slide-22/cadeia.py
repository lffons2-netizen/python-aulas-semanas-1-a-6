# Semana 6 | Slide 22 | Bloco 2
class Animal:
    def respirar(self):
        print("Respirando...")

class Mamifero(Animal):
    def amamentar(self):
        print("Amamentando...")

class Cachorro(Mamifero):
    def latir(self):
        print("Latindo...")

rex = Cachorro()
rex.respirar()                  # de Animal
rex.amamentar()                 # de Mamifero
rex.latir()                     # próprio
print(isinstance(rex, Animal))  # True
print(isinstance(rex, str))     # False
