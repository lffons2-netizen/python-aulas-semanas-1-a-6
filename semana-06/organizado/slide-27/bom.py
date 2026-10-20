# Semana 6 | Slide 27 | Bloco 2
class Email:
    def enviar(self, msg):
        print(f"Email: {msg}")

class SMS:
    def enviar(self, msg):
        print(f"SMS: {msg}")

class Notificador:
    def __init__(self):
        self.canais = []            # TEM canais

    def adicionar_canal(self, canal):
        self.canais.append(canal)

    def enviar(self, msg):
        for canal in self.canais:   # polimorfismo
            canal.enviar(msg)

n = Notificador()
n.adicionar_canal(Email())
n.adicionar_canal(SMS())
n.enviar("Olá!")
