def fatorial(n):
    """Calcula n! recursivamente para inteiro não negativo."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Use um inteiro não negativo.")
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

if __name__ == "__main__":
    try:
        numero = int(input("Inteiro de 0 a 100: "))
        if numero > 100:
            raise ValueError("Nesta demonstração, use até 100 para limitar a recursão.")
        print(f"Fatorial: {fatorial(numero)}")
    except ValueError as erro:
        print(f"Erro: {erro}")
