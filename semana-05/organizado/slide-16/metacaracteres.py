# Semana 5 | Slide 16 | Bloco 1
import re

# Validar data no formato YYYY-MM-DD
padrao = r"^\d{4}-\d{2}-\d{2}$"
print(re.match(padrao, "2026-08-30"))  # match
print(re.match(padrao, "30/08/2026"))  # None

# Extrair números de um texto
texto = "Comprei 3 livros por 120 reais"
numeros = re.findall(r"\d+", texto)
print(numeros)  # ['3', '120']
