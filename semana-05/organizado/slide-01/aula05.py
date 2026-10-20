# Semana 5 | Slide 1 | Bloco 1
import re

try:
    with open("contatos.txt") as f:
        texto = f.read()
    emails = re.findall(r"\S+@\S+", texto)
    print(emails)
except FileNotFoundError:
    print("Arquivo não encontrado!")
