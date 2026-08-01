---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 07'
---

<!-- _class: capa -->

<div class="emoji">📝</div>

# Especificação: Documento e Histórias

## Aula 07 · Bloco 2 — Requisitos

<div class="meta">O cartão não é a especificação — é a promessa de uma conversa</div>

---

## 🎯 Nesta aula

1. **Dois formatos**, um mesmo objetivo
2. O **template** da história de usuário
3. **INVEST** — seis critérios
4. **Critérios de aceite** e Gherkin
5. **Glossário** e regras de negócio

---

<!-- _class: tabela-densa -->

## Documento × história de usuário

| | **Documento** | **História** |
|---|---|---|
| O que é | lista numerada e completa, escrita antes | lembrete de conversa, escrito quando necessário |
| Otimiza para | contrato, auditoria, rastreabilidade | adaptação e diálogo |
| Fecha quando | é aprovado | os critérios são acordados |
| Cai bem em | escopo fechado, regulação, time distribuído | cliente presente, entrega incremental |
| Falha quando | o requisito muda toda semana | não há ninguém para conversar |

---

<!-- _class: lead -->

## 💡 A diferença não é rigor

História bem-feita, **com critérios de aceite**,
é tão precisa quanto um requisito numerado.

A diferença é **quando** a precisão aparece:
antes de tudo, ou no momento de construir.

*O cartão não é a especificação —
é a promessa de uma conversa.*

Se a conversa não acontecer, você tem um formato ágil
com o conteúdo de um bilhete.

---

## O template

```
Como <papel>,
quero <ação ou capacidade>
para que <benefício>.
```

| Parte | Pergunta | Por que importa |
|---|---|---|
| Como ⟨papel⟩ | **quem?** | "como usuário" quase sempre esconde preguiça |
| quero ⟨ação⟩ | **o quê?** | a capacidade, não a tela |
| para que ⟨benefício⟩ | **por quê?** | é o que permite priorizar |

---

## Do sistema-guia

> **H-01** — Como **aluno**, quero **ver os espaços livres num período** para que **eu não atravesse o campus atrás de sala vazia**.
>
> **H-03** — Como **infraestrutura**, quero **interditar um espaço e avisar quem tinha reserva** para que **eu consiga fazer o conserto sem alguém aparecer para usar uma sala interditada**.

---

<!-- _class: lead -->

## ⚠️ O "para que" é o que mais some

E é o mais valioso.

Sem ele, ninguém consegue priorizar —
e ninguém percebe quando a ação pedida
não é a melhor forma de obter aquele benefício.

Uma história **sem** benefício é um pedido.
Uma história **com** benefício é um problema a resolver.

---

<!-- _class: tabela-densa -->

## INVEST

| Letra | Critério | A história falha quando |
|---|---|---|
| **I** | *Independent* | só faz sentido depois de outras três |
| **N** | *Negotiable* | já vem com a solução fechada |
| **V** | *Valuable* | entrega valor a quem constrói, não a quem usa |
| **E** | *Estimable* | ninguém diz se é grande ou pequena |
| **S** | *Small* | não cabe num ciclo de trabalho |
| **T** | *Testable* | não dá para dizer objetivamente se ficou pronta |

---

<!-- _class: tabela-densa -->

## Três defeituosas, e o conserto

| Defeituosa | Falha | Consertada |
|---|---|---|
| "quero um sistema de reservas" | **S T** | quebrar em consultar, reservar, cancelar |
| "quero criar a tabela de espaços" | **V** | é tarefa técnica dentro de outra história |
| "quero que o sistema seja rápido" | **T** | vira não-funcional com número |

> 💡 **Nem tudo precisa ser história.** Forçar tudo no formato produz frases tortas — como a terceira linha.

---

## Critérios de aceite

A história diz **o que se quer**. O critério diz **como saber que ficou pronto**.

Para a **H-03** — interditar um espaço e avisar quem tinha reserva:

1. A interdição exige espaço, período e motivo;
2. Reservas no período passam à situação "interrompida";
3. Cada solicitante é notificado em até 5 minutos;
4. O espaço não aparece nas consultas daquele período;
5. A interdição prevalece sobre qualquer reserva (`RN-05`);
6. Cancelar a interdição **não** restaura as reservas interrompidas.

---

<!-- _class: lead -->

## 💡 Repare no critério 6

Ele responde a uma pergunta
que a história **não fazia**.

Isso é normal e desejável:
escrever critério é **onde as lacunas aparecem** —
e é muito mais barato que descobri-las depois.

⚠️ Critério de aceite **não é roteiro de teste**.
Diz *o que* precisa ser verdade, não *como* clicar.

---

## Gherkin: um texto, três públicos

```gherkin
Cenário: Interdição atinge reserva já confirmada
  Dado que o Laboratório B-12 tem reserva confirmada
       para 12/08 das 14h às 16h
  Quando a infraestrutura interdita o B-12
       de 12/08 08h a 13/08 18h
  Então a reserva passa à situação "interrompida"
    E o solicitante recebe notificação em até 5 minutos
```

**Dado** = o estado antes · **Quando** = a ação · **Então** = o resultado observável.

---

<!-- _class: lead -->

## ⚠️ O defeito mais comum em Gherkin

Escrever **interface** no *Quando*:

*"Quando o usuário clica no botão Interditar"*

O *Quando* é o **comportamento**:
*"quando a infraestrutura interdita o espaço"*.

Se o cenário quebra quando a tela muda de lugar,
ele estava testando a tela.

---

<!-- _class: diagrama -->

## Da regra ao teste, sem perder o fio

![w:1120](img/historia-para-teste.svg)

---

<!-- _class: tabela-densa -->

## Glossário e regras de negócio

**Glossário** — escrito **com** o cliente. Sem ele, "espaço", "sala", "ambiente" e "local" convivem significando ora a mesma coisa, ora coisas diferentes.

**Regras de negócio** — verdadeiras **mesmo que nenhum sistema exista**.

| | História | Regra de negócio |
|---|---|---|
| Origem | um interessado quer algo | o domínio, a norma, a lei |
| Vive | num ciclo, e sai do backlog | enquanto a norma valer |
| Onde fica | backlog | documento do domínio |

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-07/`:

1. **`ex01.md`** — seis histórias, três papéis, nenhuma "como usuário";
2. **`ex02.md`** — cinco histórias que falham no INVEST: aponte as letras e reescreva;
3. **`ex03.md`** — critérios de aceite de três delas, um por caminho de erro;
4. **`ex04.md`** — três critérios em Gherkin, sem botão em nenhum `Quando`;
5. **Desafio 🌶️ `ex05.md`** — monte o glossário a partir de uma conversa gravada — e ache **o conceito que ainda não tem nome**.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 08 — Análise, priorização e validação**

Ler o próprio documento procurando defeito,
e decidir o que **não** será feito agora.
