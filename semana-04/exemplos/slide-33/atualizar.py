# Semana 4 | Slide 33
# Organização: Módulo exibido no slide 30, reunido ao principal do slide 33.
# arquivo: atualizar.py
def atualizar(estoque, antigo, novo):
    # localiza o indice do produto
    if antigo in estoque:
        i = estoque.index(antigo)
        estoque[i] = novo  # substitui
    return estoque

if __name__ == "__main__":
    print(atualizar(["mose"], "mose",
                    "mouse"))
