# 🏗️ Curso de Projeto de Software

> 📋 Pré-requisito: [Curso de Git e GitHub](https://github.com/jreluiz/curso-git-github) concluído.
> 🎒 Não é preciso saber programar. Aqui não se escreve código — escreve-se a decisão que vem antes do código.

Software que dá errado raramente dá errado na hora de programar. Dá errado antes: no requisito que ninguém entendeu igual, na classe que faz coisas demais, na arquitetura escolhida por moda. Este curso é sobre esse "antes".

## 🎯 Objetivos do curso

Ao final do curso, você será capaz de:

- Explicar **por que existe uma engenharia em volta do código** e o que muda quando um programa vira produto de software;
- Escolher um **modelo de processo** para um contexto concreto — e defender a escolha, inclusive quando a resposta certa for cascata;
- Trabalhar com **desenvolvimento ágil** sem confundir agilidade com ausência de processo;
- **Elicitar, especificar, priorizar e validar requisitos** funcionais e não-funcionais, entregando um documento que outra pessoa consegue usar;
- Ler e escrever os **cinco diagramas UML que se usam de verdade**: casos de uso, classes, sequência, atividades e estados;
- Avaliar um projeto por **coesão e acoplamento**, aplicar princípios de bom projeto e reconhecer os **padrões** que resolvem problemas recorrentes;
- Registrar uma **decisão de arquitetura** e as alternativas que você descartou — com o motivo;
- Trabalhar como um profissional: todo artefato versionado com Git e revisado via GitHub.

> 📏 **A competência central do curso não é desenhar.** É decidir entre alternativas e sustentar a decisão por escrito. Em projeto de software, `"depende"` é uma resposta legítima — desde que você complete a frase: *depende de quê*.

## 🗺️ Plano de aulas

### Bloco 1 — Software, processos e agilidade

| Aula | Tema | Conteúdo |
|:---:|------|----------|
| 01 | [Por que engenharia de software existe](bloco-1-software-e-processos/aula-01-por-que-engenharia-de-software/README.md) | Programa × produto, por que projetos falham, custo da mudança, atributos de qualidade, papéis |
| 02 | [Ciclo de vida e modelos de processo](bloco-1-software-e-processos/aula-02-ciclo-de-vida-e-processos/README.md) | As 4 atividades fundamentais, cascata, incremental, iterativo, dirigido a plano × ágil |
| 03 | [Desenvolvimento ágil](bloco-1-software-e-processos/aula-03-desenvolvimento-agil/README.md) | Manifesto, Scrum, Kanban e WIP, práticas do XP, o ágil teatral |
| 04 | [Como o software chega ao usuário](bloco-1-software-e-processos/aula-04-entrega-continua-e-devops/README.md) | Integração contínua, pipeline, entrega × implantação, DevOps, métricas DORA, *feature flag* |

### Bloco 2 — Requisitos

| Aula | Tema | Conteúdo |
|:---:|------|----------|
| 05 | [O que é um requisito](bloco-2-requisitos/aula-05-o-que-e-um-requisito/README.md) | Funcional × não-funcional, LGPD e acessibilidade, stakeholders, requisito × solução |
| 06 | [Elicitação](bloco-2-requisitos/aula-06-elicitacao/README.md) | Entrevista, observação, análise de documentos, workshop, prototipação |
| 07 | [Especificação: documento e histórias](bloco-2-requisitos/aula-07-especificacao-e-historias/README.md) | História de usuário, INVEST, critérios de aceite, BDD e Gherkin, regras de negócio |
| 08 | [Análise, priorização e validação](bloco-2-requisitos/aula-08-analise-priorizacao-validacao/README.md) | Ambiguidade, MoSCoW, esforço × valor, backlog, rastreabilidade, mudança de escopo |

### Bloco 3 — Modelagem e UML

| Aula | Tema | Conteúdo |
|:---:|------|----------|
| 09 | [Por que modelar e o que é UML](bloco-3-modelagem-e-uml/aula-09-por-que-modelar-e-uml/README.md) | Modelo × realidade, os 14 diagramas e os 5 que importam, quanto UML é suficiente |
| 10 | [Casos de uso](bloco-3-modelagem-e-uml/aula-10-casos-de-uso/README.md) | Ator e fronteira, `include`/`extend`, a especificação textual dos três fluxos, granularidade |
| 11 | [Diagrama de classes](bloco-3-modelagem-e-uml/aula-11-diagrama-de-classes/README.md) | Visibilidade, associação e multiplicidade, agregação × composição, herança, análise × projeto |
| 12 | [Modelagem dinâmica](bloco-3-modelagem-e-uml/aula-12-modelagem-dinamica/README.md) | Sequência, atividades e estados — e qual usar para qual pergunta |

### Bloco 4 — Projeto de software

| Aula | Tema | Conteúdo |
|:---:|------|----------|
| 13 | [Princípios de bom projeto](bloco-4-projeto-de-software/aula-13-principios-de-projeto/README.md) | Coesão, acoplamento, separação de responsabilidades, SOLID em dose gentil |
| 14 | [Arquitetura de software](bloco-4-projeto-de-software/aula-14-arquitetura-de-software/README.md) | Camadas, MVC, monolito × microsserviços, componentes e implantação, C4, ADR |
| 15 | [Padrões de projeto](bloco-4-projeto-de-software/aula-15-padroes-de-projeto/README.md) | Strategy, Observer, Facade, Singleton, Factory Method — e o padrão pelo padrão |
| 16 | [Qualidade, evolução e próximos passos](bloco-4-projeto-de-software/aula-16-qualidade-evolucao-proximos-passos/README.md) | Verificação × validação, testes, dívida técnica, LGPD, IA no desenvolvimento |

## 🧭 O sistema-guia

Um único sistema atravessa as 16 aulas, crescendo a cada conceito: a **Reserva de Espaços do Campus** — laboratórios, salas de estudo e o auditório, hoje reservados por e-mail e planilha, com duas turmas caindo na mesma sala de vez em quando.

Ele foi escolhido por dois motivos. O primeiro: **você é usuário dele**, então não precisamos gastar meia aula explicando o negócio antes de chegar ao conceito. O segundo: ele tem **poucas peças e muita tensão** — dá para segurar o domínio inteiro na cabeça e ainda assim discutir de verdade, que é exatamente o que um curso de projeto precisa:

- **Interessados que se contradizem** — o professor precisa da sala para a banca de amanhã; o grupo de alunos reservou há duas semanas;
- **Fluxo com exceções** — a reserva cancelada, a que a manutenção derruba, a que ninguém apareceu para usar;
- **Requisitos não-funcionais que não são decorativos** — o pico cai na semana de provas, quase todo acesso vem do celular no meio do campus, e a sala acessível precisa ser encontrável;
- **Regras de negócio que nenhum diagrama expressa sozinho** — banca tem prioridade sobre estudo em grupo até 24 h antes; reserva não confirmada em 15 minutos libera o espaço.

📄 **O documento completo do sistema-guia** — contexto, interessados, vocabulário do domínio, o fluxo e as 8 regras de negócio — está em [recursos/sistema-guia.md](recursos/sistema-guia.md). São duas páginas. Leia antes da Aula 05; a partir dali quase toda aula volta a ele.

> ⚠️ Por ser o sistema trabalhado nas aulas, a Reserva de Espaços **não pode** ser usada nos projetos. Para isso existe o [catálogo de sistemas para praticar](recursos/sistemas-para-praticar.md).

## 📦 Projetos práticos

| Projeto | Quando | Modalidade |
|---------|:---:|------------|
| [Trabalho em dupla — Documento de requisitos via Pull Request](projetos/trabalho-em-dupla.md) | Bloco 2 | Dupla (PRs revisados) |
| [Projeto final — Dossiê de projeto de software](projetos/projeto-final.md) | Bloco 4 | Individual |

## 🔁 O ritual Git de toda aula

**Toda aula começa e termina com Git.** Sem exceção:

```bash
# ── Início da aula ──
cd exercicios-projeto-software
git pull                                  # atualiza (se você usa mais de um PC)

# ── Durante a aula ──
mkdir aula-XX-tema && cd aula-XX-tema      # uma pasta por aula
# ... lê o caso, decide, desenha o diagrama, escreve a justificativa ...
git add .
git commit -m "Resolve exercícios da aula XX"   # commit por exercício concluído

# ── Fim da aula (OBRIGATÓRIO) ──
git push                                   # sem push = sem entrega!
```

> 📏 **Regra do curso (e do mercado):** todo artefato vem acompanhado da **justificativa por escrito**. Um diagrama sem argumento é um desenho bonito — e some na primeira pergunta de quem vai construir o sistema.

## 🛠️ Ambiente

Consulte o [guia de preparação do ambiente](recursos/ambiente.md). O resumo é curto: **um editor de texto e o seu repositório de exercícios**. Os diagramas são escritos em [Mermaid](https://mermaid.js.org/), que o GitHub renderiza sozinho; o único diagrama que o Mermaid não desenha — o de casos de uso — sai em PlantUML, e nem isso exige instalação.

## 🤝 Fazendo POO em paralelo?

Provavelmente sim, e o curso conta com isso — mas **não depende disso**. Sempre que um conceito daqui encostar em classe, herança ou interface, aparece um bloco assim:

> 🧩 **Ponte com POO:** o que você está vendo lá, com o nome que ele tem aqui.

Esses blocos são **opcionais**. Se você ainda não chegou em herança no outro curso, pule — nenhuma aula deste curso deixa de fazer sentido sem eles.

## ⚡ Links rápidos

- 🧭 [Sistema-guia: Reserva de Espaços](recursos/sistema-guia.md) — o documento que o cliente entregaria a você
- 📐 [Notações UML no repositório](recursos/notacoes-uml.md) — qual diagrama em Mermaid, qual em PlantUML e por quê
- 🧯 [Erros comuns](recursos/erros-comuns.md) — do requisito que era solução ao microsserviço para três usuários
- 🏢 [Sistemas para praticar](recursos/sistemas-para-praticar.md) — 12 contextos para exercícios e projetos
- 📚 [Glossário PT/EN](recursos/glossario.md) — para não travar por vocabulário na literatura em inglês
- 🔗 [Links úteis](recursos/links-uteis.md)
- 📖 [Curso de Git e GitHub](https://github.com/jreluiz/curso-git-github) (pré-requisito)

## 📚 Bibliografia

**Livros-base — são dois, porque são duas literaturas diferentes, e o curso não força uma só:**

| Obra | Onde ela é a referência |
|---|---|
| SOMMERVILLE, Ian. **Engenharia de Software**. 10. ed. São Paulo: Pearson. | **Blocos 1 e 2** — processos, agilidade, entrega contínua e requisitos |
| BEZERRA, Eduardo. **Princípios de Análise e Projeto de Sistemas com UML**. 3. ed. Rio de Janeiro: Elsevier. | **Blocos 3 e 4** — UML e projeto orientado a objetos, no nível certo para quem está começando |

**Bibliografia de apoio:**

| Obra | Onde ela ajuda mais |
|---|---|
| PRESSMAN, Roger S.; MAXIM, Bruce R. **Engenharia de software: uma abordagem profissional**. 9. ed. Porto Alegre: AMGH, 2021. | Bloco 1 — a segunda opinião sobre processos e qualidade; onde o Sommerville é conciso, ele é detalhista |
| VAZQUEZ, Carlos Eduardo; SIMÕES, Guilherme Siqueira. **Engenharia de requisitos: software orientado ao negócio**. Rio de Janeiro: Brasport, 2016. | Bloco 2 — elicitação e especificação em português, com o foco na conversa com o cliente |
| FOWLER, Martin. **UML essencial**. 3. ed. Porto Alegre: Bookman, 2005. | Bloco 3 — o que cada diagrama significa, em poucas páginas, quando a dúvida é só de notação |
| GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; VLISSIDES, John. **Padrões de projeto: soluções reutilizáveis de software orientado a objetos**. Porto Alegre: Bookman, 2000. | Aula 15 — a fonte original dos padrões; é livro de **consulta**, não de leitura corrida |
| MARTIN, Robert C. **Arquitetura limpa: o guia do artesão para estrutura e design de software**. Rio de Janeiro: Alta Books, 2019. | Bloco 4 — princípios de projeto e fronteiras entre camadas, depois da Aula 13 |

**O que é gratuito e cabe numa tarde:** o [Manifesto Ágil em português](https://agilemanifesto.org/iso/ptbr/manifesto.html) — quatro valores e doze princípios, e a Aula 03 discute cada um —, o [Guia do Scrum](https://scrumguides.org/download.html) e o [Refactoring Guru](https://refactoring.guru/pt-br/design-patterns), que apresenta os padrões da Aula 15 com diagrama e código.

As aulas marcam com `> 📖` onde aprofundar cada tema. **O curso é autocontido** — o livro é o passo seguinte, não um pré-requisito. As demais referências online estão em [Links úteis](recursos/links-uteis.md).

---

*Este repositório continua evoluindo — material novo é commitado aqui. Primeiro passo de toda sessão de estudo: `git pull`.* 🙂
