# Semana 3 | Slide 13 | Bloco 1
# procedimento com parametros
def cabecalho(titulo, largura=30):
    print(titulo.center(largura))
    print("-" * largura)

cabecalho("RELATORIO")

# erro comum:
x = cabecalho("A") + 1  # TypeError
