from cadastro import validar_email, validar_cpf

# Semana 6 | Slide 11 | Bloco 1
class Cliente:
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf

    def validar(self):
        return (validar_email(self.email)
                and validar_cpf(self.cpf))

    def exibir(self):
        print(f"{self.nome} - {self.email}")

cliente = Cliente("Ana", "ana@email.com",
                  "123.456.789-00")
cliente.exibir()          # Ana - ana@email.com
print(cliente.validar())  # True
