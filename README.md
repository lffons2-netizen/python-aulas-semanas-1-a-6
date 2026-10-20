# Python — aulas das semanas 1 a 6

Códigos das aulas de Python, separados por **semana, slide e bloco**. Inclui os trechos que aparecem em imagens. Portugol foi excluído.

## Escolha uma semana

| Semana | Conteúdo |
|---|---|
| [1](semana-01/) | Introdução, variáveis, operadores, strings e entrada/saída |
| [2](semana-02/) | Condicionais, match/case, for e while |
| [3](semana-03/) | Funções, parâmetros, mutabilidade e módulos |
| [4](semana-04/) | Listas, tuplas, conjuntos e manipulação de coleções |
| [5](semana-05/) | Arquivos, expressões regulares e exceções |
| [6](semana-06/) | Programação orientada a objetos |

## Duas versões

- **`original/`**: transcrição dos códigos dos slides, inclusive erros didáticos e quebras visuais do PDF. `transcricao.md` mostra todos os códigos da semana; cada slide também possui seus blocos em `.txt`.
- **`organizado/`**: exemplos separados em arquivos `.py`, com módulos relacionados na mesma pasta. Quebras que impediam a execução foram corrigidas e continuações reunidas. Fragmentos de sintaxe incompleta ficam em `.md`.

Os arquivos não formam um único programa. Execute um exemplo por vez. Exemplos classificados como **erro didático** podem lançar exceções de propósito; **trechos que requerem contexto** dependem das variáveis da explicação. Veja o índice de cada semana e o [registro de alterações](ALTERACOES.md).

## Como abrir no VS Code

1. Clique em **Code → Download ZIP** e extraia, ou clone este repositório.
2. Abra a pasta extraída no VS Code.
3. Instale Python 3.10 ou superior e a extensão Python do VS Code.
4. Abra um terminal na pasta do exemplo e execute seu arquivo.

Exemplo já existente nos slides:

```bash
cd semana-04/organizado/slide-33
python principal.py
```

No Windows, `py` pode substituir `python`; em alguns sistemas, use `python3`.

## Arquivos de entrada

A semana 5 usa arquivos como `dados.txt`, `dados.csv`, `dados.json`, `acesso.log` e `produtos.csv`. A semana 6 usa `clientes.txt`. O conteúdo desses arquivos não foi inventado para o repositório. Crie-os com os dados da sua atividade e execute o programa a partir da pasta em que eles estão. Os exemplos de tratamento de arquivo inexistente funcionam sem criá-los.

## Verificação

Consulte [VALIDACAO.md](VALIDACAO.md) para os testes realmente executados e seus limites. A versão original não passa por correção ou compilação.

Material organizado para estudo a partir dos PDFs fornecidos. Não há licença de redistribuição atribuída ao material original.
