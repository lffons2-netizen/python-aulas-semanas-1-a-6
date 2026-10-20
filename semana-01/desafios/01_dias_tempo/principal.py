total = int(input("Quantidade de segundos: "))
dias = total // 86400
horas = total % 86400 // 3600
minutos = total % 3600 // 60
segundos = total % 60
print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos")
