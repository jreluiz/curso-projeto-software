# Aula 13 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 13 — Princípios de Bom Projeto](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

---

### Q-A13-01

Duas soluções diferentes satisfazem os mesmos requisitos e ambas funcionam. O que as separa?

- **a)** A quantidade de código que cada uma exige;
- **b)** a aderência de cada uma aos padrões de projeto do catálogo GoF;
- **c)** o custo de mudá-las depois — um bom projeto é aquele em que uma mudança provável exige alterar poucos lugares, e onde encontrá-los é óbvio;
- **d)** o desempenho medido em produção sob carga real.

↩︎ *Aula 13, seção 1 — Onde o projeto entra*

---

### Q-A13-02

O critério de bom projeto fala em mudança provável, não em mudança possível. Por quê?

- **a)** Porque projetar para toda mudança concebível produz um sistema de abstrações vazias, caro de escrever e impossível de ler;
- **b)** porque mudanças improváveis não chegam a acontecer em sistemas bem especificados;
- **c)** porque o cliente só paga pelas mudanças que ele já previu em contrato;
- **d)** porque mudanças possíveis são tratadas na fase de manutenção, não na de projeto.

↩︎ *Aula 13, seção 1 — Onde o projeto entra*

---

### Q-A13-03

Qual é o teste que revela falta de coesão numa classe?

- **a)** Contar o número de linhas e comparar com um limite estabelecido pelo time;
- **b)** verificar se a classe tem mais métodos públicos do que privados;
- **c)** medir quantas outras classes dependem dela;
- **d)** descrever a responsabilidade dela em uma frase, sem usar "e" e sem usar "gerencia" — se não conseguir, ela tem mais de uma responsabilidade.

↩︎ *Aula 13, seção 2 — Coesão*

---

### Q-A13-04

Um time quebrou uma classe coesa de 200 linhas em trinta classes de uma linha cada. O que aconteceu com a qualidade do projeto?

- **a)** Melhorou: classes menores são sempre mais fáceis de entender e testar;
- **b)** piorou: coesão alta não quer dizer classe pequena, e a divisão aumentou o acoplamento entre os pedaços — agora é preciso abrir sete arquivos para entender qualquer coisa;
- **c)** ficou igual: a quantidade total de código não mudou;
- **d)** melhorou quanto à coesão e piorou quanto ao desempenho.

↩︎ *Aula 13, seção 2 — Coesão*

---

### Q-A13-05

O que significa buscar baixo acoplamento?

- **a)** Eliminar toda dependência entre módulos, para que cada um funcione isoladamente;
- **b)** controlar a quantidade e o tipo das dependências, preferindo depender de contratos, que mudam pouco, em vez de implementações, que mudam muito;
- **c)** reduzir ao mínimo o número de classes do sistema;
- **d)** substituir chamadas diretas por comunicação assíncrona sempre que possível.

↩︎ *Aula 13, seção 3 — Acoplamento*

---

### Q-A13-06

Qual é o critério mais útil para decidir onde separar responsabilidades?

- **a)** Separar por camada técnica: dados, lógica e apresentação;
- **b)** separar por tamanho, mantendo classes com número parecido de linhas;
- **c)** separar por ordem de construção, agrupando o que será feito na mesma iteração;
- **d)** separar o que muda por motivos diferentes — cada fonte de mudança tem seu calendário, e juntá-las obriga a reabrir e retestar tudo a cada alteração.

↩︎ *Aula 13, seção 4 — Separação de responsabilidades*

---

### Q-A13-07

Por que a formulação correta do SRP é "um motivo para mudar" e não "fazer apenas uma coisa"?

- **a)** Porque "uma coisa" é indefinível, enquanto "um motivo para mudar" você consegue apontar com o dedo;
- **b)** porque a formulação original em inglês não admite tradução literal;
- **c)** porque uma classe legitimamente faz várias coisas, desde que todas sejam pequenas;
- **d)** porque "um motivo para mudar" é mais fácil de verificar automaticamente por ferramenta.

↩︎ *Aula 13, seção 4 — Separação de responsabilidades*

---

### Q-A13-08

Você cria a interface `Notificador` quando existe — e vai existir por muito tempo — uma única implementação, que é e-mail. Como avaliar?

- **a)** É boa prática: a interface prepara o sistema para mudanças futuras sem custo relevante;
- **b)** é indiferente, porque uma indireção a mais não afeta a leitura do código;
- **c)** é dívida disfarçada de boa prática: paga-se a indireção hoje pela chance de precisar dela um dia. A regra é esperar o segundo caso concreto;
- **d)** é erro grave: interfaces só devem existir quando exigidas pelo framework.

↩︎ *Aula 13, seção 5 — Abstração e encapsulamento como decisão*

---

⬅️ [Voltar à Aula 13](../README.md) | ➡️ [Revisão da Aula 14](../../aula-14-arquitetura-de-software/revisao/README.md)
