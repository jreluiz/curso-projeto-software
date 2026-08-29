# Aula 04 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 04 — Arquitetura como decisão de projeto](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

📝 **As respostas vão pelo formulário:** [responder a revisão da Aula 04](https://docs.google.com/forms/d/e/1FAIpQLSc5e2VR3Ps0wQ4X2bxP23tjj431NzDZa3ocmKgBZIKauFE2fA/viewform)

Leia as 8 questões aqui e decida suas respostas antes de abrir o formulário: é **uma resposta por aluno**, com conta Google, e não dá para editar depois de enviar. Ele também pede seu usuário do GitHub. Se o seu nome não estiver na lista da turma, marque a última opção e escreva o nome completo no campo seguinte.

As três últimas são marcadas **[ENADE]**: trazem um **texto-base** com uma situação de projeto, seguido do comando. São mais longas de ler e cobram interpretação, não memória — as alternativas continuam simples, como nas demais.

---

### Q-A04-01

Segundo a aula, o teste que identifica se uma decisão é arquitetural é perguntar:

- **a)** se ela envolve a escolha de alguma tecnologia ou biblioteca externa;
- **b)** quanto custa mudar de ideia sobre ela daqui a seis meses;
- **c)** se ela foi tomada pelo arquiteto do sistema ou pelo restante da equipe;
- **d)** se ela afeta o desempenho do sistema em produção.

↩︎ *Aula 04, seção 1 — Por que isto é assunto de gestão*

---

### Q-A04-02

Um documento de projeto afirma: "a arquitetura do sistema é React com Node e Postgres". De acordo com a aula, o problema dessa frase é que ela:

- **a)** cita tecnologias sem indicar as versões que serão adotadas pela equipe;
- **b)** mistura tecnologias de camadas diferentes numa mesma descrição;
- **c)** confunde a lista de ferramentas com as decisões que estruturam o sistema;
- **d)** não menciona a infraestrutura em que o sistema será implantado.

↩︎ *Aula 04, seção 2 — O que é arquitetura de software*

---

### Q-A04-03

No sistema de delivery, alguém buscou o número de pedidos na fila direto no banco, pulando a camada de negócio. Dois meses depois, a regra mudou — pedido cancelado não conta — e a tela do entregador continuou errada. Segundo a aula, isso ilustra que:

- **a)** a camada de persistência deveria conter as regras de negócio relacionadas aos dados que guarda;
- **b)** o estilo em camadas é inadequado para sistemas que exibem informação em tempo real;
- **c)** a violação da regra do estilo é um atalho razoável sob pressão, cujo custo aparece só na mudança seguinte;
- **d)** a tela do entregador deveria ter sido implementada como um serviço independente.

↩︎ *Aula 04, seção 4 — Estilos arquitetônicos*

---

### Q-A04-04

De acordo com a aula, a razão de existir dos microsserviços é resolver um problema:

- **a)** de organização: permitir que times independentes entreguem sem esperar uns pelos outros;
- **b)** de desempenho: distribuir a carga entre vários servidores menores e mais baratos;
- **c)** de confiabilidade: garantir que a falha de um serviço nunca afete os demais;
- **d)** de manutenção: reduzir o tamanho do código que cada desenvolvedor precisa entender.

↩︎ *Aula 04, seção 5 — Monolito × microsserviços, com honestidade*

---

### Q-A04-05

A linha "alternativas descartadas" é apontada na aula como a parte que dá sentido ao ADR porque:

- **a)** demonstra ao patrocinador que a equipe avaliou o problema com o cuidado devido;
- **b)** permite retomar rapidamente a segunda opção caso a primeira se mostre inviável;
- **c)** documenta quem propôs cada alternativa, tornando possível cobrar depois;
- **d)** registra sob quais premissas a decisão foi tomada, permitindo revê-la quando elas mudarem.

↩︎ *Aula 04, seção 6 — Registrar a decisão: o ADR*

---

### Q-A04-06

**[ENADE]**

Uma equipe de três pessoas propôs, para uma plataforma de contratação de serviços ainda sem usuários, uma arquitetura dividida em sete serviços implantados de forma independente. A justificativa apresentada na reunião foi a necessidade de escalabilidade, sem que nenhum número de carga esperada fosse apresentado.

A plataforma é financiada pela reserva pessoal de dois fundadores, que dura seis meses, e não há equipe de operação: os próprios desenvolvedores respondem por eventuais falhas em produção.

Considerando a situação descrita e o conteúdo da aula, a proposta é inadequada principalmente porque:

- **a)** não há times independentes a desacoplar, de modo que resta apenas o custo operacional da divisão;
- **b)** sete serviços é um número excessivo mesmo para equipes grandes e experientes;
- **c)** plataformas de contratação de serviços são, por natureza, mais adequadas ao estilo em camadas;
- **d)** a decisão foi tomada pela equipe técnica, quando caberia aos fundadores decidi-la.

↩︎ *Aula 04, seção 5 — Monolito × microsserviços, com honestidade*

---

### Q-A04-07

**[ENADE]**

Numa transportadora com 60 veículos, a equipe decidiu processar a telemetria em tempo real. A decisão foi tomada em uma conversa técnica de vinte minutos, sem participação do gestor de frota nem da diretoria.

Seis meses depois, o projeto está atrasado: o processamento em tempo real exigiu infraestrutura que não constava do orçamento e uma disponibilidade que a operação não sabia que teria de sustentar. A regra de negócio que motivou a funcionalidade exige avisar sobre manutenção com três dias de antecedência.

Considerando a situação descrita e o conteúdo da aula, o erro da equipe foi:

- **a)** ter escolhido o processamento em tempo real, que é tecnicamente inadequado a esse volume de veículos;
- **b)** não ter registrado a decisão em um ADR, o que impediu a diretoria de acompanhá-la;
- **c)** não ter incluído a equipe de operação na conversa técnica que definiu a solução;
- **d)** ter decidido sem que o custo da escolha aparecesse para quem pagava e para quem sustentaria a operação.

↩︎ *Aula 04, seção 7 — A decisão arquitetural é do projeto, não do time técnico*

---

### Q-A04-08

**[ENADE]**

Uma equipe registrou, no início do projeto, um ADR decidindo guardar os dados clínicos e os administrativos em bancos separados, por causa da exigência de auditoria sobre acesso a dado de saúde. O documento tinha meia página e listava duas alternativas descartadas.

Um ano depois, com o projeto em andamento e outra equipe assumindo, alguém propôs unificar os dois bancos para simplificar os relatórios. A proposta foi levada à reunião como novidade, e três pessoas passaram duas horas discutindo os mesmos pontos já registrados no ADR — que ninguém consultou porque não sabia que existia.

Considerando a situação descrita e o conteúdo da aula, o que falhou foi:

- **a)** o formato do ADR, que por ser curto demais não preservou os argumentos da decisão original;
- **b)** o uso do registro, e não o registro em si: um ADR só evita refazer o debate se for consultado;
- **c)** a decisão original, que deveria ter sido revista formalmente antes da troca de equipe;
- **d)** a numeração dos ADRs, que impediu localizar o documento referente ao assunto discutido.

↩︎ *Aula 04, seção 6 — Registrar a decisão: o ADR*

---

⬅️ [Voltar à Aula 04](../README.md) | 🏠 [Início](../../../README.md)
