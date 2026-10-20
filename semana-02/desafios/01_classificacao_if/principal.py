def classificar(idade, renda):
    """Regras de exemplo: Diamante >=30/10000; Ouro >=25/5000; Prata >=18/2000."""
    if idade < 0 or renda < 0:
        raise ValueError("Idade e renda não podem ser negativas.")
    if idade >= 30 and renda >= 10000:
        return "Diamante"
    elif idade >= 25 and renda >= 5000:
        return "Ouro"
    elif idade >= 18 and renda >= 2000:
        return "Prata"
    else:
        return "Bronze"

if __name__ == "__main__":
    idade = int(input("Idade: "))
    renda = float(input("Renda: "))
    print(f"Categoria: {classificar(idade, renda)}")
