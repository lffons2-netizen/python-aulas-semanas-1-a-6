from conta import ContaBancaria

conta = ContaBancaria("Ana", 1000)
conta.depositar(500)
conta.sacar(200)
conta.extrato()
print(conta.saldo)   # somente leitura
