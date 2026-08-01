# 🏢 Sistemas para Praticar

Doze contextos prontos para trabalhar. Servem aos exercícios das aulas, ao [trabalho em dupla](../projetos/trabalho-em-dupla.md) e ao [projeto final](../projetos/projeto-final.md) — a ideia é que nem todo mundo especifique a mesma coisa e as revisões entre colegas fiquem interessantes.

**Como usar:** escolha um, leia duas vezes e comece pelos **atores** — quem usa, quem paga, quem audita, quem é prejudicado. Depois procure onde os interesses deles se chocam: é lá que estão os requisitos difíceis, e é isso que se avalia num trabalho de engenharia de software.

Cada contexto abaixo é **deliberadamente incompleto e um pouco ambíguo**, como todo pedido de cliente real. As lacunas não são descuido: preenchê-las com uma decisão escrita e justificada é o exercício.

| # | Sistema | Dificuldade | O que ele cobra de você |
|:---:|---------|:---:|---|
| 1 | [Achados e perdidos do campus](#1-achados-e-perdidos-do-campus) | ⭐ | Pareamento ambíguo, prazo como comportamento |
| 2 | [Empréstimo de equipamentos](#2-empréstimo-de-equipamentos) | ⭐ | Ciclo de vida de objeto, multa, reserva |
| 3 | [Carona entre colegas](#3-carona-entre-colegas) | ⭐⭐ | Confiança, reputação, segurança pessoal |
| 4 | [Controle de estágio supervisionado](#4-controle-de-estágio-supervisionado) | ⭐⭐ | Muitos stakeholders, prazos, documentos |
| 5 | [Delivery de restaurante do bairro](#5-delivery-de-restaurante-do-bairro) | ⭐⭐ | Fluxo de exceção pesado, tempo real |
| 6 | [Rede de doação de alimentos](#6-rede-de-doação-de-alimentos) | ⭐⭐ | Logística, validade, requisitos sociais |
| 7 | [Semana acadêmica com submissões](#7-semana-acadêmica-com-submissões) | ⭐⭐⭐ | Revisão por pares, anonimato, certificados |
| 8 | [Ouvidoria municipal](#8-ouvidoria-municipal) | ⭐⭐⭐ | SLA, encaminhamento, transparência pública |
| 9 | [Marketplace de serviços autônomos](#9-marketplace-de-serviços-autônomos) | ⭐⭐⭐ | Pagamento intermediado, disputa, reputação |
| 10 | [Prontuário de clínica-escola](#10-prontuário-de-clínica-escola) | ⭐⭐⭐ | LGPD a sério, sigilo, trilha de auditoria |
| 11 | [Frota e manutenção preventiva](#11-frota-e-manutenção-preventiva) | ⭐⭐⭐⭐ | Telemetria, disponibilidade, custo de parada |
| 12 | [Assembleia e votação digital](#12-assembleia-e-votação-digital) | ⭐⭐⭐⭐ | Requisitos não-funcionais em conflito direto |

> ⚠️ A **Reserva de Espaços do Campus** não está nesta lista de propósito: ela é o [sistema-guia](sistema-guia.md), trabalhado nas 16 aulas, com requisitos, casos de uso e diagramas publicados no material. Usá-la em projeto seria copiar a resposta.

---

## 1. Achados e perdidos do campus

A portaria recebe o que aparece perdido pelo campus: guarda-chuva, casaco, garrafa, chave, óculos, celular, carteira, documento, notebook. Cada item entra com uma descrição, onde e quando foi encontrado e quem entregou. Hoje tudo fica numa prateleira, e quem procura precisa ir até lá perguntar.

Quem perdeu registra o que era, onde acha que perdeu e quando. Alguém precisa **casar as duas pontas** — e antes de devolver, precisa de alguma prova de que a coisa é mesmo daquela pessoa: uma marca, uma foto antiga, a senha do aparelho, o nome dentro da carteira.

Item de valor tem tratamento próprio: fica em armário fechado e a devolução é registrada. Passados **90 dias**, o que ninguém reclamou é doado — e a instituição precisa conseguir provar depois que o prazo foi cumprido. Documento nunca é doado: vai para a secretaria.

> **Tensões:** publicar a foto do item ajuda quem perdeu a reconhecer × a foto de uma carteira aberta ou de um crachá expõe dado pessoal · facilitar a reclamação × impedir que alguém leve o que não é seu.
> **Armadilhas:** "item encontrado" e "aviso de perda" são duas coisas diferentes, e o **pareamento entre elas é o sistema** — quem funde as duas numa entidade só perde o problema inteiro; o prazo de 90 dias não é um campo de data, é um comportamento (alerta, mudança de estado, descarte registrado); descrever um guarda-chuva preto é ambíguo por natureza, e o sistema tem que conviver com isso em vez de fingir que resolve.

---

## 2. Empréstimo de equipamentos

O setor de audiovisual empresta câmeras, tripés, microfones, projetores e notebooks. Cada item tem patrimônio, estado de conservação e um valor — e alguns só podem sair com quem fez o treinamento de uso.

O empréstimo tem prazo, e a devolução em atraso gera penalidade: hoje é uma suspensão manual que o servidor esquece de aplicar metade das vezes. Itens podem ser reservados com antecedência para um evento, e o mesmo item não pode estar emprestado e reservado no mesmo período. Quando um equipamento volta danificado, ele sai de circulação até a avaliação técnica.

O setor quer saber quais itens quase nunca saem (para justificar não comprar mais) e quais vivem em fila de espera.

> **Tensões:** usuário quer prazo elástico × setor precisa do equipamento de volta para o próximo · reserva antecipada trava o item para quem precisa hoje.
> **Armadilhas:** o item tem um **ciclo de vida** (disponível → reservado → emprestado → em avaliação → em manutenção → baixado) — este é o sistema ideal para treinar diagrama de estados; não confunda o *tipo* de equipamento com a *unidade* física que sai emprestada.

---

## 3. Carona entre colegas

Um aplicativo para quem faz o mesmo trajeto até o campus dividir a carona. O motorista publica origem, destino, horário e quantas vagas tem; passageiros pedem para entrar; o motorista aceita ou não; o rateio da gasolina é combinado entre eles, fora do aplicativo.

Como todo mundo aqui é estranho, existe avaliação mútua depois da viagem e a possibilidade de denunciar comportamento inadequado. Uma parte dos usuários — e a instituição concorda — não quer que seu endereço exato de casa apareça para desconhecidos antes de a carona ser confirmada.

A instituição gostaria de divulgar o aplicativo oficialmente, mas o jurídico está nervoso: **até onde ela é responsável pelo que acontece dentro de um carro que não é dela?**

> **Tensões:** conveniência de ver o ponto exato × privacidade de quem oferece a carona · liberdade de avaliar × injustiça de uma avaliação ruim isolada · interesse da instituição em divulgar × risco jurídico.
> **Armadilhas:** "denunciar usuário" abre um fluxo inteiro que quase todo mundo esquece de especificar (quem analisa? em quanto tempo? o denunciado é notificado?); o requisito de privacidade aqui **não é decorativo** e muda o desenho das telas e dos dados.

---

## 4. Controle de estágio supervisionado

O aluno consegue um estágio, e aí começa a papelada: plano de atividades assinado pela empresa, termo de compromisso com a instituição, seguro, relatórios parciais, avaliação do supervisor da empresa, avaliação do orientador acadêmico e relatório final. Cada documento tem prazo, e prazo perdido pode invalidar o semestre de estágio inteiro.

São quatro interessados com visões bem diferentes: o **aluno** quer saber o que falta e não perder prazo; o **supervisor da empresa** quer gastar cinco minutos por semestre com isso; o **orientador acadêmico** quer acompanhar sem ler 60 relatórios de uma vez; a **coordenação de estágios** precisa do que o Ministério da Educação pede, no formato que ele pede.

Hoje tudo isso vive em e-mails, PDFs assinados à mão e uma planilha que só uma pessoa entende.

> **Tensões:** o supervisor da empresa não é da instituição e não vai criar conta nem lembrar senha · o aluno quer flexibilidade de prazo, a coordenação responde por conformidade legal.
> **Armadilhas:** este é o sistema ideal para treinar **requisito × solução** — quase todo pedido chega como "quero um botão que…"; note que o processo tem estados e transições com regras (um estágio pode ser interrompido, prorrogado, ou trocar de supervisor no meio).

---

## 5. Delivery de restaurante do bairro

Um restaurante quer o próprio canal de pedidos para parar de pagar comissão de aplicativo. Cardápio com itens, opções (ponto da carne, sem cebola), acompanhamentos que custam à parte e combos que valem menos que a soma das partes.

O cliente monta o pedido, escolhe entrega ou retirada, paga on-line ou na entrega, e acompanha o andamento. A cozinha vê os pedidos na ordem em que precisa produzir — que não é a ordem em que eles chegaram, porque tem prato que sai em 5 minutos e prato que sai em 30. O entregador recebe a rota. O dono quer saber o que vendeu, quanto sobrou e qual item dá prejuízo.

E aí a realidade: acabou um ingrediente no meio do expediente, o cliente pediu para cancelar quando o prato já estava na chapa, o pagamento on-line não confirmou, o endereço estava errado, o entregador não encontrou ninguém em casa.

> **Tensões:** cliente quer cancelar até o último segundo × cozinha já gastou insumo · entregador quer rota curta × cliente quer comida quente.
> **Armadilhas:** o parágrafo de cima é o coração do trabalho — **cada uma daquelas frases é um fluxo de exceção**, e é aí que mora a regra de negócio; "status do pedido" parece trivial até você desenhar o diagrama de estados e descobrir que ele tem caminho de volta.

---

## 6. Rede de doação de alimentos

Uma organização conecta quem tem excedente de alimento (padarias, restaurantes, mercados, hortas) a instituições que servem refeições (abrigos, casas de apoio, cozinhas comunitárias). O doador anuncia o que tem, em que quantidade e até quando aquilo é seguro para consumo; as instituições sinalizam interesse; alguém precisa buscar.

O tempo é o inimigo: pão do dia vale hoje e não vale amanhã. Nem toda instituição tem transporte, nem toda tem geladeira, e existem voluntários que fazem a coleta com o próprio carro. A organização precisa comprovar aos financiadores quanto alimento foi resgatado, e precisa rastrear a origem de cada lote se alguém passar mal.

Boa parte dos usuários acessa por celular simples, com internet instável, e algumas voluntárias têm baixa visão.

> **Tensões:** justiça na distribuição (quem recebe quando duas instituições pedem o mesmo lote?) × rapidez · rastreabilidade exigida pelo financiador × simplicidade para o doador que tem 30 segundos.
> **Armadilhas:** os requisitos de **acessibilidade e de funcionamento com rede ruim** são funcionais na consequência e não-funcionais na forma — este contexto existe para treinar exatamente isso; a "validade" do alimento não é um campo, é uma regra que muda o comportamento do sistema com o passar das horas.

---

## 7. Semana acadêmica com submissões

O evento anual tem palestras, minicursos com vagas limitadas e uma sessão de trabalhos submetidos por alunos. A comissão organizadora abre chamada, recebe resumos, distribui cada resumo para dois avaliadores, coleta as notas e os pareceres, decide os aceitos e monta a programação.

Participantes se inscrevem no evento e nos minicursos — que enchem em minutos assim que a inscrição abre. A presença é registrada na entrada de cada atividade, e o certificado só sai para quem tem a carga horária mínima. Quem submeteu trabalho recebe certificado diferente, e o orientador aparece nele.

A avaliação é **cega**: o avaliador não pode saber de quem é o trabalho e o autor não pode saber quem avaliou. Um avaliador não pode receber o trabalho do próprio orientando. Empate de notas vai para um terceiro avaliador.

> **Tensões:** anonimato da avaliação × necessidade da comissão de auditar quem avaliou o quê · pico brutal de acesso na abertura das inscrições × orçamento de infraestrutura de um evento estudantil.
> **Armadilhas:** o mesmo indivíduo é participante, autor, avaliador e organizador ao mesmo tempo — se você modelar isso como quatro classes por herança, vai travar; certificado tem regra de carga horária, e regra de carga horária tem exceção (quem palestrou também recebe).

---

## 8. Ouvidoria municipal

O cidadão registra uma manifestação — reclamação, denúncia, sugestão, elogio ou pedido de informação — sobre qualquer serviço da prefeitura: buraco na rua, poste apagado, atendimento no posto de saúde. Pode registrar pelo site, pelo telefone (com um atendente digitando) ou presencialmente.

Cada manifestação é classificada, encaminhada ao órgão responsável e tem **prazo legal de resposta**. O cidadão acompanha por um protocolo. Denúncia pode ser **anônima**, e nesse caso ninguém — nem dentro da prefeitura — pode chegar ao autor. Se o órgão responsável responde qualquer bobagem só para fechar o prazo, o cidadão pode reabrir.

A lei ainda exige que a prefeitura publique estatísticas: quantas manifestações, por assunto, por bairro, com tempo médio de resposta. E o secretário cujo órgão sempre atrasa não gosta nada dessa transparência.

> **Tensões:** transparência obrigatória × exposição de setores mal avaliados · anonimato da denúncia × necessidade de pedir mais informações a quem denunciou · prazo legal × capacidade real de atendimento.
> **Armadilhas:** "prazo" aqui não é campo de data, é comportamento (alerta, escalonamento, indicador público); o encaminhamento errado é a regra e não a exceção — o fluxo de **redirecionar entre órgãos** precisa existir desde o começo.

---

## 9. Marketplace de serviços autônomos

Uma plataforma para contratar serviços locais: aulas particulares, conserto, frete pequeno, faxina, design. O prestador publica o que faz, sua região de atendimento e sua disponibilidade; o cliente descreve o que precisa e recebe propostas com preço e prazo.

O dinheiro fica **retido na plataforma** e só é liberado quando o cliente confirma que o serviço foi feito — e é justamente aí que nasce o problema: o cliente que não confirma por esquecimento, o cliente que não confirma de má-fé, o prestador que entregou pela metade. Existe um fluxo de disputa, com prazo, evidências e uma decisão da plataforma. Há também cancelamento antes da execução, com regras de multa diferentes conforme quem cancelou e quando.

A plataforma vive de comissão. Prestador e cliente têm avaliações mútuas, e nota baixa demais tira o prestador dos resultados de busca — o que ele considera injusto quando a nota veio de um único cliente difícil.

> **Tensões:** proteger o cliente (segurar o dinheiro) × proteger o prestador (que já trabalhou) · comissão da plataforma × incentivo dos dois lados a combinar por fora.
> **Armadilhas:** especificar só o caminho feliz aqui é praticamente não especificar nada; a disputa é um caso de uso completo, com ator (o mediador da plataforma) que muita gente esquece de listar; o dinheiro tem estados próprios, independentes dos estados do serviço.

---

## 10. Prontuário de clínica-escola

A clínica-escola de psicologia (ou fisioterapia, ou odontologia) atende a comunidade e, ao mesmo tempo, é onde os alunos aprendem. Cada atendimento é feito por um aluno, sob supervisão de um professor que responde tecnicamente pelo caso.

O prontuário contém dado de saúde — a categoria mais protegida da LGPD. O paciente tem direito de saber o que está guardado sobre ele, de corrigir o que está errado e de pedir a exclusão; só que registro clínico tem prazo legal de guarda, e "excluir" nem sempre é permitido. O aluno que atendeu no semestre passado não deveria continuar vendo o prontuário no semestre seguinte. O supervisor precisa ver tudo dos seus supervisionados. A coordenação precisa de estatística — **sem identificar ninguém**.

Casos com indício de risco à vida ou de violência têm procedimento próprio, com notificação obrigatória a órgãos externos, e isso rompe o sigilo por determinação legal.

> **Tensões:** sigilo do paciente × necessidade pedagógica de discutir o caso · direito ao apagamento × obrigação legal de guarda · estatística útil × risco de reidentificação em turma pequena.
> **Armadilhas:** controle de acesso aqui **não é detalhe de implementação, é requisito de negócio** e precisa estar especificado por papel; toda leitura de prontuário deixa rastro (trilha de auditoria é requisito, não recurso de banco); consentimento tem versão e data — não é um campo booleano.

---

## 11. Frota e manutenção preventiva

Uma transportadora de médio porte opera 60 veículos. O sistema acompanha cada um: quilometragem, abastecimentos, pneus, documentação, multas, e o plano de manutenção — que é por quilometragem para uns itens e por tempo para outros, o que vier primeiro.

Os veículos mais novos enviam telemetria automaticamente (quilometragem, código de falha, localização); os mais antigos dependem de o motorista digitar o hodômetro no fim do turno, e ele às vezes esquece ou erra. O sistema precisa funcionar com as duas fontes, sabendo que uma delas mente.

Parar um caminhão para manutenção custa caro; deixar de parar custa mais caro ainda quando ele quebra na estrada com carga. O gestor quer que o sistema **sugira** a janela de manutenção onde ela atrapalha menos, considerando as viagens já programadas. A oficina, própria, tem capacidade limitada de box e mecânico.

> **Tensões:** disponibilidade da frota × prevenção · dado automático confiável × dado manual barato · agenda de viagens (comercial) × agenda de oficina (manutenção).
> **Armadilhas:** "o quanto antes" não é requisito — a regra de acionamento da manutenção precisa de número e de fonte; este contexto é o melhor da lista para **ADR** (integrar telemetria via qual protocolo? processar em lote ou em tempo real? o que fazer quando o dado atrasa três dias?).

---

## 12. Assembleia e votação digital

Uma entidade — associação de moradores, centro acadêmico, conselho profissional — quer realizar assembleias e votações à distância, com a mesma validade das presenciais.

O estatuto exige: só vota quem está em dia; algumas deliberações precisam de **quórum mínimo** e outras de maioria qualificada; existe voto por procuração, com limite de procurações por pessoa; e a apuração precisa ser **auditável** — qualquer associado pode contestar o resultado e alguém tem que conseguir provar que ele está correto.

Ao mesmo tempo, o voto deve ser **secreto**. Ninguém pode descobrir em que alguém votou, nem os administradores do sistema, nem depois. Mas o sistema também precisa impedir que a mesma pessoa vote duas vezes, e precisa comprovar a cada associado que o voto dele foi contabilizado.

A assembleia é ao vivo: há discussão, alguém propõe emenda ao texto, e o que vai a voto no fim não é exatamente o que estava na convocação.

> **Tensões:** sigilo do voto × auditabilidade da apuração — este é o conflito central, e ele **não se resolve escolhendo um lado** · voto por procuração × princípio de um associado, um voto · pauta fechada na convocação × emenda proposta ao vivo.
> **Armadilhas:** a maioria das duplas escreve "o voto deve ser secreto e auditável" como dois requisitos independentes e segue em frente — o trabalho começa quando você percebe que eles se contradizem e precisa **escrever a decisão de projeto** que concilia os dois (ou assume o que está abrindo mão); "quórum" muda o que o sistema faz durante a votação, não só no fim.

---

## Como escolher o seu

| Se você quer… | Escolha entre |
|---|---|
| Um escopo pequeno e sob controle, para acertar o processo | 1, 2 |
| Muitos stakeholders com interesses diferentes | 4, 8, 10 |
| Fluxos de exceção ricos, bons para casos de uso | 5, 9 |
| Requisitos não-funcionais que decidem o projeto | 6, 10, 12 |
| Um bom caso para diagrama de estados | 1, 2, 5, 9 |
| Um bom caso para ADR e arquitetura | 11, 12 |
| Dificuldade máxima com escopo ainda enxuto | 12 |

> 📏 **Vale para todos:** o enunciado é o ponto de partida, não a especificação. Você vai precisar **decidir** o que fica de fora — e escrever isso. Um documento que diz *"pagamento em criptomoeda está fora do escopo desta versão porque nenhum stakeholder pediu e o custo de conformidade é alto"* vale mais que um que finge que a pergunta não existe.

---

🏠 [Voltar ao início](../README.md)
