# Semana 5 | Slide 27 | Bloco 1
import csv

def filtrar_produtos(caminho, preco_min):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                preco = float(linha["preco"])
                if preco >= preco_min:
                    print(f"{linha['nome']}: R$ {preco:.2f}")
    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")
    except KeyError:
        print("Coluna 'preco' não encontrada no CSV.")
    except ValueError:
        print("Valor de preço inválido.")

filtrar_produtos("produtos.csv", 100)
