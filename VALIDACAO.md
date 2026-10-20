# Validação da reorganização

- 84 atividades com arquivo de entrada e README conferidos.
- 112 arquivos Python verificados quanto à sintaxe, incluindo os testes.
- 11 testes de integração/regressão na raiz, com subtestes para executar todas as 84 atividades em cópias temporárias.
- 5 testes adicionais do projeto bancário, chamados pela suíte principal.
- Conferidos os resultados de cálculos, classificadores e seus limites, bloqueio após três erros, divisão por zero, coleções vazias, preservação da lista original, mediana/modas, relatórios JSON, CSV sem colunas obrigatórias, datas inexistentes e arquivos ausentes.
- Os dois exemplos com opções independentes tiveram ambas as opções executadas.
- Todos os links locais dos READMEs e enunciados foram conferidos.

## Executar novamente

```bash
python -m unittest discover -s testes -v
```

Resultado desta atualização: **OK**. Os testes usam a biblioteca padrão, entradas predefinidas e cópias temporárias, sem sobrescrever os dados das atividades.

Os testes cobrem os cenários descritos; não garantem todas as entradas possíveis. A classificação de clientes e as taxas do banco seguem as regras didáticas documentadas nos respectivos READMEs.
