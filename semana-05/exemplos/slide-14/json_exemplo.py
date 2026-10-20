# Semana 5 | Slide 14 | Bloco 2
import json

# Leitura
with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)
    print(dados)

# Escrita
dados = {"nome": "Ana", "idade": 25}
with open("saida.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)
