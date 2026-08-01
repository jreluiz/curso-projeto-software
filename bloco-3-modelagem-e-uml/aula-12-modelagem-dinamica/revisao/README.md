# Aula 12 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 12 — Modelagem Dinâmica](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

---

### Q-A12-01

Qual pergunta separa a visão estática da dinâmica?

- **a)** "Isto é verdade o tempo todo, ou isto acontece?" — o que é verdade o tempo todo é estático; o que acontece pede diagrama dinâmico;
- **b)** "Isto pertence ao domínio ou à tecnologia?";
- **c)** "Isto o cliente valida, ou só a equipe entende?";
- **d)** "Isto muda com frequência, ou é estável?".

↩︎ *Aula 12, seção 1 — O que o retângulo não conta*

---

### Q-A12-02

Você desenhou um diagrama de sequência e há uma mensagem que não corresponde a nenhum passo do caso de uso. O que concluir?

- **a)** Que o diagrama de sequência está mais detalhado, o que é esperado;
- **b)** que um dos dois documentos está errado — e essa conferência é um dos usos mais valiosos do diagrama de sequência;
- **c)** que a mensagem é uma chamada interna e não precisa aparecer na especificação;
- **d)** que o caso de uso precisa ser reescrito no formato de história de usuário.

↩︎ *Aula 12, seção 2 — Sequência: o cenário virando mensagens*

---

### Q-A12-03

Um diagrama de sequência tem apenas o ator e uma caixa chamada "Sistema". Qual é o diagnóstico?

- **a)** Está correto para o nível de contexto, equivalente ao C4 nível 1;
- **b)** falta apenas acrescentar as ativações e os retornos;
- **c)** ele não mostra nada que a especificação já não dissesse — sequência é sobre colaboração entre partes do sistema, não sobre o fluxo do usuário;
- **d)** está correto, desde que o cenário tenha um único passo.

↩︎ *Aula 12, seção 2 — Sequência: o cenário virando mensagens*

---

### Q-A12-04

Por que o diagrama de atividades é o preferido para validar processo com o cliente?

- **a)** Porque é o único diagrama dinâmico que a UML padroniza formalmente;
- **b)** porque exige menos tempo de desenho que os outros dois;
- **c)** porque mostra quem faz cada coisa, o que interessa ao cliente;
- **d)** porque a secretaria lê um fluxograma sem treinamento — e ele descreve o processo, não a colaboração entre partes do software.

↩︎ *Aula 12, seção 4 — Atividades: o fluxo do trabalho*

---

### Q-A12-05

Qual é a palavra decisiva na definição do diagrama de estados?

- **a)** "Transição": o diagrama existe para mostrar o que dispara cada mudança;
- **b)** "Final": todo diagrama de estados precisa de um estado final marcado;
- **c)** "Evento": só eventos externos provocam mudança de estado;
- **d)** "Um": o diagrama descreve um objeto — não o sistema. O ciclo do `Bloqueio` é um; o da `Reserva` é outro diagrama.

↩︎ *Aula 12, seção 5 — Estados: o ciclo de vida de um objeto*

---

### Q-A12-06

No diagrama de estados do `Bloqueio` não há seta de `encerrado` para `ativo`. O que essa ausência comunica?

- **a)** Que o diagrama está incompleto e a transição foi esquecida;
- **b)** que a transição é possível mas rara, e por isso foi omitida;
- **c)** que bloqueio encerrado não volta — é uma regra, e o diagrama de estados a tornou visível;
- **d)** que a transição depende de intervenção manual e por isso não é modelada.

↩︎ *Aula 12, seção 5 — Estados: o ciclo de vida de um objeto*

---

### Q-A12-07

A transição `agendado → ativo` acontece pela passagem do tempo, e não por alguém clicar. Que consequência isso tem?

- **a)** Nenhuma para o projeto: é apenas uma anotação no diagrama;
- **b)** o sistema precisa saber observar o tempo — e isso vira uma peça a construir, operar e monitorar;
- **c)** a transição deveria ser removida, por não ter ator associado;
- **d)** o estado `agendado` deveria ser modelado como atributo, não como estado.

↩︎ *Aula 12, seção 5 — Estados: o ciclo de vida de um objeto*

---

### Q-A12-08

Seu diagrama ficou trivial — uma linha reta, sem decisão nem alternativa. O que isso indica?

- **a)** Que a pergunta pedia outro diagrama: desenho trivial e desenho ilegível são os dois sinais de escolha errada;
- **b)** que o cenário escolhido é simples e o diagrama está correto;
- **c)** que faltou incluir os fluxos de exceção no mesmo desenho;
- **d)** que o diagrama deveria ser substituído por texto corrido.

↩︎ *Aula 12, seção 6 — Qual usar quando*

---

⬅️ [Voltar à Aula 12](../README.md) | ➡️ [Revisão da Aula 13](../../../bloco-4-projeto-de-software/aula-13-principios-de-projeto/revisao/README.md)
