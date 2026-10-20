# Semana 6 | Slide 15 | Bloco 1
class Calculadora:
    def __init__(self, valor):
        self.valor = valor

    def dobrar(self):              # instância
        return self.valor * 2

    @classmethod
    def criar_com_zero(cls):       # classe
        return cls(0)

    @staticmethod
    def somar(a, b):               # estático
        return a + b

c = Calculadora(10)
print(c.dobrar())                          # 20
print(Calculadora.criar_com_zero().valor)  # 0
print(Calculadora.somar(5, 3))             # 8
