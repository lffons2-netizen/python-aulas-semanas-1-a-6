# Semana 3 | Slide 43 | Bloco 1
def media(a, b, casas=2):
    m = (a + b) / 2
    return round(m, casas)

print(media(8, 6))
# 7.0

print(media(8, 5, 1))
# 6.5
