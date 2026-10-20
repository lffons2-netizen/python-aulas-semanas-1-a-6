# Semana 5 | Slide 17 | Bloco 1
import re

texto = "O ano de 2026 começou e 2027 virá."

# match — verifica o início
print(re.match(r"O ano", texto))  # match

# search — procura em qualquer lugar
print(re.search(r"\d{4}", texto))  # 2026

# findall — todas as ocorrências
print(re.findall(r"\d{4}", texto))  # ['2026', '2027']

# sub — substituição
novo = re.sub(r"\d{4}", "ANO", texto)
print(novo)  # "O ano de ANO começou e ANO virá."

# split — divisão
partes = re.split(r"\s+", texto)
print(partes)  # ['O', 'ano', 'de', '2026', ...]
