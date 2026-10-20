# Semana 6 | Slide 19 | Bloco 1
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular    # público
        self._saldo = saldo       # protegido
        self.__senha = "1234"     # privado

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
        self._saldo += valor

    def get_saldo(self):
        return self._saldo

conta = ContaBancaria("Ana", 1000)
print(conta.titular)       # Ana
print(conta._saldo)        # 1000 (funciona, mas evite)
print(conta.get_saldo())   # 1000
# print(conta.__senha)     # AttributeError

# Name mangling: o Python renomeia o atributo
print(conta._ContaBancaria__senha)  # 1234 (má prática)
