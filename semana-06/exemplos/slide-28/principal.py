# Semana 6 | Slide 28 | Bloco 1
import re
class Cliente:
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf

    def validar_email(self):
        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(padrao, self.email))

    def validar_cpf(self):
        padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
        return bool(re.match(padrao, self.cpf))

    def __str__(self):
        return f"{self.nome} <{self.email}>"

c1 = Cliente("Ana Silva", "ana@email.com", "123.456.789-00")
c2 = Cliente("Bruno", "bruno.invalido", "987.654.321-00")
print(c1)                  # Ana Silva <ana@email.com>
print(c1.validar_email())  # True
print(c1.validar_cpf())    # True
print(c2.validar_email())  # False
