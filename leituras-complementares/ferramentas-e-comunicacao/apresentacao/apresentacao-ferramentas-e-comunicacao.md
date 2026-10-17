---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 12'
---

<!-- _class: capa -->

<div class="emoji">🧰</div>

# Ferramentas e Comunicação

## Aula 12 · Bloco 3 — Ferramentas e Qualidade

<div class="meta">A ferramenta não decide nada. Ela mostra.</div>

---

## 🎯 Nesta aula

1. A ferramenta **não é o método**
2. Ferramentas para modelos **sequenciais**
3. Ferramentas para modelos **ágeis**
4. **Kanban** e o limite de trabalho em andamento
5. **Gestão da comunicação**
6. O plano de comunicação **numa tabela**

---

## A ferramenta funcionava perfeitamente

A transportadora comprou uma ferramenta ágil, migrou os projetos para quadros e chamou as fases de sprints.

Escopo, prazo e orçamento continuaram **fechados no início do ano**.

Seis meses depois, a equipe está frustrada: prometeram adaptação e ela nunca aconteceu.

---

<!-- _class: lead -->

## Trocar a ferramenta é barato

Mudar o contrato,
a expectativa da diretoria
e a disponibilidade do cliente
**não é**.

É por isso que a adoção
quase sempre para
na parte visível.

---

## O que se ganha de verdade

**Visibilidade.** Ela não decide nada, não prioriza nada e não conserta processo. Mostra.

E mostrar já é bastante: o quadro que expõe catorze itens parados não resolve nada — e torna impossível continuar dizendo que está tudo andando.

> 💡 A pergunta antes de escolher: **o projeto é preditivo ou adaptativo?**

---

## Sequenciais: EAP, Gantt, marco

```
   Cadastro de veículos      ████████████
   Registro de abastecimento             ████████
   Mapeamento do ERP         ████████████████
   Integração de telemetria                  ████████████████████
   Homologação                                                   ████████
   Entrada em operação                                                   ◆
   ├────────┬────────┬────────┬────────┬────────┬────────┬────────┬──────┤
  mar      abr      mai      jun      jul      ago      set      out
```

**Caminho crítico:** mapeamento + telemetria = 63 dias, contra 35 do cadastro.

---

## Como se lê um Gantt

Nesta ordem: **o marco** no fim, **a cadeia mais longa** até ele, e **onde há folga**.

Atrasar o cadastro em uma semana **não move a entrega**. Atrasar o mapeamento move — ele está no caminho crítico.

> ⚠️ O Gantt é a foto de uma decisão, e envelhece. Se as barras não mudam há dois meses, ou o projeto é perfeito ou ninguém está replanejando.

---

## Ágeis: backlog, quadro, burndown

| Instrumento | Pergunta que responde |
|---|---|
| **Backlog ordenado** | o que fazemos a seguir? |
| **Quadro** | onde o trabalho está travando? |
| **Burndown** | vamos chegar? |

Os três são de **fluxo** — e nenhum diz se o que está sendo feito **importa**.

---

## O quadro, com limites

```
   ┌────────────┐  ┌──────────────┐  ┌─────────────┐  ┌──────────┐
   │  A FAZER   │  │   FAZENDO    │  │   REVISÃO   │  │  PRONTO  │
   │            │  │  limite: 2   │  │  limite: 1  │  │          │
   ├────────────┤  ├──────────────┤  ├─────────────┤  ├──────────┤
   │ Relatório  │  │ Reg. retorno │  │ Reg. saída  │  │ Cadastro │
   │ Filtro     │  │ Mapea. ERP   │  │             │  │          │
   └────────────┘  └──────────────┘  └─────────────┘  └──────────┘
```

---

<!-- _class: tabela-densa -->

## O burndown se lê pela inclinação

| Dia | Ideal | Real | O que já diz |
|:---:|:---:|:---:|---|
| 3 | 32 | 38 | a inclinação real é menor: atenção |
| 5 | 24 | 30 | dá para prever que metade não sai |
| 7 | 16 | **34** | **subiu** — entrou escopo no meio |
| 10 | 0 | 22 | fechou com pouco mais da metade |

**A leitura útil acontece no dia 5**, não no dia 10.

---

## Por que o limite funciona

- **Começar é grátis, terminar é caro.** Sem limite, todos começam;
- **Item parado não entrega valor.** Cinco itens 80% prontos valem zero;
- **O limite força a conversa certa.** De *"quem está livre?"* para *"o que precisa terminar?"*.

A regra prática: **limite menor que o número de pessoas**.

---

<!-- _class: lead -->

## ⚠️ O limite mais revelador

não é o de "Fazendo".

É o das colunas de **espera** —
revisão, homologação —,

que costumam não ter limite
porque parece que
"só estão aguardando".

---

<!-- _class: tabela-densa -->

## O plano de comunicação

| Interessado | Precisa saber | Frequência | Formato |
|---|---|---|---|
| Diretoria | se data e custo se sustentam | mensal | 1 página, com semáforo |
| Gestor de frota | o que muda na operação | quinzenal | reunião 30 min + resumo |
| Equipe | tudo que afeta a semana | diária | conversa e quadro |
| Oficina | quando o sistema sugere janelas | por marco | comunicado curto |
| Auditoria | o que foi decidido e quem aprovou | sob demanda | registro no repositório |

---

## Três regras que a tornam usável

**Uma linha por interessado**, não por reunião — senão quem não tem reunião some do plano.

**Quem envia é uma pessoa.** "A equipe informa" não informa nada.

**Notícia ruim vai antes do canal previsto**, e diretamente. O plano estabelece o mínimo, não o teto.

---

<!-- _class: lead -->

## O que fecha o Bloco 3

Risco, qualidade, documentação
e comunicação são a mesma coisa:

**fazer a informação chegar
a tempo a quem decide.**

Nenhuma produz software.
Todas evitam que ele
seja feito errado.

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-12/`:

1. **`ex01.md`** — cinco situações: Gantt, quadro ou burndown?
2. **`ex02.md`** — caminho crítico, folga, e o efeito de duas semanas de atraso;
3. **`ex03.md`** — 14 cartões em "Fazendo": diagnóstico e limites;
4. **`ex04.md`** — plano de comunicação do prontuário, com o comitê de ética;
5. **`ex05.md`** 🌶️ — a ferramenta ágil comprada para projetos preditivos.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 13 — Versão, mudança e configuração**

O Bloco 4 começa
onde a mudança encontra
o sistema que já está no ar.
