# Semana 6 | Slide 16 | Bloco 1
class ContaBancaria:
    """Representa uma conta bancária."""

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.historico = []      # lista de transações

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        self.saldo += valor
        self.historico.append(f"+{valor}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
        self.historico.append(f"-{valor}")
