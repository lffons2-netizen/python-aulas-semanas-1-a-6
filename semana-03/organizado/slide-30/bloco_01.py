# Semana 3 | Slide 30 | Bloco 1
def rel(titulo, *itens,
        fmt="txt", **extras):
    print(titulo, fmt)
    print(itens)    # tupla
    print(extras)   # dicionario

rel("Vendas", "jan", "fev",
    fmt="pdf", autor="Ana")
