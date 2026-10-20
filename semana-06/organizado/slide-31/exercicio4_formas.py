# Semana 6 | Slide 31 | Bloco 1
from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def perimetro(self): ...

    def descricao(self):         # método concreto
        nome = self.__class__.__name__
        return (f"{nome}: área={self.area():.2f}, "
                f"perímetro={self.perimetro():.2f}")

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return math.pi * self.raio ** 2
    def perimetro(self):
        return 2 * math.pi * self.raio
