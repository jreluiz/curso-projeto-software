---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 01'
---

<!-- _class: capa -->

<div class="emoji">🧭</div>

# Por Que Gerir um Projeto de Software

## Aula 01 · Bloco 1 — Fundamentos de Projetos

<div class="meta">Decisão sem dono trava. E trava por semanas.</div>

---

## 🎯 Nesta aula

1. O projeto que **ninguém gerenciou**
2. **Projeto × operação**
3. Por que projetos de software **falham**
4. Os **conflitos** que todo projeto tem
5. A equipe e seus **papéis**
6. Matriz de responsabilidades — **RACI**

---

## O projeto que ninguém gerenciou

O setor de audiovisual precisa de um sistema de empréstimo.
Quatro pessoas, meio período. Combinaram: *"a gente começa e vai vendo"*.

**Cinco meses depois:** uma tela de cadastro bonita, nenhuma tela de devolução, e uma discussão sobre qual banco de dados usar.

Ninguém mentiu. Ninguém faltou.

---

<!-- _class: lead -->

## Gerir é manter três respostas de pé

**O quê** entregamos — e o que decidimos não entregar.

**Quando** — e o que acontece se a data não for cumprida.

**Quem decide** quando as duas primeiras se chocarem.

---

## Projeto × operação

| | Projeto | Operação |
|---|---|---|
| **Duração** | temporário | contínua |
| **Resultado** | único | repetitivo |
| **Equipe** | reunida para aquilo | permanente |
| **Termina quando** | o resultado é aceito | não termina |

O teste, em cinco segundos: **existe um dia em que isso acaba e alguém assina o aceite?**

---

## A fronteira tem nome e data

```
   Ideia          ┌──────────┐    ◆ ACEITE    ┌───────────┐
   aprovada  ───▶ │ PROJETO  │ ────────────▶  │ OPERAÇÃO  │
                  │ temporário│               │ permanente│
                  └──────────┘                └─────┬─────┘
                        ▲                            │
                        └────── demanda grande ──────┘
                              abre projeto NOVO
```

O laço de volta é o que confunde — e produz o "projeto" de dois anos.

---

## Por que projetos de software falham

**Escopo que cresce sem replanejar** — cada pedido é pequeno e razoável.

**Prazo definido antes do escopo** — ninguém perguntou o que cabe.

**Interessado que aparece no fim** — o auditor, na homologação.

**Decisão que ninguém toma** — duas opções, nenhuma autoridade.

> 💡 Nenhuma das quatro é *"a equipe não sabia programar"*.

---

## O custo cresce conforme demora a aparecer

| Causa | Aparece | Corrigir custa |
|---|---|---|
| Decisão que ninguém toma | 1ª semana | uma tarde |
| Prazo antes do escopo | 1º mês | recortar escopo |
| Escopo que cresce | 2º mês em diante | replanejar prazo |
| Interessado no fim | homologação | refazer o vetado |

**A mais barata de evitar é a primeira** — e é a que a equipe resolve sozinha.

---

<!-- _class: lead -->

## O sintoma comum às quatro

A informação existia
e **não chegou a quem decidia**.

O pedido combinado no corredor.
O auditor fora da lista.
As alternativas discutidas
por quem não podia escolher.

---

## Os conflitos que todo projeto tem

Na Ouvidoria municipal, a operação quer prazo folgado e a **lei fixa o prazo**.

| | Conflito de **objetivo** | Conflito de **pessoa** |
|---|---|---|
| **Origem** | metas legítimas e incompatíveis | relação, estilo, histórico |
| **Sinal** | os dois têm razão no próprio papel | o argumento não se sustenta |
| **Resolve com** | decisão de quem tem autoridade | conversa, mediação |

---

<!-- _class: lead -->

## ⚠️ Tratar objetivo como pessoa

produz reunião infinita.

Ninguém cede, porque ceder
significa falhar na própria função.

O que destrava é alguém
com autoridade decidir.

---

## A equipe e seus papéis

| Papel | Pergunta que ele responde |
|---|---|
| **Patrocinador** | vale a pena fazer isto? |
| **Gerente de projeto** | como está, e o que trava? |
| **Analista** | o que exatamente é para fazer? |
| **Time** | como isto vai funcionar? |
| **Usuário-chave** | isto resolve meu dia? |

No audiovisual faltou o **usuário-chave** — e por isso não existe tela de devolução.

---

<!-- _class: tabela-densa -->

## A matriz RACI

| Decisão | Pró-Reitoria | Coordenação | Gerente | Balcão |
|---|:---:|:---:|:---:|:---:|
| Aprovar o orçamento | **A** | C | R | I |
| Escopo da 1ª entrega | I | **A** | R | C |
| Escolher a tecnologia | I | I | **A** | — |
| Aceitar o sistema | C | **A** | R | C |

**R** faz · **A** responde · **C** é consultado · **I** é informado · **—** não participa

---

<!-- _class: lead -->

## ⚠️ Um A por linha. Sempre.

Dois aprovadores parecem diplomacia.

Quando os dois discordam,
a decisão trava — e na prática
**não é ninguém** que responde.

---

## Duas linhas que surpreendem

**Quem paga não decide tudo.** A Pró-Reitoria é **A** do orçamento e apenas **I** do escopo: ela sabe quanto pode gastar e não sabe o que o balcão precisa em março.

**Quem executa raramente aprova.** O gerente é **R** em quase tudo e **A** só na tecnologia — a decisão que é dele por competência.

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-01/`:

1. **`ex01.md`** — projeto ou operação? Seis casos, teste do aceite;
2. **`ex02.md`** — classificar quatro fracassos nas causas;
3. **`ex03.md`** — três conflitos da Ouvidoria: objetivo ou pessoa?
4. **`ex04.md`** — montar a RACI do empréstimo de equipamentos;
5. **`ex05.md`** 🌶️ — cortar escopo com data imóvel, dizendo o que se perde.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 02 — Ciclos de vida**

Decidimos *o quê* e *quem*.
Falta decidir **em que ordem** —
e quantas vezes voltamos atrás.
