import unittest
from banco import Cliente, Conta, ContaCorrente, ContaPoupanca
from principal import demonstrar
from contextlib import redirect_stdout
from io import StringIO

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("Ana")

    def test_classe_abstrata(self):
        with self.assertRaises(TypeError):
            Conta("1", self.cliente)

    def test_polimorfismo(self):
        corrente = ContaCorrente("1", self.cliente, 100)
        poupanca = ContaPoupanca("2", self.cliente, 100)
        corrente.sacar(10)
        poupanca.sacar(10)
        self.assertEqual(corrente.saldo, 88)
        self.assertEqual(poupanca.saldo, 90)

    def test_operacoes_invalidas_nao_alteram_saldo(self):
        conta = ContaCorrente("1", self.cliente, 100)
        for valor in (0, -1, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                conta.depositar(valor)
        with self.assertRaises(ValueError):
            conta.sacar(100)
        self.assertEqual(conta.saldo, 100)

    def test_encapsulamento(self):
        conta = ContaPoupanca("1", self.cliente, 100)
        with self.assertRaises(AttributeError):
            conta.saldo = 0
        conta.depositar(10)
        historico = conta.historico
        historico.clear()
        self.assertEqual(len(conta.historico), 1)
        with self.assertRaises(ValueError):
            self.cliente.nome = " "

    def test_rendimento_e_instancias(self):
        conta = ContaPoupanca("1", self.cliente, 100)
        conta.render(0.01)
        self.assertEqual(conta.saldo, 101)
        with redirect_stdout(StringIO()):
            clientes, contas = demonstrar()
        self.assertGreaterEqual(len(clientes) + len(contas), 10)
        self.assertEqual(len(contas), 12)

if __name__ == "__main__":
    unittest.main()
