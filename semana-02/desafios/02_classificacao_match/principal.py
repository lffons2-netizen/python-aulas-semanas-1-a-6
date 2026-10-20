def classificar(idade, renda):
    """Regras de exemplo: Diamante >=30/10000; Ouro >=25/5000; Prata >=18/2000."""
    if idade < 0 or renda < 0:
        raise ValueError("Idade e renda não podem ser negativas.")
    match (idade, renda):
        case (i, r) if i >= 30 and r >= 10000:
            return "Diamante"
        case (i, r) if i >= 25 and r >= 5000:
            return "Ouro"
        case (i, r) if i >= 18 and r >= 2000:
            return "Prata"
        case _:
            return "Bronze"

if __name__ == "__main__":
    idade = int(input("Idade: "))
    renda = float(input("Renda: "))
    print(f"Categoria: {classificar(idade, renda)}")
