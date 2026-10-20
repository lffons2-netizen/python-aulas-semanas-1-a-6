# Semana 4 | Slide 32 | Bloco 1
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
