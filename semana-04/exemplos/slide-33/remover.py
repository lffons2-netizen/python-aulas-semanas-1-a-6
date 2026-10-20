# Semana 4 | Slide 33
# Organização: Módulo exibido no slide 29, reunido ao principal do slide 33.
# arquivo: remover.py
def remover(estoque, produto):
    # so remove se o item existir
    if produto in estoque:
        estoque.remove(produto)
    else:
        print("Produto nao encontrado")
    return estoque

if __name__ == "__main__":
    print(remover(["mouse", "hd"], "hd"))
