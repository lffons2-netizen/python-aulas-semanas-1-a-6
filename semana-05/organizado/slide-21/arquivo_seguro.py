# Semana 5 | Slide 21 | Bloco 1
try:
    with open("nao_existe.txt", "r") as f:
        conteudo = f.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")
except PermissionError:
    print("Sem permissão para ler o arquivo!")
