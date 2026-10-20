segundos = int(input("Quantidade de segundos: "))
horas = segundos // 3600
minutos = segundos % 3600 // 60
segundos_restantes = segundos % 60
print(f"{horas} h, {minutos} min e {segundos_restantes} s")
