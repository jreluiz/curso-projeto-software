# Aula 04 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 04 — Como o Software Chega ao Usuário](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

---

### Q-A04-01

Uma pessoa fica três semanas num branch "para não quebrar nada" e enfrenta 40 conflitos ao integrar. Como se explica isso?

- **a)** É uma consequência aritmética: quanto mais tempo dois trabalhos ficam separados, mais eles divergem — não tem a ver com habilidade;
- **b)** é falta de domínio do Git por parte de quem criou o branch;
- **c)** é sinal de que a funcionalidade era grande demais para uma pessoa só;
- **d)** é um problema da ferramenta de controle de versão, resolvido trocando de estratégia de merge.

↩︎ *Aula 04, seção 1 — Versionar é decisão de engenharia*

---

### Q-A04-02

Uma equipe tem servidor de CI instalado, mas ninguém integra há duas semanas. Ela pratica integração contínua?

- **a)** Sim, porque a ferramenta está configurada e roda os testes;
- **b)** não: CI é um hábito do time sustentado por automação — ali há apenas uma ferramenta ligada;
- **c)** sim, desde que os testes automatizados estejam passando;
- **d)** a pergunta não se aplica: CI é uma característica da ferramenta, não do time.

↩︎ *Aula 04, seção 2 — Integração contínua*

---

### Q-A04-03

Por que as etapas baratas vêm primeiro na esteira?

- **a)** Porque a ordem é imposta pelas ferramentas de automação;
- **b)** porque os testes de aceite dependem do ambiente de produção estar disponível;
- **c)** porque falhar cedo é falhar barato — compilação em segundos, unidade em minutos, aceite em dezenas de minutos;
- **d)** porque os testes de unidade encontram mais defeitos que os demais.

↩︎ *Aula 04, seção 3 — Ambientes e a esteira*

---

### Q-A04-04

Qual é a diferença entre **entrega** contínua e **implantação** contínua?

- **a)** Entrega é o termo em português e implantação é a tradução de *deployment*: significam o mesmo;
- **b)** entrega trata de código e implantação trata de infraestrutura;
- **c)** entrega é automática e implantação exige aprovação humana;
- **d)** na entrega contínua o sistema está sempre pronto para subir e uma pessoa decide quando; na implantação contínua tudo que passa nos testes vai à produção automaticamente.

↩︎ *Aula 04, seção 4 — Entrega contínua × implantação contínua*

---

### Q-A04-05

O sistema-guia tem entrega contínua funcionando. Por que ainda assim não se implanta na semana de provas?

- **a)** Porque a esteira fica mais lenta em períodos de pico;
- **b)** porque a entrega contínua não permite implantar em qualquer dia;
- **c)** porque a equipe de TI está em férias nesse período;
- **d)** porque a capacidade técnica é contínua, mas a decisão de subir continua humana e contextual — e o calendário diz que ali o uso multiplica.

↩︎ *Aula 04, seção 4 — Entrega contínua × implantação contínua*

---

### Q-A04-06

Dos cinco itens que caracterizam DevOps, quantos são sobre ferramenta — e o que isso revela?

- **a)** Todos os cinco: DevOps é essencialmente automação;
- **b)** três dos cinco, o que mostra equilíbrio entre cultura e tecnologia;
- **c)** apenas um, o que mostra que DevOps é majoritariamente sobre quem responde pelo quê — uma decisão organizacional com consequências de arquitetura;
- **d)** nenhum: DevOps é exclusivamente uma mudança cultural.

↩︎ *Aula 04, seção 5 — DevOps em uma tela*

---

### Q-A04-07

Qual é o resultado contraintuitivo da pesquisa DORA?

- **a)** Que a frequência de implantação é a métrica mais importante das quatro;
- **b)** que velocidade e estabilidade não são opostos — quem implanta com mais frequência falha menos e se recupera mais rápido, porque implanta mudanças pequenas;
- **c)** que times pequenos sempre superam times grandes nas quatro métricas;
- **d)** que o tempo para restaurar é irrelevante quando a taxa de falha é baixa.

↩︎ *Aula 04, seção 6 — As quatro métricas DORA*

---

### Q-A04-08

O que uma **chave de funcionalidade** permite, e qual é o seu custo?

- **a)** Permite separar implantar de liberar, mandando código incompleto à produção desligado — e cobra complexidade: cada chave é um caminho a mais, e duas chaves geram quatro combinações para testar;
- **b)** permite reverter uma implantação sem perda de dados, e não tem custo relevante;
- **c)** permite que o código incompleto não seja compilado, reduzindo o tempo da esteira;
- **d)** permite liberar para todos os usuários ao mesmo tempo, ao custo de mais uma implantação.

↩︎ *Aula 04, seção 7 — Chave de funcionalidade*

---

⬅️ [Voltar à Aula 04](../README.md) | ➡️ [Revisão da Aula 05](../../../bloco-2-requisitos/aula-05-o-que-e-um-requisito/revisao/README.md)
