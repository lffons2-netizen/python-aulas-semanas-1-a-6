# Semana 5 | Slide 20 | Bloco 1
try:
    # código que pode falhar
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Valor inválido!")
except ZeroDivisionError:
    print("Não pode dividir por zero!")
else:
    print("Resultado:", resultado)
finally:
    print("Fim da execução.")
