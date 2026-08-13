---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 03'
---

<!-- _class: capa -->

<div class="emoji">⚙️</div>

# Os Processos de um Projeto

## Aula 03 · Bloco 1 — Fundamentos de Projetos

<div class="meta">Replanejar não é fracasso do plano. É o uso previsto dele.</div>

---

## 🎯 Nesta aula

1. Os **cinco grupos** de processo
2. **Iniciação** — o termo de abertura
3. **Planejamento** — escopo, EAP e cronograma
4. **Execução e controle** — a linha de base
5. **Encerramento** — aceite, arquivo, lições aprendidas

---

## Os cinco grupos de processo

```
   ┌───────────┐   ┌──────────────┐   ┌──────────┐
   │ Iniciação │──▶│ Planejamento │──▶│ Execução │
   └───────────┘   └──────┬───────┘   └────┬─────┘
                          ▲                │
                          │                ▼
                          │      ┌──────────────────┐   ┌──────────────┐
                          └──────│ Monit. e controle│──▶│ Encerramento │
                                 └──────────────────┘   └──────────────┘
```

**Não são fases** — acontecem em paralelo e se repetem a cada ciclo.

---

<!-- _class: lead -->

## O laço de volta é o que importa

Replanejar não é fracasso do plano:
é **o uso previsto dele**.

Adaptativo passa por ali
a cada duas semanas.
Preditivo, a cada marco.

---

<!-- _class: tabela-densa -->

## Iniciação: o termo de abertura

| | |
|---|---|
| **Problema** | controle em planilha; penalidade não aplicada |
| **Resultado esperado** | empréstimo, devolução e reserva registrados |
| **Fora do escopo** | compra de equipamento, integração com patrimônio |
| **Prazo** | em uso no início do período letivo — data de calendário |
| **Premissas** | verba aprovada; equipe de 4 em tempo parcial |
| **Restrições** | verba expira no fim do exercício |

---

## Duas linhas que salvam projeto

**Fora do escopo.** Escrever o que **não** será feito é mais útil que escrever o que será — é ali que nasce o pedido de outubro.

**Premissas.** Algo que se assume verdadeiro **sem ter certeza**. Se cai, o plano cai junto.

> 💡 "Equipe de 4 em tempo parcial" é exatamente o tipo de coisa que muda em agosto sem ninguém avisar o projeto.

---

## Planejamento: a EAP

```
                    ┌──────────────────────┐
                    │ Sistema de empréstimo│
                    └──────────┬───────────┘
          ┌────────────┬────────┴────────┬─────────────┐
    ┌─────▼─────┐ ┌────▼─────┐    ┌──────▼──────┐ ┌────▼──────┐
    │ Cadastro  │ │Empréstimo│    │   Reserva   │ │Implantação│
    └───────────┘ └────┬─────┘    └─────────────┘ └────┬──────┘
                  ┌────┴────┐                     ┌────┴─────┐
              Saída  Retorno  Penalidade      Migração  Treinamento
```

**A soma das partes é o todo.** O que não está na EAP não está no projeto.

---

<!-- _class: lead -->

## ⚠️ EAP que virou ciclo de vida

Se o segundo nível for
*levantamento, desenho, construção, testes*,

você desenhou o **processo**,
não o produto —

e perdeu a única pergunta
que a EAP responde bem.

---

## O cronograma vem da EAP

| Folha da EAP | Duração | Depende de | Responsável |
|---|:---:|---|---|
| Cadastro de itens | 3 sem | — | dupla A |
| Registro de saída | 2 sem | cadastro | dupla A |
| Registro de retorno | 2 sem | registro de saída | dupla B |
| Penalidade por atraso | 1 sem | registro de retorno | dupla B |
| Treinamento do balcão | 1 sem | tudo acima | gerente |

A coluna **depende de** é o que transforma lista em cronograma.

---

## Controle: a linha de base

| Entrega | Linha de base | Real | Desvio |
|---|---|---|---|
| Cadastro de itens | 15/03 | 14/03 | −1 dia |
| Empréstimo e devolução | 30/04 | 12/05 | **+12 dias** |
| Reserva | 31/05 | — | em andamento |
| Implantação | 30/06 | — | previsto 12/07 |

Metade da tabela olha para trás; **a outra metade para a frente** — e é ela que permite decidir.

---

## O desvio dispara decisão, não relatório

| Decisão | O que custa | Quando faz sentido |
|---|---|---|
| **Recuperar o prazo** | horas extras, qualidade | a causa já passou |
| **Cortar escopo** | funcionalidade esperada | há escopo cortável |
| **Mover a data** | credibilidade, contrato | a data não é imóvel |

**Nenhuma delas é "seguir tentando"** — que é o que acontece quando ninguém decide.

---

## Encerramento: três partes

**Aceite formal** — alguém com autoridade declara que atende. Sem isso o projeto não termina: apenas para.

**Arquivo** — o que se produziu fica onde a próxima pessoa encontra.

**Lições aprendidas** — é o único dos três que serve a **outro** projeto.

---

<!-- _class: lead -->

## ⚠️ O custo de não encerrar

não aparece neste projeto.

Aparece no próximo —
e por isso ninguém o atribui
à decisão que o causou.

---

## Lição aprendida não é lista de culpados

O registro útil descreve **situação** e **decisão**:

> *"A integração com o legado foi deixada para o último mês, e o único conhecedor do sistema saiu de férias."*

Um registro que acusa pessoas garante que o próximo projeto não escreva nenhum.

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-03/`:

1. **`ex01.md`** — oito atividades nos cinco grupos de processo;
2. **`ex02.md`** — termo de abertura da rede de doação, com premissas;
3. **`ex03.md`** — EAP em Mermaid, com um entregável que não é software;
4. **`ex04.md`** — as três decisões possíveis diante de +12 dias;
5. **`ex05.md`** 🌶️ — encerrar com um aceite recusado, e sem culpar ninguém.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 04 — Arquitetura como decisão de projeto**

A decisão mais cara de reverter
não é técnica por acaso:
ela consome orçamento
e exige disponibilidade da operação.
