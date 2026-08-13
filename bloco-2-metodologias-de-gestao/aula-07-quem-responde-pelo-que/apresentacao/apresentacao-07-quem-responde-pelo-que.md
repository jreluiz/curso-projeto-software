---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 07'
---

<!-- _class: capa -->

<div class="emoji">🎭</div>

# Quem Responde pelo Quê

## Aula 07 · Bloco 2 — Metodologias de Gestão

<div class="meta">Quando escopo, data e custo travam, a qualidade cede em silêncio</div>

---

## 🎯 Nesta aula

1. Duas perguntas, **duas naturezas**
2. O **gerente de projeto**: o que ele decide
3. O **Product Owner**: o que ele decide
4. Quando os dois **colidem**
5. **Stakeholder**: o que se cobra dele
6. A matriz **poder × interesse**

---

## Duas decisões na mesma segunda-feira

**"O fluxo de disputa entra antes ou depois do pagamento retido?"**
→ pergunta de **valor**

**"A reserva acaba em quatro meses — o que se faz com isso?"**
→ pergunta de **entrega**

Num projeto pequeno as duas caem na mesma pessoa. O problema é ninguém ter dito **qual está sendo respondida**.

---

<!-- _class: lead -->

## A frase mais curta que separa os três

O **PO** decide o quê e o porquê.

O **time** decide o como.

O **gerente** responde
pelo quando e por quanto.

---

## O gerente de projeto

| Decide | Não decide |
|---|---|
| replanejar quando há desvio | o que é mais valioso |
| escalar um risco à diretoria | qual funcionalidade entra primeiro |
| pedir aditivo ou mais gente | como o time organiza o trabalho |
| o que se comunica, a quem | a solução técnica |

O trabalho dele é **antecipar**: ver em maio o atraso que apareceria em julho.

---

<!-- _class: lead -->

## A assimetria da carreira

O gerente é cobrado
**pelo que apareceu**,
não pelo que não aconteceu.

Quem decidiu em maio e evitou
dois meses de atraso não tem como provar:
o projeto entregou no prazo,
e parece que foi fácil.

---

## O Product Owner exige três coisas

| Falta | Sintoma no time |
|---|---|
| **disponibilidade** | dúvidas se acumulam; o time decide sozinho e erra |
| **autoridade** | toda decisão sobe uma instância |
| **conhecimento do negócio** | o backlog é ordenado por quem grita mais alto |

**PO por procuração não é PO.** Se ele valida cada ordenação com um comitê, o PO de fato é o comitê — que não está disponível toda semana.

---

## Quando os dois colidem

Falta um mês. O backlog tem quinze itens. O gerente quer cortar sete; o PO diz que quatro deles dão sentido ao produto.

**Os dois estão certos dentro do próprio papel.**

| Se ceder… | Quem decide |
|---|---|
| o **escopo** | Product Owner |
| a **data** | patrocinador, ou o contrato |
| o **custo** | patrocinador |
| a **qualidade** | **ninguém** — não é variável |

---

## As quatro variáveis

```
        ┌─────────────┐        ┌──────────────┐
        │   ESCOPO    │────────│     DATA     │
        │  PO decide  │        │ patrocinador │
        └──────┬──────┘        └──────┬───────┘
               │                      │
        ┌──────┴──────┐        ┌──────┴───────┐
        │  QUALIDADE  │────────│    CUSTO     │
        │ não é       │        │ patrocinador │
        │ variável    │        └──────────────┘
        └─────────────┘
```

**Três travadas, a quarta cede.** E a quarta cede em silêncio.

---

<!-- _class: lead -->

## ⚠️ Qualidade não é folga

Quando escopo, data e custo
estão todos travados,

a única folga que sobra
é a qualidade —

e ela cede **sem que ninguém
tenha decidido nada**.

---

## Stakeholder: o que se cobra dele

| Do stakeholder | Exemplo |
|---|---|
| estar disponível quando só ele tem a informação | o supervisor que valida o formato do relatório |
| decidir dentro do prazo combinado | o comitê de ética, que se reúne uma vez por mês |
| assumir a consequência do que pediu | quem exigiu o relatório extra |
| comunicar mudança no próprio contexto | a secretaria que troca de sistema e não avisa |

---

## O stakeholder que não vai aparecer

Três saídas, e a escolha é do projeto:

- **Substituir a fonte** — alguém de dentro que conheça o assunto;
- **Reduzir o que se pede** — um clique num link, em vez de acesso ao sistema;
- **Assumir e registrar** — decidir sem ele, com a premissa escrita.

**Continuar marcando reuniões que ele não atende não é uma delas.**

---

<!-- _class: tabela-densa -->

## Matriz poder × interesse — Ouvidoria

| Interessado | Poder | Interesse | Estratégia |
|---|:---:|:---:|---|
| Secretário de Governo | alto | alto | gerenciar de perto |
| Ouvidor-geral | médio | alto | manter informado e consultar |
| Secretário do órgão que atrasa | alto | **contra** | gerenciar de perto |
| Cidadão | baixo | alto | manter informado |
| Controladoria | alto | baixo | manter satisfeito |

---

<!-- _class: lead -->

## Interesse não é estar a favor

O secretário do órgão que atrasa
tem interesse **alto** e joga contra.

Ele precisa da mesma atenção
que o patrocinador —
por motivo oposto.

Opositor surpreendido é muito
mais caro que opositor consultado.

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-07/`:

1. **`ex01.md`** — oito decisões entre GP, PO e time;
2. **`ex02.md`** — três situações em que acumular GP e PO decide errado;
3. **`ex03.md`** — o que se cobra de cada interessado do controle de estágio;
4. **`ex04.md`** — matriz poder × interesse do prontuário;
5. **`ex05.md`** 🌶️ — quinze itens, um mês, e a variável que vai ceder.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 08 — Descobrir, enxugar, melhorar**

Design Thinking, MVP e Lean
não são sinônimos de "trabalhar melhor".

Cada um responde
a uma pergunta diferente.
