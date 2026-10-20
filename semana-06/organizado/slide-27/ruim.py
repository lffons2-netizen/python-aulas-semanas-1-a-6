# Semana 6 | Slide 27 | Bloco 1
class NotificadorEmail:
    def enviar(self, msg):
        print(f"Email: {msg}")

# SMS não é um Email!
class NotificadorSMS(NotificadorEmail):
    def enviar(self, msg):
        print(f"SMS: {msg}")
