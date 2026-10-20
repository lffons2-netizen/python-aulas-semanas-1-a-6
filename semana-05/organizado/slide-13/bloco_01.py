# Semana 5 | Slide 13 | Bloco 1
f = open("dados.txt", "r")
try:
    conteudo = f.read()
finally:
    f.close()
