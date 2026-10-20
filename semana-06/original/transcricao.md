# Transcrição dos códigos Python

## Semana 6

Slides sem blocos ou exemplos de código Python transcritos: 2, 3, 4, 8, 33, 34, 35, 36, 37, 38, 39.

### Slide 1

aula06.py

```python
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def aprovado(self):
        return self.nota >= 7

print(Aluno("Ana", 8.5).aprovado())  # True
```

### Slide 5

cadastro.py

```python
import re

def validar_email(email):
    """Valida formato de email."""
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))

def validar_cpf(cpf):
    """Valida formato de CPF (000.000.000-00)."""
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.match(padrao, cpf))
```

### Slide 6

processar_cadastros.py

```python
def processar_cadastros(caminho):
    """Lê e valida cadastros do arquivo."""
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print(f"Arquivo {caminho} não encontrado.")
        return [], []
    except PermissionError:
        print(f"Sem permissão para ler {caminho}.")
        return [], []

    validos, invalidos = [], []
    for linha in linhas:
        try:
            nome, email, cpf = linha.strip().split(";")
            if validar_email(email) and validar_cpf(cpf):
                validos.append({"nome": nome, "email": email, "cpf": cpf})
            else:
                invalidos.append({"nome": nome, "motivo": "dados inválidos"})
        except ValueError:
            invalidos.append({"nome": "?", "motivo": "formato inválido"})
    return validos, invalidos
```

executar.py

```python
v, inv = processar_cadastros("clientes.txt")
print(f"Válidos: {len(v)}")
print(f"Inválidos: {len(inv)}")
for c in v:
    print(f"    {c['nome']} - {c['email']}")
for c in inv:
    print(f"    {c['nome']} - {c['motivo']}")
```

### Slide 7

limitacao.py

```python
cliente = {"nome": "Ana", "email": "ana@email.com"}

# 1. Nada impede um dicionário inconsistente
cliente["emial"] = "ana@"     # erro de digitação aceito
del cliente["nome"]           # campo obrigatório some

# 2. Dados e regras vivem separados
validar_email(cliente["email"])   # e se alguém esquecer?

# 3. Sem comportamento próprio
cliente.validar()   # AttributeError: 'dict' object
                    # has no attribute 'validar'
```

### Slide 9

procedural.py

```python
itens = [(45.90, 2), (120.0, 1)]

def calcular_total(itens):
    total = 0
    for preco, qtd in itens:
        total += preco * qtd
    return total

print(calcular_total(itens))
# 211.8
```

funcional.py

```python
itens = [(45.90, 2), (120.0, 1)]

total = sum(
    map(lambda i: i[0] * i[1],
        itens)
)

print(total)
# 211.8
```

orientado_objetos.py

```python
class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar(self, preco, qtd):
        self.itens.append((preco, qtd))

    def total(self):
        return sum(p * q for p, q
                   in self.itens)

pedido = Pedido()
pedido.adicionar(45.90, 2)
pedido.adicionar(120.0, 1)
print(pedido.total())  # 211.8
```

### Slide 10

procedural.py

```python
# Modelo procedural: dados soltos
cliente1 = {"nome": "Ana",
            "email": "ana@email.com",
            "cpf": "123.456.789-00"}
cliente2 = {"nome": "Bruno",
            "email": "bruno@email.com",
            "cpf": "987.654.321-00"}

def validar_cliente(cliente):
    return (validar_email(cliente["email"])
            and validar_cpf(cliente["cpf"]))

def exibir_cliente(cliente):
    print(f"{cliente['nome']} - {cliente['email']}")
```

### Slide 11

orientado_objetos.py

```python
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
```

### Slide 12

Fragmentos de sintaxe e exemplos apresentados no slide

```python
class NomeDaClasse:
objeto = NomeDaClasse(args)
ana = Cliente("Ana", ...)
class Cliente:
ana = Cliente(...)
type(42)
```

### Slide 13

cliente.py

```python
class Cliente:
    """Representa um cliente da empresa."""

    def __init__(self, nome, email, cpf):
        """Construtor: inicializa os atributos."""
        self.nome = nome
        self.email = email
        self.cpf = cpf

    def exibir(self):
        """Exibe os dados do cliente."""
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"CPF: {self.cpf}")

# Criação de objetos
ana = Cliente("Ana Silva", "ana@email.com", "123.456.789-00")
bruno = Cliente("Bruno Costa", "bruno@email.com", "987.654.321-00")

# Uso dos objetos
ana.exibir()
print("---")
bruno.exibir()
```

### Slide 14

produto.py

```python
class Produto:
    # Atributo de CLASSE (compartilhado por todos)
    taxa_imposto = 0.10

    def __init__(self, nome, preco):
        # Atributos de INSTÂNCIA (um por objeto)
        self.nome = nome
        self.preco = preco

    def preco_com_imposto(self):
        return round(self.preco * (1 + Produto.taxa_imposto), 2)

p1 = Produto("Notebook", 2500.00)
p2 = Produto("Mouse", 45.90)

print(p1.nome)                  # Notebook
print(p1.preco_com_imposto())   # 2750.0
print(p2.preco_com_imposto())   # 50.49
print(Produto.taxa_imposto)     # 0.1
```

Trecho na observação

```python
p1.taxa_imposto = 0.2
```

### Slide 15

calculadora.py

```python
class Calculadora:
    def __init__(self, valor):
        self.valor = valor

    def dobrar(self):              # instância
        return self.valor * 2

    @classmethod
    def criar_com_zero(cls):       # classe
        return cls(0)

    @staticmethod
    def somar(a, b):               # estático
        return a + b

c = Calculadora(10)
print(c.dobrar())                          # 20
print(Calculadora.criar_com_zero().valor)  # 0
print(Calculadora.somar(5, 3))             # 8
```

circulo.py

```python
import math
class Circulo:
    def __init__(self, raio):
        self.raio = raio

    @property
    def area(self):
        return math.pi * self.raio ** 2
c = Circulo(5)
print(f"{c.area:.2f}")  # 78.54, sem ()
```

### Slide 16

conta.py

```python
class ContaBancaria:
    """Representa uma conta bancária."""

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.historico = []      # lista de transações

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        self.saldo += valor
        self.historico.append(f"+{valor}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
        self.historico.append(f"-{valor}")
```

### Slide 17

O método extrato continua a classe ContaBancaria do slide anterior.

conta.py — continuação do slide 16

```python
    def extrato(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        for h in self.historico:
            print(f"  {h}")

conta = ContaBancaria("Ana Silva", 1000)
conta.depositar(500)
conta.sacar(200)
conta.extrato()
```

padrao_mutavel.py

```python
# ERRADO: a lista é compartilhada!
def __init__(self, itens=[]):
    self.itens = itens

# CERTO: cada objeto ganha a sua lista
def __init__(self, itens=None):
    self.itens = itens if itens is not None else []
```

### Slide 18

Fragmentos da coluna Exemplo da tabela

```python
Cliente(...)
print(obj)
repr(obj)
len(obj)
a == b
a < b
a + b
for x in obj
```

dunder.py

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):      # para o usuário
        return f"{self.nome} (R$ {self.preco:.2f})"

    def __repr__(self):     # para o dev
        return f"Produto({self.nome!r}, {self.preco!r})"

    def __eq__(self, outro):
        if not isinstance(outro, Produto):
            return False
        return (self.nome == outro.nome
               and self.preco == outro.preco)

    def __lt__(self, outro):
        return self.preco < outro.preco

p1, p2 = Produto("Notebook", 2500.0), Produto("Mouse", 45.9)
print(p1)                       # Notebook (R$ 2500.00)
print(repr(p1))                 # Produto('Notebook', 2500.0)
print(p1 == Produto("Notebook", 2500.0))   # True
print(p1 < p2)                  # False
```

### Slide 19

encapsulamento.py

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular    # público
        self._saldo = saldo       # protegido
        self.__senha = "1234"     # privado

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
        self._saldo += valor

    def get_saldo(self):
        return self._saldo

conta = ContaBancaria("Ana", 1000)
print(conta.titular)       # Ana
print(conta._saldo)        # 1000 (funciona, mas evite)
print(conta.get_saldo())   # 1000
# print(conta.__senha)     # AttributeError

# Name mangling: o Python renomeia o atributo
print(conta._ContaBancaria__senha)  # 1234 (má prática)
```

### Slide 20

propriedade.py

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco      # já passa pelo setter!

    @property
    def preco(self):
        """Getter: acessado como atributo."""
        return self._preco

    @preco.setter
    def preco(self, valor):
        """Setter: valida antes de atribuir."""
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = valor

p = Produto("Notebook", 2500)
print(p.preco)    # 2500 (chama o getter)
p.preco = 3000    # chama o setter
print(p.preco)    # 3000
p.preco = -100    # ValueError
```

### Slide 21

heranca.py

```python
class Animal:                  # classe mãe
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} faz um som")

class Cachorro(Animal):        # classe filha
    def emitir_som(self):
        print(f"{self.nome} late: Au au!")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} mia: Miau!")

Animal("Genérico").emitir_som()  # Genérico faz um som
Cachorro("Rex").emitir_som()     # Rex late: Au au!
Gato("Mimi").emitir_som()        # Mimi mia: Miau!
```

super.py

```python
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # usa a mãe
        self.raca = raca        # e adiciona

rex = Cachorro("Rex", "Labrador")
print(rex.nome, rex.raca)  # Rex Labrador
```

### Slide 22

heranca_multipla.py

```python
class Voador:
    def voar(self):
        print("Voando...")

class Nadador:
    def nadar(self):
        print("Nadando...")

class Pato(Voador, Nadador):
    pass

p = Pato()
p.voar()    # Voando...
p.nadar()   # Nadando...
```

cadeia.py

```python
class Animal:
    def respirar(self):
        print("Respirando...")

class Mamifero(Animal):
    def amamentar(self):
        print("Amamentando...")

class Cachorro(Mamifero):
    def latir(self):
        print("Latindo...")

rex = Cachorro()
rex.respirar()                  # de Animal
rex.amamentar()                 # de Mamifero
rex.latir()                     # próprio
print(isinstance(rex, Animal))  # True
print(isinstance(rex, str))     # False
```

### Slide 23

polimorfismo.py

```python
class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

class Vaca(Animal):
    def emitir_som(self):
        return "Muuu!"

# Mesma chamada, comportamentos diferentes
for animal in [Cachorro(), Gato(), Vaca()]:
    print(animal.emitir_som())

def fazer_som(animal):
    """Funciona com qualquer objeto que tenha emitir_som()."""
    print(animal.emitir_som())
```

Exemplos da observação

```python
len("abc")
len([1, 2])
len({"a": 1})
```

### Slide 24

duck_typing.py

```python
class Pato:
    def emitir_som(self):
        return "Quack!"

class Pessoa:
    def emitir_som(self):
        return "Olá!"

# Não importa o tipo, só o método
for obj in [Pato(), Pessoa()]:
    print(obj.emitir_som())
```

ruim.py

```python
def calcular_area(forma):
    if forma.tipo == "circulo":
        return 3.14 * forma.raio ** 2
    elif forma.tipo == "quadrado":
        return forma.lado ** 2
```

bom.py

```python
class Circulo:
    def __init__(self, raio): self.raio = raio
    def area(self): return 3.14 * self.raio ** 2
class Quadrado:
    def __init__(self, lado): self.lado = lado
    def area(self): return self.lado ** 2

for forma in [Circulo(5), Quadrado(4)]:
    print(forma.area())   # 78.5 e 16
```

### Slide 25

formas.py

```python
from abc import ABC, abstractmethod
import math

class Forma(ABC):                    # o contrato
    @abstractmethod
    def area(self):
        """Toda forma deve calcular sua área."""

    @abstractmethod
    def perimetro(self):
        """Toda forma deve calcular o perímetro."""

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return math.pi * self.raio ** 2
    def perimetro(self):
        return 2 * math.pi * self.raio
```

uso_formas.py

```python
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2
    def perimetro(self):
        return 4 * self.lado

c, q = Circulo(5), Quadrado(4)
print(round(c.area(), 2))   # 78.54
print(q.area())             # 16

f = Forma()   # TypeError: Can't instantiate
              # abstract class Forma
```

### Slide 26

heranca.py

```python
class Animal:
    def respirar(self):
        print("Respirando...")

class Cachorro(Animal):   # Cachorro É UM Animal
    def latir(self):
        print("Latindo...")

rex = Cachorro()
rex.respirar()   # herdado
rex.latir()      # próprio
```

composicao.py

```python
class Motor:
    def ligar(self):
        print("Motor ligado")

class Carro:
    def __init__(self):
        self.motor = Motor()   # Carro TEM UM Motor

    def ligar(self):
        self.motor.ligar()
        print("Carro pronto para andar")
Carro().ligar()
```

### Slide 27

ruim.py

```python
class NotificadorEmail:
    def enviar(self, msg):
        print(f"Email: {msg}")

# SMS não é um Email!
class NotificadorSMS(NotificadorEmail):
    def enviar(self, msg):
        print(f"SMS: {msg}")
```

bom.py

```python
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
```

### Slide 28

exercicio1_cliente.py

```python
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
```

### Slide 29

exercicio2_animais.py

```python
class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def emitir_som(self):
        return f"{self.nome} faz {self.som}"

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Au au!")
    def buscar(self):
        return f"{self.nome} está buscando a bolinha"

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Miau!")
    def arranhar(self):
        return f"{self.nome} arranhou o sofá"

rex, mimi = Cachorro("Rex"), Gato("Mimi")
print(rex.emitir_som())   # Rex faz Au au!
print(rex.buscar())       # Rex está buscando a bolinha
print(mimi.emitir_som())  # Mimi faz Miau!
print(mimi.arranhar())    # Mimi arranhou o sofá
```

### Slide 30

O método extrato no segundo painel pertence à classe do primeiro painel, conforme indicado no slide.

exercicio3_conta.py

```python
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo
        self._historico = []

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        self._saldo += valor
        self._historico.append(f"+{valor}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo -= valor
        self._historico.append(f"-{valor}")
```

teste_conta.py

```python
    def extrato(self):          # (na classe)
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self._saldo:.2f}")
        for h in self._historico:
            print(f"  {h}")

conta = ContaBancaria("Ana", 1000)
conta.depositar(500)
conta.sacar(200)
conta.extrato()
print(conta.saldo)   # somente leitura
```

### Slide 31

exercicio4_formas.py

```python
from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def perimetro(self): ...

    def descricao(self):         # método concreto
        nome = self.__class__.__name__
        return (f"{nome}: área={self.area():.2f}, "
                f"perímetro={self.perimetro():.2f}")

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return math.pi * self.raio ** 2
    def perimetro(self):
        return 2 * math.pi * self.raio
```

retangulo.py

```python
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura
    def perimetro(self):
        return 2 * (self.largura + self.altura)

for f in [Circulo(5), Retangulo(4, 6)]:
    print(f.descricao())
```

### Slide 32

exercicio5_produtos.py

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_preco_final(self):
        return self.preco

    def __str__(self):
        return f"{self.nome}: R$ {self.calcular_preco_final():.2f}"

class ProdutoFisico(Produto):
    def __init__(self, nome, preco, frete):
        super().__init__(nome, preco)
        self.frete = frete

    def calcular_preco_final(self):
        return self.preco + self.frete

class ProdutoDigital(Produto):
    def calcular_preco_final(self):
        return self.preco * 0.9   # 10% de desconto
```

teste_produtos.py

```python
produtos = [
    ProdutoFisico("Notebook", 2500, 50),
    ProdutoDigital("Curso Python", 200),
    ProdutoFisico("Mouse", 45.90, 15),
]
for p in produtos:
    print(p)
```
