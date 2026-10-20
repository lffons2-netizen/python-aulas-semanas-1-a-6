preco = float(input("Preço: "))
percentual = float(input("Desconto (%): "))
preco_final = preco * (1 - percentual / 100)
print(f"Preço final: R$ {preco_final:.2f}")
