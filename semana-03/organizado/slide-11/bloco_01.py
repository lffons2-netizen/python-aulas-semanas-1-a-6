# Semana 3 | Slide 11 | Bloco 1
# retorno antecipado
def dividir(a, b):
    if b == 0:
        return None   # sai antes
    return a / b

# devolver varios valores
def dividir2(a, b):
    return a // b, a % b

q, r = dividir2(7, 2)  # 3 e 1
