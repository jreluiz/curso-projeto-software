---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 16'
---

<!-- _class: capa -->

<div class="emoji">🏁</div>

# Governança

## Aula 16 · Bloco 4 — Projeto Avançado

<div class="meta">Quem decide, quem responde, quem audita — e o fim do caminho</div>

---

## 🎯 Nesta aula

1. Governança — **quem decide e quem responde**
2. **PMI e PMBOK** — o arcabouço de projeto
3. **ITIL** — serviço, não projeto
4. **COBIT** — controle e auditoria
5. Qual sigla responde **qual pergunta**
6. **ESG** e o mapa do curso

---

## Três perguntas sem resposta escrita

A diretoria eleita contratou o sistema que vai apurar **a eleição seguinte** — a que pode tirá-la do cargo.

- **Quem decide** se o sistema entra em uso?
- **Quem responde** se a apuração for contestada?
- **Quem audita**, e com que acesso?

Ninguém agiu de má-fé. E ninguém escreveu nada.

---

## Governança × gestão

| | Gestão | Governança |
|---|---|---|
| **Pergunta** | como fazemos? | quem decide, e quem responde? |
| **Horizonte** | o projeto | a organização |
| **Produz** | entrega | direção, autoridade e controle |
| **Falha assim** | atraso, retrabalho | decisão tomada por quem não podia |

---

<!-- _class: lead -->

## ⚠️ "Governança só atrasa"

é a queixa de quem só conheceu
os sintomas ruins dela.

Um projeto sem governança
não é mais rápido:

ele apenas **descobre mais tarde**
que a decisão não valia.

---

## PMBOK: o arcabouço de projeto

| Estrutura | O que é |
|---|---|
| **Cinco grupos de processo** | iniciação, planejamento, execução, controle, encerramento |
| **Dez áreas de conhecimento** | integração, escopo, cronograma, custos, qualidade, recursos, comunicações, riscos, aquisições, partes interessadas |

Quase tudo deste curso está em alguma dessas caixas.

**Pergunta:** *como se conduz um esforço temporário até um resultado aceito?*

---

## ITIL: serviço, não projeto

| Conceito | O que é |
|---|---|
| **Serviço** | o que a TI entrega continuamente |
| **Incidente** | interrupção não planejada |
| **Problema** | a **causa raiz** por trás de incidentes repetidos |
| **Requisição** | pedido rotineiro: acesso novo, senha |
| **Acordo de nível de serviço** | compromisso de tempo e disponibilidade |

**Pergunta:** *como se sustenta um serviço em operação?*

---

<!-- _class: lead -->

## ⚠️ "Problema" muda de significado

Na Aula 09, problema é
**o que já aconteceu**.

No ITIL, problema é
**a causa de incidentes repetidos**.

Vocabulários diferentes —
e trocá-los numa reunião com operações
produz mal-entendido garantido.

---

## COBIT: governar × gerenciar

| | Governar | Gerenciar |
|---|---|---|
| **Faz** | avalia, dirige e monitora | planeja, constrói, executa |
| **Quem** | conselho, diretoria | gestores |
| **Pergunta** | vamos na direção certa? | executamos bem? |

**Pergunta:** *como se demonstra que a TI está sob controle?*

---

## A sequência de perguntas da auditoria

```
   ┌───────────┐   ┌───────────┐   ┌──────────┐   ┌───────────────┐
   │  Existe   │──▶│ Ele foi   │──▶│ Há       │──▶│ O registro é  │
   │procedimento?│  │ seguido?  │   │registro? │   │ recuperável?  │
   └───────────┘   └───────────┘   └──────────┘   └───────────────┘
```

Falhar na **última** é o mais frustrante: o procedimento existia, foi seguido — e ninguém consegue mostrar.

---

## Qual sigla responde qual pergunta

| Se a pergunta é… | O arcabouço é |
|---|---|
| como levo este esforço até o aceite? | **PMBOK** |
| como sustento este sistema em operação? | **ITIL** |
| como demonstro que a TI está sob controle? | **COBIT** |
| como o time organiza o trabalho quinzenal? | **Scrum** |

---

## O que os separa é o horizonte

```
   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌──────────────┐
   │  Scrum  │──▶│  PMBOK  │──▶│  ITIL   │──▶│    COBIT     │
   │ iteração│   │ projeto │   │ serviço │   │ organização  │
   └─────────┘   └─────────┘   └─────────┘   └──────────────┘

    quinzenal                                        anual
```

**Cobrar de um a resposta que está no horizonte do outro** é a origem de quase toda frustração com metodologia.

---

## ESG em projeto de TI

| Eixo | Como aparece |
|---|---|
| **Ambiental** | o relatório que ninguém lê rodando de hora em hora |
| **Social** | acessibilidade; exclusão de quem tem celular antigo |
| **Governança** | quem decide, quem responde, quem audita |

Três decisões deste curso têm impacto ESG — e **nenhuma foi tomada por esse motivo**.

---

## O mapa do curso

| Bloco | O que ele respondeu |
|---|---|
| **1 — Fundamentos** | o que é projeto, qual ciclo, quais processos, arquitetura |
| **2 — Metodologias** | o que o ágil diz, como o Scrum distribui autoridade |
| **3 — Ferramentas e qualidade** | antecipar risco, medir, documentar, comunicar |
| **4 — Avançado** | a mudança chega sem quebrar, quem está do outro lado |

---

<!-- _class: lead -->

## O que sobra quando os nomes
## forem esquecidos

**Toda decisão tem dono,
alternativa descartada e custo.**

**"Depende" é resposta legítima —
desde que você complete a frase.**

**A informação precisa chegar
a tempo a quem decide.**

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-16/`:

1. **`ex01.md`** — seis perguntas para os quatro arcabouços;
2. **`ex02.md`** — seis situações entre projeto e serviço;
3. **`ex03.md`** — as três perguntas de governança da assembleia digital;
4. **`ex04.md`** — impacto ESG de três decisões técnicas;
5. **`ex05.md`** 🌶️ — **autoavaliação:** uma decisão que você tomaria diferente hoje.

---

<!-- _class: lead -->

## 🏁 Fim do curso

Artefato preenchido
com a decisão errada dentro
não vale nada.

O que fica é decidir entre alternativas
e sustentar a decisão por escrito.

Obrigado — e `git push`.
