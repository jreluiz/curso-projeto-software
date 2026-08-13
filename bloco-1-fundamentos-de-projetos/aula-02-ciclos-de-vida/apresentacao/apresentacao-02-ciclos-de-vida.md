---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 02'
---

<!-- _class: capa -->

<div class="emoji">🔁</div>

# Ciclos de Vida

## Aula 02 · Bloco 1 — Fundamentos de Projetos

<div class="meta">Em que ordem, e quantas vezes voltamos atrás</div>

---

## 🎯 Nesta aula

1. A mesma equipe, **dois projetos, duas ordens**
2. O ciclo **clássico** — e o que ele acertou
3. **Incremental** — entregar em pedaços
4. **Iterativo** — refazer o mesmo pedaço melhor
5. **Preditivo × adaptativo** — um eixo, não dois campos
6. Escolher o ciclo é **decisão de projeto**

---

## Dois contratos, a mesma fornecedora

**Ouvidoria municipal** — escopo em edital, 8 meses com multa, mudança exige aditivo de 30 a 60 dias.

**Marketplace de serviços** — dois fundadores, 6 meses de reserva, e ninguém sabe se alguém quer o produto.

Rodar os dois do mesmo jeito é erro **nos dois casos**.

---

<!-- _class: lead -->

## Ciclo de vida não é metodologia

Nem ferramenta, nem cultura.

É a resposta a uma pergunta:
*em que ordem fazemos as coisas,
e quantas vezes voltamos atrás?*

---

## O ciclo clássico

```
   ┌────────────┐   ┌─────────┐   ┌───────────┐   ┌────────┐   ┌────────────┐
   │ Requisitos │──▶│ Projeto │──▶│ Construção│──▶│ Testes │──▶│ Implantação│
   └────────────┘   └─────────┘   └───────────┘   └────────┘   └────────────┘
```

**Ele acertou duas coisas** que nenhum ciclo posterior aboliu:

- existe uma **ordem natural** — não se testa o que não foi construído;
- **decisão registrada** vale mais que decisão lembrada.

---

## O custo tem nome: descoberta tardia

```
   custo de corrigir
        │                                              ╱
        │                                        ╱
        │                            ╱
        │              ╱
        │   ╱
        └───────┬────────┬───────────┬────────────┬──────
             requisitos projeto  construção    testes
```

Testes só no fim = **todo erro de requisito descoberto no ponto mais caro**.

---

<!-- _class: lead -->

## ⚠️ Cascata não é erro histórico

O erro é usá-la onde
a incerteza é alta.

Com escopo em edital e multa,
adotar ciclo adaptativo cria
uma expectativa que o contrato
não permite cumprir.

---

## Incremental: entregar em pedaços

| Entrega | Contém | Já dá para usar? |
|:---:|---|---|
| 1 | cadastrar item, emprestar, devolver | sim — substitui a planilha |
| 2 | reserva e conflito com empréstimo | sim |
| 3 | penalidade automática por atraso | sim |
| 4 | relatórios de uso | sim |

A penalidade é o pedido que a chefia mais repete — e ficou em **terceiro**.

---

## A ordem é ditada pela dependência

Sem registro de empréstimo e devolução, **não há como saber que houve atraso**.

O recorte incremental responde *"o que resolve mais dor primeiro?"* — respeitando o que depende de quê.

> 💡 É decisão de **gestão**, não técnica. E quem sabe a dor é quem a sofre.

---

## Incremental × iterativo

```
   INCREMENTAL   ┌───────┐     ┌───────┐     ┌───────┐
                 │  A    │  →  │  A B  │  →  │ A B C │      cresce
                 └───────┘     └───────┘     └───────┘

   ITERATIVO     ┌───────┐     ┌───────┐     ┌───────┐
                 │  A    │  →  │  A′   │  →  │  A″   │      melhora
                 └───────┘     └───────┘     └───────┘
```

Quadro pintado por partes é incremental. Esboçado e refinado três vezes é iterativo.

---

<!-- _class: lead -->

## ⚠️ "Somos iterativos"

é o disfarce mais comum.

O teste: nas últimas três entregas,
**alguma mexeu em algo já entregue?**

Se não, o time é incremental —
o que é legítimo, desde que ninguém
conte com o aprendizado que não acontece.

---

## Preditivo × adaptativo

| | Preditivo | Adaptativo |
|---|---|---|
| **Escopo** | definido no início | refinado no caminho |
| **Mudança** | exceção, com controle formal | esperada |
| **Sucesso é** | entregar o combinado | entregar o que resolve |
| **Exige** | requisitos estáveis | quem decide valor, toda semana |

**É um eixo, não dois campos** — e a maioria dos projetos vive no meio.

---

## O híbrido, na clínica-escola

| Parte do projeto | Ponta | Por quê |
|---|---|---|
| Controle de acesso e guarda legal | **preditiva** | a LGPD não muda no meio do projeto |
| Rotina de atendimento do aluno | **adaptativa** | ninguém sabe como será o uso |

Regime único falha nos dois lados: a parte legal fica frouxa, a de uso fica engessada.

---

## Escolher o ciclo: quatro perguntas

1. O escopo é **conhecido e estável**?
2. A mudança é **barata ou cara**?
3. Existe alguém disponível para **decidir valor toda semana**?
4. O usuário consegue **usar uma parte antes do todo**?

As duas primeiras decidem **onde no eixo**; a terceira, se o adaptativo é executável; a quarta, o **formato da entrega**.

---

<!-- _class: tabela-densa -->

## O registro cabe em meia página

| | |
|---|---|
| **Decisão** | preditivo, com entrega incremental em três fases |
| **Quem decidiu** | gerente do projeto, coordenação consultada |
| **Por quê** | escopo em edital; aditivo de 60 dias inviabiliza o adaptativo |
| **O que se perde** | o que se descobrir sobre o uso entra só no contrato seguinte |
| **Revisar se** | a prefeitura aceitar aditivar por demanda da operação |

A última linha é a que falta em quase todo registro.

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-02/`:

1. **`ex01.md`** — seis entregas: incremental ou iterativa?
2. **`ex02.md`** — três projetos no eixo preditivo–adaptativo;
3. **`ex03.md`** — recortar o empréstimo em três entregas utilizáveis;
4. **`ex04.md`** — o time que se diz iterativo: a afirmação se sustenta?
5. **`ex05.md`** 🌶️ — decisão de ciclo para a semana acadêmica, com o cenário que a derrubaria.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 03 — Os processos de um projeto**

A ordem está decidida.
Falta o que acontece **em volta** dela —
e que existe em qualquer ciclo.
