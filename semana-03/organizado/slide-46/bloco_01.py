# Semana 3 | Slide 46 | Bloco 1
# script_desafio.py
from calculadora import somar, \
                       multiplicar

def orc(qtd, preco, frete=0):
    """Total do pedido."""
    s = multiplicar(qtd, preco)
    return somar(s, frete)

print(orc(3, 49.9, 15))  # 164.7
