# Semana 5 | Slide 8 | Bloco 3
from adicionar import adicionar
from remover import remover

estoque = ["mouse", "teclado"]
adicionar(estoque, "monitor")
remover(estoque, "mouse")
print(estoque)  # ['teclado', 'monitor']
