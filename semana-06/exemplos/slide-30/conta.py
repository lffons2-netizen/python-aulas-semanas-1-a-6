# Semana 6 | Slide 30
# Organização: Método extrato do segundo painel inserido na classe ContaBancaria.
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo
        self._historico = []

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        self._saldo += valor
        self._historico.append(f"+{valor}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo -= valor
        self._historico.append(f"-{valor}")

    def extrato(self):          # (na classe)
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self._saldo:.2f}")
        for h in self._historico:
            print(f"  {h}")
