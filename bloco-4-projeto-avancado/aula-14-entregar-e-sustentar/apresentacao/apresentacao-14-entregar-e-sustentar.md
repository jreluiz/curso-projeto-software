---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 14'
---

<!-- _class: capa -->

<div class="emoji">🚀</div>

# Entregar e Sustentar

## Aula 14 · Bloco 4 — Projeto Avançado

<div class="meta">Manter custa mais que construir</div>

---

## 🎯 Nesta aula

1. O que acontece **depois que sobe**
2. O **pipeline** e os ambientes
3. **Feature flag** e o lançamento controlado
4. Mudança precisa de **caminho de volta**
5. **Observabilidade** — registro, métrica e alerta
6. **Manutenção** e **dívida técnica**

---

## Três perguntas no minuto seguinte

A mudança sobe às 18h de uma terça.

- **Como voltamos, se quebrar?**
- **Como sabemos que quebrou**, antes de o cliente reclamar?
- **Quem responde por isso às 21h de sábado?**

Nenhuma é sobre construir. Todas são sobre **sustentar**.

---

<!-- _class: lead -->

## Um projeto de oito meses

gera **anos** de operação.

Manter custa mais que construir,
e quase todo o esforço de um curso
vai para a parte curta.

Esta aula é sobre a longa.

---

## O pipeline e os ambientes

```
   ┌──────────────┐  ┌─────────────┐  ┌──────────────┐  ┌───────────┐
   │Desenvolvimento│─▶│ Integração  │─▶│ Homologação  │─▶│ Produção  │
   │  funciona     │  │  funciona   │  │  o cliente   │  │ o usuário │
   │  isolado?     │  │   junto?    │  │   aprova?    │  │    usa    │
   └──────────────┘  └─────────────┘  └──────────────┘  └───────────┘
```

**O mesmo pacote atravessa todos.** Só a configuração muda.

---

## Feature flag: implantar ≠ liberar

| Estratégia | Como funciona |
|---|---|
| **Feature flag** | sobe desligado, liga-se para um grupo |
| **Lançamento gradual** | 5% dos usuários, depois 25%, depois todos |
| **Dois ambientes em paralelo** | o novo sobe ao lado, o tráfego é trocado |
| **Janela de manutenção** | avisa-se, para, sobe, religa |

O ganho é de gestão: **quem decide liberar passa a ser quem entende do negócio**.

---

<!-- _class: lead -->

## ⚠️ Flag é dívida com prazo

Cada uma acrescenta
um caminho a mais no sistema.

Duas flags produzem
**quatro combinações**.

Toda flag precisa de data
para ser removida.

---

## Voltar nem sempre é possível

| Tipo de mudança | Voltar é |
|---|---|
| código novo, sem tocar em dados | fácil: republica-se a anterior |
| mudança de configuração | fácil, se a anterior estiver versionada |
| estrutura de banco que só acrescenta | possível, com cuidado |
| estrutura que **remove ou converte** | **caro ou impossível** |

A última muda o risco — e precisa estar **escrita antes**.

---

<!-- _class: tabela-densa -->

## O plano de volta, em quatro linhas

| | |
|---|---|
| **Quando decidimos voltar?** | se pedidos confirmados caírem abaixo de 80% por 10 min |
| **Quem decide?** | quem estiver de plantão, sem consultar ninguém |
| **Como se volta?** | republicar a versão anterior; o banco não foi alterado |
| **Quanto leva?** | cerca de 4 minutos |

**A primeira linha é a que sempre falta** — e sem ela, volta-se por desgaste.

---

## Observabilidade não é monitorar a máquina

Processador em 30%, memória em 40%, tudo verde. E **30% dos pedidos falham há dois dias**.

| Elemento | Exemplo no delivery |
|---|---|
| **Registro** | "pedido 4471 recusado: pagamento não confirmado" |
| **Métrica** | pedidos confirmados por hora |
| **Alerta** | pedidos confirmados caíram 50% em 15 min |

Instrumenta-se o **comportamento do negócio**.

---

<!-- _class: lead -->

## ⚠️ Alerta que não exige ação

treina o time a ignorá-lo.

Depois de duas semanas
de avisos irrelevantes, ninguém olha —

e o importante chega
no mesmo canal que os outros.

**Se não for para acordar alguém,
é métrica.**

---

## Manutenção: os quatro tipos

| Tipo | O que é | Proporção |
|---|---|---|
| **Corretiva** | consertar defeito | a **menor** |
| **Adaptativa** | acompanhar lei, integração, sistema | grande e inevitável |
| **Perfectiva** | melhorar o que já funciona | a **maior** |
| **Preventiva** | reduzir risco de defeito futuro | a que mais se corta |

**Contrato que cobre só a corretiva deixa de fora a maior parte do trabalho.**

---

## Dívida técnica: duas formas

**Deliberada e registrada** — *"vamos duplicar esta regra para entregar na sexta, e unificar na semana 3"*. Legítima, e às vezes a decisão certa.

**Acidental e silenciosa** — ninguém decidiu nada, e a estrutura foi ficando. É a qualidade cedendo sem autorização, da Aula 07.

**A diferença é o registro** — e ele é o que permite pagá-la.

---

## Traduzir é o que a faz disputar prioridade

| Em vocabulário técnico | Em vocabulário de quem paga |
|---|---|
| "esse módulo tem alto acoplamento" | "cada mudança ali leva 3× mais tempo" |
| "precisamos refatorar antes" | "duas funcionalidades agora e nenhuma em março, ou uma agora e quatro até março" |
| "a cobertura está baixa aqui" | "sempre que mexemos aqui, algo quebra em outro lugar" |

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-14/`:

1. **`ex01.md`** — pipeline do delivery, com o que sobe em cada etapa;
2. **`ex02.md`** — oito chamados nos quatro tipos de manutenção;
3. **`ex03.md`** — como se volta em quatro mudanças, e o plano da que não volta;
4. **`ex04.md`** — cinco eventos, três métricas, dois alertas com ação;
5. **`ex05.md`** 🌶️ — a dívida técnica explicada a um dono de restaurante.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 15 — O usuário do outro lado**

O sistema está no ar,
instrumentado e sustentável.

Falta saber se alguém
**consegue usá-lo**.
