# Semana 5 | Slide 8 | Bloco 1
def adicionar(estoque, produto):
    if produto not in estoque:
        estoque.append(produto)
    return estoque
