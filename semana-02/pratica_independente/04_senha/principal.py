SENHA_CORRETA = "python123"
tentativas = 0
while tentativas < 3:
    senha = input("Senha: ")
    tentativas += 1
    if senha == SENHA_CORRETA:
        print(f"Acesso permitido em {tentativas} tentativa(s).")
        break
    print(f"Senha incorreta. Tentativas restantes: {3 - tentativas}")
else:
    print("Acesso bloqueado após 3 erros.")
