# Aula 12 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 12 — Operação: observabilidade e manutenção](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

As três últimas são marcadas **[ENADE]**: trazem um **texto-base** com uma situação de projeto, seguido do comando. São mais longas de ler e cobram interpretação, não memória — as alternativas continuam simples, como nas demais.

---

### Q-A12-01

Segundo a aula, para responder *"o delivery está bom?"* sem perguntar a ninguém, o que mais vale acompanhar?

- **a)** a proporção de pedidos confirmados, que mostra o que o cliente está vivendo;
- **b)** o uso de processador dos servidores, que mostra se a máquina está sobrecarregada;
- **c)** a quantidade de memória livre, que mostra se o sistema está perto de travar;
- **d)** o número de linhas gravadas no log por minuto, que mostra se o sistema está ativo.

↩︎ *Aula 12, seção 1 — Monitorar a máquina não é observar o serviço*

---

### Q-A12-02

O pedido 4471 passou pelos serviços de pedido, pagamento, cozinha e aviso ao cliente, e levou 40 segundos para ser confirmado. Para descobrir em qual serviço o tempo foi gasto, o sinal mais adequado é:

- **a)** uma métrica com o tempo médio de confirmação de todos os pedidos do dia;
- **b)** o uso de processador de cada servidor no momento em que o pedido foi feito;
- **c)** o rastro do pedido, que mostra o caminho dele por cada serviço e o tempo gasto em cada um;
- **d)** o CHANGELOG da última versão implantada.

↩︎ *Aula 12, seção 2 — Logs, métricas e rastros*

---

### Q-A12-03

Um serviço tem SLO de 99,9% de disponibilidade em 30 dias. Segundo a aula, o orçamento de erro desse serviço é:

- **a)** o valor que a empresa reserva para pagar multas quando o serviço fica fora do ar;
- **b)** os cerca de 43 minutos de indisponibilidade que o serviço pode ter em 30 dias sem violar o objetivo;
- **c)** o número máximo de defeitos que o time pode deixar chegar à produção em um mês;
- **d)** a diferença entre o custo previsto e o custo real de operar o serviço.

↩︎ *Aula 12, seção 3 — SLO: quanto de falha é aceitável*

---

### Q-A12-04

Os pagamentos do delivery pararam minutos depois de uma implantação. Segundo a aula, a primeira prioridade de quem responde ao incidente é:

- **a)** encontrar a causa do defeito antes de mexer em qualquer coisa, para não piorar a situação;
- **b)** identificar quem fez a implantação, para que explique o que mudou;
- **c)** escrever o postmortem enquanto os detalhes ainda estão frescos na memória;
- **d)** restaurar o serviço — reverter a implantação ou desligar a flag — e investigar a causa depois.

↩︎ *Aula 12, seção 4 — Incidente: restaurar primeiro, entender depois*

---

### Q-A12-05

Uma resolução nova obriga o prontuário de uma clínica-escola a registrar quem consultou cada prontuário, e quando. A mudança no sistema para atender a resolução é uma manutenção:

- **a)** corretiva, porque o sistema estava errado ao não registrar as consultas;
- **b)** perfectiva, porque melhora o que já funcionava, a pedido de quem usa;
- **c)** preventiva, porque reduz o risco de defeitos no futuro;
- **d)** adaptativa, porque acompanha uma mudança no ambiente externo ao sistema.

↩︎ *Aula 12, seção 6 — Manutenção, evolução e dívida técnica*

---

### Q-A12-06

**[ENADE]**

Numa sexta-feira à noite, um desenvolvedor de uma loja virtual executou um script de limpeza no banco de dados de produção, acreditando estar conectado ao banco de testes. Seis horas de pedidos se perderam. Descobriu-se, então, que a cópia de segurança diária falhava havia semanas: o aviso de falha era enviado a um endereço de e-mail que ninguém lia.

Na reunião de segunda-feira, o diretor propôs demitir o desenvolvedor e proibir que qualquer pessoa da equipe tivesse acesso ao banco de produção.

Considerando a situação descrita e o conteúdo da aula, a condução mais adequada é:

- **a)** acatar a proposta do diretor, já que a causa do incidente foi o erro de uma pessoa;
- **b)** fazer um postmortem sem culpa, que investigue as causas contribuintes — o acesso fácil à produção, o backup nunca restaurado, o aviso que ninguém recebia — e defina ações com dono e prazo;
- **c)** encerrar o assunto sem registro, porque os dados não podem mais ser recuperados e discuti-lo só desgasta a equipe;
- **d)** exigir que o desenvolvedor escreva sozinho o relatório do incidente, como forma de assumir a responsabilidade.

↩︎ *Aula 12, seção 5 — Postmortem sem culpa*

---

### Q-A12-07

**[ENADE]**

O time de um aplicativo de agendamento recebe cerca de 300 alertas por semana: processador acima de 70%, disco acima de 80%, uma requisição lenta isolada, um servidor que reinicia e volta sozinho em segundos. Quase todos se resolvem sem que ninguém faça nada, e o time passou a silenciar o canal.

Num domingo, os agendamentos deixaram de ser gravados por quatro horas. O alerta correspondente disparou, no mesmo canal, e ninguém viu; o problema só foi descoberto pelas reclamações dos clientes.

Considerando a situação descrita e o conteúdo da aula, a mudança mais adequada é:

- **a)** contratar uma pessoa para acompanhar o canal de alertas em tempo integral;
- **b)** acrescentar novos alertas, para cobrir também outros casos parecidos com o dos agendamentos;
- **c)** deixar como alerta só o que exige ação e afeta o cliente, como agendamentos não gravados, e levar o resto para o painel;
- **d)** aumentar os limites de todos os alertas, para que disparem com menos frequência.

↩︎ *Aula 12, seção 3 — SLO: quanto de falha é aceitável*

---

### Q-A12-08

**[ENADE]**

Há dois anos, para cumprir o prazo de lançamento, o time de um sistema de delivery copiou a regra de cálculo do frete para três lugares do código, prometendo unificá-la "depois". A promessa não foi registrada em lugar nenhum. Hoje, cada mudança no frete leva uma semana e costuma quebrar um dos três lugares.

O time pede ao dono "três semanas para refatorar o frete", e o dono recusa, porque prefere as funcionalidades novas que os clientes pedem.

Considerando a situação descrita e o conteúdo da aula, a atitude mais adequada do time é:

- **a)** registrar a dívida e apresentá-la ao dono em tempo e dinheiro — quanto custa cada mudança no frete hoje, e quanto custaria depois de unificar —, para que ele decida;
- **b)** refatorar o frete aos poucos, escondido dentro das próximas funcionalidades, sem avisar o dono;
- **c)** recusar-se a fazer funcionalidades novas até que o frete seja refatorado;
- **d)** aceitar a recusa e não tocar mais no assunto, já que dívida técnica é problema só da equipe técnica.

↩︎ *Aula 12, seção 6 — Manutenção, evolução e dívida técnica*

---

⬅️ [Voltar à Aula 12](../README.md) | 🏠 [Início](../../../README.md)
