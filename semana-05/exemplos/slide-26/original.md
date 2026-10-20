# Código original do exemplo

Transcrição do exemplo fornecido no PDF, antes da organização. Quebras visuais podem impedir sua execução. Execute principal.py para usar a versão organizada.

## Slide 26

```python
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
```
