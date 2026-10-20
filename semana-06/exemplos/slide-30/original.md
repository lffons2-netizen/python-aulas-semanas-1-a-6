# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 30

```python
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
```

```python
    def extrato(self):          # (na classe)
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self._saldo:.2f}")
        for h in self._historico:
            print(f"  {h}")

conta = ContaBancaria("Ana", 1000)
conta.depositar(500)
conta.sacar(200)
conta.extrato()
print(conta.saldo)   # somente leitura
```
