# Semana 6 | Slide 26 | Bloco 1
class Animal:
    def respirar(self):
        print("Respirando...")

class Cachorro(Animal):   # Cachorro É UM Animal
    def latir(self):
        print("Latindo...")

rex = Cachorro()
rex.respirar()   # herdado
rex.latir()      # próprio
