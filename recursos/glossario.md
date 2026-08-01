# 📚 Glossário PT/EN

Quase toda a literatura, toda a documentação de ferramenta e metade das conversas de trabalho estão em inglês. O que trava quem está começando nesses textos raramente é o conceito — é o **vocabulário**: você já entende o que é acoplamento e mesmo assim empaca em *coupling*.

Este glossário é para consultar, não para decorar. Guarde o link.

> 💡 Aqui está o vocabulário **da engenharia de software**. O vocabulário **do domínio** do sistema-guia — espaço, recurso, reserva, bloqueio — é outra coisa, e vive na [seção 5 do sistema-guia](sistema-guia.md#5-vocabulário-do-domínio). Todo projeto de software tem os dois, e confundi-los é fonte garantida de mal-entendido.

**Índice:** [Processo](#1-processo-e-ciclo-de-vida) · [Ágil](#2-ágil) · [Requisitos](#3-requisitos) · [UML](#4-modelagem-e-uml) · [Projeto](#5-projeto-e-arquitetura) · [Qualidade](#6-qualidade-testes-e-evolução) · [Entrega](#7-entrega-e-operação) · [Os que ninguém traduz](#8-os-que-ninguém-traduz) · [Falsos amigos](#9-falsos-amigos)

---

## 1. Processo e ciclo de vida

| Português | English | O que é |
|---|---|---|
| Engenharia de software | *software engineering* | O campo que trata de todo o ciclo de produção de software, não só da programação |
| Ciclo de vida | *life cycle* | Do primeiro levantamento à aposentadoria do sistema |
| Modelo de processo | *process model* | O arranjo escolhido para as atividades: cascata, incremental, iterativo, ágil |
| Cascata | *waterfall* | Fases em sequência, cada uma terminando antes da seguinte começar |
| Dirigido a plano | *plan-driven* | Processo em que o planejamento antecede e governa a execução |
| Iterativo | *iterative* | Refaz o mesmo trabalho com mais profundidade a cada ciclo |
| Incremental | *incremental* | Entrega o produto em fatias, cada uma funcionando |
| Prototipação | *prototyping* | Construir algo descartável para aprender ou validar |
| Parte interessada / interessado | *stakeholder* | Quem afeta ou é afetado pelo sistema — inclusive quem nunca vai usá-lo |
| Prazo final | *deadline* | — |
| Marco | *milestone* | Ponto verificável do cronograma |
| Esforço | *effort* | Trabalho medido em pessoa-hora, distinto de prazo |
| Escopo | *scope* | O que está e o que não está incluído |
| Inchaço de escopo | *scope creep* | Escopo que cresce sem que ninguém tenha decidido aumentá-lo |

---

## 2. Ágil

| Português | English | O que é |
|---|---|---|
| Desenvolvimento ágil | *agile development* | Família de abordagens baseadas em ciclos curtos e adaptação |
| Reunião diária | *daily / stand-up* | Sincronização curta e diária do time |
| Retrospectiva | *retrospective* | Reunião sobre como o time trabalhou, não sobre o produto |
| Planejamento da iteração | *sprint planning* | Onde o time decide o que cabe no próximo ciclo |
| Revisão / demonstração | *sprint review* | Apresentação do incremento ao cliente |
| Lista de pendências do produto | *product backlog* | Fila priorizada de tudo que se quer fazer |
| Dono do produto | *Product Owner* | Papel que responde pelo *o quê* e pela ordem |
| Definição de pronto | *Definition of Done* | Critério único do time para "terminado" |
| Ponto de história | *story point* | Unidade relativa de esforço, sem correspondência com hora |
| Velocidade | *velocity* | Quantos pontos o time conclui por ciclo — para prever, não para cobrar |
| Trabalho em andamento | *work in progress* (WIP) | O que já começou e ainda não terminou |
| Melhoria contínua | *continuous improvement* | — |
| Programação em par | *pair programming* | Duas pessoas, um teclado |

> 💡 *Sprint*, *backlog*, *Scrum Master* e *Kanban* praticamente não se traduzem no mercado brasileiro. Use em inglês sem culpa — mas saiba o que significam em português, porque em edital, concurso e livro traduzido eles aparecem vertidos.

---

## 3. Requisitos

| Português | English | O que é |
|---|---|---|
| Requisito | *requirement* | O que o sistema deve fazer ou qual qualidade deve ter |
| Requisito funcional | *functional requirement* | Algo que o sistema **faz** |
| Requisito não-funcional | *non-functional requirement* (NFR) | Uma **qualidade ou restrição** sobre como ele faz |
| Atributo de qualidade | *quality attribute* | Outro nome para requisito não-funcional, comum em arquitetura |
| Elicitação / levantamento | *elicitation* | Descobrir os requisitos — *elicit* é "extrair", não "perguntar" |
| Especificação | *specification* | O documento que registra os requisitos de forma verificável |
| Documento de requisitos | *requirements document* / *SRS* | O artefato consolidado |
| Rastreabilidade | *traceability* | Poder ligar requisito → projeto → código → teste |
| Verificável | *verifiable / testable* | Que permite responder objetivamente se foi cumprido |
| Ambíguo | *ambiguous* | Que admite mais de uma leitura razoável |
| História de usuário | *user story* | "Como ⟨papel⟩, quero ⟨ação⟩ para que ⟨benefício⟩" |
| Critério de aceite | *acceptance criteria* | As condições que tornam a história aprovada |
| Épico | *epic* | História grande demais, que será quebrada |
| Regra de negócio | *business rule* | Restrição do domínio, verdadeira mesmo sem sistema nenhum |
| Domínio | *domain* | A área de conhecimento do problema |
| Priorização | *prioritization* | Decidir a ordem — e, portanto, o que fica de fora |
| Negociação | *negotiation* | O que acontece quando dois requisitos não cabem juntos |

---

## 4. Modelagem e UML

| Português | English | O que é |
|---|---|---|
| Modelagem | *modeling* | Representar o sistema de forma simplificada e proposital |
| Caso de uso | *use case* | Objetivo de um ator que gera resultado de valor |
| Ator | *actor* | Papel externo que interage com o sistema |
| Fronteira do sistema | *system boundary* | A linha entre o que é o sistema e o que é o mundo |
| Fluxo principal | *main / basic flow* | O caminho em que tudo dá certo |
| Fluxo alternativo | *alternative flow* | Outro caminho válido para o mesmo objetivo |
| Fluxo de exceção | *exception flow* | O que acontece quando não dá certo |
| Pré-condição / pós-condição | *precondition / postcondition* | O que vale antes e depois do caso de uso |
| Diagrama de classes | *class diagram* | Visão estática: as coisas do domínio e suas relações |
| Atributo | *attribute* | Dado que a classe guarda |
| Operação / método | *operation / method* | O que a classe sabe fazer |
| Visibilidade | *visibility* | Público `+`, privado `-`, protegido `#`, pacote `~` |
| Associação | *association* | Ligação estrutural entre classes |
| Multiplicidade | *multiplicity* | Quantos objetos participam de cada lado |
| Agregação | *aggregation* | Todo-parte em que a parte sobrevive ao todo (losango branco) |
| Composição | *composition* | Todo-parte em que a parte morre com o todo (losango preto) |
| Herança / generalização | *inheritance / generalization* | Relação "é-um" |
| Diagrama de sequência | *sequence diagram* | Mensagens trocadas ao longo do tempo |
| Linha de vida | *lifeline* | A linha vertical de cada participante |
| Diagrama de atividades | *activity diagram* | O fluxo de trabalho, com decisões e paralelismo |
| Diagrama de estados | *state machine diagram* | O ciclo de vida de **um** objeto |
| Diagrama de componentes | *component diagram* | As partes construíveis e suas interfaces |
| Diagrama de implantação | *deployment diagram* | Onde cada coisa roda |
| Estereótipo | *stereotype* | Extensão de significado, escrita entre `«guillemets»` |

---

## 5. Projeto e arquitetura

| Português | English | O que é |
|---|---|---|
| **Projeto (de software)** | **design** | As decisões de estrutura e organização — **não** é "desenho", e **não** é o *project* de gerência |
| Projeto detalhado | *detailed design* | O nível das classes e dos métodos |
| Arquitetura | *architecture* | As decisões caras de reverter e a relação entre as partes |
| Coesão | *cohesion* | O quanto o que está junto trata do mesmo assunto |
| Acoplamento | *coupling* | O quanto uma parte depende de outra |
| Separação de responsabilidades | *separation of concerns* | Cada parte com um motivo para mudar — *concern* aqui é "interesse", não "preocupação" |
| Abstração | *abstraction* | Esconder o que não importa neste nível |
| Encapsulamento | *encapsulation* | Esconder o estado interno atrás de uma interface |
| Interface | *interface* | O contrato público, separado da implementação |
| Camada | *layer* | Divisão **lógica** de responsabilidade |
| Camada física | *tier* | Divisão **física** de execução — não confunda com *layer* |
| Componente | *component* | Parte substituível com interface definida |
| Serviço | *service* | Componente acessado remotamente, por contrato |
| Monolito | *monolith* | Sistema implantado como uma unidade só |
| Microsserviços | *microservices* | Vários serviços implantados de forma independente |
| Padrão de projeto | *design pattern* | Solução recorrente para um problema em um contexto |
| Antipadrão | *anti-pattern* | Solução comum que costuma piorar as coisas |
| Compromisso / balanceamento | *trade-off* | Ganhar de um lado pagando do outro. **Não existe projeto sem isso** |
| Registro de decisão de arquitetura | *Architecture Decision Record* (ADR) | Documento curto: contexto, decisão, alternativas, consequências |
| Preocupação transversal | *cross-cutting concern* | O que atravessa vários módulos (log, segurança, transação) |

> ⚠️ **O falso amigo mais caro do curso:** *design* em engenharia de software é **projeto**, no sentido de projetar uma estrutura — o que um engenheiro civil faz antes da obra. Não é a parte visual. *Software design* traduz-se por *projeto de software*; a aparência da interface é *UI design*.

---

## 6. Qualidade, testes e evolução

| Português | English | O que é |
|---|---|---|
| Verificação | *verification* | "Construímos o produto **corretamente**?" (contra a especificação) |
| Validação | *validation* | "Construímos o **produto certo**?" (contra a necessidade) |
| Teste de unidade | *unit test* | Testa uma peça isolada |
| Teste de integração | *integration test* | Testa as peças conversando |
| Teste de sistema | *system test* | Testa o produto inteiro |
| Teste de aceite | *acceptance test* | O cliente confere se serve |
| Teste de regressão | *regression test* | Garante que o que funcionava continua funcionando |
| Cobertura | *coverage* | Percentual de código exercitado pelos testes — bom indicador, péssima meta |
| Defeito / erro / falha | *defect / fault / failure* | O engano humano, o problema no código, o comportamento errado observado |
| Revisão de código | *code review* | Leitura crítica do que outra pessoa escreveu |
| Refatoração | *refactoring* | Mudar a estrutura interna **sem** mudar o comportamento externo |
| Mau cheiro de código | *code smell* | Sintoma de que algo está mal projetado |
| Dívida técnica | *technical debt* | Atalho consciente hoje, com juros depois |
| Legado | *legacy* | Sistema em produção que ninguém quer mexer e ninguém pode desligar |
| Manutenção corretiva / adaptativa / evolutiva | *corrective / adaptive / perfective maintenance* | Consertar, acomodar mudança externa, melhorar |
| Manutenibilidade | *maintainability* | O quanto o sistema aceita ser mudado |
| Confiabilidade | *reliability* | O quanto se pode contar com ele ao longo do tempo |
| Usabilidade | *usability* | O quanto ele é aprendível e eficiente de usar |
| Acessibilidade | *accessibility* (a11y) | O quanto ele serve a pessoas com deficiência |

---

## 7. Entrega e operação

| Português | English | O que é |
|---|---|---|
| Integração contínua | *continuous integration* (CI) | Integrar e testar a cada mudança, várias vezes ao dia |
| Entrega contínua | *continuous delivery* (CD) | Manter o sistema **sempre pronto** para ser implantado |
| Implantação contínua | *continuous deployment* | Implantar automaticamente o que passou nos testes |
| Implantação | *deployment* | Colocar a versão no ar |
| Esteira | *pipeline* | A sequência automatizada de build, teste e implantação |
| Compilação / empacotamento | *build* | Transformar código em artefato executável |
| Versão / liberação | *release* | O conjunto empacotado que vai ao usuário |
| Reversão | *rollback* | Voltar à versão anterior |
| Chave de funcionalidade | *feature flag / toggle* | Liga e desliga um recurso sem novo *deploy* |
| Ambiente | *environment* | Desenvolvimento, homologação, produção |
| Homologação | *staging* | O ambiente parecido com produção onde se confere antes |
| Produção | *production* | Onde o usuário de verdade está |
| Tempo de indisponibilidade | *downtime* | — |
| Disponibilidade | *availability* | Percentual de tempo em que o sistema responde |
| Escalabilidade | *scalability* | Aguentar mais carga sem redesenhar tudo |
| Latência | *latency* | Tempo até a primeira resposta |
| Vazão | *throughput* | Quantidade de trabalho por unidade de tempo |
| Acordo de nível de serviço | *Service Level Agreement* (SLA) | Compromisso contratado de qualidade de serviço |
| Observabilidade | *observability* | Conseguir entender o que o sistema está fazendo por fora |

---

## 8. Os que ninguém traduz

Existem e têm tradução, mas em conversa de trabalho brasileira aparecem em inglês. Use assim — só não se perca quando o livro traduzido usar o termo em português.

| Termo | Tradução que você vai ver em livro |
|---|---|
| *deploy* | implantação |
| *build* | compilação, geração |
| *commit* | confirmação de alterações |
| *branch* | ramo |
| *merge* | mesclagem, integração |
| *pull request* | solicitação de integração |
| *issue* | ocorrência, chamado |
| *bug* | defeito |
| *feature* | funcionalidade, recurso |
| *framework* | arcabouço |
| *sprint* | iteração |
| *backlog* | lista de pendências |
| *stakeholder* | parte interessada |
| *trade-off* | compromisso, balanceamento |
| *design pattern* | padrão de projeto |
| *code review* | revisão de código |
| *hotfix* | correção emergencial |

---

## 9. Falsos amigos

Os que fazem o aluno traduzir a frase inteira ao contrário do que ela diz:

| Palavra em inglês | Não é | É |
|---|---|---|
| *design* | desenho | **projeto** (a decisão de estrutura) |
| *concern* (em *separation of concerns*) | preocupação | **interesse, assunto, responsabilidade** |
| *eventually* | eventualmente | **por fim, mais cedo ou mais tarde** |
| *actually* | atualmente | **na verdade** |
| *library* | livraria | **biblioteca** |
| *realize* | realizar | **perceber** |
| *support* | suportar (aguentar) | **apoiar, dar suporte a** |
| *require* | requerer (pedir) | **exigir, precisar de** |
| *assume* | assumir (responsabilidade) | **supor, presumir** |
| *argument* | discussão | **argumento (parâmetro)** |
| *statement* | declaração à imprensa | **comando, instrução** |
| *implement* | implemento | **implementar** |
| *legacy* | legado (herança positiva) | **sistema antigo que ainda roda** |
| *pretend* | pretender | **fingir** — *intend* é que é pretender |
| *sensible* | sensível | **sensato** — sensível é *sensitive* (e é essa a palavra em "dado sensível") |

> 💡 Quando um termo em inglês não fizer sentido, tente lê-lo como se ele fosse **literal e concreto**: *elicit* é "extrair", e é por isso que elicitação não é só perguntar; *coupling* é o engate de dois vagões, e é por isso que acoplamento alto significa que um puxa o outro.

---

🏠 [Voltar ao início](../README.md)
