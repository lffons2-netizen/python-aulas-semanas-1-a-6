# Semana 4 | Slide 33
# Organização: Módulo exibido no slide 28, reunido ao principal do slide 33.
# arquivo: adicionar.py
def adicionar(estoque, produto):
    # evita duplicidade no estoque
    if produto not in estoque:
        estoque.append(produto)  # insere
    return estoque

# teste rapido do modulo
if __name__ == "__main__":
    print(adicionar(["mouse"], "teclado"))
