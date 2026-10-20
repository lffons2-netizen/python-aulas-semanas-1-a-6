def relatorio(titulo, *linhas, **config):
    """Formata título e linhas; aceita largura e caractere de separação."""
    largura = int(config.get("largura", 40))
    caractere = str(config.get("caractere", "-"))[:1] or "-"
    separador = caractere * max(1, largura)
    return "\n".join([titulo.center(max(1, largura)), separador, *map(str, linhas), separador])

if __name__ == "__main__":
    titulo = input("Título: ")
    linhas = input("Linhas separadas por ponto e vírgula: ").split(";")
    print(relatorio(titulo, *linhas, largura=40, caractere="="))
