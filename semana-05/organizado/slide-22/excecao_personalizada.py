# Semana 5 | Slide 22 | Bloco 2
class SaldoInsuficienteError(Exception):
    """Exceção para saldo insuficiente."""
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError(
            f"Saldo {saldo} insuficiente "
            f"para saque de {valor}")
    return saldo - valor

try:
    sacar(100, 200)
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
