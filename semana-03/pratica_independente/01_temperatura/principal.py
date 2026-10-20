def celsius_para_fahrenheit(c):
    """Converte Celsius em Fahrenheit e devolve o resultado."""
    return c * 9 / 5 + 32

if __name__ == "__main__":
    celsius = float(input("Temperatura em Celsius: "))
    print(f"Fahrenheit: {celsius_para_fahrenheit(celsius):.1f}")
