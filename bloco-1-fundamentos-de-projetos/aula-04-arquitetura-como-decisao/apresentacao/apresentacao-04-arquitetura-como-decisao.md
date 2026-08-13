---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 04'
---

<!-- _class: capa -->

<div class="emoji">🏛️</div>

# Arquitetura como Decisão de Projeto

## Aula 04 · Bloco 1 — Fundamentos de Projetos

<div class="meta">A decisão mais cara de reverter</div>

---

## 🎯 Nesta aula

1. Por que isto é **assunto de gestão**
2. O que **é** arquitetura de software
3. Estilos arquitetônicos — **camadas**
4. **Monolito × microsserviços**, com honestidade
5. Registrar a decisão — o **ADR**
6. A decisão é **do projeto**, não do time técnico

---

## Vinte minutos que custaram seis meses

Na transportadora, a equipe decidiu processar telemetria **em tempo real**. Conversa técnica, vinte minutos, ninguém de fora.

Seis meses depois: infraestrutura que ninguém orçou, disponibilidade que a operação não sabia que precisaria sustentar.

A alternativa — **lote, de hora em hora** — atenderia a regra, que avisa com **três dias** de antecedência.

---

<!-- _class: lead -->

## A pergunta que separa

*Se decidirmos errado,
quanto custa mudar de ideia
daqui a seis meses?*

Se a resposta for "uma semana",
não é arquitetura — é ferramenta,
e pode ser delegada.

---

## O que é arquitetural, e o que não é

| É arquitetural | Não é |
|---|---|
| dividir o sistema em camadas | qual biblioteca de gráficos usar |
| processar em lote ou em tempo real | o nome das variáveis |
| prontuário no mesmo banco do administrativo | o formato de data na tela |
| continuar operando quando o ERP cai | qual editor a equipe usa |

**Nenhuma das quatro é o nome de uma tecnologia.**

---

## Estilo: camadas

```
   ┌──────────────────────────────┐
   │  Apresentação — telas        │
   ├──────────────────────────────┤
   │  Negócio — regras, validações│
   ├──────────────────────────────┤
   │  Persistência — acesso       │
   ├──────────────────────────────┤
   │  ▓▓▓ Banco de dados ▓▓▓      │
   └──────────────────────────────┘

   A regra: a apresentação NÃO fala com a persistência.
```

---

## A violação é um atalho razoável

No delivery, mostrar a fila de pedidos buscando **direto no banco** funciona e é mais rápido de escrever.

Dois meses depois a regra muda: pedido cancelado não conta na fila. A camada de negócio é ajustada — e **a tela do entregador continua errada**.

Ninguém lembra do atalho, e o defeito vira lenda.

---

## Monolito × microsserviços

| | Monolito | Microsserviços |
|---|---|---|
| **Implantação** | uma, simples | várias, coordenadas |
| **Falha** | derruba tudo | isolada *(se o resto tolerar)* |
| **Custo operacional** | baixo | alto: rede, versões, monitoramento |
| **Exige** | pouco | equipe de operação madura |

**Microsserviços resolvem um problema de organização, não de tecnologia.**

---

<!-- _class: lead -->

## ⚠️ Microsserviço para três usuários

é o exemplo canônico
de decisão tomada por moda.

Se a resposta a *"qual problema
isso resolve?"* for "escalabilidade"
sem um número de carga ao lado,
a decisão não tem fundamento.

---

## Três perguntas, nenhuma técnica

1. **Quantos times independentes** vão mexer nisso?
2. **Quem vai operar** isso depois, às três da manhã?
3. **Qual parte precisa escalar sozinha**, e com que número?

O caminho barato, na dúvida: **monolito com fronteiras internas bem marcadas**. Dividir depois é trabalhoso; juntar depois é pior.

---

<!-- _class: tabela-densa -->

## O ADR da transportadora

| | |
|---|---|
| **Situação** | 60 veículos, 22 com telemetria; a regra avisa com 3 dias |
| **Decisão** | processar em **lote, de hora em hora** |
| **Descartadas** | *tempo real* — infra não orçada, disponibilidade insustentável; *lote diário* — perde a janela |
| **Consequências** | informação até 1 h desatualizada — irrelevante numa janela de 3 dias |
| **Revisar se** | surgir regra que exija reação em minutos |

---

<!-- _class: lead -->

## A linha das alternativas é o ADR

Sem ela, o documento diz
"decidimos processar em lote" —
que qualquer um descobre lendo o código.

Com ela, quem chegar em dois anos
sabe **sob quais premissas**.

---

## Três regras de uso do ADR

**Um ADR por decisão**, numerado e nunca apagado. Decisão revista ganha ADR novo que **supera** o anterior.

**Escrito quando a decisão é tomada** — reconstituir depois produz justificativa plausível, que não é a verdadeira.

**Meia página.** Se passar disso, virou documento de arquitetura, que é outra coisa e ninguém lê.

---

## O que fechou o Bloco 1

As quatro aulas contam a mesma história:

**Decisão sem dono trava.**
**Decisão sem registro se perde.**
**Decisão sem o custo declarado é aceita por engano.**

A matriz da Aula 01, o registro de ciclo da 02, a linha de base da 03 e o ADR desta aula são **quatro formatos do mesmo hábito**.

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-04/`:

1. **`ex01.md`** — seis decisões: arquiteturais ou não?
2. **`ex02.md`** — camadas do delivery, com a violação real;
3. **`ex03.md`** — resposta à proposta de microsserviços para três pessoas;
4. **`ex04.md`** — ADR do prontuário, com duas alternativas descartadas;
5. **`ex05.md`** 🌶️ — comunicar a decisão a três públicos diferentes.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 05 — O Manifesto Ágil, lido devagar**

Até aqui, decisões tomadas
por quem tinha autoridade formal.

A partir de agora, entram os métodos
que **distribuem** essa autoridade.
