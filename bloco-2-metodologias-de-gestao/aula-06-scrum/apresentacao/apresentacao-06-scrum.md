---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 06'
---

<!-- _class: capa -->

<div class="emoji">🔄</div>

# Scrum

## Aula 06 · Bloco 2 — Metodologias de Gestão

<div class="meta">Ele torna os problemas visíveis sem resolvê-los</div>

---

## 🎯 Nesta aula

1. O que o Scrum **é**, e o que ele não é
2. As três **responsabilidades**
3. Os cinco **eventos**
4. Os três **artefatos** e seus compromissos
5. A **Sprint** em uma tela
6. **Velocidade não é meta**

---

## Três responsabilidades, cinco eventos, três artefatos

E para de definir. Não diz como estimar, testar, escrever requisito nem organizar código.

| O Scrum define | O Scrum **não** define |
|---|---|
| quem responde por quê | como estimar |
| quando o time se reúne, e para quê | como escrever requisito |
| o que existe de artefato | como testar ou implantar |
| que a Sprint tem tamanho fixo | qual é o tamanho |

---

<!-- _class: lead -->

## Ele torna os problemas visíveis

sem resolvê-los.

Se a equipe não termina nada
em duas semanas, a primeira revisão
expõe isso.

O arcabouço não conserta —
impede que fique escondido
por seis meses.

---

## As três responsabilidades

| | Responde por | Decide |
|---|---|---|
| **Product Owner** | o **valor** do produto | o que se faz e em que ordem |
| **Scrum Master** | a **eficácia** do processo | como o time trabalha |
| **Desenvolvedores** | a **entrega** do incremento | como se faz e quanto cabe |

**PO decide o quê. Time decide o como. Ninguém decide os dois.**

---

## Três fronteiras que se atravessa por engano

**O PO não decide como.** Ele diz que o balcão precisa registrar devolução; não diz em que tela.

**O Scrum Master não decide o quê.** Quando ele decide escopo, o PO vira decorativo.

**Os desenvolvedores decidem quanto cabe.** Sprint com escopo imposto deixa de ser compromisso e vira meta.

---

<!-- _class: lead -->

## ⚠️ Responsabilidade não é pessoa

Num time de quatro, uma pessoa
acumula Scrum Master e desenvolvedora.

O que não pode é acumular
**Product Owner e Scrum Master**:

um puxa por escopo, o outro protege
o processo — e a mesma pessoa
sempre cede para quem pressiona mais.

---

## Os cinco eventos

```
   ┌──────────┐   ┌──────────────┐   ┌──────────────────────┐
   │ Product  │──▶│ Planejamento │──▶│  SPRINT (1 a 4 sem)  │
   │ Backlog  │   │  da Sprint   │   │   ┌──────────────┐   │
   └──────────┘   └──────────────┘   │   │ Daily 15 min │   │
        ▲                            │   └──────────────┘   │
        │                            └──────────┬───────────┘
        │         ┌──────────────┐   ┌──────────▼───────────┐
        └─────────│Retrospectiva │◀──│ Revisão c/ interess. │
                  │   do time    │   └──────────────────────┘
                  └──────────────┘
```

---

## Duas distinções que decidem tudo

**Revisão ≠ Retrospectiva.** A primeira olha o **produto** e é aberta; a segunda olha o **processo do time** e é do time. Fundir as duas custa sempre a segunda.

**A Daily é do time, não para o chefe.** O teste: numa Daily de verdade, **o plano do dia muda** por causa do que alguém disse.

---

## Os três artefatos e seus compromissos

| Artefato | Compromisso |
|---|---|
| **Product Backlog** | **Meta do Produto** — o objetivo de longo prazo |
| **Sprint Backlog** | **Meta da Sprint** — o porquê deste ciclo |
| **Incremento** | **Definição de Pronto** — o que "terminado" significa |

O compromisso é a parte que torna o artefato **verificável** em vez de decorativo.

---

## A Definição de Pronto

- [ ] revisado por outra pessoa;
- [ ] testado com os três casos de exceção acordados;
- [ ] texto de tela revisado por quem atende na portaria;
- [ ] publicado no ambiente de homologação.

**Todos podem ser respondidos com sim ou não** por alguém que não escreveu o código. *"Código de qualidade"* não passa nesse teste.

---

<!-- _class: lead -->

## A Definição de Pronto muda a velocidade

Um time que acrescenta
"revisado por outra pessoa"
vai entregar **menos** itens.

Isso não é piora: é o mesmo trabalho
medido com régua mais honesta.

Quem não sabe disso lê a queda
como queda de desempenho.

---

## A Sprint em uma tela

| Momento | O que acontece |
|---|---|
| Segunda, dia 1 | **Planejamento**: meta definida, time puxa 6 itens |
| Todo dia, 15 min | **Daily**: o time replaneja as 24 h seguintes |
| Sexta, dia 10 | **Revisão**: a portaria diz que falta buscar por data |
| Sexta, dia 10 | **Retrospectiva**: dois itens ficaram parados na revisão |
| Segunda, dia 11 | nova Sprint, **com o ajuste já em vigor** |

---

## Velocidade não é meta

| Legítimo | Indevido |
|---|---|
| prever quanto cabe na próxima Sprint | comparar dois times |
| perceber que o time desacelerou | compor avaliação individual |
| dimensionar expectativa com o cliente | fixar como meta a ser batida |

Como meta, ela é **trivialmente inflacionável**: basta estimar mais alto.

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-06/`:

1. **`ex01.md`** — oito decisões para as três responsabilidades;
2. **`ex02.md`** — cronograma de uma Sprint de duas semanas;
3. **`ex03.md`** — Definição de Pronto com cinco itens verificáveis;
4. **`ex04.md`** — diagnosticar quatro Sprints com defeito;
5. **`ex05.md`** 🌶️ — a diretoria quer comparar a velocidade de três times.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 07 — Quem responde pelo quê**

O Scrum nomeia os donos de fábrica.

Falta o papel que ele não descreve —
e que continua existindo:
contrato, prazo, risco e diretoria.
