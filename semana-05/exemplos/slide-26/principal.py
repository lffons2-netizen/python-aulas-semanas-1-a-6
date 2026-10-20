# Semana 5 | Slide 26 | Bloco 1
def dividir():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = a / b
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
    else:
        print(f"Resultado: {resultado:.2f}")
    finally:
        print("Operação encerrada.")

dividir()
