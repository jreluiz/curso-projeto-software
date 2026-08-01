# Aula 14 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 14 — Arquitetura de Software](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

---

### Q-A14-01

Qual é o teste que separa decisão arquitetural de decisão de projeto detalhado?

- **a)** Se a decisão envolve mais de um módulo, é arquitetural;
- **b)** quanto custaria mudar isto daqui a seis meses? Caro e espalhado é arquitetura; barato e local é projeto detalhado;
- **c)** se a decisão precisa de aprovação da liderança técnica, é arquitetural;
- **d)** se a decisão aparece no diagrama de classes, é projeto detalhado.

↩︎ *Aula 14, seção 1 — As decisões difíceis de mudar*

---

### Q-A14-02

*"Nossa arquitetura é React com Spring Boot e PostgreSQL."* Qual é o problema dessa frase?

- **a)** Que ela mistura tecnologias de camadas diferentes;
- **b)** que ela não menciona a versão de cada tecnologia;
- **c)** que ela expõe decisões internas que deveriam ficar restritas ao time;
- **d)** que é uma lista de tecnologias, não uma arquitetura: não diz quais são as partes, como conversam, onde ficam os dados nem o que acontece quando algo cai.

↩︎ *Aula 14, seção 1 — As decisões difíceis de mudar*

---

### Q-A14-03

Numa arquitetura em camadas, quem define o contrato de "notificar", e quem o implementa?

- **a)** O domínio define o contrato e a infraestrutura o implementa — se a dependência apontar ao contrário, o domínio passa a saber que existe e-mail;
- **b)** a infraestrutura define e implementa, porque conhece os detalhes do envio;
- **c)** a camada de aplicação define, porque orquestra os casos de uso;
- **d)** a apresentação define, porque é quem exibe o resultado ao usuário.

↩︎ *Aula 14, seção 2 — Camadas*

---

### Q-A14-04

Qual é a diferença entre *layer* e *tier*?

- **a)** *Layer* é o termo usado em sistemas web e *tier* em sistemas desktop;
- **b)** *Layer* trata de dados e *tier* trata de processamento;
- **c)** *layer* é divisão lógica no código; *tier* é divisão de execução em máquinas — um sistema com quatro *layers* pode rodar inteiro num único *tier*;
- **d)** são sinônimos, e a distinção existe apenas na literatura mais antiga.

↩︎ *Aula 14, seção 2 — Camadas*

---

### Q-A14-05

Qual é o valor prático do MVC, resumido em uma regra?

- **a)** Que cada uma das três partes deve ter o mesmo tamanho de código;
- **b)** que o controlador centraliza todas as decisões do sistema;
- **c)** que a visão não contém regra de negócio — senão o mesmo cálculo é repetido no aplicativo, no relatório e na rotina automática, e as três versões divergem em seis meses;
- **d)** que o modelo deve ser independente do banco de dados escolhido.

↩︎ *Aula 14, seção 3 — Cliente-servidor e MVC*

---

### Q-A14-06

Qual problema os microsserviços resolvem, de fato?

- **a)** O problema técnico de desempenho sob alta carga;
- **b)** o problema organizacional de muitos times pisando no pé uns dos outros ao implantar um sistema só — se você não tem esse problema, está comprando o remédio sem a doença;
- **c)** o problema de manter o código organizado à medida que o sistema cresce;
- **d)** o problema de isolar falhas para que uma parte não derrube as outras.

↩︎ *Aula 14, seção 4 — Monolito × microsserviços*

---

### Q-A14-07

Um monolito mal modularizado é migrado para microsserviços. O que se obtém?

- **a)** Um sistema mais escalável, ainda que mais caro de operar;
- **b)** os mesmos defeitos anteriores, agora contidos em fronteiras explícitas;
- **c)** um ganho de organização, porque a separação física força a separação lógica;
- **d)** vários monólitos mal modularizados conversando por rede — com todos os defeitos anteriores mais os novos.

↩︎ *Aula 14, seção 4 — Monolito × microsserviços*

---

### Q-A14-08

O que torna um ADR realmente útil, e por que ele é imutável?

- **a)** A tabela de alternativas descartadas com o motivo — é ela que permite a quem vem depois saber se o motivo ainda vale; e editar o ADR antigo apagaria o que se pensava na época;
- **b)** o registro da data e dos responsáveis, que serve de comprovação em auditoria;
- **c)** a descrição técnica detalhada da solução adotada, que orienta a implementação;
- **d)** a lista de consequências positivas, que justifica a decisão perante o negócio.

↩︎ *Aula 14, seção 7 — ADR: registrar a decisão*

---

⬅️ [Voltar à Aula 14](../README.md) | ➡️ [Revisão da Aula 15](../../aula-15-padroes-de-projeto/revisao/README.md)
