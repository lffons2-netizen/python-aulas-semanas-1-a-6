from banco import Cliente, ContaCorrente, ContaPoupanca

def demonstrar():
    """Cria 15 instâncias, usa polimorfismo e trata operações inválidas."""
    clientes = [Cliente("Ana"), Cliente("Bruno"), Cliente("Carla")]
    contas = []
    for indice in range(6):
        titular = clientes[indice % len(clientes)]
        contas.append(ContaCorrente(f"CC-{indice + 1}", titular, 100))
        contas.append(ContaPoupanca(f"CP-{indice + 1}", titular, 100))
    # A mesma operação responde à implementação de taxa_saque de cada classe.
    for conta in contas:
        conta.depositar(50)
        conta.sacar(10)
        print(conta)
    print(f"Instâncias criadas: {len(clientes) + len(contas)}")
    try:
        contas[0].sacar(10000)
    except ValueError as erro:
        print(f"Saque recusado: {erro}")
    try:
        clientes[0].nome = ""
    except ValueError as erro:
        print(f"Nome recusado: {erro}")
    return clientes, contas

if __name__ == "__main__":
    demonstrar()
