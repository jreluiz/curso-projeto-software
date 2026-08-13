---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 15'
---

<!-- _class: capa -->

<div class="emoji">👥</div>

# O Usuário do Outro Lado

## Aula 15 · Bloco 4 — Projeto Avançado

<div class="meta">40% não conseguiram votar. E o sistema funcionava.</div>

---

## 🎯 Nesta aula

1. O sistema que funciona e **ninguém usa**
2. Análise de interface — **quem, para quê, em que contexto**
3. As **heurísticas** que pegam a maior parte
4. **UX não é UI**
5. Projeto de **interação**
6. **Acessibilidade** não é item extra

---

## O sistema funcionava

Apura corretamente. Garante o sigilo. Registra tudo para auditoria. Esteve no ar o tempo todo.

**E 40% dos associados não conseguiram votar:**

- o botão de confirmar ficava **abaixo da dobra** no celular;
- a mensagem de erro dizia *"operação inválida"*;
- a maioria tem mais de 60 anos e acessou **pelo telefone, na rua**.

---

<!-- _class: lead -->

## Passou em toda verificação

e falhou na única coisa
que importava.

É a validação sem verificação
da Aula 10 —
agora do lado do usuário.

---

## Três perguntas, nenhuma sobre tela

| Pergunta | Na assembleia |
|---|---|
| **Quem usa?** | associados de 25 a 85 anos, familiaridade desigual |
| **Para quê?** | votar uma vez, em 5 min, e ter certeza |
| **Em que contexto?** | celular, na rua, internet instável, baixa visão |

O contexto é o que **mais muda o desenho** e o que **menos se levanta**.

---

## Uso raro × uso diário

| | Uso raro | Uso diário |
|---|---|---|
| **Prioriza** | ser óbvio | ser rápido |
| **Aceita** | mais passos, se cada um for claro | atalhos, densidade |
| **Erra ao** | supor familiaridade | tratar como primeira vez |

Onze cliques no prontuário — uso diário — é problema. Na votação anual, pode ser aceitável.

---

## As heurísticas que pegam a maior parte

| Heurística | Violação na assembleia |
|---|---|
| **Visibilidade do estado** | o associado não sabe se o voto foi registrado |
| **Linguagem do usuário** | "operação inválida" |
| **Prevenção de erro** | permitir clicar duas vezes e depois recusar |
| **Reconhecer, não lembrar** | exigir o número da pauta digitado |
| **Ajuda a se recuperar** | erro sem instrução de saída |

---

## Mensagem de erro é interface

| | Ruim | Boa |
|---|---|---|
| **o que aconteceu** | "operação inválida" | "você já votou nesta pauta" |
| **por que** | — | "cada associado vota uma vez por pauta" |
| **o que fazer agora** | — | "volte à lista para ver as pautas em aberto" |

É a correção **mais barata** desta aula, e a que quase nenhum projeto aloca.

---

<!-- _class: lead -->

## O teste com cinco pessoas

Peça a quem não participou
que execute a tarefa,
sem ajuda, **em silêncio**.

O silêncio é a parte difícil —
e o que a pessoa não consegue
fazer sozinha **é o resultado**.

---

## UX não é UI

| | UI — interface | UX — experiência |
|---|---|---|
| **É** | o que se vê e se toca | o que acontece com a pessoa |
| **Inclui** | telas, botões, cores | passos, espera, o que se entende no erro |
| **Melhora com** | desenho visual | reduzir passos, antecipar erro |

**Uma tela bonita que exige onze cliques piorou a experiência.**

---

## O sintoma que identifica em segundos

*"Está feio"* → **UI**.

*"Levo dez minutos para lançar um atendimento"* → **UX**, e nenhuma paleta resolve.

> ⚠️ UI se resolve com um profissional de desenho. **UX se resolve com decisão de projeto** — de quem definiu o escopo e a arquitetura.

---

## Fluxo, estado e retorno

```
        ┌──────────────┐  abre a pauta   ┌──────────┐
        │ Autenticado  │────────────────▶│ Votando  │
        └──────────────┘                 └────┬─────┘
                                  escolhe │   ▲ volta
                                          ▼   │ atrás
        ┌──────────────┐   confirma  ┌──────────────┐
        │  Registrado  │◀────────────│ Confirmando  │
        │ + comprovante│             └──────────────┘
        └──────────────┘
```

Sem **Confirmando** e sem **comprovante**, o fluxo funciona igual — e produz os 40%.

---

## Acessibilidade: quatro camadas

| Camada | Exemplo |
|---|---|
| **Estrutura** | ordem de leitura correta, campos com rótulo |
| **Fluxo** | dar tempo suficiente; não exigir precisão de toque |
| **Conteúdo** | linguagem simples, contraste, texto alternativo |
| **Alternativa** | quem não consegue pelo digital tem outro caminho |

**Decidida no início é quase de graça. Retrofitada, é reconstrução.**

---

<!-- _class: lead -->

## Ela melhora o sistema
## para todo mundo

Contraste serve a quem tem baixa visão
**e a quem está no sol**.

Alvo de toque grande serve a quem
tem tremor **e a quem está no ônibus**.

O público beneficiado é sempre maior
que o público que a exigência nomeia.

---

<!-- _class: checkpoint -->

## 🏋️ Exercícios da aula

Na pasta `aula-15/`:

1. **`ex01.md`** — contexto de uso de três perfis do prontuário;
2. **`ex02.md`** — cinco situações, cinco heurísticas violadas;
3. **`ex03.md`** — oito decisões entre UX e UI;
4. **`ex04.md`** — fluxo de interação de "solicitar carona", com volta atrás;
5. **`ex05.md`** 🌶️ — o cliente que pediu confirmação em um clique só.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 16 — Governança**

Quem decide, quem responde,
quem audita.

E o mapa das dezesseis aulas.
