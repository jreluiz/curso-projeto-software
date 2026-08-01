# 🎓 Projeto Final — Dossiê de Projeto de Software

> 📅 **Quando:** Bloco 4, após a [Aula 14](../bloco-4-projeto-de-software/aula-14-arquitetura-de-software/README.md).
> 🎯 **O que é:** o curso inteiro numa entrega só — um problema do mundo vira requisitos, modelos, decisões de arquitetura e um plano de teste, tudo com a justificativa escrita.

Individual. Tema de sua escolha. **Nenhuma linha de código.**

## 🎯 O que se prova aqui

Que você consegue, sozinho, atravessar o caminho inteiro:

```
   problema do mundo  →  requisitos  →  modelos  →  decisões de projeto  →  plano de teste
        (§1)              (§2)          (§3, §4)         (§5, §6)              (§7)
```

E, principalmente, que **cada passagem de uma caixa para a seguinte vem acompanhada do motivo**. Um dossiê sem justificativa é um álbum de desenhos.

## 🌍 Escolhendo o tema

Três critérios, nesta ordem:

1. **Você entende o domínio?** Projetar bem exige saber quando o enunciado está mentindo. O trabalho de alguém da família, um hobby, a rotina de um lugar que você frequenta — vale mais que um tema "impressionante" que você conhece de fora;
2. **Tem conflito suficiente?** Se todos os interessados querem a mesma coisa, não há decisão a tomar — e é a decisão que se avalia aqui. Procure um domínio com pelo menos duas pessoas que discordam;
3. **Cabe em duas semanas?** Projetar o Instagram inteiro não é ambição, é falta de recorte. **Recortar é a primeira habilidade do projetista.**

Pode ser um do [catálogo de sistemas para praticar](../recursos/sistemas-para-praticar.md) (prefira os ⭐⭐⭐ e ⭐⭐⭐⭐) ou de autoria própria — esta última é incentivada. A Reserva de Espaços do Campus está fora: é o sistema-guia, e está publicada nas aulas.

> 💡 Se você fez o [trabalho em dupla](trabalho-em-dupla.md), pode **continuar o mesmo sistema** — o documento de requisitos de lá vira a base dos §1 e §2, e você usa o tempo no que é novo. Diga isso no README e credite a dupla.

## ✅ Requisitos obrigatórios

### 1. Visão do produto

- [ ] O **problema** em 3 a 5 parágrafos, em português corrido, sem nomear telas nem tecnologia;
- [ ] Quem são os **usuários e demais interessados**, com o que cada um ganha e o que teme;
- [ ] **O que está fora do escopo**, numa tabela com o motivo de cada exclusão.

### 2. Requisitos

- [ ] Mínimo de **12 requisitos funcionais** numerados;
- [ ] Mínimo de **8 requisitos não-funcionais** numerados, todos com número, unidade ou critério objetivo;
- [ ] Mínimo de **6 regras de negócio** numeradas (`RN-01`…), verdadeiras mesmo sem o sistema;
- [ ] **Glossário** do domínio, mínimo de 8 termos;
- [ ] Uma seção de **questões em aberto**.

### 3. Casos de uso

- [ ] **Diagrama de casos de uso** em PlantUML, com o `.puml` e o `.svg` commitados;
- [ ] **3 casos de uso especificados** no formato completo: ficha, fluxo principal, fluxos alternativos e **fluxos de exceção**;
- [ ] Cada exceção cita a regra (`RN-NN`) ou a observação de contexto que a origina;
- [ ] Nenhum caso de uso chamado "Gerenciar X" ou com nome de tela.

### 4. Modelos

- [ ] **Diagrama de classes de análise** em Mermaid, com multiplicidades **nos dois lados** de toda associação;
- [ ] Pelo menos uma **composição**, com as duas perguntas da [Aula 11, §4](../bloco-3-modelagem-e-uml/aula-11-diagrama-de-classes/README.md#4-agregação--composição) respondidas por escrito;
- [ ] **1 diagrama de sequência** de um dos casos de uso especificados, com a conferência mensagem ↔ passo do fluxo;
- [ ] **1 diagrama de estados ou de atividades**, com a **justificativa da escolha** — por que este e não o outro;
- [ ] Uma seção com **o que os diagramas não conseguem expressar** e onde essa informação vive.

### 5. Arquitetura

- [ ] **1 ADR completo** no formato da [Aula 14, §7](../bloco-4-projeto-de-software/aula-14-arquitetura-de-software/README.md#7-adr-registrar-a-decisão): contexto, decisão, **no mínimo três alternativas descartadas com motivo**, e consequências positivas **e negativas**;
- [ ] Um diagrama das **camadas** ou dos **componentes** do sistema, com a regra de dependência explícita.

### 6. Padrão de projeto

- [ ] **1 padrão aplicado**, com: o problema em uma frase, a evidência de que ele existe, o diagrama da solução e as consequências;
- [ ] A **alternativa sem padrão**, e por que ela perde;
- [ ] E a honestidade de dizer se ele era **mesmo necessário** — *"apliquei e, olhando agora, não valia a pena"* é uma resposta que vale nota cheia se estiver bem argumentada.

### 7. Plano de testes de aceite

- [ ] Mínimo de **8 casos de teste** derivados dos critérios de aceite, com pré-condição, passos e resultado esperado;
- [ ] Pelo menos **3** cobrindo caminho de exceção;
- [ ] Indicação de qual requisito ou regra cada caso verifica;
- [ ] Uma linha dizendo **qual regra você não conseguiu testar por aceite**, e por quê.

### 8. Processo

- [ ] Mínimo de **10 commits** distribuídos ao longo do desenvolvimento (não 10 no último dia);
- [ ] Mensagens de commit descritivas, em português;
- [ ] Todos os diagramas Mermaid **renderizando no GitHub** — conferidos na página, não só no editor.

## 📦 Estrutura do repositório

```
projeto-<seu-tema>/
├── README.md                 # a porta de entrada
├── 01-visao.md               # problema, interessados, escopo e o que ficou de fora
├── 02-requisitos.md          # RF, RNF, regras de negócio, glossário, questões em aberto
├── 03-casos-de-uso.md        # diagrama + as 3 especificações
├── 04-modelos.md             # classes + sequência + estados/atividades
├── 05-arquitetura.md         # ADR + camadas/componentes
├── 06-padrao.md              # o padrão aplicado e a alternativa
├── 07-testes-de-aceite.md    # o plano
└── diagramas/
    ├── casos-de-uso.puml
    └── casos-de-uso.svg
```

### O `README.md` precisa ter

- O que é o sistema, em **um parágrafo**, para quem nunca ouviu falar dele;
- O **diagrama de classes renderizado** (Mermaid direto no arquivo);
- Link para os demais arquivos, com uma linha dizendo o que cada um responde;
- **As três decisões de projeto de que você mais se orgulha**, cada uma com a alternativa que você descartou;
- Uma seção **"o que eu faria diferente"** — e ela precisa ser específica. "Melhoraria o modelo" não conta; "trataria finalidade como classe em vez de atributo, porque a instituição vai querer cadastrar novas" conta.

## 🌶️ Extras para ir além

- **C4 de contexto e contêineres**, com uma linha por contêiner dizendo por que ele existe separado;
- **Critérios de aceite em Gherkin**, em português, incluindo um cenário de exceção;
- **Matriz de rastreabilidade** ligando regra de negócio → requisito → critério → caso de teste;
- **Análise de dívida técnica antecipada**: escolha uma decisão sua que é um atalho consciente, registre-a como dívida com motivo, custo e condição de quitação;
- **Um segundo ADR** sobre uma decisão que você tomou e depois reverteu — com o ADR novo substituindo o antigo, como manda a Aula 14.

## 📤 Entrega

Repositório público, mais uma **demonstração de 5 minutos** (ao vivo ou gravada) mostrando:

1. O problema, em 30 segundos, para quem nunca ouviu falar dele;
2. **Uma decisão** que você tomou e a alternativa que descartou — com o motivo;
3. Um caso de uso especificado, focando nos **fluxos de exceção**;
4. O ADR, e por que aquela decisão é arquitetural e não detalhe;
5. **Um ponto do seu projeto que você sabe que está fraco** — e o que faria com mais tempo. Este item não é opcional: é onde se vê que você avalia o próprio trabalho.

## 🧭 Como isso é avaliado

Em ordem de peso:

1. **A justificativa das decisões** — um projeto mediano bem defendido vale mais que um projeto ótimo sem argumento. É o critério que atravessa o curso inteiro;
2. **Coerência entre as sete partes** — requisitos, casos de uso, classes, arquitetura e testes precisam contar a **mesma** história. Um caso de uso que menciona um conceito ausente do diagrama de classes reprova por incoerência, mesmo que os dois estejam bons isoladamente;
3. **Fidelidade ao domínio** — o modelo representa o problema que você descreveu, inclusive nas partes chatas;
4. **Tratamento das exceções** — o caminho feliz é a parte fácil; o que se avalia é o que acontece quando dá errado;
5. **Honestidade sobre os limites** — o que ficou de fora, o que não deu para testar, o que você faria diferente.

> 📏 **O critério que resume tudo:** uma pessoa que nunca viu o seu tema consegue ler o repositório, entender o domínio, discordar de uma decisão sua **com argumento** e saber exatamente onde o sistema quebraria se ela estivesse certa? Se sim, o dossiê está pronto.

---

🏠 [Voltar ao início](../README.md)
