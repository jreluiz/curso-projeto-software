---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 09'
---

<!-- _class: capa -->

<div class="emoji">⚠️</div>

# Risco

## Aula 09 · Bloco 3 — Ferramentas e Qualidade

<div class="meta">Risco sem dono e sem gatilho é literatura</div>

---

## 🎯 Nesta aula

1. Risco **não é problema**
2. A natureza do risco — **causa, evento, efeito**
3. Como se **levanta** risco
4. A matriz **probabilidade × impacto**
5. As **quatro respostas** ao risco
6. Risco precisa de **dono e gatilho**

---

## Risco não é problema

| | Risco | Problema |
|---|---|---|
| **Quando** | pode acontecer | já aconteceu |
| **O que se faz** | acompanha, com resposta pronta | resolve |
| **Some quando** | o evento acontece, ou a janela passa | é resolvido |

O servidor lento há três semanas é **problema**.
O único conhecedor do legado que se aposenta em quatro meses é **risco**.

---

<!-- _class: lead -->

## A confusão custa dos dois lados

Chamar problema de risco
**adia a solução** — fica monitorado
enquanto o servidor segue lento.

Tratar risco como problema
é não fazer nada até ele virar um.

---

## Causa, evento, efeito

```
   CAUSA                  →   EVENTO INCERTO         →   EFEITO
   algo que já é verdade      o que pode acontecer       o que custa
```

> **R-01** — Porque a documentação do ERP está desatualizada e há um só conhecedor, **a integração pode levar o dobro do estimado**, atrasando a entrega em 6 semanas.

*"Risco: integração"* não é risco. É assunto.

---

## Escrever o risco já sugere a resposta

Se a causa é **documentação desatualizada e um só conhecedor**, a resposta aparece sozinha: mapear a integração cedo, gravar sessões com quem sabe.

> ⚠️ Se o texto tiver **duas causas incertas**, são dois riscos. *"Se o fornecedor atrasar E a equipe ficar reduzida…"* mistura eventos com probabilidades diferentes.

---

## De onde vêm os riscos

| Fonte | O que ela dá |
|---|---|
| **As premissas do termo de abertura** | toda premissa é um risco — a fonte mais barata e mais ignorada |
| **Lições aprendidas** | o que deu errado antes tende a dar de novo |
| **Quem executa** | quem vai integrar sabe o que preocupa |

Categorias: técnico · pessoas · externo · gestão · **organizacional**

---

<!-- _class: lead -->

## ⚠️ O mais perigoso é organizacional

e é o que menos se escreve.

*"O patrocinador pode perder a eleição
e o projeto perder o padrinho"*

é constrangedor de registrar —
e é o tipo de coisa que mata projeto.

---

## A matriz probabilidade × impacto

| | Impacto baixo | Impacto médio | Impacto alto |
|---|---|---|---|
| **Prob. alta** | 🟡 monitorar | 🔴 atacar já | 🔴 atacar já |
| **Prob. média** | 🟢 aceitar | 🟡 monitorar | 🔴 atacar já |
| **Prob. baixa** | 🟢 aceitar | 🟢 aceitar | 🟡 **monitorar** |

O canto inferior direito é onde moram os riscos que **acabam com o projeto**.

---

## Combine a régua antes de classificar

| Nível | Probabilidade | Impacto (prazo) |
|---|---|---|
| **baixo** | seria surpresa | até 1 semana |
| **médio** | acontece em projetos assim | 1 a 4 semanas |
| **alto** | é mais provável que não | mais de 4 semanas, ou a data cai |

Sem a régua escrita, a classificação vira **negociação sobre adjetivos**.

---

## As quatro respostas

| Resposta | O que se faz | O que custa |
|---|---|---|
| **Evitar** | mudar o plano para o risco não existir | escopo |
| **Mitigar** | reduzir probabilidade ou impacto | esforço agora |
| **Transferir** | passar o impacto a outro | dinheiro e dependência |
| **Aceitar** | conviver, conscientemente e por escrito | nada agora, tudo depois |

---

<!-- _class: lead -->

## ⚠️ Evitar é a mais esquecida

e às vezes a mais barata.

Muita reunião discute
como **mitigar** algo que o projeto
poderia simplesmente não fazer.

Antes de "como reduzimos?",
vale perguntar
"precisamos mesmo disto agora?".

---

<!-- _class: tabela-densa -->

## Uma linha do registro de riscos

| | |
|---|---|
| **ID** | R-01 |
| **Risco** | doc. do ERP desatualizada → integração pode dobrar → +6 semanas |
| **Probabilidade · Impacto** | alta · alto |
| **Resposta** | mitigar: mapear a integração no 1º mês |
| **Dono** | Ana |
| **Gatilho** | mapeamento não concluído até 30/03 |

---

<!-- _class: lead -->

## Duas colunas separam gestão de literatura

**Dono** é uma pessoa, não uma área.

**Gatilho** é o sinal observável,
com número e data.

*"Fila acima de 4 veículos"* é gatilho.
*"Quando piorar"* não é.

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-09/`:

1. **`ex01.md`** — seis itens: risco ou problema?
2. **`ex02.md`** — reescrever cinco riscos em causa → evento → efeito;
3. **`ex03.md`** — seis riscos da frota na matriz, um deles baixa/alto;
4. **`ex04.md`** — trocar a resposta de cada risco, uma delas "evitar";
5. **`ex05.md`** 🌶️ — registro completo, com um risco organizacional.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 10 — Qualidade que se mede**

O risco antecipa o que pode acontecer.

A métrica mostra o que
**está** acontecendo — quando
alguém escolheu medir a coisa certa.
