# Semana 6 | Slide 17
# Organização: Classe do slide 16 reunida ao método extrato do slide 17.
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

    def extrato(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        for h in self.historico:
            print(f"  {h}")

conta = ContaBancaria("Ana Silva", 1000)
conta.depositar(500)
conta.sacar(200)
conta.extrato()
