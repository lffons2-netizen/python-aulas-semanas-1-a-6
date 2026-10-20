# Python — exemplos e atividades resolvidas

Aulas das semanas **1 a 6**, organizadas pelo tipo de atividade. Foram retirados os fragmentos conceituais, tabelas de métodos, códigos de imagens/diagramas e exemplos usados somente para demonstrar erros.

| Semana | Conteúdo | Abrir |
|---|---|---|
| 1 | Introdução e cálculos | [Semana 1](semana-01/README.md) |
| 2 | Condicionais e laços | [Semana 2](semana-02/README.md) |
| 3 | Funções e módulos | [Semana 3](semana-03/README.md) |
| 4 | Listas, tuplas e conjuntos | [Semana 4](semana-04/README.md) |
| 5 | Arquivos, regex e exceções | [Semana 5](semana-05/README.md) |
| 6 | Orientação a objetos | [Semana 6](semana-06/README.md) |

## Organização de cada semana

- `exemplos/`: programas completos apresentados nos slides e exercícios guiados; cada pasta tem `original.md` e a versão organizada em arquivos Python.
- `pratica_independente/`: atividades do professor, agora resolvidas.
- `desafios/`: desafios durante a aula, bônus e referências aos sprints.
- `entregaveis/`: projetos finais ou checklist com links para os arquivos que devem ser entregues.
- `ENUNCIADOS.md`: texto dos slides usados para conferir os requisitos.

Cada atividade tem seu próprio README, os números dos slides e o comando de execução. Quando um desafio e um entregável pedem o mesmo sistema, ambos apontam para a mesma solução.

## Como executar no VS Code

Use Python 3.10 ou superior. Abra o terminal **na pasta da atividade** e execute:

```bash
python principal.py
```

Exemplo:

```bash
cd semana-04/entregaveis/sistema_produtos
python principal.py
```

Alguns exemplos têm mais de um programa independente: o `principal.py` permite escolher qual executar. Os arquivos de dados incluídos são fictícios e estão identificados nos READMEs. Os programas da semana 5 gravam relatórios na pasta da própria atividade.

## Decisões nos enunciados abertos

- Semana 2: o slide 50 tem o título “6 mini-desafios”, mas enumera **quatro**. Foram resolvidos os quatro, além dos quatro desafios anteriores e do cadastro bônus.
- A classificação de clientes não define limites. A regra adotada está documentada nas pastas dos classificadores; pode ser alterada para a regra do professor.
- Semana 3: foram escolhidas três funções simples para utilidades.py, porque o enunciado deixa a escolha aberta. Moda retorna todas as modas em caso de empate.
- Semana 4: o mesmo sistema resolve o bônus do slide 40 e o entregável do slide 42.
- Semana 5: todos os cinco cenários do slide 29 estão resolvidos, com leitura/escrita, regex, exceção personalizada e relatório.
- Semana 6: o slide 33 manda escolher um cenário. Foi escolhido **Banco**, também usado no projeto final; não foram criados cinco projetos quando apenas um foi pedido.
- O escopo solicitado é Python. Os trechos em Portugol presentes nos enunciados não foram implementados.

Os códigos em `original.md` são transcrições; os programas de práticas, desafios e entregáveis são **soluções novas elaboradas a partir dos enunciados**.

## Conferir os testes

```bash
python -m unittest discover -s testes -v
```

Veja os resultados e os limites em [VALIDACAO.md](VALIDACAO.md).
