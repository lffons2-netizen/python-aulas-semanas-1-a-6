# Semana 4 | Slide 18 | Bloco 1
# declaracao do conjunto (chaves)
frutas = {"maca", "uva", "maca"}
# duplicatas sao eliminadas
print(frutas)  # {'maca', 'uva'}
# teste de pertinencia (acesso)
print("uva" in frutas)  # True
# percorrendo o conjunto
for f in frutas:
    print(f)
