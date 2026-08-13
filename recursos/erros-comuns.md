# 🧯 Erros Comuns

Em Java, o compilador aponta o erro. Em modelagem de dados, a notação aponta. **Em gestão de projeto nada aponta.** Um cronograma otimista é aprovado sem reclamação; um risco sem dono fica bonito na planilha; uma matriz de responsabilidades com dois responsáveis passa na reunião. O preço só chega depois, e chega grande.

Este arquivo é o substituto do compilador: o catálogo das patologias que aparecem toda vez, com o sintoma que as denuncia e a pergunta que as resolve. Volte aqui antes de entregar qualquer artefato.

**Índice:** [Fundamentos e processos](#parte-1--fundamentos-e-processos) · [Metodologias](#parte-2--metodologias) · [Risco, qualidade e documentação](#parte-3--risco-qualidade-e-documentação) · [Entrega, usuário e governança](#parte-4--entrega-usuário-e-governança)

---

## Parte 1 — Fundamentos e processos

### Projeto confundido com operação

**Sintoma:** o "projeto" não tem data de fim. Ele vira uma equipe permanente cuidando de um sistema, e ninguém percebe que a natureza mudou.

**Causa:** projeto e operação usam as mesmas pessoas e as mesmas ferramentas, então a diferença não aparece no dia a dia.

**Cura:** projeto é **temporário e produz um resultado único**; operação é contínua e repetitiva. A pergunta que separa: *"existe um dia em que isso acaba e alguém assina o aceite?"* Se não existe, você está gerindo operação com vocabulário de projeto — e vai cobrar do time um encerramento que nunca vem.

### Conflito de objetivo tratado como conflito de pessoa

**Sintoma:** *"o pessoal da infraestrutura é difícil de lidar"*. A conversa vira temperamento, e a decisão fica parada.

**Causa:** dois setores com metas legítimas e incompatíveis — quem responde por disponibilidade vai mesmo resistir a mudança em produção.

**Cura:** antes de falar em pessoa, escreva as duas metas lado a lado. Conflito de objetivo se resolve com **decisão de quem tem autoridade**; conflito de pessoa se resolve com conversa. Tratar o primeiro como o segundo produz reunião infinita.

### RACI com dois **A**

**Sintoma:** a matriz de responsabilidades tem dois "Aprovador" na mesma linha, e a decisão trava toda vez.

**Causa:** medo de deixar alguém de fora. Colocar os dois parece diplomacia.

**Cura:** **um A por linha, sempre.** Vários podem ser consultados (C) e informados (I); vários podem executar (R). Mas quem responde pela decisão é uma pessoa só — se são duas, na prática não é ninguém.

### Incremental confundido com iterativo

**Sintoma:** o time diz que é iterativo e entrega funcionalidade nova a cada ciclo, sem nunca voltar ao que já entregou.

**Causa:** os dois termos aparecem juntos e viram sinônimo.

**Cura:** **incremental é entregar em pedaços; iterativo é refazer o mesmo pedaço melhor.** Um quadro pintado por partes é incremental; um quadro esboçado inteiro e refinado três vezes é iterativo. Quase todo projeto real precisa dos dois, e chamar tudo de iterativo esconde que ninguém está revisitando decisão nenhuma.

### Preditivo tratado como sinônimo de cascata

**Sintoma:** *"preditivo é ultrapassado"*.

**Causa:** confundir o **eixo** (quanto se decide antecipadamente) com um **modelo específico** de ciclo de vida.

**Cura:** preditivo e adaptativo são as pontas de um eixo, e a escolha depende de quanta incerteza existe. Construir uma ponte é preditivo por boas razões. O erro não é ser preditivo: é ser preditivo num projeto onde ninguém sabe ainda o que quer.

### O encerramento que não acontece

**Sintoma:** o projeto "acabou" quando o sistema entrou no ar. Não há aceite assinado, não há lições aprendidas, e três meses depois ninguém sabe se ele deu certo.

**Causa:** encerramento parece burocracia, e a equipe já foi realocada.

**Cura:** encerrar é **obter aceite formal, arquivar o que se produziu e registrar o que se aprendeu**. Sem isso o projeto seguinte repete os mesmos erros, e a organização paga duas vezes pela mesma lição.

### Chamar de arquitetura o que é escolha de ferramenta

**Sintoma:** *"a arquitetura é React com Node e Postgres"*.

**Causa:** confundir a lista de tecnologias com as decisões que estruturam o sistema.

**Cura:** arquitetura são as **decisões difíceis de reverter** — como o sistema se divide, quem conversa com quem, o que acontece quando uma parte cai. A tecnologia é consequência delas, e quase sempre a parte mais fácil de trocar.

### Decisão de arquitetura sem alternativa descartada

**Sintoma:** o registro diz *"decidimos usar arquitetura em camadas"* e para aí.

**Causa:** registrar a decisão parece suficiente.

**Cura:** o valor do registro está no **que foi descartado e por quê**. Quem chega daqui a um ano não precisa saber que você escolheu camadas — precisa saber que você considerou e rejeitou outra coisa, e sob quais premissas. Se as premissas mudarem, a decisão pode ser revista com segurança.

---

## Parte 2 — Metodologias

### "Ágil quer dizer que não documentamos"

**Sintoma:** o time não escreve nada e cita o Manifesto quando alguém reclama.

**Causa:** ler os quatro valores como se fossem quatro negações. O Manifesto diz *"software em funcionamento **mais que** documentação abrangente"* — e depois diz, com todas as letras, que os itens à direita também têm valor.

**Cura:** a pergunta certa não é *"documentamos ou não?"*, é **"qual documento alguém vai ler depois?"**. Oitenta páginas que ninguém abre é desperdício em qualquer processo; meia página explicando uma decisão é barata e salva o time que chega no ano que vem.

### Ágil confundido com ausência de plano

**Sintoma:** não há previsão de nada, e a resposta a *"quando fica pronto?"* é *"depende da sprint"*.

**Causa:** confundir **plano fixo** com **planejar**.

**Cura:** o ágil planeja o tempo todo — só planeja em horizonte curto e revisa com frequência. Quem não consegue dizer o que espera entregar nas próximas seis semanas não é ágil: está sem plano.

### Cascata disfarçada de sprint

**Sintoma:** sprint 1 de levantamento, sprint 2 de desenho, sprint 3 de construção, sprint 4 de teste.

**Causa:** adotar o vocabulário sem mudar o fluxo.

**Cura:** cada iteração precisa entregar algo **utilizável**, ainda que pequeno. Fatias horizontais por especialidade são cascata com nome novo, e o risco continua concentrado no fim.

### O quadro Kanban que é um cemitério

**Sintoma:** a coluna "em andamento" tem 14 cartões e nada sai.

**Causa:** nenhum limite de trabalho em andamento. Começar é grátis, terminar é caro.

**Cura:** **limite explícito por coluna.** Quando o limite bate, ninguém puxa item novo — ajuda-se a terminar o que já está lá. O desconforto é o ponto: ele torna visível o gargalo que a fila escondia.

### Product Owner confundido com gerente de projeto

**Sintoma:** a mesma pessoa define prioridade do produto, cobra prazo e negocia contrato — e o time recebe ordens contraditórias dela mesma.

**Causa:** os dois papéis decidem coisas, e "quem manda" parece um cargo só.

**Cura:** o **PO responde pelo valor**: o que se faz e em que ordem. O **GP responde pela entrega**: prazo, custo, risco e comunicação. Podem ser a mesma pessoa num projeto pequeno, desde que ela saiba **com qual chapéu** está decidindo em cada momento.

### Scrum Master mandando no escopo

**Sintoma:** ele reprioriza o backlog e decide o que entra na sprint.

**Causa:** confundir "responsável pelo processo" com "chefe do time".

**Cura:** o Scrum Master **remove impedimento e protege o processo**. Não decide escopo, não manda em ninguém e não é o gerente com nome novo. Quando ele decide escopo, o PO vira decorativo.

### Velocidade tratada como meta

**Sintoma:** a velocidade sobe todo mês e nada chega mais rápido ao usuário.

**Causa:** usar para cobrar uma medida que existe para prever.

**Cura:** velocidade serve para **estimar quanto cabe na próxima iteração**. Como meta, ela é trivialmente inflacionável — basta estimar mais alto. É o exemplo clássico de métrica que vira meta e para de medir.

### MVP que é a primeira fatia do plano

**Sintoma:** *"nosso MVP é o módulo de cadastro"*.

**Causa:** entender MVP como "versão reduzida" em vez de **experimento**.

**Cura:** um MVP tem **hipótese, forma de medir e critério de decisão**. Se você não consegue completar a frase *"se acontecer X, a gente muda de direção"*, não é MVP: é a entrega 1 de 8.

### Design Thinking usado como dinâmica de post-it

**Sintoma:** meio dia de oficina com papel colorido, e o escopo do projeto segue exatamente o mesmo.

**Causa:** executar as etapas sem a que dá sentido a elas — entender o usuário de verdade.

**Cura:** as etapas produzem **decisão**. Se depois da oficina ninguém mudou de ideia sobre nada, ou o problema já estava claro (e não precisava da oficina) ou ela não foi feita para valer.

---

## Parte 3 — Risco, qualidade e documentação

### Risco confundido com problema

**Sintoma:** a lista de riscos contém *"o servidor está lento"*.

**Causa:** tratar como risco tudo que preocupa.

**Cura:** risco é **incerto**; problema já aconteceu. Servidor lento é problema, e problema se resolve, não se monitora. Se tudo virar risco, a lista fica longa e ninguém a lê.

### Risco sem dono e sem gatilho

**Sintoma:** a matriz tem 20 riscos bem classificados e nenhum nome ao lado.

**Causa:** identificar é fácil e agradável; responsabilizar é desconfortável.

**Cura:** risco sem **dono** e sem **gatilho** — o sinal de que ele está virando problema — não é gestão de risco, é literatura. Cada linha precisa responder: quem acompanha, e o que faz disparar a resposta.

### Risco escrito sem causa e sem efeito

**Sintoma:** *"risco: integração"*.

**Causa:** anotar o assunto em vez do risco.

**Cura:** escreva **causa → evento incerto → efeito**: *"porque a documentação do ERP está desatualizada, a integração pode levar o dobro do previsto, atrasando a entrega em 6 semanas"*. Só assim dá para estimar probabilidade e impacto, e só assim a resposta fica óbvia.

### Métrica que virou meta

**Sintoma:** a cobertura de testes chegou a 90% e os defeitos continuam iguais.

**Causa:** medir o que é fácil de medir e depois cobrar por isso.

**Cura:** toda métrica cobrada é otimizada — inclusive por caminhos que não melhoram nada. Pergunte sempre **que decisão essa métrica apoia**. Se ela não muda nenhuma decisão, ela não serve; se ela virou meta, ela parou de medir.

### Maturidade confundida com qualidade

**Sintoma:** *"somos nível 3, então nosso software é bom"*.

**Causa:** confundir maturidade **de processo** com qualidade **de produto**.

**Cura:** maturidade diz que o processo é definido e repetível — o que aumenta a chance de qualidade, sem garanti-la. É possível produzir software ruim de forma muito madura, e ótimo software num processo caótico. As duas coisas se medem separado.

### Documentação escrita para ninguém

**Sintoma:** um documento de 60 páginas entregue no fim do projeto, que ninguém abriu.

**Causa:** documentar por exigência, sem leitor definido.

**Cura:** antes de escrever, responda **quem lê e para decidir o quê**. Documento sem leitor é custo puro — e pior, dá a sensação de que o assunto está resolvido.

### Documentação que envelhece em silêncio

**Sintoma:** o documento descreve um sistema que mudou há oito meses, e alguém toma decisão com base nele.

**Causa:** documento separado da coisa que ele descreve, sem responsável pela atualização.

**Cura:** **documentação errada é pior que documentação ausente** — a ausente ninguém usa; a errada engana. Ou o documento vive perto do que descreve e é atualizado junto, ou ele leva data e um dono.

### Ferramenta ágil com gestão sequencial por trás

**Sintoma:** o time usa quadro e sprint, mas o escopo, o prazo e o orçamento foram todos fechados no início e não se discutem.

**Causa:** trocar a ferramenta é barato; mudar o contrato e a expectativa da diretoria não é.

**Cura:** a ferramenta não é o método. Se as três variáveis estão travadas, o projeto é preditivo — e chamar as fases de "sprint" só engana o time, que descobre no fim que a adaptação nunca foi possível.

### O plano de comunicação que é uma lista de reuniões

**Sintoma:** todo mundo é convidado para tudo, e ninguém sabe o que aconteceu.

**Causa:** confundir comunicar com reunir.

**Cura:** o plano responde, por interessado: **o que ele precisa saber, com que frequência, em que formato e quem envia**. A diretoria quer uma página por mês; o time quer o detalhe todo dia. Mandar o mesmo para os dois falha nos dois.

---

## Parte 4 — Entrega, usuário e governança

### O *branch* longo tratado como cuidado

**Sintoma:** *"vou terminar tudo direitinho antes de integrar"* — e três semanas depois a integração leva dois dias.

**Causa:** parece prudente adiar a integração até estar pronto.

**Cura:** **o conflito cresce com o tempo.** Integrar cedo e com frequência transforma um problema grande e imprevisível em vários pequenos e baratos. Adiar não evita o custo: multiplica.

### Entrega contínua confundida com implantação contínua

**Sintoma:** *"não podemos fazer entrega contínua, o negócio não aceita mudança todo dia"*.

**Causa:** os dois termos são parecidos e a sigla é a mesma.

**Cura:** **entrega contínua** é estar sempre *pronto* para implantar; **implantação contínua** é implantar automaticamente. A primeira é decisão de engenharia e quase sempre vale a pena; a segunda é decisão de negócio. Recusar a segunda não obriga a abrir mão da primeira.

### Mudança sem caminho de volta

**Sintoma:** a implantação quebrou e a única saída é corrigir para frente, com o sistema fora do ar.

**Causa:** planejar a subida e não planejar a descida.

**Cura:** toda mudança relevante precisa de **como voltar** decidido antes de subir. Se voltar for impossível — migração de dados destrutiva, por exemplo —, isso muda o risco e precisa estar escrito.

### Observabilidade confundida com monitoramento de servidor

**Sintoma:** os painéis mostram processador e memória, e ninguém percebeu que 30% dos pedidos falham há dois dias.

**Causa:** medir a máquina em vez do que o usuário faz.

**Cura:** instrumentar o **comportamento do negócio** — pedido criado, pagamento confirmado, entrega concluída. Servidor saudável com serviço quebrado é o caso mais comum, e o mais caro de descobrir tarde.

### Manutenção tratada como "corrigir defeito"

**Sintoma:** o orçamento de manutenção cobre só correção, e toda melhoria vira "projeto novo".

**Causa:** o nome sugere conserto.

**Cura:** manutenção é **corretiva, adaptativa, perfectiva e preventiva** — e a corretiva costuma ser a menor fatia. Adaptar-se a uma lei nova não é defeito de ninguém, mas consome o mesmo time.

### UX confundido com UI

**Sintoma:** *"vamos melhorar a experiência" e o que muda é a paleta de cores.*

**Causa:** a interface é a parte visível, e a única em que é fácil mexer.

**Cura:** UI é o que se vê; **UX é o que acontece com a pessoa** — quantos passos, quanto ela espera, o que ela entende quando dá errado. Uma tela bonita que exige 11 cliques piorou a experiência.

### Acessibilidade tratada como fase final

**Sintoma:** *"depois a gente adapta"* — e depois custa três vezes mais, ou não acontece.

**Causa:** confundir acessibilidade com ajuste visual.

**Cura:** ela atravessa estrutura, fluxo e conteúdo. Decidida no início, é quase de graça; retrofitada, é reconstrução. E, em serviço público, é obrigação legal e não escolha.

### ITIL aplicado a projeto

**Sintoma:** o projeto adota gestão de incidentes e catálogo de serviços e afunda em cerimônia.

**Causa:** os arcabouços parecem intercambiáveis porque todos falam de processo.

**Cura:** **ITIL é sobre serviço em operação; PMBOK é sobre projeto.** Cada um responde uma pergunta diferente, e usar o errado importa burocracia sem trazer benefício. Antes de adotar um, escreva a pergunta que você quer que ele responda.

### Governança confundida com burocracia

**Sintoma:** *"governança só atrasa"*.

**Causa:** conhecer governança apenas pelos seus sintomas ruins — comitê que não decide, formulário que ninguém lê.

**Cura:** governança responde **quem decide, quem responde e quem audita**. Um projeto sem isso não é mais rápido: ele apenas descobre mais tarde que a decisão foi tomada por quem não podia tomá-la.

---

## Método universal de revisão

Antes de entregar qualquer artefato deste curso, faça as quatro perguntas:

1. **Quem lê isto, e para decidir o quê?** Se não há leitor nem decisão, o artefato não precisa existir;
2. **O que aqui é fato e o que é premissa?** Premissa não marcada é a origem da maioria dos desastres de projeto;
3. **Qual alternativa eu descartei, e por quê?** Decisão sem alternativa registrada não é decisão, é hábito;
4. **O que eu perco com esta escolha?** Se a resposta for "nada", você ainda não entendeu a escolha.

---

🏠 [Voltar ao início](../README.md)
