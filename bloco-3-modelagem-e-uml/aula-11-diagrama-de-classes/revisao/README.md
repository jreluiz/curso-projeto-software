# Aula 11 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 11 — Diagrama de Classes](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

---

### Q-A11-01

`CadastrarEspaco` foi entregue como classe num diagrama de análise. Qual é o problema?

- **a)** O nome deveria estar no plural, para representar o conjunto de espaços;
- **b)** falta declarar a visibilidade dos atributos;
- **c)** o nome deveria seguir a convenção de nomenclatura em inglês;
- **d)** classe é substantivo: aquilo é uma operação com fantasia de classe, e provavelmente pertence a alguma classe de verdade.

↩︎ *Aula 11, seção 1 — As coisas que existem*

---

### Q-A11-02

Por que a regra de bolso é "atributo privado, operação pública"?

- **a)** Porque é a convenção adotada pela maioria das linguagens orientadas a objetos;
- **b)** porque atributos públicos consomem mais memória em tempo de execução;
- **c)** porque quem controla o próprio estado consegue garantir que ele nunca fique inválido — uma `Reserva` que deixa qualquer um mexer em `fim` não promete que `fim` é depois de `inicio`;
- **d)** porque operações privadas não podem ser testadas automaticamente.

↩︎ *Aula 11, seção 2 — Visibilidade*

---

### Q-A11-03

Qual é o erro mais comum ao definir multiplicidades?

- **a)** Usar `*` em vez de `0..*`, que é a notação correta em Mermaid;
- **b)** esquecer que toda associação tem duas multiplicidades e que as duas precisam ser lidas em voz alta, nos dois sentidos;
- **c)** colocar multiplicidade em associações de herança;
- **d)** usar intervalos fechados como `2..5`, que a UML não recomenda.

↩︎ *Aula 11, seção 3 — Associação e multiplicidade*

---

### Q-A11-04

`Reserva "1" *-- "0..1" ConfirmacaoDeUso`. O que o mínimo `0` afirma sobre o mundo?

- **a)** Que uma reserva pode nunca ter confirmação — e é exatamente esse `0` que representa o problema da sala vazia;
- **b)** que a confirmação é opcional do ponto de vista da interface, mas obrigatória no banco;
- **c)** que a confirmação pode ser criada antes da reserva;
- **d)** que a reserva pode ser apagada sem apagar a confirmação.

↩︎ *Aula 11, seção 3 — Associação e multiplicidade*

---

### Q-A11-05

Quais são as duas perguntas que decidem entre agregação e composição?

- **a)** A parte pode existir sem o todo? E, se o todo for destruído, a parte vai junto?
- **b)** A parte é criada junto com o todo? E o todo conhece o número de partes?
- **c)** A relação é obrigatória nos dois sentidos? E há mais de uma parte?
- **d)** A parte tem identidade própria? E o todo aparece antes dela no diagrama?

↩︎ *Aula 11, seção 4 — Agregação × composição*

---

### Q-A11-06

A distinção entre agregação e composição não muda nenhuma decisão nem nenhuma regra do domínio. O que fazer?

- **a)** Escolher agregação, que é a opção mais conservadora;
- **b)** usar associação simples e seguir em frente: losango errado documenta uma mentira, losango ausente apenas documenta menos;
- **c)** escolher composição, porque ela expressa vínculo mais forte;
- **d)** deixar a decisão para a fase de projeto, quando a tecnologia estiver definida.

↩︎ *Aula 11, seção 4 — Agregação × composição*

---

### Q-A11-07

`SalaDeEstudo` e `Laboratorio` como subclasses de `Espaco`. Por que a modelagem está errada?

- **a)** Porque `Espaco` deveria ser uma interface, não uma superclasse;
- **b)** porque as subclasses não têm atributos próprios suficientes;
- **c)** porque a sala pode ser convertida em laboratório no recesso — e o objeto precisaria mudar de classe, o que não existe. O que muda é um atributo ou um objeto associado;
- **d)** porque a UML não permite mais de duas subclasses para a mesma superclasse.

↩︎ *Aula 11, seção 5 — Herança e generalização*

---

### Q-A11-08

Aplicando a técnica dos substantivos, você não consegue decidir se `Finalidade` é classe ou atributo. O que isso significa?

- **a)** Que a técnica falhou e é preciso recorrer a outra abordagem;
- **b)** que `Finalidade` deve ser modelada como atributo, por ser o caso mais simples;
- **c)** que o documento de requisitos está incompleto e precisa ser refeito;
- **d)** que a técnica produziu uma pergunta para o cliente — e é assim que deve ser: modelagem que não gera pergunta está inventando o domínio.

↩︎ *Aula 11, seção 7 — Do substantivo à classe*

---

⬅️ [Voltar à Aula 11](../README.md) | ➡️ [Revisão da Aula 12](../../aula-12-modelagem-dinamica/revisao/README.md)
