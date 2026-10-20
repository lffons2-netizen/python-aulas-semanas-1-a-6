# Semana 5 | Slide 22 | Bloco 1
def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - valor

try:
    sacar(100, 200)
except ValueError as e:
    print(f"Erro: {e}")  # Erro: Saldo insuficiente
