print("1 - Somar | 2 - Subtrair | 3 - Multiplicar | 4 - Dividir")
opcao = int(input("Operação: "))
a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
match opcao:
    case 1:
        print(f"Resultado: {a + b}")
    case 2:
        print(f"Resultado: {a - b}")
    case 3:
        print(f"Resultado: {a * b}")
    case 4:
        if b == 0:
            print("Não é possível dividir por zero.")
        else:
            print(f"Resultado: {a / b}")
    case _:
        print("Operação inválida.")
