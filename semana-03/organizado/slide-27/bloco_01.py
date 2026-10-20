# Semana 3 | Slide 27 | Bloco 1
def criar(nome, ativo=True):
    if ativo:
        s = "Disponivel"
    else:
        s = "Esgotado"
    return nome + " - " + s

print(criar("Caneta"))  # Disponivel
print(criar("Caneta", False))
