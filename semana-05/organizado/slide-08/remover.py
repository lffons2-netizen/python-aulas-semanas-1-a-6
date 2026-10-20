# Semana 5 | Slide 8 | Bloco 2
def remover(estoque, produto):
    if produto in estoque:
        estoque.remove(produto)
    else:
        print("Produto não encontrado")
    return estoque
