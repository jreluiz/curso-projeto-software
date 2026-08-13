# Aula 14 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 14 — Entregar e sustentar](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

As três últimas são marcadas **[ENADE]**: trazem um **texto-base** com uma situação de projeto, seguido do comando. São mais longas de ler e cobram interpretação, não memória — as alternativas continuam simples, como nas demais.

---

### Q-A14-01

Segundo a aula, a regra que faz o pipeline valer é que:

- **a)** cada ambiente execute a bateria completa de verificação;
- **b)** o mesmo pacote atravesse todos os ambientes, mudando apenas a configuração;
- **c)** a passagem entre ambientes exija aprovação de um responsável;
- **d)** o ambiente de homologação seja isolado da rede de produção.

↩︎ *Aula 14, seção 2 — O pipeline e os ambientes*

---

### Q-A14-02

O ganho de gestão trazido pela **feature flag** é que ela:

- **a)** reduz o número de defeitos que chegam a produção;
- **b)** dispensa o ambiente de homologação para funcionalidades pequenas;
- **c)** separa a decisão de liberar da decisão de implantar;
- **d)** elimina a necessidade de plano de retorno para a mudança.

↩︎ *Aula 14, seção 3 — Feature flag e o lançamento controlado*

---

### Q-A14-03

No plano de retorno de uma mudança, a linha apontada como mais importante e a que sempre falta é:

- **a)** quanto tempo leva para voltar;
- **b)** quem executa o procedimento de retorno;
- **c)** qual versão anterior será restaurada;
- **d)** qual critério define que se deve voltar.

↩︎ *Aula 14, seção 4 — Mudança em produção precisa de caminho de volta*

---

### Q-A14-04

Um painel exibe processador em 30% e memória em 40%, tudo em verde, enquanto 30% dos pedidos falham há dois dias. Segundo a aula, o que falta é:

- **a)** instrumentar o comportamento do negócio, e não apenas a máquina;
- **b)** reduzir o intervalo de coleta das métricas de infraestrutura;
- **c)** configurar alertas sobre os indicadores já existentes no painel;
- **d)** aumentar a capacidade do servidor para absorver a carga.

↩︎ *Aula 14, seção 5 — Observabilidade: registro, métrica e alerta*

---

### Q-A14-05

Entre os quatro tipos de manutenção, a aula aponta como **a maior** em volume:

- **a)** a corretiva, que conserta defeitos encontrados em produção;
- **b)** a adaptativa, que acompanha mudanças de lei e de integrações;
- **c)** a preventiva, que reduz o risco de defeitos futuros;
- **d)** a perfectiva, que melhora o que já funciona a pedido de quem usa.

↩︎ *Aula 14, seção 6 — Manutenção: os quatro tipos*

---

### Q-A14-06

**[ENADE]**

Uma equipe planejou a publicação de uma nova versão que converte todos os endereços cadastrados para um formato novo, removendo o formato antigo do banco de dados. A publicação foi agendada para uma terça-feira à tarde.

No plano de implantação, o item "retorno" foi preenchido com a frase "reverter para a versão anterior em caso de falha". Nenhuma outra informação foi registrada sobre o assunto.

Considerando a situação descrita e o conteúdo da aula, o defeito do plano é que:

- **a)** a publicação deveria ter sido agendada para um horário de menor movimento;
- **b)** a conversão de dados exigiria aprovação prévia do comitê de mudanças;
- **c)** uma migração destrutiva não tem retorno, e o plano precisa ser outro;
- **d)** faltou indicar o tempo estimado para a execução do procedimento de retorno.

↩︎ *Aula 14, seção 4 — Mudança em produção precisa de caminho de volta*

---

### Q-A14-07

**[ENADE]**

Um contrato de manutenção prevê o atendimento de defeitos identificados no sistema, com prazos definidos por gravidade. No primeiro ano de vigência, entraram três demandas: adequar o cadastro a uma exigência legal nova, acompanhar a mudança de interface de um parceiro de entrega, e implementar um filtro solicitado pelo cliente.

O fornecedor alegou que nenhuma das três é defeito, e a discussão sobre quem paga se estendeu por semanas, com o prazo legal da primeira correndo.

Considerando a situação descrita e o conteúdo da aula, o problema de origem foi:

- **a)** o fornecedor ter interpretado o contrato de forma restritiva e literal;
- **b)** o contrato cobrir apenas a manutenção corretiva, que é a menor parte do trabalho;
- **c)** o cliente ter solicitado um filtro novo dentro de um contrato de manutenção;
- **d)** a ausência de um comitê para classificar as demandas antes do encaminhamento.

↩︎ *Aula 14, seção 6 — Manutenção: os quatro tipos*

---

### Q-A14-08

**[ENADE]**

A equipe de um restaurante identificou que uma estrutura mal resolvida no sistema faz com que cada alteração naquela área leve três vezes mais tempo do que deveria. Faltam duas semanas para a temporada de inverno, quando o volume de pedidos dobra, e o dono quer duas funcionalidades novas antes disso.

A equipe apresentou a situação ao dono usando os termos "acoplamento", "refatoração" e "dívida técnica". O dono respondeu que prefere as funcionalidades.

Considerando a situação descrita e o conteúdo da aula, o que faltou à equipe foi:

- **a)** traduzir a dívida em tempo e dinheiro, para que ela pudesse disputar prioridade;
- **b)** insistir na decisão técnica, já que o dono não tem formação para avaliá-la;
- **c)** registrar a dívida formalmente antes de levá-la à discussão;
- **d)** apresentar a proposta com antecedência maior em relação à temporada.

↩︎ *Aula 14, seção 7 — Evolução e dívida técnica*

---

⬅️ [Voltar à Aula 14](../README.md) | 🏠 [Início](../../../README.md)
