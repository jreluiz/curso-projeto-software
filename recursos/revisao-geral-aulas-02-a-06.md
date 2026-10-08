# Revisão geral — Aulas 02 a 06

### R-01

Um projeto tem o escopo fechado em edital e será entregue em quatro partes utilizáveis, cada uma acrescentando ao que já está no ar. Segundo a aula, esse projeto:

- **a)** é contraditório: escopo fechado em edital exige entrega única ao fim do prazo;
- **b)** é preditivo e incremental ao mesmo tempo, porque o eixo e o recorte das entregas são coisas diferentes;
- **c)** é adaptativo, porque entregar em partes é característica da ponta adaptativa do eixo;
- **d)** é iterativo, porque cada parte melhora aquilo que a parte anterior entregou.

↩︎ *Aula 02, seções 3 e 5 — Incremental: entregar em pedaços; Preditivo × adaptativo: um eixo, não dois campos*

---

### R-02

No termo de abertura de um projeto consta, entre as premissas, "o servidor do datacenter institucional estará disponível em março". Em março, o datacenter informa que não haverá vaga antes de julho. Segundo a aula:

- **a)** trata-se de uma restrição mal classificada, porque a indisponibilidade foi imposta de fora do projeto;
- **b)** o projeto deve prosseguir, porque premissa é estimativa de trabalho e não compromisso formal;
- **c)** o termo de abertura perde validade e precisa de nova assinatura do patrocinador;
- **d)** a premissa não se confirmou, e o plano que foi construído sobre ela cai junto.

↩︎ *Aula 03, seção 2 — Iniciação: o termo de abertura*

---

### R-03

Numa reunião de maio, o cliente pediu um relatório que não constava da EAP nem da linha de base aprovada em março. A equipe aceitou e passou a construí-lo sem alterar o plano. Em julho, o painel de acompanhamento aponta atraso. Segundo a aula, o que explica o atraso registrado contra a equipe é que:

- **a)** o pedido deveria ter sido recusado, por não constar da EAP aprovada em março;
- **b)** a EAP precisa ser refeita sempre que o cliente solicita um entregável novo;
- **c)** o pedido entrou no trabalho sem entrar no plano, e a linha de base seguiu a mesma;
- **d)** o painel de acompanhamento não deveria estar visível a todos os interessados do projeto.

↩︎ *Aula 03, seções 3 e 4 — Planejamento: escopo, EAP e cronograma; Execução e controle: a linha de base*

---

### R-04

Duas decisões foram tomadas na mesma reunião: trocar a biblioteca de gráficos do painel, e passar a guardar os dados clínicos num banco separado dos administrativos. Aplicando o teste apresentado na aula, é arquitetural:

- **a)** apenas a segunda, porque mudar de ideia sobre ela daqui a seis meses custa caro demais;
- **b)** apenas a primeira, porque envolve a escolha de uma tecnologia externa ao sistema;
- **c)** as duas, porque ambas foram tomadas formalmente numa reunião do projeto;
- **d)** nenhuma das duas, porque decisão arquitetural é só a que define a divisão em camadas.

↩︎ *Aula 04, seções 1 e 2 — Por que isto é assunto de gestão; O que é arquitetura de software*

---

### R-05

Uma equipe propôs dividir o sistema em cinco serviços independentes, justificando a escolha pela necessidade de "ser escalável". Não há número de carga esperada, a equipe tem quatro pessoas e ninguém opera o sistema fora do horário comercial. Segundo a aula, o que falta à proposta é:

- **a)** a aprovação do patrocinador, único que pode autorizar uma mudança de arquitetura;
- **b)** o número que transforma "escalável" em requisito, e times independentes que justifiquem a divisão;
- **c)** um ADR registrando as alternativas descartadas antes de a divisão ser implantada;
- **d)** a comparação com o estilo em camadas, que é o indicado para equipes pequenas.

↩︎ *Aula 04, seções 3 e 5 — Atributos de qualidade: o que decide a escolha; Monolito × microsserviços, com honestidade*

---

### R-06

Num time, alguém afirma que registrar a decisão de arquitetura contraria o Manifesto Ágil, que "valoriza software em funcionamento mais que documentação abrangente". Segundo a aula, esse argumento:

- **a)** não procede: o valor só vale quando os dois lados competem, e meia página de ADR não compete com a entrega;
- **b)** procede, porque o tempo gasto no registro é tempo que deixa de ir para a entrega;
- **c)** procede, porque o Manifesto não menciona arquitetura em nenhum dos seus doze princípios;
- **d)** não procede, porque o Manifesto exige o registro de todas as decisões técnicas do projeto.

↩︎ *Aula 05, seções 2 e 3 — Os quatro valores, um a um; O que o Manifesto não diz*

---

### R-07

Uma diretoria determinou que todos os projetos passem a ser conduzidos de forma ágil. Num deles, o escopo está fechado em contrato, o cliente comparece apenas à medição mensal e ninguém pode alterar prazo ou orçamento. O time adotou as cerimônias e o vocabulário. Segundo a aula:

- **a)** a adoção é inviável, e a equipe deve recusar formalmente a determinação da diretoria;
- **b)** a adoção está completa, porque as cerimônias são a parte executável do ágil;
- **c)** o problema é a duração das cerimônias, que precisa ser ajustada ao ritmo mensal do cliente;
- **d)** a adoção vai parar na parte visível, porque falta quem ordene o trabalho toda semana com autoridade.

↩︎ *Aula 05, seções 5 e 6 — Ágil não é ausência de processo; O ágil teatral*

---

### R-08

Numa organização, o Scrum Master define quais itens entram em cada Sprint, e o gerente de projeto decide a ordem do Product Backlog. Segundo a aula, o que está trocado é:

- **a)** nada, porque em times pequenos é comum que uma pessoa acumule responsabilidades;
- **b)** apenas a segunda, porque ordenar o Product Backlog é responsabilidade do Scrum Master;
- **c)** as duas: quem ordena o backlog é o Product Owner, e quem diz quanto cabe são os desenvolvedores;
- **d)** apenas a primeira, porque o gerente de projeto responde pelo prazo acordado com o cliente.

↩︎ *Aula 06, seção 2 — As três responsabilidades*

---

### R-09

**[ENADE]**

Um time realiza, ao fim de cada Sprint, uma única reunião de duas horas. Na primeira hora demonstra o incremento ao gestor da área e ao pessoal do balcão; na segunda, com as mesmas pessoas ainda na sala, discute o próprio modo de trabalhar.

Nas últimas quatro Sprints, a segunda hora terminou sem que ninguém apontasse nada a mudar. Dois desenvolvedores comentam em particular que a etapa de revisão de código atrasa toda entrega, mas o assunto nunca foi levantado na reunião.

Considerando a situação descrita e o conteúdo da aula, o problema é que:

- **a)** fundir os dois eventos custou a Retrospectiva: com interessados na sala, ninguém levanta o que não funciona;
- **b)** a duração de duas horas excede o tempo máximo previsto para os dois eventos somados;
- **c)** a Revisão não deveria incluir o pessoal do balcão, que não responde pelo produto entregue;
- **d)** o atraso na revisão de código é assunto da reunião diária, e não da reunião de fim de Sprint.

↩︎ *Aula 06, seção 3 — Os cinco eventos*

---

### R-10

**[ENADE]**

Um time acrescentou à sua Definição de Pronto dois itens: "revisado por outra pessoa" e "testado com os casos de exceção acordados". Nas três Sprints seguintes, o número de itens entregues por Sprint caiu de nove para seis.

A diretoria, que acompanha a velocidade do time num painel, registrou o período como queda de desempenho e pediu explicações ao Scrum Master.

Considerando a situação descrita e o conteúdo da aula, a resposta correta ao pedido é que:

- **a)** a queda é real, e o time precisa voltar ao patamar de nove itens nas próximas Sprints;
- **b)** o que subiu foi a exigência, não caiu o desempenho: a velocidade de antes e a de agora medem coisas diferentes;
- **c)** os dois itens novos pesaram demais na lista e deveriam sair dela até a entrega se recuperar;
- **d)** a velocidade deixou de servir para prever entregas, e o time deve adotar outra unidade de estimativa.

↩︎ *Aula 06, seções 4 e 6 — Os três artefatos e seus compromissos; Velocidade não é meta*

---

⬅️ [Voltar ao plano de aulas](../README.md)
