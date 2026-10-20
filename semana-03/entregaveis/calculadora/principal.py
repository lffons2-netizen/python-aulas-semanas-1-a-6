import calculadora
try:
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
    print(f"Soma: {calculadora.somar(a, b)}")
    print(f"Subtração: {calculadora.subtrair(a, b)}")
    print(f"Multiplicação: {calculadora.multiplicar(a, b)}")
    print(f"Divisão: {calculadora.dividir(a, b)}")
except ValueError as erro:
    print(f"Erro: {erro}")
