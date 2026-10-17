# 🔗 Links Úteis — Projeto de Software

> A **bibliografia** do curso está no [README](../README.md#-bibliografia), com os três livros-base e as obras de apoio. Esta página é o resto: o que está **online**, e serve para consultar durante a aula.

## 🧭 Processos e agilidade

- [Manifesto Ágil — versão em português](https://agilemanifesto.org/iso/ptbr/manifesto.html) — quatro valores, 68 palavras. Leia o original antes de aceitar qualquer interpretação de terceiros;
- [Os 12 princípios por trás do Manifesto](https://agilemanifesto.org/iso/ptbr/principles.html) — mais úteis que os valores para decidir o que fazer na segunda-feira, e é a Aula 05 inteira;
- [Guia do Scrum](https://scrumguides.org/) — o guia oficial, com tradução para o português na [página de downloads](https://scrumguides.org/download.html). São 13 páginas, e todo o resto que existe sobre Scrum é comentário sobre elas;
- [Kanban Guide](https://kanbanguides.org/) — a definição enxuta de fluxo, limite de trabalho em andamento e métricas;
- [Agile Alliance — mapa de práticas](https://www.agilealliance.org/agile101/subway-map-to-agile-practices/) — cada prática com uma página explicando quando ela faz sentido.

## 📋 Gestão, risco e qualidade

- [PMI — Project Management Institute](https://www.pmi.org/) — a instituição por trás do PMBOK; a seção de padrões diz o que cada publicação cobre;
- [ISO 21500 — orientação sobre gerenciamento de projetos](https://www.iso.org/standard/75704.html) — a norma internacional, útil para ver que os grupos de processo não são invenção de uma instituição só;
- [Design Thinking — Interaction Design Foundation](https://www.interaction-design.org/literature/topics/design-thinking) — as cinco etapas explicadas com exemplos, em inglês acessível;
- [Lean Enterprise Institute](https://www.lean.org/explore-lean/what-is-lean/) — valor, fluxo e desperdício na origem, sem o folclore de consultoria.

## 📐 Artefatos e diagramas

- [Mermaid — documentação](https://mermaid.js.org/intro/) — a sintaxe que usamos no repositório. As páginas de [fluxograma](https://mermaid.js.org/syntax/flowchart.html), [Gantt](https://mermaid.js.org/syntax/gantt.html) e [estados](https://mermaid.js.org/syntax/stateDiagram.html) resolvem o curso inteiro;
- [mermaid.live](https://mermaid.live) — editor online, mostra o erro de sintaxe na hora. **Depure aqui antes de commitar**;
- [Guia de artefatos de gestão do curso](artefatos-de-gestao.md) — RACI, EAP, Gantt, matriz de risco, quadro Kanban e burndown, com um exemplo pronto de cada.

## 🌿 Versão e configuração (Aula 09)

- [Pro Git, em português](https://git-scm.com/book/pt-br/v2) — o livro oficial do Git, gratuito. Os capítulos 2 e 3 (o básico e as ramificações) bastam para a aula;
- [Versionamento Semântico 2.0.0](https://semver.org/lang/pt-BR/) — a especificação inteira cabe numa página, em português;
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/) — a convenção de mensagem de commit que liga `feat` e `fix` ao número de versão;
- [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) — o formato de CHANGELOG que a aula usa, com as seis categorias de mudança;
- [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/) — o texto original do GitFlow, de 2010. Leia primeiro a **nota de 2020** no topo, em que o próprio autor diz para quem o modelo não serve;
- [Trunk-based development — DORA](https://dora.dev/capabilities/trunk-based-development/) e [trunkbaseddevelopment.com](https://trunkbaseddevelopment.com/) — a pesquisa por trás dos ramos curtos, e o guia prático;
- [The Twelve-Factor App — Configurações](https://12factor.net/pt_br/config) — por que configuração e segredo não moram no código;
- [GitHub — proteção de push](https://docs.github.com/pt/code-security/secret-scanning/introduction/about-push-protection) — o bloqueio que impede um segredo de chegar ao repositório público.

## 🔁 Integração contínua (Aula 10)

- [Continuous Integration, por Martin Fowler](https://martinfowler.com/articles/continuousIntegration.html) — o texto de referência da prática, de 2000, revisto em 2024. A lista das onze práticas cabe numa tela;
- [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) — a pirâmide de testes explicada nível por nível, com exemplos de código, por Ham Vocke;
- [Continuous integration — DORA](https://dora.dev/capabilities/continuous-integration/) — o que a pesquisa encontrou sobre integração contínua e como medir se o time pratica;
- [Code Coverage Best Practices — Google Testing Blog](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html) — por que não existe número ideal de cobertura, e como usá-la sem virar meta;
- [Flaky Tests at Google and How We Mitigate Them](https://testing.googleblog.com/2016/05/flaky-tests-at-google-and-how-we.html) — de onde vêm os 16% de testes instáveis da aula;
- [GitHub Actions — fortalecimento de segurança](https://docs.github.com/pt/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions) — fixar componentes pelo hash, permissão mínima e segredos no pipeline, em português.

## 🚦 Entrega e implantação contínuas (Aula 11)

- [Continuous Delivery, por Martin Fowler](https://martinfowler.com/bliki/ContinuousDelivery.html) — uma página, com a diferença entre entrega contínua e implantação contínua;
- [Blue-Green Deployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) e [Canary Release](https://martinfowler.com/bliki/CanaryRelease.html) — as duas estratégias da aula, com o problema do banco de dados em cada uma;
- [Parallel Change](https://martinfowler.com/bliki/ParallelChange.html) — o expandir e contrair, passo a passo;
- [Relatório da CrowdStrike sobre 19/07/2024](https://www.crowdstrike.com/en-us/blog/falcon-content-update-preliminary-post-incident-report/) — o caso da seção 3, contado por quem errou, com as medidas que vieram depois;
- [Relatório do Google Cloud sobre 12/06/2025](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW) — o caso da flag que faltou, com os compromissos do Google;
- [Site Reliability Engineering — introdução](https://sre.google/sre-book/introduction/) — o livro de SRE do Google, gratuito, de onde vêm os 70% de interrupções causadas por mudança.

## 🔭 Operação: observabilidade e manutenção (Aula 12)

- [Site Reliability Engineering — o livro inteiro](https://sre.google/sre-book/table-of-contents/) — gratuito. Para a aula: capítulos 4 (SLO), 6 (monitoramento e os quatro sinais de ouro), 14 (incidentes) e 15 (postmortem sem culpa);
- [Postmortem do GitLab de 31/01/2017](https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/) — o caso da seção 5, com os backups que falhavam em silêncio, contado por quem errou;
- [Blameless PostMortems and a Just Culture, por John Allspaw](https://www.etsy.com/codeascraft/blameless-postmortems) — por que procurar culpado faz o próximo incidente demorar mais;
- [OpenTelemetry — documentação](https://opentelemetry.io/pt/docs/) — o padrão aberto para emitir logs, métricas e rastros, com parte em português;
- [Technical Debt Quadrant, por Martin Fowler](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) — a dívida deliberada e a inadvertida, a prudente e a imprudente.

## 🚀 Entrega, operação e usuário

- [DORA — pesquisa e métricas](https://dora.dev/) — as métricas de desempenho de entrega (frequência de implantação, tempo de espera da mudança, taxa de falha, tempo de recuperação e, desde 2024, taxa de retrabalho) e os relatórios *State of DevOps*. É a fonte das Aulas 10 e 11 e da leitura *Qualidade que se mede*;
- [Feature Toggles, por Pete Hodgson](https://martinfowler.com/articles/feature-toggles.html) — o artigo de referência sobre *feature flags*, com os tipos e o custo de cada um;
- [GitHub Actions — documentação](https://docs.github.com/pt/actions) — se você quiser ver uma esteira de CI de verdade rodando, é o caminho mais barato, e está em português;
- [Nielsen Norman Group — as 10 heurísticas de usabilidade](https://www.nngroup.com/articles/ten-usability-heuristics/) — a base da leitura *O usuário do outro lado*, e a lista que pega a maior parte dos problemas de interface;
- [WCAG — diretrizes de acessibilidade (W3C)](https://www.w3.org/WAI/standards-guidelines/wcag/) e [eMAG — modelo brasileiro para governo](https://emag.governoeletronico.gov.br/) — de onde saem os requisitos de acessibilidade que ninguém pede e todo mundo precisa.

## 🏛️ Governança

- [ITIL — página oficial da AXELOS](https://www.axelos.com/certifications/itil-service-management) — o que o ITIL cobre, e por que ele é sobre **serviço** e não sobre projeto;
- [COBIT — ISACA](https://www.isaca.org/resources/cobit) — objetivos de governança e de gestão, e o que uma auditoria de TI procura;
- [Pacto Global da ONU — os princípios](https://www.pactoglobal.org.br/os-10-principios) — a origem da agenda que hoje se chama ESG;
- [LGPD — Lei nº 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) — o texto da lei; os artigos 5º, 7º e 11 são os que aparecem em decisão de projeto;
- [ANPD — Autoridade Nacional de Proteção de Dados](https://www.gov.br/anpd/pt-br) — guias orientativos em linguagem menos jurídica.

## 🎓 Materiais do curso

- [Curso de Git e GitHub](https://github.com/jreluiz/curso-git-github) — **pré-requisito**;
- [Curso de POO com Java](https://github.com/jreluiz/curso-java-poo) — o correquisito; os blocos `> 🧩 Ponte com POO` apontam para lá;
- [Curso de Modelagem de Dados](https://github.com/jreluiz/curso-modelagem-dados) — o passo seguinte, quando o projeto virar banco de dados;
- [Projetos para praticar](projetos-para-praticar.md) · [Artefatos de gestão](artefatos-de-gestao.md) · [Erros comuns](erros-comuns.md) · [Glossário](glossario.md) · [Preparação do ambiente](ambiente.md).

---

🏠 [Voltar ao início](../README.md)
