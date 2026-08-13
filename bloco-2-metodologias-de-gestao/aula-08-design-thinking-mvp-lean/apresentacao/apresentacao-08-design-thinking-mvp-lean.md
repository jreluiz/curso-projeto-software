---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 08'
---

<!-- _class: capa -->

<div class="emoji">🔍</div>

# Descobrir, Enxugar, Melhorar

## Aula 08 · Bloco 2 — Metodologias de Gestão

<div class="meta">Três nomes, três perguntas — e usar o errado é caro</div>

---

## 🎯 Nesta aula

1. Três respostas para **três perguntas diferentes**
2. **Design Thinking** — as cinco etapas
3. **MVP** — o menor produto que ensina algo
4. O que MVP **não é**
5. **Lean** — valor, fluxo e desperdício
6. Qual usar **quando**

---

## Cada um responde a uma pergunta

| Abordagem | A pergunta |
|---|---|
| **Design Thinking** | *não sabemos qual é o problema certo* |
| **MVP** | *não sabemos se alguém quer isto* |
| **Lean / Six Sigma** | *sabemos o que fazer, e fazemos mal* |

**Marketplace** → a segunda. **Ouvidoria** → a terceira.

---

<!-- _class: lead -->

## ⚠️ O erro mais caro

é usar Lean
onde a pergunta era MVP.

Otimizar a construção de algo
que ninguém quer produz desperdício
com excelente indicador de eficiência.

---

## Design Thinking: as cinco etapas

```
   Empatia ─▶ Definição ─▶ Ideação ─▶ Prototipação ─▶ Teste
                  ▲            ▲                        │
                  │            └──── a ideia não serve ─┤
                  └──────────── o problema era outro ───┘
```

O teste manda de volta para a definição — **e é isso que o torna útil**.

---

## O pedido não é o problema

**Pedido:** *"queremos um sistema para cadastrar itens perdidos"*.

**Uma manhã observando a portaria:** o item quase sempre está lá. Quem procura **não sabe descrever** o que perdeu de um jeito que case com quem achou.

O problema é **pareamento sob descrição ambígua** — e são dois projetos diferentes.

---

<!-- _class: lead -->

## ⚠️ Design Thinking não é

dinâmica de post-it.

Se depois da oficina
ninguém mudou de ideia sobre nada,

ou o problema já estava claro,
ou a etapa de **empatia**
não foi feita para valer.

---

## MVP: as três partes obrigatórias

| Parte | No marketplace |
|---|---|
| **Hipótese** | prestadores pagam comissão para encontrar clientes |
| **Como medir** | 30 cadastrados e 10 serviços concluídos em 8 semanas |
| **Critério de decisão** | menos de 5 concluídos → mudamos de direção |

**A terceira quase nunca existe.** Sem ela, não é MVP.

---

<!-- _class: lead -->

## Se você não consegue completar

*"se acontecer X,
a gente muda de direção"*,

**não é MVP** —
é a entrega 1 de 8,
com nome bonito.

---

## O que MVP não é

| Chamam de MVP | É na verdade |
|---|---|
| a primeira fatia do plano | **entrega incremental** — legítima, e não testa nada |
| a versão com menos funcionalidades | **escopo reduzido** |
| o protótipo de tela | **protótipo** — ninguém usa de verdade |
| a versão feita às pressas | **dívida técnica** |

**Incremental supõe o plano certo. O MVP suspeita do plano.**

---

## Lean: os desperdícios em software

| Desperdício | Como aparece |
|---|---|
| **Trabalho parcialmente feito** | cinco itens começados, nenhum entregue |
| **Espera** | item pronto há seis dias esperando revisão |
| **Retrabalho** | o que volta por não estar na Definição de Pronto |
| **Troca de contexto** | a pessoa em três projetos ao mesmo tempo |
| **Funcionalidade não usada** | o relatório que ninguém abre |

---

## O fluxo que revela a espera

```
   ┌──────────┐   ┌────────┐   ┌─────────┐   ┌────────┐   ┌───────────┐
   │ Análise  │──▶│ espera │──▶│ Revisão │──▶│ espera │──▶│ Publicação│
   │  2 dias  │   │ 4 dias │   │  1 dia  │   │ 3 dias │   │   1 dia   │
   └──────────┘   └────────┘   └─────────┘   └────────┘   └───────────┘

        4 dias de TRABALHO          7 dias de ESPERA
```

Contratar mais gente para as etapas de trabalho **quase não muda nada**.

---

## Lean × Six Sigma

| | Lean | Six Sigma |
|---|---|---|
| **Ataca** | desperdício | variação |
| **Pergunta** | o que aqui não vira valor? | por que o resultado oscila? |
| **Exige** | ver o fluxo inteiro | dados suficientes para medir |

**Six Sigma exige processo estável e repetido** — cabe na operação, não no projeto único.

---

## Qual usar quando

1. **Sabemos qual é o problema?** Se não → Design Thinking;
2. **Sabemos se alguém quer a solução?** Se não → MVP;
3. **Sabemos as duas e entregamos mal?** → Lean.

> ⚠️ As três podem ser usadas para **adiar decisão**. O teste: que decisão vai mudar com o resultado? Se ninguém nomeia uma, é ritual.

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-08/`:

1. **`ex01.md`** — quatro situações, qual abordagem e por qual pergunta;
2. **`ex02.md`** — cinco etapas do Design Thinking em achados e perdidos;
3. **`ex03.md`** — MVP do marketplace, com número e prazo no critério;
4. **`ex04.md`** — três desperdícios num fluxo, com a mudança de cada;
5. **`ex05.md`** 🌶️ — a oficina de dois dias determinada para a Ouvidoria.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 09 — Risco**

Fecha o Bloco 2.

O Bloco 3 abre com o que
o projeto ainda não sabe —
e pode custar caro.
