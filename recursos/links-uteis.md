# 🔗 Links Úteis — Projeto de Software

## 📖 Referência (para consultar, não para ler de capa a capa)

- **SOMMERVILLE, Ian. *Engenharia de Software*. 10. ed. São Paulo: Pearson** — o livro dos Blocos 1 e 2: processos, agilidade e requisitos. O [site do autor](https://software-engineering-book.com/) tem os slides e o material de apoio das 10 edições, em inglês;
- **BEZERRA, Eduardo. *Princípios de Análise e Projeto de Sistemas com UML*. 3. ed. Rio de Janeiro: Elsevier** — o livro dos Blocos 3 e 4: UML e projeto orientado a objetos, escrito em português e no nível certo para quem está começando;
- [UML — especificação oficial (OMG)](https://www.omg.org/spec/UML/) — a fonte, para quando alguém discordar do significado de um símbolo. Densa: use como dicionário, nunca como leitura;
- [Glossário PT/EN do curso](glossario.md) — para não travar por vocabulário na literatura em inglês.

## 🧭 Processos e agilidade

- [Manifesto Ágil — versão em português](https://agilemanifesto.org/iso/ptbr/manifesto.html) — quatro valores, 68 palavras. Leia o original antes de aceitar qualquer interpretação de terceiros;
- [Os 12 princípios por trás do Manifesto](https://agilemanifesto.org/iso/ptbr/principles.html) — mais úteis que os valores para decidir o que fazer na segunda-feira;
- [Scrum Guide](https://scrumguides.org/) — o guia oficial, com tradução para o português na [página de downloads](https://scrumguides.org/download.html). São 13 páginas, e todo o resto que existe sobre Scrum é comentário sobre elas;
- [Kanban Guide](https://kanbanguides.org/) — a definição enxuta de fluxo, WIP e métricas;
- [Agile Alliance — glossário de práticas](https://www.agilealliance.org/agile101/subway-map-to-agile-practices/) — mapa das práticas ágeis, cada uma com uma página explicando quando faz sentido.

## 📋 Requisitos

- [INVEST in Good Stories, and SMART Tasks](https://xp123.com/invest-in-good-stories-and-smart-tasks/) — o artigo de Bill Wake que criou o acrônimo INVEST. Curto e bem escrito;
- [Gherkin — referência da sintaxe (Cucumber)](https://cucumber.io/docs/gherkin/reference/) — `Dado / Quando / Então` com todos os detalhes; o Gherkin aceita palavras-chave em português;
- [LGPD — Lei nº 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) — o texto da lei. Os artigos 5º (definições), 7º e 11 (bases legais) são os que aparecem em requisito;
- [ANPD — Autoridade Nacional de Proteção de Dados](https://www.gov.br/anpd/pt-br) — guias orientativos em linguagem menos jurídica;
- [WCAG — diretrizes de acessibilidade (W3C)](https://www.w3.org/WAI/standards-guidelines/wcag/) e [eMAG — modelo brasileiro para governo](https://emag.governoeletronico.gov.br/) — de onde saem os requisitos de acessibilidade que ninguém pede e todo mundo precisa.

## 📐 Diagramas e notações

- [Mermaid — documentação](https://mermaid.js.org/intro/) — a sintaxe que usamos no repositório. As páginas de [classes](https://mermaid.js.org/syntax/classDiagram.html), [sequência](https://mermaid.js.org/syntax/sequenceDiagram.html), [estados](https://mermaid.js.org/syntax/stateDiagram.html) e [fluxograma](https://mermaid.js.org/syntax/flowchart.html) resolvem 100% do curso;
- [mermaid.live](https://mermaid.live) — editor online, mostra o erro de sintaxe na hora. **Depure aqui antes de commitar**;
- [PlantUML — diagrama de casos de uso](https://plantuml.com/use-case-diagram) — a documentação da única ferramenta não-Mermaid do curso; está em inglês, mas é quase toda exemplo de código;
- [PlantUML Web Server](https://www.plantuml.com/plantuml/uml/) — cole o código, exporte o `.svg`, sem instalar nada;
- [Guia de notações do curso](notacoes-uml.md) — qual diagrama em qual ferramenta, com um exemplo pronto de cada.

## 🏛️ Arquitetura e projeto

- [c4model.com](https://c4model.com/) — o modelo C4 explicado pelo autor, com exemplos dos quatro níveis. Leia pelo menos Contexto e Contêineres;
- [adr.github.io](https://adr.github.io/) — o que é um Architecture Decision Record, com modelos prontos de várias famílias. O de Michael Nygard é o mais usado e cabe em meia página;
- [Refactoring Guru — Padrões de Projeto (em português)](https://refactoring.guru/pt-br/design-patterns) — o catálogo GoF com diagrama, exemplo de código e, o que importa mais, **quando não usar**;
- [Refactoring Guru — Código com mau cheiro](https://refactoring.guru/pt-br/refactoring/smells) — o catálogo de sintomas que antecede a refatoração;
- [martinfowler.com/bliki](https://martinfowler.com/bliki/) — verbetes curtos sobre projeto, arquitetura e processo. Comece por [Technical Debt](https://martinfowler.com/bliki/TechnicalDebt.html) e [Microservice Premium](https://martinfowler.com/bliki/MicroservicePremium.html) — o segundo é o antídoto contra microsserviço por moda;
- [The Twelve-Factor App (em português)](https://12factor.net/pt_br/) — doze restrições de projeto para aplicação que roda em servidor. Curto e ainda atual.

## 🚀 Entrega e DevOps

- [DORA — pesquisa e métricas](https://dora.dev/) — as quatro métricas (frequência de implantação, tempo de espera, tempo de restauração, taxa de falha) e os relatórios *State of DevOps*;
- [Feature Toggles, por Pete Hodgson](https://martinfowler.com/articles/feature-toggles.html) — o artigo de referência sobre *feature flags*, com os tipos e o custo de cada um;
- [GitHub Actions — documentação](https://docs.github.com/pt/actions) — se você quiser ver uma esteira de CI de verdade rodando, é o caminho mais barato (e está em português).

## 🎓 Materiais do curso

- [Curso de Git e GitHub](https://github.com/jreluiz/curso-git-github) — **pré-requisito**;
- [Curso de POO com Java](https://github.com/jreluiz/curso-java-poo) — o correquisito; os blocos `> 🧩 Ponte com POO` apontam para lá;
- [Curso de Modelagem de Dados](https://github.com/jreluiz/curso-modelagem-dados) — o passo seguinte quando o diagrama de classes virar banco de dados;
- [Sistema-guia: Reserva de Espaços](sistema-guia.md) · [Erros comuns](erros-comuns.md) · [Sistemas para praticar](sistemas-para-praticar.md) · [Notações UML](notacoes-uml.md) · [Glossário](glossario.md) · [Preparação do ambiente](ambiente.md).

---

🏠 [Voltar ao início](../README.md)
