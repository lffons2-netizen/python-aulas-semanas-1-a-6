def calcular_media(notas):
    """Retorna a media."""
    t = sum(notas)
    return t / len(notas)

media = calcular_media(
    [8, 6, 10])  # GLOBAL
# print(t) -> NameError
