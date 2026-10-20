# Verificação em cópias temporárias; dados sintéticos somente para teste de leitura.
import pathlib,subprocess,tempfile,shutil,json,ast,concurrent.futures,sys
root=pathlib.Path(__file__).resolve().parent
files=sorted(root.glob('semana-*/organizado/**/*.py'))
for f in files:compile(f.read_text(),str(f),'exec')
cases={
 (1,32):'Ana\n20\n',(1,38):'60\n1.67\n',(1,39):'100\n',(1,40):'30\n',(1,41):'4\n5\n',(1,42):'ana\nsilva\n',
 (2,11):'18\n',(2,14):'8\n6\n10\n',(2,15):'8\n6\n10\n',(2,18):'1\n',(2,20):'1\n',(2,21):'1\n',(2,22):'1\n',(2,44):'12\n8\n',(2,46):'8\n',(2,47):'1\n',(2,49):'2\n0\n',
 (4,34):'3\n10\n5\n20\n',(4,35):'1 2 3 4\n',(4,36):'10 5 20 3\n',(4,37):'ana ana joao\n',(4,38):'7 9 8\n',(5,20):'2\n',(5,26):'10\n4\n'}
def run(f):
 rel=f.relative_to(root);parts=rel.parts;w=int(parts[0][-2:]);n=int(parts[2][-2:]);data=cases.get((w,n),'')
 with tempfile.TemporaryDirectory() as td:
  dest=pathlib.Path(td)/'slide';shutil.copytree(f.parent,dest)
  if w==5:
   (dest/'dados.txt').write_text('Linha A\nLinha B\n')
   (dest/'dados.csv').write_text('nome,idade\nAna,25\n')
   (dest/'dados.json').write_text('{"nome": "Ana", "idade": 25}')
  try:
   r=subprocess.run([sys.executable,f.name],cwd=dest,input=data,text=True,capture_output=True,timeout=3)
   return {'file':str(rel),'returncode':r.returncode,'stdout':r.stdout[-1500:],'stderr':r.stderr[-1500:],'stdin':data}
  except subprocess.TimeoutExpired:return {'file':str(rel),'returncode':124,'stdout':'','stderr':'tempo excedido','stdin':data}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:results=list(pool.map(run,files))
expected = {
    'semana-01/organizado/slide-31/bloco_01.py': 'TypeError',
    'semana-01/organizado/slide-33/bloco_02.py': 'ValueError',
    'semana-03/organizado/slide-13/bloco_01.py': 'TypeError',
    'semana-03/organizado/slide-41/bloco_01.py': 'ModuleNotFoundError',
    'semana-06/organizado/slide-07/limitacao.py': 'AttributeError',
    'semana-06/organizado/slide-20/propriedade.py': 'ValueError',
    'semana-06/organizado/slide-25/uso_formas.py': 'TypeError',
}
for result in results:
    wanted = expected.get(result['file'])
    if wanted:
        assert result['returncode'] != 0 and wanted + ':' in result['stderr'], result
        result['verificacao'] = 'erro didático esperado'
    else:
        assert result['returncode'] == 0, result
        result['verificacao'] = 'execução concluída'
# Conferência de resultados dos exercícios guiados e módulos relacionados.
checks = {
    'semana-02/organizado/slide-15/situacao_academica.py': ['APROVADO'],
    'semana-04/organizado/slide-33/principal.py': ['mouse2', 'teclado', 'Total: 3'],
    'semana-04/organizado/slide-35/bloco_01.py': ['[2, 4]'],
    'semana-05/organizado/slide-26/divisao_segura.py': ['Resultado: 2.50', 'Operação encerrada.'],
    'semana-06/organizado/slide-30/teste_conta.py': ['1300.00', '+500', '-200'],
    'semana-06/organizado/slide-31/retangulo.py': ['78.54', '24.00'],
    'semana-06/organizado/slide-32/teste_produtos.py': ['2550.00', '180.00', '60.90'],
}
by_file = {r['file']: r for r in results}
for name, texts in checks.items():
    for text in texts:
        assert text in by_file[name]['stdout'], (name, text, by_file[name])
# Caminhos de erro da divisão, além da execução normal acima.
extra_results = []
for data, message in [('abc\n', 'Entrada inválida!'), ('10\n0\n', 'Não é possível dividir por zero.')]:
    file = root / 'semana-05/organizado/slide-26/divisao_segura.py'
    result = subprocess.run([sys.executable, str(file)], input=data, text=True, capture_output=True, timeout=3)
    assert result.returncode == 0 and message in result.stdout and 'Operação encerrada.' in result.stdout
    extra_results.append({'entrada': data, 'mensagem_verificada': message})
(root/'validacao_execucao.json').write_text(json.dumps({'arquivos': results, 'casos_adicionais': extra_results}, ensure_ascii=False, indent=2))
print(f'Sintaxe: {len(files)} OK; execuções normais: {len(files)-len(expected)}; erros didáticos esperados: {len(expected)}; casos adicionais de exceções: {len(extra_results)}.')
