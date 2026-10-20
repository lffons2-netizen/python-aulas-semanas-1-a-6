# Validação

- **239 blocos originais**: comparação literal com a transcrição de origem, por semana/slide/bloco. Sem alterações na versão original.
- **235 arquivos Python organizados**: todos passam na análise de sintaxe.
- **228 execuções concluídas** em cópias temporárias, com entradas de teste para os programas interativos e dados sintéticos somente durante os testes de arquivos.
- **7 erros didáticos esperados**, conferidos pelo tipo da exceção: string imutável; conversão inválida; procedimento sem retorno; nome de módulo incorreto; dicionário sem método; preço negativo; instanciação de classe abstrata.
- Resultados conferidos em situação acadêmica, módulos de estoque, filtro de pares, divisão, conta bancária, formas e preços com polimorfismo.
- Duas entradas adicionais verificam ValueError e divisão por zero, incluindo a execução de finally.
- Todos os caminhos do catálogo apontam para arquivos existentes.

## Repetir

Na raiz do repositório:

```bash
python verificar.py
```

O verificador roda os exemplos em diretórios temporários, sem sobrescrever os arquivos de estudo. Usa apenas a biblioteca padrão e grava o relatório em `validacao_execucao.json`. Os dados sintéticos de leitura existem somente nas cópias temporárias; não são novos exemplos atribuídos aos slides.

A verificação não garante todas as entradas possíveis. Os fragmentos em Markdown e os códigos originais deliberadamente inválidos não são anunciados como programas executáveis.
