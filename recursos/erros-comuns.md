# 🧯 Erros Comuns

Em Java, o compilador aponta o erro. Em SQL, o banco aponta. **Aqui nada aponta.** Um requisito ambíguo compila; um diagrama errado renderiza igualzinho ao certo; uma arquitetura ruim funciona por seis meses. O preço só chega depois, e chega em outra pessoa.

Este arquivo é o substituto do compilador: o catálogo das patologias que aparecem toda vez, com o sintoma que as denuncia e a pergunta que as resolve. Volte aqui antes de entregar qualquer artefato.

**Índice:** [Processo e agilidade](#parte-1--processo-e-agilidade) · [Requisitos](#parte-2--requisitos) · [Casos de uso](#parte-3--casos-de-uso) · [Classes](#parte-4--diagrama-de-classes) · [Projeto e arquitetura](#parte-5--projeto-e-arquitetura)

---

## Parte 1 — Processo e agilidade

### "Ágil quer dizer que não documentamos"

**Sintoma:** o time não escreve nada e cita o Manifesto quando alguém reclama.

**Causa:** ler os quatro valores como se fossem quatro negações. O Manifesto diz *"software em funcionamento **mais que** documentação abrangente"* — e depois diz, com todas as letras, que os itens à direita também têm valor.

**Cura:** a pergunta certa não é *"documentamos ou não?"*, é **"qual documento alguém vai ler depois?"**. Um documento de 80 páginas que ninguém abre é desperdício em qualquer processo. Um ADR de meia página que explica por que o banco é relacional é barato e salva o time que chega no ano que vem.

---

### Cascata disfarçada de sprint

**Sintoma:** sprint 1 é "levantar requisitos", sprint 2 é "modelar", sprint 3 é "programar", sprint 4 é "testar".

**Causa:** trocar os nomes das fases sem trocar a lógica. O ciclo continua sendo uma sequência única de fases, e o cliente continua vendo software só no fim.

**Cura:** o teste é simples: **ao final de cada iteração, existe algo funcionando que o cliente consegue usar e criticar?** Se a resposta é não, a iteração não é iteração — é uma fase com nome novo. Iterativo significa que *todas* as atividades acontecem em *cada* ciclo, sobre uma fatia menor do produto.

---

### Cascata tratada como erro histórico

**Sintoma:** o aluno responde "cascata" como se fosse a alternativa errada em qualquer questão.

**Causa:** o curso de todo mundo conta a história do cascata como uma piada, e ninguém diz onde ele ganha.

**Cura:** cascata vence quando **os requisitos são estáveis e a mudança é cara ou proibida**: sistema embarcado que vai para a fábrica, software com certificação regulatória, contrato de escopo fechado com órgão público. O erro nunca foi o modelo — foi aplicá-lo onde o requisito muda toda semana.

---

### O quadro Kanban que é um cemitério

**Sintoma:** 14 cartões em "Em andamento", nenhum em "Concluído" há dias.

**Causa:** quadro sem **limite de WIP**. Sem limite, todo mundo começa e ninguém termina — e trabalho começado não entrega valor nenhum.

**Cura:** limite de trabalho em andamento por coluna, e a regra que vem junto: **quando bate o limite, você não começa outro cartão — você ajuda a terminar um.** O gargalo aparece sozinho na coluna que enche.

---

### Confundir o papel com a pessoa

**Sintoma:** "o Scrum Master é o chefe do time"; "o Product Owner é quem programa o que sobra".

**Causa:** encaixar papéis novos no organograma antigo.

**Cura:** papel é **responsabilidade**, não cargo. Product Owner responde por *o que* e em que ordem; o time responde por *como* e por quanto cabe; o Scrum Master responde por remover impedimento e proteger o processo — e não decide escopo nem manda em ninguém. Uma pessoa pode acumular papéis; o que não pode é o papel sumir.

---

### Velocidade tratada como meta

**Sintoma:** "precisamos aumentar a velocidade da equipe para 40 pontos".

**Causa:** transformar um instrumento de previsão em instrumento de avaliação.

**Cura:** velocidade serve para **planejar a próxima iteração**, não para comparar times nem para cobrar. É trivialmente inflacionável — basta estimar tudo mais alto. Métrica que vira meta deixa de ser métrica.

> ⚠️ Vale para as métricas DORA também. Frequência de implantação alta com taxa de falha alta não é maturidade — é pressa.

---

## Parte 2 — Requisitos

### O requisito que já é a solução

**Sintoma:** *"O sistema deve ter um botão vermelho no canto superior direito para cancelar a reserva."*

**Causa:** o cliente descreve a tela que imaginou, e o analista anota a tela em vez da necessidade.

**Cura:** pergunte **"por quê?"** até chegar na necessidade, e escreva o requisito lá em cima: *"O solicitante deve poder cancelar uma reserva futura."* Onde fica o botão e de que cor ele é são decisões de projeto — e devem ficar livres para melhorar sem alterar o requisito.

> 💡 Teste rápido: se o requisito menciona **botão, tela, menu, tabela do banco ou nome de tecnologia**, quase sempre ele é uma solução disfarçada.

---

### O requisito que ninguém consegue testar

**Sintoma:** *"O sistema deve ser rápido"*, *"a interface deve ser amigável"*, *"o sistema deve ser seguro"*.

**Causa:** escrever o adjetivo em vez do critério. Todo mundo concorda com a frase — e é exatamente esse o problema: concordar não custa nada quando ninguém sabe o que ela exige.

**Cura:** todo requisito precisa responder à pergunta **"como eu saberia que isto foi cumprido?"**. Se não há resposta objetiva, ele não é requisito — é desejo.

| Desejo | Requisito |
|---|---|
| O sistema deve ser rápido | A busca por espaço livre deve responder em até 2 s para 95% das requisições, com 500 usuários simultâneos |
| A interface deve ser amigável | Um aluno que nunca usou o sistema deve concluir uma reserva em até 3 minutos, sem ajuda |
| O sistema deve ser seguro | Só o próprio solicitante, a secretaria e a infraestrutura podem ver quem reservou cada espaço |

---

### Funcional confundido com não-funcional

**Sintoma:** "*login* é requisito não-funcional porque é de segurança".

**Causa:** classificar pelo **assunto** em vez de pela natureza.

**Cura:** a pergunta é **"isto é algo que o sistema faz, ou uma qualidade de como ele faz?"**. "Autenticar o usuário" é uma função — o sistema faz isso, tem entrada e saída. "As senhas devem ser armazenadas com *hash* e sal" é uma restrição de qualidade sobre essa função. O mesmo assunto (segurança) gera os dois tipos.

> ⚠️ Atalho que funciona: se você consegue escrever um caso de uso para aquilo, é funcional. Não-funcional é o que atravessa **vários** casos de uso ao mesmo tempo.

---

### Os não-funcionais que ninguém escreve

**Sintoma:** o documento tem 40 requisitos funcionais e três não-funcionais, todos sobre desempenho.

**Causa:** cliente nenhum pede acessibilidade, LGPD ou tratamento de pico espontaneamente. Ele acha que "é óbvio que vai funcionar".

**Cura:** os não-funcionais quase sempre são **derivados do contexto**, não coletados. Passe esta lista em todo sistema: desempenho sob pico · disponibilidade · segurança e controle de acesso · privacidade e dados pessoais (LGPD) · acessibilidade · usabilidade · dispositivos e navegadores suportados · volume de dados · retenção e trilha de auditoria · idioma. Em cada item, ou você escreve um requisito, ou escreve por que ele não se aplica.

---

### O stakeholder que ninguém ouviu

**Sintoma:** o sistema atende lindamente ao usuário final e é inviável para quem opera, audita ou paga.

**Causa:** confundir *stakeholder* com *usuário*. Quem nunca vai abrir o sistema também tem interesse nele: a coordenação que precisa do relatório de ocupação, a infraestrutura que precisa interditar a sala, o setor que responde pelo patrimônio.

**Cura:** liste os interessados **antes** dos requisitos e, para cada um, escreva o que ele ganha e o que ele teme. E procure ativamente o **conflito** — se todos os interesses concordam, você não terminou o levantamento.

> 💡 No sistema-guia: o grupo de alunos reservou a sala há duas semanas; o professor precisa dela para uma banca marcada ontem. Os dois têm razão, e alguém precisa decidir. Essa decisão é um requisito.

---

### Requisito com "e" no meio

**Sintoma:** *"O sistema deve permitir que a infraestrutura bloqueie o espaço e notifique os atingidos e exporte o relatório em PDF."*

**Causa:** anotar a frase do cliente inteira, do jeito que ela saiu.

**Cura:** um requisito, uma verificação. Se metade pode estar pronta e a outra metade não, são dois requisitos. Requisito composto também estraga a rastreabilidade: não dá para dizer que "RF-07 está implementado" quando 40% dele não está.

---

### O documento sem glossário

**Sintoma:** "espaço", "sala", "ambiente" e "local" aparecem no mesmo documento significando ora a mesma coisa, ora coisas diferentes.

**Causa:** o vocabulário do cliente é ambíguo e ninguém fixou os termos.

**Cura:** glossário do domínio junto do documento, uma linha por termo, escrito **com** o cliente. É a página mais barata de escrever e a que mais evita retrabalho — inclusive porque vira o vocabulário do código depois.

---

## Parte 3 — Casos de uso

### O caso de uso que virou tela

**Sintoma:** casos de uso chamados "Tela de login", "Menu principal", "Preencher formulário de cadastro", "Clicar em salvar".

**Causa:** modelar a interface em vez do objetivo.

**Cura:** um caso de uso é um **objetivo do ator que produz um resultado de valor observável**. Teste da frase: *"o aluno usa o sistema para \_\_\_\_\_\_"*. Ninguém usa o sistema para "clicar em salvar" — usa para **reservar um espaço**. Se o nome não é `verbo + complemento` no infinitivo e não vale como resposta ao "para quê", não é caso de uso.

---

### O sistema como ator dele mesmo

**Sintoma:** o diagrama tem um bonequinho chamado "Sistema", "Banco de Dados" ou "Servidor".

**Causa:** confundir ator com componente.

**Cura:** ator é **externo à fronteira** e interage com o sistema por vontade própria ou por evento. O banco de dados está *dentro*. Já um sistema externo de verdade — o cadastro acadêmico que confirma a matrícula, o gateway que envia e-mail — é ator, e ator legítimo.

> ⚠️ Ator é **papel**, não pessoa. A mesma professora é "Solicitante" quando reserva a sala e "Coordenação" quando pede o relatório de ocupação: dois atores, uma pessoa.

---

### `include` e `extend` trocados

**Sintoma:** `Reservar espaço` --extend--> `Autenticar`.

**Causa:** as duas setas parecem intercambiáveis e a direção da seta é contraintuitiva no `extend`.

**Cura:** decore pela obrigatoriedade e pela direção:

| | Significa | Quem aponta para quem | Exemplo |
|---|---|---|---|
| `include` | O comportamento **sempre** acontece; foi extraído para não repetir | O caso **base** aponta para o incluído | `Reservar espaço` ──include──▶ `Autenticar` |
| `extend` | O comportamento acontece **às vezes**, sob condição | O caso **extensor** aponta para o base | `Reservar com prioridade` ──extend──▶ `Reservar espaço` |

Regra prática: leia em voz alta *"isto acontece sempre?"*. Sempre → `include`. Só quando… → `extend`, e a seta vai na direção contrária da que você ia desenhar.

> 💡 Na dúvida, **não use nenhum dos dois.** Dois casos de uso independentes e bem especificados valem mais que um diagrama cheio de setas que ninguém interpreta igual.

---

### Granularidade em qualquer lugar menos no lugar

**Sintoma:** o mesmo diagrama tem `Usar o sistema` e `Digitar CPF`.

**Causa:** não existir um critério de tamanho, então cada caso de uso sai do tamanho do humor de quem escreveu.

**Cura:** o critério é a **sessão**: um caso de uso é o que o ator faz em um uso contínuo do sistema, com começo, meio e fim, e que ele consideraria "resolvido" ao sair. `Digitar CPF` é um passo do fluxo. `Usar o sistema` é o sistema inteiro. `Reservar um laboratório para a semana que vem` está no ponto.

---

### O diagrama que é o entregável

**Sintoma:** dez elipses lindamente organizadas e nenhuma especificação escrita.

**Causa:** o diagrama é rápido, bonito e cabe no slide. A especificação dá trabalho.

**Cura:** o **diagrama de casos de uso é o índice; o conteúdo é a especificação textual** — fluxo principal, fluxos alternativos, fluxos de exceção, pré e pós-condições. Quem vai construir o sistema lê a especificação, não as elipses. Um diagrama sem nenhuma especificação por trás não documenta nada.

---

### O fluxo sem exceção

**Sintoma:** a especificação tem oito passos e todos dão certo.

**Causa:** escrever o caminho que você imaginou usando o sistema num dia bom.

**Cura:** em cada passo do fluxo principal, pergunte **"e se não?"** — e se o horário acabou de ser tomado, e se o aluno não tem os pré-requisitos, e se o serviço externo não responde, e se o usuário fecha o navegador no meio. O fluxo principal descreve o sistema; **os fluxos de exceção são onde mora a regra de negócio de verdade.**

---

## Parte 4 — Diagrama de classes

### Verbo como nome de classe

**Sintoma:** classes chamadas `CadastrarEspaco`, `GerenciarAgenda`, `ProcessarReserva`.

**Causa:** trazer o hábito de pensar em funções para um diagrama que descreve **coisas**.

**Cura:** classe é **substantivo** — representa algo que existe no domínio, tem identidade e guarda estado. `CadastrarEspaco` não é uma coisa, é uma operação; ela pertence a alguma classe, provavelmente com o nome `cadastrar()`. Se a "classe" só tem métodos e nenhum atributo com significado, ela é um procedimento com fantasia de objeto.

---

### O atributo que era classe (e vice-versa)

**Sintoma:** `Reserva` com os atributos `espaco`, `nomeDoEspaco`, `capacidadeDoEspaco`, `recursosDoEspaco`.

**Causa:** achatar uma coisa do domínio dentro de outra.

**Cura:** se o candidato a atributo tem **atributos próprios** ou **participa de relacionamentos próprios**, ele é classe. Espaço tem código, capacidade, recursos e uma porção de reservas: é classe, e `Reserva` se associa a ela. O caminho contrário também é erro: `Sexo` como classe com dois objetos não é modelagem, é burocracia.

---

### Multiplicidade lida num sentido só

**Sintoma:** `Espaco 1 ── * Reserva` e ninguém perguntou se uma reserva pode ocupar dois espaços.

**Causa:** ler a associação na direção em que ela foi escrita e parar por aí.

**Cura:** **toda associação tem duas multiplicidades e as duas precisam ser lidas em voz alta**, no plural: *"Um espaço recebe quantas reservas?"* e *"Uma reserva ocupa quantos espaços?"*. E cuidado com o mínimo: `1` e `0..1` dizem coisas muito diferentes sobre o mundo — um obriga, o outro permite ausência.

---

### Agregação × composição decidida no chute

**Sintoma:** losangos pretos e brancos distribuídos por intuição estética.

**Causa:** a definição de livro ("todo-parte") vale para as duas, então ela não decide nada.

**Cura:** duas perguntas, nesta ordem:

1. **A parte pode existir sem o todo?** Se pode, é agregação (losango branco);
2. **Se o todo for destruído, a parte vai junto?** Se vai, é composição (losango preto).

`Espaco` e `Recurso`: desativar a sala não faz o projetor deixar de existir → agregação. `Reserva` e `ConfirmacaoDeUso`: a confirmação só existe dentro daquela reserva e morre com ela → composição.

> 💡 Se a distinção não muda nenhuma decisão de implementação nem nenhuma regra do domínio, **use associação simples e siga em frente**. Losango errado documenta uma mentira; losango ausente só documenta menos.

---

### Herança onde cabia composição

**Sintoma:** `SalaDeEstudo` e `Laboratorio` como subclasses de `Espaco`, e a sala que foi convertida em laboratório no recesso não cabe no modelo.

**Causa:** herança é a primeira ferramenta que a gente aprende, e vira martelo.

**Cura:** herança é para **é-um permanente e imutável**. Se o objeto pode **mudar de categoria durante a vida**, ou pertencer a **duas categorias ao mesmo tempo**, herança está errada — o que muda é um atributo, um estado ou um objeto associado (`Espaco` tem um `TipoDeUso`, que tem período de vigência).

> ⚠️ Teste do "é-um": *"toda sala de estudo é uma sala de estudo, para sempre?"* Se você precisa dizer "é, mas...", não é herança.

---

### Classe de análise com detalhe de implementação

**Sintoma:** no diagrama da fase de análise já aparecem `EspacoDAO`, `EspacoController`, `idEspaco: Long` e `List<Reserva>`.

**Causa:** misturar o modelo que descreve o **domínio** com o modelo que descreve a **solução**.

**Cura:** são dois diagramas com propósitos diferentes, e nesta ordem. A classe de **análise** fala a língua do cliente: `Espaco`, `Reserva`, `Bloqueio` — sem tipo de linguagem, sem *framework*, sem chave técnica. A classe de **projeto** acrescenta tipos, visibilidade, padrões e as classes que só existem por causa da tecnologia. Fazer as duas ao mesmo tempo entrega um diagrama que o cliente não valida e o programador não usa.

---

### O diagrama que ninguém leu como frase

**Sintoma:** o modelo está bonito e afirma, sem que ninguém tenha percebido, que uma reserva pode existir sem espaço.

**Cura:** o ritual final de todo diagrama — leia **cada** associação como uma frase em português e pergunte se é verdade no domínio. Cinco minutos de leitura em voz alta encontram mais defeitos que uma hora encarando o desenho.

---

## Parte 5 — Projeto e arquitetura

### A classe-Deus

**Sintoma:** `SistemaReservas` com 40 métodos: autentica, reserva, calcula ocupação, envia e-mail, gera relatório e formata data.

**Causa:** crescimento por acréscimo. Nunca houve o momento em que alguém decidiu criar essa classe — cada método foi "só mais um".

**Cura:** o teste da descrição em uma frase: **descreva a responsabilidade da classe sem usar "e" e sem usar "gerencia"**. Se não consegue, ela tem mais de uma responsabilidade. Corte pelo motivo de mudar: o que muda quando a regra de prioridade muda não deve estar junto do que muda quando o layout do e-mail muda.

---

### Alta coesão confundida com "classe pequena"

**Sintoma:** o projeto tem 30 classes de uma linha cada, e entender qualquer coisa exige abrir sete arquivos.

**Causa:** transformar uma medida de **pertencimento** numa medida de **tamanho**.

**Cura:** coesão alta é ter **tudo que trata do mesmo assunto no mesmo lugar** — a classe pode ser grande e coesa. Quebrar uma classe coesa em cinco não aumenta a coesão; aumenta o acoplamento entre os pedaços, que é exatamente o contrário do objetivo.

---

### Baixo acoplamento confundido com "sem dependência nenhuma"

**Sintoma:** interfaces e camadas de indireção em cima de código que só tem uma implementação e nunca terá outra.

**Causa:** ler "baixo acoplamento" como "zero acoplamento". Só que módulo que não se conecta a nada não faz parte de sistema nenhum.

**Cura:** acoplamento é inevitável e necessário — o que se controla é **quantidade e tipo**. Depender da **interface** (contrato estável) é acoplamento saudável; depender de **detalhe interno** de outro módulo é o caro. A pergunta é: *"se aquele módulo mudar por dentro, este aqui precisa mudar também?"*.

> ⚠️ Abstração sem segundo caso concreto é dívida, não flexibilidade. Espere o segundo caso aparecer.

---

### Chamar de arquitetura o que é escolha de ferramenta

**Sintoma:** "nossa arquitetura é React com Spring Boot e PostgreSQL".

**Causa:** confundir a **pilha de tecnologia** com a **estrutura do sistema**.

**Cura:** arquitetura são as **decisões difíceis de reverter** e a relação entre as partes: quais são os componentes, como eles se comunicam, onde ficam os dados, o que acontece quando um pedaço cai. Isso continua igual se você trocar o *framework*. Listar tecnologias é o resultado da arquitetura, não a arquitetura.

> 💡 Teste: *"quanto custaria mudar essa decisão daqui a seis meses?"* Caro e espalhado por todo o sistema → é arquitetura. Barato e local → é projeto detalhado, decida depois.

---

### Microsserviços para três usuários

**Sintoma:** o sistema tem 200 usuários, um time de quatro pessoas e sete serviços com bancos separados.

**Causa:** copiar a solução de uma empresa cujo problema você não tem. A Netflix não adotou microsserviços por elegância — adotou por ter centenas de times pisando no pé um do outro.

**Cura:** microsserviços resolvem **problema organizacional e de escala independente**, e cobram caro por isso: rede que falha, transação distribuída, dado duplicado, sete *deploys*, observabilidade. Comece monolito **bem modularizado**; a fronteira que você desenhar por dentro é o que permitirá extrair um serviço no dia em que houver motivo.

---

### O padrão aplicado sem o problema

**Sintoma:** `AbstractStrategyFactoryProvider` numa tela de cadastro com três campos.

**Causa:** ter acabado de estudar padrões e querer usá-los. É uma fase — o importante é que ela acabe antes do projeto final.

**Cura:** todo padrão tem a estrutura **contexto → problema → solução → consequências**. Se você não consegue enunciar o *problema* em uma frase, e as *consequências* (todo padrão cobra alguma coisa: mais classes, mais indireção, mais dificuldade de depurar), não aplique. Padrão é resposta; sem pergunta, é só complexidade com nome bonito.

> ⚠️ E o contrário também conta: reconhecer que você **já implementou** um Observer sem saber o nome é sinal de que entendeu o padrão. O nome serve para conversar, não para justificar.

---

### Singleton usado como variável global

**Sintoma:** `Configuracao.getInstance()` chamado em 40 lugares, inclusive dentro das regras de negócio.

**Causa:** o padrão resolve mesmo um problema real (instância única), e de quebra oferece acesso global de graça — e é o "de graça" que estraga.

**Cura:** o acesso global é o efeito colateral, não o benefício. Ele esconde dependências (a assinatura do método não diz que ele depende daquilo), impede substituir o objeto em teste e acopla todo mundo a um ponto só. Prefira **receber a dependência** por parâmetro ou construtor. Se a unicidade for mesmo obrigatória, mantenha-a — mas passe a instância adiante em vez de buscá-la de qualquer canto.

---

### Verificação confundida com validação

**Sintoma:** "os testes passaram, então o sistema está certo".

**Causa:** as duas palavras parecem sinônimos em português corrente.

**Cura:** duas perguntas diferentes, ambas necessárias:

- **Verificação** — *"estamos construindo o produto **corretamente**?"* Confere o sistema contra a especificação. Testes, revisão de código, análise estática;
- **Validação** — *"estamos construindo o **produto certo**?"* Confere a especificação contra a necessidade real. Demonstração ao cliente, protótipo, teste de aceite.

Um sistema pode passar em 100% dos testes e estar completamente errado: é o caso clássico do requisito bem implementado que ninguém queria.

---

### Dívida técnica usada como sinônimo de código feio

**Sintoma:** toda gambiarra é chamada de "dívida técnica", inclusive as que ninguém escolheu contrair.

**Causa:** a metáfora pegou e virou apelido geral para código ruim.

**Cura:** dívida é uma **decisão consciente de entregar antes pagando juros depois** — e, como toda dívida, ela precisa ser **registrada, com o motivo e a data**. Código ruim feito por descuido ou pressa não é dívida, é defeito: não houve empréstimo, ninguém aprovou e não há plano de pagamento. A diferença importa porque uma se negocia com o negócio e a outra se corrige.

---

## Método universal de revisão

Quando o artefato "parece certo" mas alguma coisa incomoda, rode estas cinco perguntas:

1. **Leia cada linha em voz alta como uma frase em português.** É verdade no domínio? (Serve para requisito, associação, multiplicidade e fluxo.)
2. **Pergunte "como eu saberia que isto foi cumprido?"** Se não há resposta objetiva, não está pronto.
3. **Pergunte "e se não?" em cada passo.** O caminho feliz é a parte fácil.
4. **Pergunte "por que não a outra alternativa?"** Se você não considerou nenhuma outra, não decidiu — só aceitou a primeira ideia.
5. **Pergunte "o que muda se isto mudar?"** É assim que se enxerga acoplamento, e é assim que se separa arquitetura de detalhe.

> 📏 As cinco cabem em uma frase só: **um artefato de projeto não vale pelo que ele mostra, vale pelo que ele permite alguém questionar.**

---

🏠 [Voltar ao início](../README.md)
