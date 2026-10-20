# Semana 6 | Slide 22 | Bloco 1
class Voador:
    def voar(self):
        print("Voando...")

class Nadador:
    def nadar(self):
        print("Nadando...")

class Pato(Voador, Nadador):
    pass

p = Pato()
p.voar()    # Voando...
p.nadar()   # Nadando...
