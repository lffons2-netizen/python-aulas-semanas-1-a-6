# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 31

```python
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
```

```python
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura
    def perimetro(self):
        return 2 * (self.largura + self.altura)

for f in [Circulo(5), Retangulo(4, 6)]:
    print(f.descricao())
```
