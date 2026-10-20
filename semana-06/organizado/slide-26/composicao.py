# Semana 6 | Slide 26 | Bloco 2
class Motor:
    def ligar(self):
        print("Motor ligado")

class Carro:
    def __init__(self):
        self.motor = Motor()   # Carro TEM UM Motor

    def ligar(self):
        self.motor.ligar()
        print("Carro pronto para andar")
Carro().ligar()
