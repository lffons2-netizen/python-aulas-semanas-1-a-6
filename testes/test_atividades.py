import ast
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
ATIVIDADES = json.loads((ROOT / 'atividades.json').read_text())
ENTRADAS_EXEMPLOS = {
    (1, 38): '60\n1.67\n', (1, 39): '100\n', (1, 40): '30\n',
    (1, 41): '4\n5\n', (1, 42): 'Ana\nSilva\n',
    (2, 15): '8\n6\n10\n', (2, 21): '1\n', (2, 44): '12\n8\n',
    (2, 46): '8\n', (2, 47): '1\n', (2, 49): '2\n0\n',
    (4, 34): '3\n10\n5\n20\n', (4, 35): '1 2 3 4\n',
    (4, 36): '10 5 20 3\n', (4, 37): 'Ana Ana Bruno\n', (4, 38): '7 9 8\n',
    (5, 14): '1\n', (5, 19): '1\n', (5, 26): '10\n4\n',
}
ENTRADAS_NOVAS = {
    (1, '01_troco'): '80\n100\n', (1, '02_tempo'): '3661\n',
    (1, '03_par_impar'): '4\n', (1, '04_media'): '8\n6\n10\n',
    (1, '05_desconto'): '100\n20\n', (1, '06_nome_invertido'): 'Ana\n',
    (1, '01_dias_tempo'): '90061\n', (1, '02_circulo'): '2\n', (1, '03_frase'): 'Python é legal\n',
    (2, '01_classificacao'): '30\n10000\n', (2, '01_classificacao_if'): '30\n10000\n',
    (2, '02_classificacao_match'): '30\n10000\n', (2, '02_calculadora'): '4\n10\n2\n',
    (2, '03_cinco_numeros'): '1\n2\n3\n4\n5\n', (2, '04_senha'): 'erro\npython123\n',
    (2, '03_positivos'): '-1\n0\n1\n2\n3\n-2\n-3\n4\n5\n6\n',
    (2, '04_nomes'): 'Ana\nBruno\nfim\n', (2, '05_cadastros'): '\n2\nAna\n18\n1\nBruno\n17\nsair\n',
    (3, '01_temperatura'): '30\n', (3, '02_senha'): 'abcdefgh\n', (3, '03_caixa'): '10 20 30\n',
    (3, '04_ficha_aluno'): 'Ana\nComputação\n18\n', (3, '05_utilidades'): '4\nana silva\n',
    (3, '06_lista_segura'): 'a,b\nc\n', (3, '01_estatistica'): '1 2 2 3\n', (3, '02_fatorial'): '5\n',
    (3, '03_relatorio'): 'Relatório\nLinha A;Linha B\n', (3, 'calculadora'): '10\n2\n',
    (4, '01_nomes'): '4\nAna\nBruno\nAna\nCarla\n',
    (4, 'sistema_produtos'): '3\nMouse\n45.90\nPerifericos\nMonitor\n899\nVideo\nTeclado\n120\nPerifericos\n100\nacima\n',
    (5, '05_estoque'): 'Perifericos\n',
}

def executar(atividade, entrada=None, alterar=None):
    """Executa uma cópia temporária, protegendo os exemplos e seus dados."""
    if entrada is None:
        if atividade['categoria'] == 'exemplos':
            entrada = ENTRADAS_EXEMPLOS.get((atividade['semana'], atividade['slides'][0]), '')
        else:
            entrada = ENTRADAS_NOVAS.get((atividade['semana'], atividade['atividade']), '')
    with tempfile.TemporaryDirectory() as temporario:
        destino = Path(temporario) / 'atividade'
        shutil.copytree(ROOT / atividade['pasta'], destino)
        if alterar:
            alterar(destino)
        resultado = subprocess.run([sys.executable, atividade['executar']], cwd=destino,
                                   input=entrada, text=True, capture_output=True, timeout=5)
        arquivos = {f.name: json.loads(f.read_text()) for f in destino.glob('*.json')}
        return resultado, arquivos

def buscar(semana, categoria, nome):
    return next(a for a in ATIVIDADES if (a['semana'], a['categoria'], a['atividade']) == (semana, categoria, nome))

class TestAtividades(unittest.TestCase):
    def test_sintaxe_e_caminhos(self):
        for arquivo in ROOT.rglob('*.py'):
            with self.subTest(arquivo=arquivo):
                ast.parse(arquivo.read_text())
        for atividade in ATIVIDADES:
            self.assertTrue((ROOT / atividade['pasta'] / atividade['executar']).is_file())

    def test_todas_as_atividades(self):
        for atividade in ATIVIDADES:
            with self.subTest(atividade=atividade['pasta']):
                resultado, _ = executar(atividade)
                self.assertEqual(resultado.returncode, 0, resultado.stderr)
                self.assertNotIn('Traceback', resultado.stderr)

    def test_calculos_e_relatorios(self):
        casos = [
            (1, 'pratica_independente', '01_troco', '20.00'),
            (1, 'pratica_independente', '02_tempo', '1 h, 1 min e 1 s'),
            (1, 'pratica_independente', '04_media', '8.00'),
            (1, 'pratica_independente', '05_desconto', '80.00'),
            (1, 'desafios', '01_dias_tempo', '1 dias, 1 horas, 1 minutos e 1 segundos'),
            (2, 'pratica_independente', '03_cinco_numeros', 'Média: 3.00'),
            (2, 'desafios', '03_positivos', 'positivos: 6'),
            (2, 'desafios', '04_nomes', 'Nomes digitados: 2'),
            (2, 'desafios', '05_cadastros', 'Total de cadastros: 1'),
            (3, 'desafios', '02_fatorial', 'Fatorial: 120'),
            (4, 'pratica_independente', '01_nomes', 'Nomes únicos: 3'),
            (4, 'entregaveis', 'sistema_produtos', 'Média: 354.97'),
            (6, 'entregaveis', 'sistema_bancario', 'Instâncias criadas: 15'),
        ]
        for semana, categoria, nome, texto in casos:
            with self.subTest(semana=semana, atividade=nome):
                resultado, _ = executar(buscar(semana, categoria, nome))
                self.assertIn(texto, resultado.stdout)

    def test_classificadores_equivalentes_e_limites(self):
        for idade, renda, categoria in [(17,100000,'Bronze'),(18,2000,'Prata'),(25,5000,'Ouro'),(30,10000,'Diamante'),(30,9999,'Ouro')]:
            for nome in ['01_classificacao_if','02_classificacao_match']:
                resultado,_ = executar(buscar(2,'desafios',nome), f'{idade}\n{renda}\n')
                self.assertIn(categoria, resultado.stdout)

    def test_tres_erros_senha_e_divisao_por_zero(self):
        resultado, _ = executar(buscar(2,'pratica_independente','04_senha'), 'a\nb\nc\n')
        self.assertIn('bloqueado após 3 erros', resultado.stdout)
        resultado, _ = executar(buscar(2,'pratica_independente','02_calculadora'), '4\n10\n0\n')
        self.assertIn('Não é possível dividir por zero', resultado.stdout)
        resultado, _ = executar(buscar(3,'entregaveis','calculadora'), '10\n0\n')
        self.assertIn('Não é possível dividir por zero', resultado.stdout)

    def test_casos_vazios_e_formatacao(self):
        resultado,_=executar(buscar(3,'pratica_independente','03_caixa'),'\n')
        self.assertIn('Total: 0.00',resultado.stdout)
        resultado,_=executar(buscar(4,'pratica_independente','01_nomes'),'0\n')
        self.assertIn('Primeiro e último: ()',resultado.stdout)
        resultado,_=executar(buscar(4,'entregaveis','sistema_produtos'),'0\n100\nacima\n')
        self.assertIn('Nenhum produto cadastrado',resultado.stdout)
        resultado,_=executar(buscar(3,'desafios','03_relatorio'))
        self.assertIn('Linha A\nLinha B',resultado.stdout)

    def test_arquivos_e_validacao(self):
        casos=[('01_clientes','clientes.json'),('03_formulario','formularios.json')]
        for nome,arquivo in casos:
            _,arquivos=executar(buscar(5,'pratica_independente',nome))
            self.assertEqual(arquivos[arquivo]['total_validos'],1)
            self.assertEqual(arquivos[arquivo]['total_invalidos'],1)
        _,arquivos=executar(buscar(5,'pratica_independente','02_log'))
        self.assertEqual(len(arquivos['resumo.json']['ips_unicos']),2)
        self.assertEqual(len(arquivos['resumo.json']['erros']),1)
        _,arquivos=executar(buscar(5,'pratica_independente','04_notas'))
        self.assertEqual(arquivos['relatorio_notas.json']['media'],8)
        self.assertEqual(len(arquivos['relatorio_notas.json']['invalidas']),2)
        _,arquivos=executar(buscar(5,'pratica_independente','05_estoque'))
        self.assertEqual(len(arquivos['relatorio_estoque.json']['filtrados']),2)
        _,arquivos=executar(buscar(5,'entregaveis','analise_dados'))
        self.assertEqual(arquivos['clientes.json']['total_validos'],1)

    def test_excecoes_de_arquivo_e_data(self):
        atividade=buscar(5,'entregaveis','analise_dados')
        resultado,arquivos=executar(atividade,alterar=lambda p:(p/'clientes.csv').unlink())
        self.assertIn('Arquivo não encontrado',resultado.stdout)
        self.assertIn('Processamento encerrado',resultado.stdout)
        self.assertNotIn('clientes.json',arquivos)
        def data_invalida(p):
            f=p/'clientes.csv';f.write_text(f.read_text().replace('2026-10-20','2026-02-30'))
        _,arquivos=executar(atividade,alterar=data_invalida)
        self.assertEqual(arquivos['clientes.json']['total_validos'],0)
        self.assertEqual(arquivos['clientes.json']['total_invalidos'],2)

    def test_csv_sem_colunas_e_opcoes_exemplos(self):
        atividade=buscar(5,'entregaveis','analise_dados')
        def cabecalho_invalido(p):
            (p/'clientes.csv').write_text('campo\nvalor\n')
        resultado,arquivos=executar(atividade,alterar=cabecalho_invalido)
        self.assertIn('Colunas obrigatórias ausentes',resultado.stdout)
        self.assertNotIn('clientes.json',arquivos)
        for slide in [14,19]:
            resultado,_=executar(buscar(5,'exemplos',f'slide-{slide:02d}'),'2\n')
            self.assertEqual(resultado.returncode,0,resultado.stderr)

    def test_lista_segura_e_estatistica(self):
        # Carrega funções sem executar a parte interativa.
        for semana,categoria,nome,arquivo in [(3,'pratica_independente','06_lista_segura','principal.py'),(3,'desafios','01_estatistica','estatistica.py')]:
            atividade=buscar(semana,categoria,nome)
            spec=importlib.util.spec_from_file_location('modulo_testado',ROOT/atividade['pasta']/arquivo)
            modulo=importlib.util.module_from_spec(spec);spec.loader.exec_module(modulo)
            if nome=='06_lista_segura':
                original=['arroz'];nova=modulo.adicionar_seguro(original,'feijao')
                self.assertEqual(original,['arroz']);self.assertEqual(nova,['arroz','feijao'])
            else:
                self.assertEqual(modulo.mediana([1,2,3,4]),2.5)
                self.assertEqual(modulo.moda([1,1,2,2]),[1,2])
                with self.assertRaises(ValueError):modulo.media([])

    def test_banco(self):
        atividade=buscar(6,'entregaveis','sistema_bancario')
        resultado=subprocess.run([sys.executable,'-m','unittest','-v','test_banco.py'],cwd=ROOT/atividade['pasta'],text=True,capture_output=True,timeout=10)
        self.assertEqual(resultado.returncode,0,resultado.stderr)
        self.assertIn('Ran 5 tests',resultado.stderr)

if __name__=='__main__':
    unittest.main()
