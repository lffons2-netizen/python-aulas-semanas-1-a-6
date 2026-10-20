# Semana 4 | Slide 33
# Organização: Módulo exibido no slide 32, reunido ao principal do slide 33.
# arquivo: pertencimento.py
def existe(estoque, produto):
    # o operador in devolve True/False
    return produto in estoque

if __name__ == "__main__":
    lista = ["mouse", "teclado"]
    if existe(lista, "mouse"):
        print("Ja cadastrado")
    else:
        print("Pode comprar")
