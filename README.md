# 🏗️ Curso de Projeto de Software

> 📋 Pré-requisito: [Curso de Git e GitHub](https://github.com/jreluiz/curso-git-github) concluído.
> 🎒 Não é preciso saber programar. Aqui não se escreve código — escreve-se a decisão que vem antes dele, e se entende o caminho que ele percorre até chegar ao usuário.

Software que dá errado raramente dá errado na hora de programar. Dá errado antes: no prazo que ninguém recalculou, no risco que não tinha dono, na decisão que duas pessoas achavam que a outra ia tomar. Este curso é sobre esse "antes" — e, no último bloco, sobre o caminho do código até a produção, que é onde a mudança mal controlada custa mais caro.

## 🎯 Objetivos do curso

Ao final do curso, você será capaz de:

- Distinguir **projeto de operação** e reconhecer as causas recorrentes de fracasso de um projeto de software;
- Montar uma **matriz de responsabilidades** em que cada decisão tem exatamente um responsável;
- Escolher o **ciclo de vida** de um projeto — clássico, incremental, iterativo — e situá-lo no eixo preditivo–adaptativo, defendendo a escolha;
- Percorrer os **cinco grupos de processo**: escrever um termo de abertura, decompor o escopo em EAP, controlar contra a linha de base e encerrar com aceite e lições aprendidas;
- Conduzir um projeto com **Scrum**, sabendo o que cada responsabilidade decide e o que cada evento produz;
- Usar **Design Thinking, MVP e Lean** onde cada um serve — e reconhecer o "MVP" que é só a primeira fatia do plano;
- Controlar **versão e configuração**: dizer o que entra no repositório, escolher a estratégia de ramificação e numerar versões que significam alguma coisa;
- Explicar o que um **pipeline de integração contínua** verifica a cada mudança, e por que a qualidade do código se mede ali;
- Distinguir **entrega contínua de implantação contínua** e escolher como implantar uma mudança arriscada — canário, *blue-green* ou *feature flag*;
- Acompanhar o sistema **depois que ele sobe**: logs, métricas e rastros, objetivos de nível de serviço, incidente com postmortem e os quatro tipos de manutenção;
- Nas **leituras complementares**, aprofundar risco, métricas, documentação, comunicação, experiência do usuário e governança — os tópicos da ementa sem aula própria;
- Trabalhar como um profissional: todo artefato versionado com Git e justificado por escrito.

> 📏 **A competência central do curso não é preencher artefato.** É decidir entre alternativas e sustentar a decisão por escrito. Em gestão de projeto, `"depende"` é uma resposta legítima — desde que você complete a frase: *depende de quê*.

## 🗺️ Plano de aulas

### Bloco 1 — Fundamentos de projetos de software

| Aula | Tema | Conteúdo |
|:---:|------|----------|
| 01 | [Por que gerir um projeto de software](bloco-1-fundamentos-de-projetos/aula-01-por-que-gerir-um-projeto/README.md) | Projeto × operação, por que projetos falham, conflitos, papéis, matriz RACI |
| 02 | [Ciclos de vida](bloco-1-fundamentos-de-projetos/aula-02-ciclos-de-vida/README.md) | Clássico, incremental, iterativo, o eixo preditivo–adaptativo e o híbrido |
| 03 | [Os processos de um projeto](bloco-1-fundamentos-de-projetos/aula-03-os-processos-de-um-projeto/README.md) | Os cinco grupos, termo de abertura, EAP, linha de base, encerramento |
| 04 | [Arquitetura como decisão de projeto](bloco-1-fundamentos-de-projetos/aula-04-arquitetura-como-decisao/README.md) | O que é arquitetura, camadas, monolito × microsserviços, ADR |

### Bloco 2 — Metodologias em gestão de projeto

| Aula | Tema | Conteúdo |
|:---:|------|----------|
| 05 | [O Manifesto Ágil, lido devagar](bloco-2-metodologias-de-gestao/aula-05-manifesto-agil/README.md) | Os quatro valores, os doze princípios, o que o Manifesto não diz, o ágil teatral |
| 06 | [Scrum](bloco-2-metodologias-de-gestao/aula-06-scrum/README.md) | As três responsabilidades, os cinco eventos, os três artefatos e seus compromissos |
| 07 | [Quem responde pelo quê](bloco-2-metodologias-de-gestao/aula-07-quem-responde-pelo-que/README.md) | Gerente de projeto, Product Owner, stakeholders e a matriz poder × interesse |
| 08 | [Descobrir, enxugar, melhorar](bloco-2-metodologias-de-gestao/aula-08-design-thinking-mvp-lean/README.md) | Design Thinking, MVP com hipótese, Lean e Six Sigma — e quando usar cada um |

### Bloco 3 — Do código à produção

| Aula | Tema | Conteúdo |
|:---:|------|----------|
| 09 | [Controle de versão e configuração](bloco-3-do-codigo-a-producao/aula-09-controle-de-versao-e-configuracao/README.md) | Item de configuração e baseline, estratégias de ramificação, versionamento semântico, release e CHANGELOG |
| 10 | [Integração contínua](bloco-3-do-codigo-a-producao/aula-10-integracao-continua/README.md) | Integrar todo dia, o build reproduzível, o pipeline e a pirâmide de testes, a verificação que barra a mudança e a métrica que vira meta |
| 11 | [Entrega e implantação contínuas](bloco-3-do-codigo-a-producao/aula-11-entrega-e-implantacao-continuas/README.md) | Entrega × implantação contínua, ambientes, o raio da explosão, implantação direta, gradual, azul-verde e canário, *feature flags* e as métricas DORA |
| 12 | [Operação: observabilidade e manutenção](bloco-3-do-codigo-a-producao/aula-12-observabilidade-e-manutencao/README.md) | Logs, métricas e rastros, SLO e orçamento de erro, incidente e postmortem sem culpa, os quatro tipos de manutenção e a dívida técnica |

### 📚 Leituras complementares

Os tópicos da ementa que não têm aula própria, no mesmo formato das aulas, para ler no seu ritmo — [ver o índice](leituras-complementares/README.md).

| Leitura | Conteúdo |
|---|---|
| [Risco](leituras-complementares/risco/README.md) | Risco × problema, causa–evento–efeito, matriz probabilidade × impacto, as quatro respostas |
| [Qualidade que se mede](leituras-complementares/qualidade-que-se-mede/README.md) | Verificação × validação, sistema de qualidade, métricas, maturidade |
| [Documentação](leituras-complementares/documentacao/README.md) | Por que e quando documentar, documentação como qualidade, o custo da ausência |
| [Ferramentas e comunicação](leituras-complementares/ferramentas-e-comunicacao/README.md) | EAP, Gantt e marco; backlog, quadro e burndown; WIP; plano de comunicação |
| [O usuário do outro lado](leituras-complementares/o-usuario-do-outro-lado/README.md) | Análise e projeto de interface, UX × UI, projeto de interação, acessibilidade |
| [Governança](leituras-complementares/governanca/README.md) | Governança de TI, PMI e PMBOK, ITIL, COBIT, ESG e o mapa do curso |

## 🏢 Os projetos das aulas

**Não há um sistema-guia único.** Cada aula trabalha um projeto do catálogo [`recursos/projetos-para-praticar.md`](recursos/projetos-para-praticar.md) — doze contextos com prazo, equipe, orçamento e as tensões que dão o que discutir.

Cada bloco ancora em dois deles, para que você não precise ler um cenário novo a cada exercício:

| Bloco | Projetos-âncora |
|---|---|
| **1 — Fundamentos** | Empréstimo de equipamentos · Ouvidoria municipal |
| **2 — Metodologias** | Achados e perdidos do campus · Marketplace de serviços autônomos |
| **3 — Do código à produção** | Delivery de restaurante · Prontuário de clínica-escola |

Todo contexto de que você precisa vem **no enunciado do exercício**. Nenhum exercício manda você "considerar um sistema qualquer".

## 📝 Como você é avaliado

| Instrumento | O que é |
|---|---|
| **Exercícios em sala** | 5 por aula nas Aulas 01–08 e 3 nas Aulas 09–12, feitos e discutidos na aula, entregues no seu repositório |
| **Revisão** | 8 questões por aula, para conferir se o conceito ficou |

O **último exercício de cada aula é o Desafio 🌶️**, e ele é sempre o mesmo tipo de tarefa: defender uma decisão por escrito, com as alternativas que você descartou e **o que se perde** com a sua escolha. É o exercício que mais se parece com o trabalho real.

## 🔁 O ritual Git de toda aula

**Toda aula começa e termina com Git.** Sem exceção:

```bash
# ── Início da aula ──
cd exercicios-projeto-software
git pull                                  # atualiza (se você usa mais de um PC)

# ── Durante a aula ──
mkdir aula-XX-tema && cd aula-XX-tema      # uma pasta por aula
# ... lê o caso, decide, monta o artefato, escreve a justificativa ...
git add .
git commit -m "Resolve exercícios da aula XX"   # commit por exercício concluído

# ── Fim da aula (OBRIGATÓRIO) ──
git push                                   # sem push = sem entrega!
```

> 📏 **Regra do curso (e do mercado):** todo artefato vem acompanhado da **justificativa por escrito**. Uma matriz bem preenchida com a decisão errada dentro não vale nada — e a justificativa é o que permite descobrir isso antes.

## 🛠️ Ambiente

Consulte o [guia de preparação do ambiente](recursos/ambiente.md). O resumo é curto: **um editor de texto e o seu repositório de exercícios**. Os artefatos são escritos em tabela Markdown ou em [Mermaid](https://mermaid.js.org/), que o GitHub renderiza sozinho. **Nada a instalar.**

## 🤝 Fazendo POO em paralelo?

Provavelmente sim, e o curso conta com isso — mas **não depende disso**. Onde um assunto daqui encosta no código do outro curso, aparece um bloco assim:

> 🧩 **Ponte com POO:** o que você está vendo lá, com o nome que ele tem aqui.

Esses blocos são **opcionais** e raros. Nenhuma aula deixa de fazer sentido sem eles.

## ⚡ Links rápidos

- 📅 [Cronograma da turma 2026/2](CRONOGRAMA.md) — as datas dos encontros, se você está cursando isto numa turma
- 📚 [Leituras complementares](leituras-complementares/README.md) — os seis tópicos da ementa sem aula própria
- 🏢 [Projetos para praticar](recursos/projetos-para-praticar.md) — os 12 contextos que abastecem os exercícios
- 📐 [Artefatos de gestão](recursos/artefatos-de-gestao.md) — RACI, EAP, Gantt, matriz de risco e quadro Kanban, em Mermaid ou tabela
- 🧯 [Erros comuns](recursos/erros-comuns.md) — 35 patologias de gestão, com sintoma, causa e cura
- 📚 [Glossário PT/EN](recursos/glossario.md) — para não travar por vocabulário na literatura em inglês
- 🔗 [Links úteis](recursos/links-uteis.md)
- 📖 [Curso de Git e GitHub](https://github.com/jreluiz/curso-git-github) (pré-requisito)

## 📚 Bibliografia

**Livros-base — são três, uma literatura por natureza de assunto:**

| Obra | Onde ela é a referência |
|---|---|
| SOMMERVILLE, Ian. **Engenharia de Software**. 10. ed. São Paulo: Pearson. | **Blocos 1 e 3** — processos, ciclos de vida, arquitetura, gerência de configuração, entrega e evolução |
| CRUZ, Fábio. **Scrum e Agile em Projetos: guia completo**. 2. ed. Rio de Janeiro: Brasport, 2018. | **Bloco 2** — Manifesto, valores e princípios, Scrum inteiro e o conjunto de técnicas ágeis |
| PMI. **Um guia do conhecimento em gerenciamento de projetos (Guia PMBOK)**. 6. ed. Newtown Square: PMI, 2017. | **Leituras complementares** — risco, qualidade e comunicação são áreas de conhecimento dele |

**Bibliografia de apoio:**

| Obra | Onde ela ajuda mais |
|---|---|
| PRESSMAN, Roger S.; MAXIM, Bruce R. **Engenharia de software: uma abordagem profissional**. 9. ed. Porto Alegre: AMGH, 2021. | Bloco 1 e leituras complementares — a segunda opinião sobre processos e qualidade; onde o Sommerville é conciso, ele é detalhista |
| MARTIN, Robert C. **Arquitetura limpa: o guia do artesão para estrutura e design de software**. Rio de Janeiro: Alta Books, 2019. | Aula 04 — fronteiras entre partes do sistema e o custo de atravessá-las |
| SUTHERLAND, Jeff. **Scrum: a arte de fazer o dobro do trabalho na metade do tempo**. Rio de Janeiro: Sextante, 2016. | Bloco 2 — de onde o Scrum veio, contado por quem o criou |
| HUMBLE, Jez; FARLEY, David. **Continuous delivery: reliable software releases through build, test, and deployment automation**. Upper Saddle River: Addison-Wesley, 2010. | **Bloco 3** — o livro que deu nome à entrega contínua: pipeline, ambientes e gerência de configuração. Há edição em português pela Bookman, *Entrega contínua* |
| KIM, Gene; HUMBLE, Jez; DEBOIS, Patrick; WILLIS, John. **The DevOps handbook**. Portland: IT Revolution, 2016. | **Bloco 3** — fluxo, retorno rápido e aprendizado contínuo, com casos de empresas. Em português: *Manual de DevOps*, Alta Books |
| FORSGREN, Nicole; HUMBLE, Jez; KIM, Gene. **Accelerate: the science of lean software and DevOps**. Portland: IT Revolution, 2018. | Aulas 10 e 11 — a pesquisa por trás das métricas DORA |
| BEYER, Betsy et al. (org.). **Site reliability engineering: how Google runs production systems**. Sebastopol: O'Reilly, 2016. | Aula 12 — SLO, orçamento de erro e postmortem sem culpa. Em português: *Engenharia de confiabilidade do Google*, Novatec |
| CHACON, Scott; STRAUB, Ben. **Pro Git**. 2. ed. New York: Apress, 2014. | Aula 09 — o Git por dentro; gratuito e traduzido |
| ISACA. **COBIT 2019: framework — governance and management objectives**. Schaumburg: ISACA, 2018. | Leitura *Governança* — o que a governança de TI cobra, e o que a auditoria procura |
| AXELOS. **ITIL Foundation: ITIL 4 edition**. Norwich: TSO, 2019. | Leitura *Governança* — a diferença entre gerir projeto e gerir serviço |

> ⚠️ **O Guia PMBOK é norma de consulta, não leitura linear.** Ninguém lê as 750 páginas dele. As referências `> 📖` das leituras complementares apontam a **área de conhecimento**, e o texto continua autocontido.

**O que é gratuito e vale abrir agora:** o [Manifesto Ágil em português](https://agilemanifesto.org/iso/ptbr/manifesto.html) — quatro valores e doze princípios, e a Aula 05 discute cada um —, o [Guia do Scrum](https://scrumguides.org/download.html), o relatório [State of DevOps](https://dora.dev/), de onde saem as métricas DORA das Aulas 10 e 11, o livro [Pro Git em português](https://git-scm.com/book/pt-br/v2), da Aula 09, e o [livro de SRE do Google](https://sre.google/books/), da Aula 12.

As aulas marcam com `> 📖` onde aprofundar cada tema. **O curso é autocontido** — os livros são o passo seguinte, não um pré-requisito.

---

*Este repositório continua evoluindo — material novo é commitado aqui. Primeiro passo de toda sessão de estudo: `git pull`.* 🙂
