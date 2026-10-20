def validar_senha(senha):
    """Retorna True quando a senha possui ao menos oito caracteres."""
    return len(senha) >= 8

if __name__ == "__main__":
    senha = input("Senha: ")
    print(f"Senha válida: {validar_senha(senha)}")
