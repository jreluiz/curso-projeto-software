---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 13'
---

<!-- _class: capa -->

<div class="emoji">🔀</div>

# Versão, Mudança e Configuração

## Aula 13 · Bloco 4 — Projeto Avançado

<div class="meta">Se essa mudança quebrar, quanto tempo até voltar?</div>

---

## 🎯 Nesta aula

1. Controle de versão como **prática de engenharia**
2. O custo do **branch longo**
3. **Item de configuração** — e não é só código
4. **Baseline** e rastreamento de mudança
5. **Integração contínua**
6. **CI/CD** — o que cada sigla entrega

---

## A pergunta que define a maturidade

O restaurante **não pode parar**. Toda mudança entra com o serviço funcionando, no meio do expediente.

> **Se essa mudança quebrar, quanto tempo até voltar ao que funcionava?**

Se a resposta for *"não sei"*, não há controle de versão. Há um lugar onde os arquivos ficam.

---

## O que o controle de versão responde

| Pergunta | Sem controle | Com controle |
|---|---|---|
| o que mudou desde a última entrega? | ninguém sabe ao certo | a lista exata |
| como volto ao que funcionava? | reconstrói-se de memória | um comando |
| quem alterou isto, e por quê? | perde-se com a rotatividade | está registrado |

---

## O custo do branch longo

```
   INTEGRA TODO DIA    ●─●─●─●─●─●─●─●─●─●    conflitos pequenos
                       └─┴─┴─┴─┴─┴─┴─┴─┴─┘    e previsíveis

   INTEGRA EM 3 SEM    ●───────────────────●  um conflito grande,
                                              imprevisível, no pior momento
```

*"Vou terminar tudo direitinho antes de integrar"* parece cuidadoso.

---

<!-- _class: lead -->

## Adiar não evita o custo

**Multiplica.**

E enquanto o ramo existe,
ninguém sabe se aquilo funciona
junto com o resto —

o cartão está em "Revisão"
e o risco continua inteiro em pé.

---

## Item de configuração não é só código

| Item | Por que entra |
|---|---|
| o código da aplicação | óbvio, e a menor parte da lista |
| o script do banco | uma versão errada derruba tudo |
| a configuração do ambiente | o mesmo código se comporta diferente |
| o cardápio e as regras de preço | mudam sem código e mudam o comportamento |
| a versão das bibliotecas | o que funcionou ontem depende delas |

---

<!-- _class: lead -->

## A pergunta que identifica um item

**Se isto mudar sozinho,
alguma coisa quebra
ou alguém se engana?**

E: *"funciona na minha máquina"*
é quase sempre um item
de configuração não controlado.

---

## Baseline e o fluxo de mudança

```
   ┌─────────────┐   ┌──────────────┐  aprovada  ┌────────────────┐
   │ Solicitação │──▶│   Análise    │───────────▶│ Implementação  │
   └─────────────┘   │  de impacto  │            └───────┬────────┘
                     └──────┬───────┘                    │
                            │ recusada                   ▼
                            ▼                    ┌────────────────┐
                   ┌─────────────────┐           │ Nova baseline  │
                   │ Registro da     │           └────────────────┘
                   │ recusa          │
                   └─────────────────┘
```

---

## Três tipos, três caminhos

| Tipo | Exemplo | Caminho |
|---|---|---|
| **Padrão** | tirar um item do cardápio | pré-aprovada: registra e faz |
| **Normal** | mudar a regra do frete | análise, aprovação, nova baseline |
| **Emergencial** | acabou ingrediente às 20h de sábado | executa e **registra depois**, com prazo |

A linha emergencial precisa dizer **o que autoriza pular** e **o que obriga a fazer depois**.

---

<!-- _class: lead -->

## ⚠️ Processo pesado demais

é contornado, não seguido.

Se aprovar uma correção de texto
leva três dias, as pessoas corrigem
direto e avisam depois —

e aí não há nem processo
nem registro.

---

## Integração contínua exige três coisas

- **Um lugar único** onde o trabalho se junta;
- **Verificação automática** a cada integração;
- **Prioridade de conserto** — integração quebrada é o problema mais importante do time.

A terceira é cultural, e é a que falha. Verificação vermelha por três dias **deixa de significar qualquer coisa**.

---

## CI/CD: três coisas distintas

| Sigla | O que é | Decisão de quem |
|---|---|---|
| **CI** — integração contínua | o trabalho se junta e é verificado várias vezes ao dia | **engenharia** |
| **CD** — entrega contínua | **sempre pronto** para implantar | **engenharia** |
| **CD** — implantação contínua | vai a produção **automaticamente** | **negócio** |

---

## As três se encadeiam

```
   ┌──────────────┐   ┌─────────────────┐   ┌──────────────────────┐
   │      CI      │──▶│ Entrega contínua│──▶│ Implantação contínua │
   │ integra e    │   │ sempre pronto   │   │    vai sozinho       │
   │ verifica     │   │                 │   │                      │
   └──────────────┘   └─────────────────┘   └──────────────────────┘
                             ▲                          │
                             └── decisão de negócio ─────┘
```

**Recusar a terceira não obriga a abrir mão da segunda.**

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-13/`:

1. **`ex01.md`** — seis itens de configuração do delivery, e o que quebra;
2. **`ex02.md`** — seis mudanças ordenadas por impacto na baseline;
3. **`ex03.md`** — fluxo de mudança emergencial, com o que ele obriga depois;
4. **`ex04.md`** — mesma esteira, ramos de 1 dia × 3 semanas;
5. **`ex05.md`** 🌶️ — a proposta ao dono que recusou implantação contínua.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 14 — Entregar e sustentar**

A mudança está pronta para subir.

O minuto seguinte é onde
a maior parte do custo
de um software acontece.
