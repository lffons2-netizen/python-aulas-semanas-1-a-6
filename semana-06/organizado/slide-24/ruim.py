# Semana 6 | Slide 24 | Bloco 2
def calcular_area(forma):
    if forma.tipo == "circulo":
        return 3.14 * forma.raio ** 2
    elif forma.tipo == "quadrado":
        return forma.lado ** 2
