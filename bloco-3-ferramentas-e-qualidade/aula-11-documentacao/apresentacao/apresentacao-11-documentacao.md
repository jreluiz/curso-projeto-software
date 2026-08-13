---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 11'
---

<!-- _class: capa -->

<div class="emoji">📄</div>

# Documentação

## Aula 11 · Bloco 3 — Ferramentas e Qualidade

<div class="meta">Quem lê, e para decidir o quê?</div>

---

## 🎯 Nesta aula

1. O documento que **ninguém leu**
2. Por que documentar — **as três razões**
3. **Quando** documentar, e quanto
4. Documentação como **elemento de qualidade**
5. O que a **ausência** custa
6. Documento que se **mantém sozinho**

---

## Sessenta páginas que ninguém abriu

O projeto entregou visão, escopo, arquitetura, dicionário de dados, plano de testes e manual.

**Oito meses depois**, a auditoria pediu evidência sobre controle de acesso. A resposta estava na **página 41**, e ninguém sabia.

Duas semanas antes, uma decisão sobre onde guardar o prontuário foi refeita em duas horas — a **página 12** não foi encontrada.

---

<!-- _class: lead -->

## As duas posições habituais, desmentidas

**Não foi falta de documentação** —
ela existia, com sessenta páginas.

**E não foi excesso** — se estivesse
organizada por pergunta,
as sessenta teriam servido.

---

## As três razões que se sustentam

| Razão | Leitor |
|---|---|
| **Decidir depois** | quem chega ao projeto no ano que vem |
| **Operar** | quem usa ou sustenta o sistema |
| **Provar** | quem audita, contrata ou fiscaliza |

**Três pessoas com pressas diferentes.** Escrever para os três de uma vez é escrever para nenhum.

---

## Cada razão pede um formato

| Razão | Formato | O que a inutiliza |
|---|---|---|
| decidir depois | meia página por decisão | virar relatório longo |
| operar | procedimento numerado | virar texto corrido |
| provar | registro com data e autor | ser reconstituído depois |

O manual de sessenta páginas fracassou exatamente aqui: **um formato só para três necessidades incompatíveis**.

---

## Quando documentar: três critérios

**Quanto custa redescobrir.** Uma decisão de arquitetura custa duas horas de reunião — e pode ser refeita **errado**. O motivo de um nome de variável está no código.

**Quantas pessoas vão passar por aqui.** Documentação é comunicação com quem ainda não chegou.

**Se alguém vai cobrar.** Auditoria, contrato e norma criam obrigação.

---

## O que documentar, e o que não

| Situação | Documentar |
|---|---|
| decisão cara de reverter | **sim**, meia página, na hora |
| regra de negócio sem origem conhecida | **sim**, junto da regra |
| procedimento que a auditoria vai pedir | **sim**, com registro de execução |
| como o código funciona internamente | quase nunca — o código é a fonte |
| o que está óbvio na tela | não |

---

<!-- _class: lead -->

## Documente a decisão,
## não a descrição

A descrição envelhece sozinha
e alguém a encontra lendo o produto.

A decisão — e o que foi descartado —
**não está em lugar nenhum**
além do documento.

---

## Escrever revela o que não se entendeu

Um requisito que não se consegue escrever de forma verificável **não está entendido**.

Quem não consegue escrever meia página explicando por que escolheu uma alternativa costuma **não ter comparado as duas** — apenas escolheu a que já conhecia.

> 💡 A folha em branco é o teste mais barato contra decisão por hábito.

---

<!-- _class: lead -->

## ⚠️ Documentação errada é pior
## que documentação ausente

A ausente ninguém usa.

A errada **engana quem confia nela** —
e quem decide não tem como saber
que estava desatualizada.

---

## O que a ausência custa

| Sintoma | O que faltava |
|---|---|
| a mesma decisão discutida duas vezes | registro da decisão e das alternativas |
| a pessoa que sabe sai, e o projeto para | procedimento operacional escrito |
| a auditoria pede evidência e se reconstitui às pressas | registro de execução |
| o time reimplementa uma regra que já existia | nada escrito sobre a regra |

O custo aparece **disperso**, em horas de várias pessoas ao longo de meses.

---

## A ausência de documentação é um risco

Na transportadora, o **R-02** da Aula 09 — o único conhecedor se aposenta — é literalmente isso. A resposta escolhida, gravar sessões, é uma forma barata de documentar.

**Formulado como risco**, com probabilidade, impacto e dono, o assunto deixa de ser sobre boas práticas e passa a ser sobre **seis semanas de atraso**.

---

<!-- _class: tabela-densa -->

## Um documento que se mantém sozinho

| | |
|---|---|
| **Pergunta** | Como se concede acesso ao prontuário a um aluno? |
| **Leitor** | secretaria da clínica, e a auditoria |
| **Atualizado** | 03/2026 · responsável: Ana |
| **Procedimento** | 1. supervisor solicita · 2. coordenação confere matrícula · 3. acesso com prazo do semestre · 4. revogação automática |
| **Evidência** | cada concessão registra solicitante, aprovador e prazo |

---

## Quatro práticas, todas por escrever menos

| Prática | Por que funciona |
|---|---|
| escrever a **decisão**, não a descrição | decisão não muda sozinha |
| viver **junto do que descreve** | a mudança de um puxa a revisão do outro |
| **um documento por pergunta** | quem procura acha; quem atualiza sabe o escopo |
| **datar e assinar** | o leitor calibra a confiança sozinho |

E a mais honesta: **apagar** o documento que não é mantido.

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-11/`:

1. **`ex01.md`** — seis documentos: qual leitor, qual decisão?
2. **`ex02.md`** — documentar ou não, em cinco situações da frota;
3. **`ex03.md`** — quanto custou cada sintoma, com números;
4. **`ex04.md`** — reorganizar o manual de sessenta páginas;
5. **`ex05.md`** 🌶️ — o mínimo de documentação, com a lista do que **não** será escrito maior.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 12 — Ferramentas e comunicação**

Risco antecipa. Métrica mostra.
Documento preserva.

Falta o que **leva tudo isso
a quem precisa**.
