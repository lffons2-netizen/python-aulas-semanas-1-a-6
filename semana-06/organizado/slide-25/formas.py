# Semana 6 | Slide 25 | Bloco 1
from abc import ABC, abstractmethod
import math

class Forma(ABC):                    # o contrato
    @abstractmethod
    def area(self):
        """Toda forma deve calcular sua área."""

    @abstractmethod
    def perimetro(self):
        """Toda forma deve calcular o perímetro."""

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return math.pi * self.raio ** 2
    def perimetro(self):
        return 2 * math.pi * self.raio
