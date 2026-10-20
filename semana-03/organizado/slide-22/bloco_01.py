# Semana 3 | Slide 22 | Bloco 1
# copia defensiva antes de alterar
def total(carrinho):
    itens = carrinho[:]  # copia rasa
    itens.append("brinde")
    return itens

original = ["arroz"]
novo = total(original)
print(original)  # ['arroz']
print(novo)      # ['arroz','brinde']
