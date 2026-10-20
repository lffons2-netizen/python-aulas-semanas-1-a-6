from abc import ABC, abstractmethod
from math import isfinite

class Cliente:
    """Representa o titular de uma ou mais contas."""
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        """Nome do cliente, validado ao atribuir."""
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Nome não pode ser vazio.")
        self._nome = valor.strip()

    def __str__(self):
        return self.nome

class Conta(ABC):
    """Classe abstrata com saldo encapsulado e operações comuns."""
    def __init__(self, numero, titular, saldo=0):
        if not isinstance(titular, Cliente):
            raise TypeError("Titular deve ser um Cliente.")
        if not isfinite(saldo) or saldo < 0:
            raise ValueError("Saldo inicial deve ser finito e não negativo.")
        self.numero = numero
        self.titular = titular
        self._saldo = float(saldo)
        self._historico = []

    @property
    def numero(self):
        """Identificador não vazio da conta."""
        return self._numero

    @numero.setter
    def numero(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Número da conta é obrigatório.")
        self._numero = valor.strip()

    @property
    def saldo(self):
        """Saldo apenas para leitura; alterações usam os métodos da classe."""
        return self._saldo

    @property
    def historico(self):
        """Entrega uma cópia, protegendo o histórico interno."""
        return self._historico[:]

    def depositar(self, valor):
        """Adiciona um valor positivo ao saldo."""
        if not isfinite(valor) or valor <= 0:
            raise ValueError("Depósito deve ser finito e positivo.")
        self._saldo += valor
        self._historico.append(f"Depósito: +{valor:.2f}")

    def sacar(self, valor):
        """Retira um valor e a taxa definida pela classe concreta."""
        if not isfinite(valor) or valor <= 0:
            raise ValueError("Saque deve ser finito e positivo.")
        total = valor + self.taxa_saque()
        if total > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= total
        self._historico.append(f"Saque: -{valor:.2f}; taxa: {self.taxa_saque():.2f}")

    @abstractmethod
    def taxa_saque(self):
        """Cada tipo de conta informa sua taxa de saque."""

    def __str__(self):
        return f"{self.numero} | {self.titular} | R$ {self.saldo:.2f}"

class ContaCorrente(Conta):
    """Conta com taxa didática fixa de R$ 2,00 por saque."""
    def __init__(self, numero, titular, saldo=0):
        super().__init__(numero, titular, saldo)

    def taxa_saque(self):
        """Sobrescreve o contrato com a taxa de conta corrente."""
        return 2.0

    def __str__(self):
        return f"Corrente: {super().__str__()}"

class ContaPoupanca(Conta):
    """Conta sem taxa de saque, com método de rendimento demonstrativo."""
    def __init__(self, numero, titular, saldo=0):
        super().__init__(numero, titular, saldo)

    def taxa_saque(self):
        """Sobrescreve o contrato sem cobrar taxa de saque."""
        return 0.0

    def render(self, taxa):
        """Aplica uma taxa didática não negativa, sem representar produto real."""
        if not isfinite(taxa) or taxa < 0:
            raise ValueError("Taxa deve ser finita e não negativa.")
        rendimento = self._saldo * taxa
        self._saldo += rendimento
        self._historico.append(f"Rendimento: +{rendimento:.2f}")

    def __str__(self):
        return f"Poupança: {super().__str__()}"
