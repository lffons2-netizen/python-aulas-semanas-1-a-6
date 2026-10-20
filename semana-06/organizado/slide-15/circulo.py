# Semana 6 | Slide 15 | Bloco 2
import math
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    @property
    def area(self):
        return math.pi * self.raio ** 2
c = Circulo(5)
print(f"{c.area:.2f}")  # 78.54, sem ()
