# Semana 4 | Slide 33
# Organização: Módulo exibido no slide 31, reunido ao principal do slide 33.
# arquivo: iterar.py
def iterar(estoque):
    # enumerate da indice e valor
    for i, produto in enumerate(estoque,
                                 start=1):
        print(i, "-", produto)
    print("Total:", len(estoque))

if __name__ == "__main__":
    iterar(["mouse", "teclado"])
