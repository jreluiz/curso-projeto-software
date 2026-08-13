---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 10'
---

<!-- _class: capa -->

<div class="emoji">📐</div>

# Qualidade que se Mede

## Aula 10 · Bloco 3 — Ferramentas e Qualidade

<div class="meta">Se a métrica virou meta, ela parou de medir</div>

---

## 🎯 Nesta aula

1. Qualidade **não é ausência de defeito**
2. **Verificação × validação**
3. O **sistema de qualidade**
4. Métricas — as que servem e as que **viram meta**
5. As quatro métricas **DORA**
6. **Maturidade** — CMMI e MPS.BR

---

## Zero defeito, zero chamado, sistema ruim

O prontuário foi entregue sem nenhum defeito conhecido. Todos os testes passam.

E: **onze cliques** para ver o caso de um aluno, busca que não aceita nome parcial, e trilha de auditoria que registra o acesso **mas não o motivo** — que é o que a norma exige.

O painel exibia tudo em verde.

---

<!-- _class: lead -->

## O painel não mostrou a falha

porque **não media a dimensão
que falhou**.

Não foi má-fé de ninguém.
Foi uma lacuna —

e é ela que produz o relatório verde
de um projeto que deu errado.

---

## Dimensões que competem entre si

| Dimensão | Pergunta |
|---|---|
| **Funcional** | faz o que precisa fazer? |
| **Confiabilidade** | continua funcionando quando algo dá errado? |
| **Usabilidade** | dá para usar sem treinamento longo? |
| **Desempenho** | responde no tempo que a tarefa exige? |
| **Segurança** | protege o que precisa ser protegido? |
| **Manutenibilidade** | dá para mudar sem quebrar? |

---

## A pergunta profissional

Não é *"como ter qualidade"*. É:

> **quais dimensões priorizamos, e o que aceitamos perder?**

Na clínica, **segurança ganha de usabilidade por decisão consciente**. Onze cliques por controle de acesso é defensável; onze cliques por descuido não é.

A diferença está em **alguém ter decidido**.

---

## Verificação × validação

| | Verificação | Validação |
|---|---|---|
| **Pergunta** | construímos **certo**? | construímos a **coisa certa**? |
| **Compara com** | a especificação | a necessidade real |
| **Quem responde** | quem constrói | quem usa |

Passar 100% na verificação e falhar na validação é o **pior resultado possível**: tudo construído como especificado, e a especificação estava errada.

---

## O ciclo que quase sempre falta

```
   ┌──────────────────┐   validação   ┌────────────────┐
   │ Necessidade real │──────────────▶│ Especificação  │
   └──────────────────┘               └────────┬───────┘
             ▲                                  │ verificação
             │                                  ▼
             │            "e serve?"     ┌────────────┐
             └───────────────────────────│  Sistema   │
                                         └────────────┘
```

**Verificação é barata e automatizável. Validação exige pessoa** — e é a primeira a ser cortada.

---

## Garantia × controle da qualidade

| | Garantia | Controle |
|---|---|---|
| **Olha para** | o **processo** que produz | o **resultado** produzido |
| **Pergunta** | trabalhamos do jeito acordado? | o que saiu está bom? |
| **Quando falha** | o defeito volta | um defeito escapa |

A auditoria da clínica vai pedir quase tudo de **garantia**.

---

<!-- _class: lead -->

## Auditoria não pergunta "está bom?"

Pergunta:

**"como você sabe que está bom?"**

E a segunda só tem resposta
se houver processo e registro.

---

## Métricas: as que servem e as que distorcem

| Métrica | Decisão que apoia | Como é distorcida |
|---|---|---|
| defeitos após a entrega | investir em revisão ou teste | parar de registrar defeito pequeno |
| tempo entre pedido e entrega | atacar espera no fluxo | fatiar itens artificialmente |
| itens que voltaram | rever a Definição de Pronto | afrouxar a Definição de Pronto |
| cobertura de testes | achar áreas sem teste | testes que não verificam nada |

---

## Três regras contra a distorção

**Medir em conjunto**, nunca isolada — velocidade sempre acompanhada de estabilidade.

**Medir o time, não a pessoa** — métrica individual custa colaboração.

**Não atrelar a bônus** — é a forma mais rápida de transformar medida em meta.

> 💡 E pergunte: **o que essa métrica não vê?**

---

## As quatro métricas DORA

| Métrica | Mede | Sinal de problema |
|---|---|---|
| **Frequência de implantação** | com que frequência chega ao usuário | de meses em meses |
| **Tempo de espera** | do commit à produção | semanas |
| **Tempo de restauração** | recuperação após falha | horas ou dias |
| **Taxa de falha** | implantações que causam problema | acima de 15% |

Duas medem **velocidade**, duas medem **estabilidade** — e elas se equilibram.

---

## Maturidade: os cinco níveis

| Nível | O que caracteriza |
|:---:|---|
| 1 — Inicial | funciona quando as pessoas certas estão no projeto |
| 2 — Gerenciado | há processo **por projeto** |
| 3 — Definido | o processo é **da organização** |
| 4 — Quantitativo | o processo é medido |
| 5 — Otimizado | a organização melhora o próprio processo |

Entre o 1 e o 2 está a diferença entre **depender de heróis e depender de método**.

---

<!-- _class: lead -->

## ⚠️ Maturidade não é qualidade

É possível produzir software ruim
de forma **muito repetível**.

E é possível produzir excelente software
num processo caótico — com duas pessoas
brilhantes que saem no ano seguinte,
levando o processo na cabeça.

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-10/`:

1. **`ex01.md`** — seis atividades: verificação ou validação?
2. **`ex02.md`** — uma exigência por dimensão, e com qual outra ela compete;
3. **`ex03.md`** — quatro métricas para a frota, com a distorção de cada;
4. **`ex04.md`** — três organizações nos níveis de maturidade;
5. **`ex05.md`** 🌶️ — a meta de 95% de cobertura com bônus atrelado.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 11 — Documentação**

Medir mostra o que acontece agora.

Documentar preserva
o que foi **decidido** —
para quem chegar depois.
