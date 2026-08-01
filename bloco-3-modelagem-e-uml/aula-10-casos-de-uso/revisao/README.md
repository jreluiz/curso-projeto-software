# Aula 10 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 10 — Casos de Uso](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

---

### Q-A10-01

Qual é o teste rápido para decidir se algo está dentro ou fora da fronteira do sistema?

- **a)** Se aquilo tem interface gráfica própria, está fora;
- **b)** se você é responsável por consertar quando aquilo quebrar, está dentro; se só pode reclamar com outra pessoa, está fora — e é ator;
- **c)** se aquilo foi desenvolvido pela mesma equipe, está dentro;
- **d)** se aquilo armazena dados do sistema, está dentro.

↩︎ *Aula 10, seção 1 — Onde termina o sistema*

---

### Q-A10-02

O banco de dados do sistema-guia é um ator?

- **a)** Sim, porque troca informação com o sistema;
- **b)** sim, porque pode falhar e exigir tratamento de exceção;
- **c)** depende de estar hospedado na mesma máquina que a aplicação;
- **d)** não: ele está dentro da fronteira, e o que está dentro nunca é ator.

↩︎ *Aula 10, seção 1 — Onde termina o sistema*

---

### Q-A10-03

Por que "Gerenciar reservas" quase nunca é um caso de uso?

- **a)** Porque o verbo "gerenciar" esconde vários objetivos diferentes — reservar, cancelar, consultar, confirmar uso —, e é o nome que se dá quando não se decidiu quais são de verdade;
- **b)** porque o nome é longo demais para caber no diagrama;
- **c)** porque gerenciamento é responsabilidade de um ator administrativo, não do sistema;
- **d)** porque casos de uso precisam começar por um verbo no gerúndio.

↩︎ *Aula 10, seção 2 — Caso de uso não é tela*

---

### Q-A10-04

`Cancelar reserva` acontece apenas às vezes, sob condição, em relação a `Reservar espaço`. Qual relacionamento e qual direção?

- **a)** `include`, do caso base para o incluído;
- **b)** `include`, do caso incluído para o base;
- **c)** `extend`, e a seta vai do extensor para o base — direção contrária à que a intuição pede;
- **d)** generalização, do específico para o geral.

↩︎ *Aula 10, seção 3 — `include`, `extend` e generalização*

---

### Q-A10-05

Qual é a relação entre o diagrama de casos de uso e a especificação textual?

- **a)** O diagrama substitui a especificação quando é suficientemente detalhado;
- **b)** a especificação é opcional e serve apenas para casos de uso complexos;
- **c)** o diagrama é o índice; o conteúdo é a especificação textual — um diagrama com dez elipses e nenhuma especificação não documenta nada;
- **d)** os dois descrevem a mesma coisa em níveis de formalidade diferentes.

↩︎ *Aula 10, seção 4 — A especificação textual — onde está o conteúdo*

---

### Q-A10-06

O `UC-02` tem 6 passos no fluxo principal e 6 casos entre alternativos e de exceção. O que isso ilustra?

- **a)** Que os fluxos de exceção são onde mora a regra de negócio — um caso de uso só com fluxo principal descreve o sistema num dia bom;
- **b)** que a especificação está desbalanceada e o fluxo principal precisa ser detalhado;
- **c)** que o caso de uso é grande demais e deveria ser quebrado;
- **d)** que faltou aplicar `include` para eliminar repetição entre os fluxos.

↩︎ *Aula 10, seção 4 — A especificação textual — onde está o conteúdo*

---

### Q-A10-07

Qual é a técnica para descobrir os fluxos de exceção?

- **a)** Consultar o registro de erros de sistemas parecidos já em produção;
- **b)** listar todas as mensagens de erro que a interface precisará exibir;
- **c)** esperar a fase de testes, quando as exceções aparecem naturalmente;
- **d)** em cada passo do fluxo principal, perguntar "e se não?" — e se o serviço externo não responder, e se o limite estourar, e se dois pedidos chegarem juntos.

↩︎ *Aula 10, seção 4 — A especificação textual — onde está o conteúdo*

---

### Q-A10-08

Como se decide se um caso de uso tem a granularidade certa?

- **a)** Pelo número de passos do fluxo principal, que deve ficar entre cinco e dez;
- **b)** pelo critério da sessão: o que o ator faz em um uso contínuo, com começo, meio e fim, e que ele consideraria resolvido ao sair;
- **c)** pelo tempo estimado de implementação, que deve caber em uma iteração;
- **d)** pelo número de atores envolvidos, que deve ser no máximo dois.

↩︎ *Aula 10, seção 6 — Granularidade*

---

⬅️ [Voltar à Aula 10](../README.md) | ➡️ [Revisão da Aula 11](../../aula-11-diagrama-de-classes/revisao/README.md)
