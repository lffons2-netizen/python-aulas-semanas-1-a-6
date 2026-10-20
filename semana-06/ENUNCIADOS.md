# Enunciados — semana 6

Texto dos slides correspondentes, para conferir a solução com o pedido do professor. A implementação deste repositório cobre somente Python, conforme solicitado; as versões em Portugol mencionadas nos slides não foram incluídas.

## Slide 33

```text
Mini-Desafios (Prática Independente)
 Mini-Desafios (Prática Independente)

   Escolha um cenário e modele o sistema do zero com as ferramentas de hoje.

   CENÁRIOS                                                        PARA CADA CENÁRIO, FAÇA


    Cenário              Classes sugeridas                                                                                       1. Modele classes com atributos e métodos.
                                                                                       2. Use __init__ para inicializar.
     Biblioteca          Livro, Usuario, Emprestimo
                                                                                       3. Implemente __str__ para exibição.
    E-commerce       Produto, Cliente, Pedido, ItemPedido                    4. Aplique encapsulamento com @property.
                                                                                       5. Use herança quando fizer sentido.
     Escola             Aluno, Professor, Turma, Disciplina                                                                                       6. Aplique polimorfismo em objetos diferentes.
                                                                                       7. Teste com prints e documente com docstrings.
    Banco             Conta, ContaCorrente, ContaPoupanca


    Streaming         Usuario, Filme, Serie, Avaliacao

                                                                               CRITÉRIO DE ENTREGA

                                                             ✓Código roda sem erro.
      Dica de modelagem: sublinhe os substantivos do enunciado (viram
                                                                        ✓Classes, herança, polimorfismo e docstrings.       classes) e os verbos (viram métodos). "O usuário empresta um livro"
       vira usuario.emprestar(livro).                         ✓Nomes descritivos (PEP 8) e repositório no GitHub.





                                                                                                                                       33
```

## Slide 37

```text
Desafio Sprint 6: Sistema Orientado a Objetos
 Desafio Sprint 6: Sistema Orientado a Objetos

   Objetivo: criar um sistema completo com POO, usando herança, polimorfismo e encapsulamento.

   ENTREGÁVEIS                                                                    EXEMPLO DE DIAGRAMA NO README


                                                                                                        README.md  (mermaid)
          Modelagem: pelo menos 4 classes, uma hierarquia de herança e uma classe
      1
             abstrata.
                                                                                       classDiagram
                                                                                          Conta <|-- ContaCorrente
                                                                                          Conta <|-- ContaPoupanca
           Implementação: __init__ e __str__ em todas as classes; @property para               Cliente "1" o-- "*" Conta
      2
            atributos validados; métodos com responsabilidade única.



      3    Polimorfismo: pelo menos um método sobrescrito e uso de super().                                                                                               Entrega: repositório no GitHub com todos os
                                                                                                   arquivos. Cole o link no Forms até o prazo.


      4    Testes: 10+ instâncias, demonstração de polimorfismo e tratamento de exceções.


                                                                                    Próxima aula: Ecossistema Científico: NumPy,
         README: diagrama de classes (Mermaid), justificativa das decisões e exemplos de        Pandas e Matplotlib.      5
            uso.




                                                                                                                                       37
```

