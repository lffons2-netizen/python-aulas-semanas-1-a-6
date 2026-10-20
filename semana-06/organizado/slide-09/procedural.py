# Semana 6 | Slide 9 | Bloco 1
itens = [(45.90, 2), (120.0, 1)]

def calcular_total(itens):
    total = 0
    for preco, qtd in itens:
        total += preco * qtd
    return total

print(calcular_total(itens))
# 211.8
