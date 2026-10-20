import re

# Semana 5 | Slide 19 | Bloco 2
texto = "CPF: 123.456.789-00, outro: 987.654.321-00"
mascarado = re.sub(r"\d{3}\.\d{3}\.\d{3}-\d{2}", "***.***.***-**", texto)
print(mascarado)  # "CPF: ***.***.***-**, outro: ***.***.***-**"
