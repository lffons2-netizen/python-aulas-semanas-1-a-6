# Sistema de análise e validação de cadastros

Semana 5; slide(s): 33.

Status: resolvido em Python.

Dados de entrada incluídos são fictícios e editáveis. apoio.py contém a exceção personalizada, validações e o fluxo try/except/else/finally. A validação de CPF verifica o formato, não os dígitos verificadores. Datas também são verificadas no calendário. O relatório é exibido com f-strings e salvo em JSON.

Justificativa: regex impede formatos incompatíveis; a verificação do calendário rejeita datas inexistentes. FileNotFoundError cobre entrada ausente; DadosInvalidosError identifica registros malformados; ValueError/KeyError/TypeError cobrem conteúdo incompatível; OSError cobre falhas de acesso/escrita. Erros por registro são listados sem descartar os registros válidos. Exemplo de saída com o CSV incluído: total_validos: 1; total_invalidos: 1; arquivo clientes.json.

## Executar

Abra o terminal nesta pasta:

```bash
python principal.py
```

Solução desenvolvida a partir do enunciado; não é transcrição de código já fornecido.
