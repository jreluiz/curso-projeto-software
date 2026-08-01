# Aula 16 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 16 — Qualidade, Evolução e Próximos Passos](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

---

### Q-A16-01

Os 240 testes passam e a secretaria diz que o sistema não serve. Como as duas coisas podem ser verdade?

- **a)** Porque são perguntas diferentes: a verificação confere o sistema contra a especificação, e a validação confere a especificação contra a necessidade real;
- **b)** porque os testes cobrem apenas o caminho principal, e a secretaria usou caminhos de exceção;
- **c)** porque a secretaria ainda não recebeu treinamento para usar o sistema;
- **d)** porque a cobertura de testes estava abaixo do mínimo aceitável.

↩︎ *Aula 16, seção 1 — Verificação × validação*

---

### Q-A16-02

O que caracteriza a pirâmide de testes invertida, e por que ela é um antipadrão?

- **a)** Muitos testes de unidade e poucos de aceite, o que deixa lacunas no comportamento observável;
- **b)** poucos testes de unidade e muitos de ponta a ponta: a bateria demora uma hora, falha por motivos aleatórios, e o time começa a ignorar a falha;
- **c)** testes de integração em maior número que os demais, o que dilui a responsabilidade;
- **d)** ausência de testes de regressão, o que permite que defeitos antigos voltem.

↩︎ *Aula 16, seção 2 — A pirâmide de testes*

---

### Q-A16-03

Por que cobertura é bom indicador e péssima meta?

- **a)** Porque a medição consome tempo de execução da esteira;
- **b)** porque ferramentas diferentes calculam cobertura de maneiras incompatíveis;
- **c)** porque 100% garante que todas as linhas foram executadas, não que alguém verificou o resultado — dá para ter cobertura total com testes que não afirmam nada;
- **d)** porque cobertura alta indica código excessivamente fragmentado.

↩︎ *Aula 16, seção 2 — A pirâmide de testes*

---

### Q-A16-04

Qual é a pergunta mais produtiva numa revisão de código?

- **a)** "Isto segue o padrão de nomenclatura do time?";
- **b)** "Você conseguiria explicar este trecho para alguém que chega amanhã?";
- **c)** "Quantas linhas essa mudança acrescentou ao total?";
- **d)** "Como você testaria isso?" — a mesma da Aula 05, e ela quase sempre revela um caso que ninguém tinha considerado.

↩︎ *Aula 16, seção 3 — Revisão de código*

---

### Q-A16-05

A regra de prioridade está duplicada em três lugares porque ninguém teve tempo de unificar. Isso é dívida técnica?

- **a)** Sim, porque foi uma escolha consciente de entregar mais rápido;
- **b)** sim, desde que a equipe registre a pendência numa lista;
- **c)** não é possível classificar sem saber o prazo do projeto;
- **d)** não: é defeito de qualidade — não houve decisão, ninguém aprovou sabendo do custo, e nada foi registrado. Chamar toda gambiarra de dívida técnica é elogiar o descuido.

↩︎ *Aula 16, seção 4 — Refatoração e dívida técnica*

---

### Q-A16-06

Por que refatorar depende de teste automatizado?

- **a)** Porque as ferramentas de refatoração exigem uma suíte de testes para funcionar;
- **b)** porque a refatoração costuma quebrar a compilação em algum momento do processo;
- **c)** porque sem ele "não mudei o comportamento externo" é uma esperança, não uma afirmação;
- **d)** porque o teste automatizado mede se a estrutura interna ficou melhor.

↩︎ *Aula 16, seção 4 — Refatoração e dívida técnica*

---

### Q-A16-07

Qual tipo de manutenção costuma ser a maior fatia, e o que isso justifica?

- **a)** A corretiva, o que justifica investir em testes automatizados;
- **b)** a evolutiva — e é por isso que manutenibilidade foi um dos atributos de qualidade lá na Aula 01: o sistema vai ser mudado muito mais vezes do que foi escrito;
- **c)** a adaptativa, o que justifica isolar dependências externas atrás de fachadas;
- **d)** as três em proporções semelhantes, o que justifica tratá-las com o mesmo processo.

↩︎ *Aula 16, seção 5 — Manutenção e evolução*

---

### Q-A16-08

Qual é o risco específico que ferramentas de IA introduzem no ciclo de desenvolvimento?

- **a)** O resultado é plausível: código gerado compila e parece razoável, e um documento gerado tem a estrutura certa — e plausível é o tipo de erro que engenharia de software mais sofre, porque nada aponta o defeito;
- **b)** o resultado costuma conter erros de sintaxe difíceis de localizar;
- **c)** o resultado é lento de produzir, o que atrasa as entregas;
- **d)** o resultado varia entre execuções, o que impede reprodutibilidade.

↩︎ *Aula 16, seção 7 — IA no ciclo de desenvolvimento*

---

⬅️ [Voltar à Aula 16](../README.md) | 🏠 [Voltar ao plano de aulas](../../../README.md)
