def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a diferença de dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna o produto de dois números."""
    return a * b

def dividir(a, b):
    """Divide dois números; rejeita divisor zero com ValueError."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b
