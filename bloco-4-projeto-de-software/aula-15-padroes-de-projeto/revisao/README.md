# Aula 15 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 15 — Padrões de Projeto](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

---

### Q-A15-01

Quais são as quatro partes que descrevem um padrão de projeto?

- **a)** Nome, autor, ano de publicação e família;
- **b)** Problema, solução, exemplo de código e diagrama;
- **c)** Contexto, problema, solução e alternativas descartadas;
- **d)** Contexto, problema, solução e consequências — e as quatro importam, porque todo padrão cobra algo.

↩︎ *Aula 15, seção 1 — O que é um padrão*

---

### Q-A15-02

Quando não se deve aplicar um padrão?

- **a)** Quando o projeto é pequeno demais para justificar o esforço de documentação;
- **b)** Quando o time ainda não estudou o catálogo GoF completo;
- **c)** quando não se consegue enunciar o problema em uma frase, nem as consequências — padrão sem problema é só complexidade com nome bonito;
- **d)** quando a linguagem escolhida não oferece suporte nativo àquele padrão.

↩︎ *Aula 15, seção 1 — O que é um padrão*

---

### Q-A15-03

Qual é o sinal de que você precisa de Strategy?

- **a)** Uma classe com mais de dez métodos públicos;
- **b)** um condicional sobre um "tipo" que se repete em mais de um lugar do código — cada variação nova exige alterações coordenadas, e uma delas vai ser esquecida;
- **c)** duas classes que herdam da mesma superclasse;
- **d)** um método muito longo, que precisa ser quebrado em partes menores.

↩︎ *Aula 15, seção 2 — Strategy*

---

### Q-A15-04

O que se paga ao adotar Strategy?

- **a)** Mais classes, e a lógica que antes se lia num lugar só agora está espalhada — quem depura precisa saber qual estratégia foi escolhida;
- **b)** o sistema fica acoplado à interface comum, o que dificulta mudanças futuras;
- **c)** o desempenho cai por causa da chamada polimórfica;
- **d)** perde-se a possibilidade de testar cada variação isoladamente.

↩︎ *Aula 15, seção 2 — Strategy*

---

### Q-A15-05

O envio de e-mail, que é um observador, falha durante uma interdição. A interdição deve falhar junto?

- **a)** Quase sempre não — mas isso é uma decisão, e precisa estar escrita: padrão não dispensa pensar no caminho de exceção;
- **b)** sim, sempre: se um observador falha, a operação não pode ser considerada concluída;
- **c)** não, e nunca é preciso decidir isso, porque observadores são independentes por definição;
- **d)** depende da ordem de registro dos observadores, que o padrão garante.

↩︎ *Aula 15, seção 3 — Observer*

---

### Q-A15-06

Por que Facade é a melhor forma de isolar um sistema legado?

- **a)** Porque ela permite substituir o legado sem que ninguém perceba a troca;
- **b)** porque todo o conhecimento sobre as esquisitices do legado fica em um lugar — no dia em que ele for substituído, muda uma classe;
- **c)** porque ela converte automaticamente os formatos de dados do legado;
- **d)** porque ela adiciona uma camada de cache que reduz a dependência do legado.

↩︎ *Aula 15, seção 4 — Facade*

---

### Q-A15-07

O Singleton entrega duas coisas. Qual delas estraga, e por quê?

- **a)** A instância única, porque impede paralelismo;
- **b)** o construtor privado, porque dificulta a criação de subclasses;
- **c)** o acesso global: ele esconde dependências, impede substituir o objeto em teste e acopla o sistema inteiro a um ponto só — e não era o requisito;
- **d)** o método estático, porque não pode ser sobrescrito.

↩︎ *Aula 15, seção 5 — Singleton, e por que ele é polêmico*

---

### Q-A15-08

Você adotou Strategy mas quem usa a estratégia continua com um `switch` para escolher qual instanciar. O que faltou?

- **a)** Faltou tornar a interface do Strategy mais genérica;
- **b)** faltou aplicar Observer, para que as estratégias se registrem sozinhas;
- **c)** nada faltou: o `switch` de escolha é parte inevitável do Strategy;
- **d)** faltou a fábrica: o Strategy define as variações, e a fábrica decide qual usar — sem ela, o `switch` que o Strategy veio eliminar apenas mudou de lugar.

↩︎ *Aula 15, seção 6 — Factory Method*

---

⬅️ [Voltar à Aula 15](../README.md) | ➡️ [Revisão da Aula 16](../../aula-16-qualidade-evolucao-proximos-passos/revisao/README.md)
