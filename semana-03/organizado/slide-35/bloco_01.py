# Semana 3 | Slide 35 | Bloco 1
def dividir(a, b):
    # devolve uma TUPLA
    return a // b, a % b

q, r = dividir(17, 5)
print(q, r)    # 3 2

res = dividir(17, 5)
print(res)     # (3, 2)
