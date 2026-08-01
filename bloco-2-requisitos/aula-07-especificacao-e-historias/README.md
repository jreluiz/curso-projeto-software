# Aula 07 — Especificação: Documento e Histórias

> 🎯 Objetivos: escrever histórias de usuário que passam no INVEST, derivar critérios de aceite verificáveis e registrar glossário e regras de negócio de um domínio.
> 🎬 Slides da aula: [apresentacao-07-especificacao-e-historias.pdf](apresentacao/apresentacao-07-especificacao-e-historias.pdf)

## 1. Dois formatos, um mesmo objetivo

Você elicitou. Tem páginas de anotação, a norma de uso dos espaços e um resumo da entrevista. Agora precisa transformar isso em algo que **outra pessoa consiga construir e testar**.

Existem dois formatos consagrados, e a escolha entre eles não é de moda:

| | **Documento de requisitos** | **História de usuário** |
|---|---|---|
| O que é | lista numerada e completa, escrita antes | um lembrete de conversa, escrito quando for necessário |
| Otimiza para | contrato, auditoria, rastreabilidade | adaptação e diálogo |
| Fecha quando | é aprovado | a conversa acontece e os critérios são acordados |
| Cai bem em | escopo fechado, exigência regulatória, time distribuído | cliente presente, entrega incremental |
| Falha quando | o requisito muda toda semana | não há ninguém para conversar |

Repare que a diferença **não** é rigor: história de usuário malfeita é vaga, mas história de usuário bem-feita, com critérios de aceite, é tão precisa quanto um requisito numerado. A diferença é **quando** a precisão aparece — antes de tudo, ou no momento de construir.

> 💡 A frase que resume a intenção das histórias: *o cartão não é a especificação, é a promessa de uma conversa.* Se a conversa não acontecer, você tem um formato ágil com o conteúdo de um bilhete.

> 📖 Sommerville trata da especificação de requisitos e dos formatos de documento no capítulo de engenharia de requisitos; histórias de usuário aparecem no capítulo de desenvolvimento ágil.

## 2. O template

A forma mais usada tem três partes, e cada uma responde a uma pergunta:

```
Como <papel>,
quero <ação ou capacidade>
para que <benefício>.
```

| Parte | Pergunta | Por que importa |
|---|---|---|
| Como ⟨papel⟩ | **quem?** | força identificar o interessado; "como usuário" quase sempre esconde preguiça |
| quero ⟨ação⟩ | **o quê?** | a capacidade, não a tela |
| para que ⟨benefício⟩ | **por quê?** | é o que permite priorizar — e às vezes revela que a ação pedida não era a melhor |

Do sistema-guia:

> **H-01** — Como **aluno**, quero **ver os espaços livres num período** para que **eu não atravesse o campus atrás de sala vazia**.
> **H-02** — Como **professor**, quero **reservar uma sala declarando que é para banca** para que **minha reserva tenha a prioridade prevista na norma**.
> **H-03** — Como **infraestrutura**, quero **interditar um espaço e avisar quem tinha reserva** para que **eu consiga fazer o conserto sem alguém aparecer para usar uma sala interditada**.

> ⚠️ **O "para que" é a parte que mais some, e é a mais valiosa.** Sem ele, ninguém consegue priorizar — e ninguém percebe quando a ação pedida não é a melhor forma de obter aquele benefício. Uma história sem benefício é um pedido; com benefício, é um problema a resolver.

## 3. INVEST

Seis critérios para saber se a história está pronta para entrar em um ciclo de trabalho:

| Letra | Critério | A história falha quando |
|---|---|---|
| **I** | *Independent* — independente | só faz sentido depois de outras três |
| **N** | *Negotiable* — negociável | já vem com a solução fechada, sem espaço para conversa |
| **V** | *Valuable* — valiosa | entrega valor a quem constrói, não a quem usa |
| **E** | *Estimable* — estimável | ninguém consegue dizer se é grande ou pequena |
| **S** | *Small* — pequena | não cabe num ciclo de trabalho |
| **T** | *Testable* — testável | não dá para dizer objetivamente se ficou pronta |

Três exemplos defeituosos e o conserto:

| Defeituosa | Falha em | Consertada |
|---|---|---|
| "Como usuário, quero um sistema de reservas" | **S**, **T** | quebrar em consultar, reservar, cancelar, confirmar uso — cada uma testável |
| "Como desenvolvedor, quero criar a tabela de espaços" | **V** | não é história de usuário; é tarefa técnica dentro de outra história |
| "Como aluno, quero que o sistema seja rápido" | **T** | vira requisito não-funcional com número, não história |

> 💡 **Nem tudo precisa ser história.** Requisito não-funcional, regra de negócio e tarefa técnica têm lugar próprio. Forçar tudo no formato "como… quero… para que…" produz frases tortas — como a terceira linha da tabela, que todo mundo já viu.

> 🧩 **Ponte com POO:** o "S" de *small* tem um parente no projeto orientado a objetos. Uma história grande demais para um ciclo e uma classe que faz coisas demais falham pelo mesmo motivo: **misturam responsabilidades que mudam por razões diferentes.** A Aula 13 dá nome a isso.

## 4. Critérios de aceite

A história diz o que se quer. O **critério de aceite** diz **como saber que ficou pronto** — e é ele que impede as duas doenças clássicas: o "quase pronto" eterno e a discussão de entrega.

Bons critérios são **específicos, observáveis e sem ambiguidade**. Para a H-03:

> **H-03** — Como infraestrutura, quero interditar um espaço e avisar quem tinha reserva.
>
> **Critérios de aceite:**
> 1. A interdição exige espaço, período e motivo;
> 2. Reservas existentes no período interditado passam à situação "interrompida";
> 3. Cada solicitante afetado recebe notificação em até 5 minutos, com espaço, período e motivo;
> 4. O espaço interditado não aparece nas consultas de disponibilidade daquele período;
> 5. A interdição prevalece sobre qualquer reserva, inclusive já confirmada (`RN-05`);
> 6. Uma interdição pode ser cancelada; nesse caso o espaço volta a aparecer, mas **as reservas interrompidas não são restauradas automaticamente**.

Repare no critério 6: ele responde a uma pergunta que a história não fazia. **É normal e desejável** — escrever critério é onde as lacunas aparecem, e é muito mais barato que descobri-las depois.

> ⚠️ Critério de aceite **não é roteiro de teste**. Ele diz *o que* precisa ser verdade, não *como* clicar. "Clicar em Interditar, preencher o campo Motivo e apertar Salvar" amarra a interface e envelhece na primeira mudança de tela.

## 5. BDD e Gherkin

Quando o critério precisa ser lido por três públicos diferentes — cliente, quem constrói e quem testa —, vale escrevê-lo num formato estruturado. É o que faz o **desenvolvimento guiado por comportamento** (BDD), com a notação **Gherkin**:

```gherkin
Funcionalidade: Interdição de espaço

  Cenário: Interdição atinge reserva já confirmada
    Dado que o Laboratório B-12 tem uma reserva confirmada para 12/08 das 14h às 16h
    Quando a infraestrutura interdita o Laboratório B-12 de 12/08 08h a 13/08 18h
    Então a reserva passa à situação "interrompida"
    E o solicitante recebe notificação em até 5 minutos
    E o Laboratório B-12 não aparece nas consultas para esse período

  Cenário: Interdição em período sem reservas
    Dado que a Sala de Estudo 3 não tem reservas para 20/08
    Quando a infraestrutura interdita a Sala de Estudo 3 em 20/08
    Então nenhuma notificação é enviada
    E a interdição é registrada normalmente
```

A estrutura é sempre a mesma:

| Palavra | Significa |
|---|---|
| **Dado** (*Given*) | o estado do mundo antes |
| **Quando** (*When*) | a ação que dispara o comportamento |
| **Então** (*Then*) | o resultado observável |
| **E** / **Mas** | continuação de qualquer um dos três |

Duas virtudes práticas: o cliente **consegue ler e discordar**, e o texto pode ser ligado a testes automatizados — o mesmo arquivo vira documentação e verificação, e as duas não divergem.

> ⚠️ O defeito mais comum em Gherkin é escrever interface no **Quando**: *"Quando o usuário clica no botão Interditar"*. O **Quando** é o comportamento — *"quando a infraestrutura interdita o espaço"*. Se o cenário quebra quando a tela muda de lugar, ele estava testando a tela.

## 6. Glossário e regras de negócio

Duas seções que custam pouco e evitam muito retrabalho.

**Glossário do domínio.** Escrito **com** o cliente, uma linha por termo. No sistema-guia, ele já existe — é a [seção 5](../../recursos/sistema-guia.md#5-vocabulário-do-domínio). Sem ele, "espaço", "sala", "ambiente" e "local" convivem no mesmo documento significando ora a mesma coisa, ora coisas diferentes, e ninguém percebe até o sistema estar pronto.

**Regras de negócio.** São verdadeiras **mesmo que nenhum sistema exista**, e por isso não pertencem a nenhuma história em particular: elas atravessam várias. No sistema-guia são `RN-01` a `RN-08`.

| | História de usuário | Regra de negócio |
|---|---|---|
| Origem | um interessado quer algo | o domínio, a norma, a lei |
| Vive | num ciclo de trabalho, e sai do backlog | pelo tempo em que a norma valer |
| Muda quando | a prioridade muda | a norma muda |
| Onde fica | backlog | documento do domínio, referenciada pelas histórias |

> 💡 A ligação entre os dois é o que dá **rastreabilidade**: a H-02 realiza a `RN-04`; o critério 5 da H-03 realiza a `RN-05`. Quando a norma mudar, essa ligação diz exatamente o que precisa ser revisto. A Aula 08 volta a isso.

## 🏋️ Exercícios da aula

Na pasta `aula-07/` do seu repositório:

1. **`ex01.md`** — escreva **seis histórias de usuário** do sistema-guia, cobrindo pelo menos três papéis diferentes, numeradas `H-01` a `H-06`. Nenhuma pode usar "como usuário". Para cada uma, marque qual etapa do [fluxo do negócio](../../recursos/sistema-guia.md#6-o-fluxo-do-negócio) ela atende — e, se sobrar etapa sem história, diga se é lacuna ou decisão;
2. **`ex02.md`** — as cinco histórias abaixo falham no INVEST. Para cada uma: aponte **quais letras** ela viola, explique em uma linha e reescreva. (a) "Como usuário, quero um sistema fácil de usar"; (b) "Como desenvolvedor, quero refatorar o módulo de agenda"; (c) "Como aluno, quero reservar salas, cancelar reservas, ver histórico e receber notificações"; (d) "Como professor, quero um botão azul no topo da tela para reservar"; (e) "Como coordenação, quero relatórios";
3. **`ex03.md`** — escolha **três** das suas histórias do `ex01` e escreva os **critérios de aceite** de cada uma — mínimo 4 por história, todos observáveis. Pelo menos um critério de cada história deve tratar do que acontece **quando dá errado**. Marque quais critérios nasceram de uma regra de negócio, citando o `RN-NN`;
4. **`ex04.md`** — converta **três critérios de aceite** do `ex03` para Gherkin, um cenário cada, em português. Depois escreva **um quarto cenário** para o mesmo comportamento, cobrindo um caminho de exceção. Nenhum `Quando` pode mencionar botão, tela ou clique — se o seu mencionar, reescreva e explique o que mudou;
5. **Desafio 🌶️ `ex05.md`** — abaixo está o trecho de uma conversa gravada. **Monte o glossário do domínio** a partir dela.

   > **Secretaria:** — Aí a pessoa manda o pedido, e eu vejo na agenda se a sala tá livre.
   > **Analista:** — Agenda é a planilha?
   > **Secretaria:** — É, a planilha é a agenda. Cada aba é um ambiente. Aí eu marco o horário e respondo confirmando.
   > **Analista:** — E se a pessoa não aparecer?
   > **Secretaria:** — Aí fica marcado do mesmo jeito, né. A marcação continua lá. Só que o professor liga reclamando que a sala tava vazia e a agenda dizia que tinha aula. Aí eu tiro o agendamento.
   > **Analista:** — Então "marcação" e "agendamento" são a mesma coisa?
   > **Secretaria:** — Mais ou menos. Agendamento é quando eu confirmo. Marcação é o pedido, antes de eu olhar.

   Entregue: **(a)** o glossário com no mínimo 6 termos, cada um com a definição que você proporia; **(b)** a lista dos termos que a secretaria usou como sinônimos e não são; **(c)** as **três perguntas** que você faria na próxima conversa para fechar as definições que ficaram ambíguas; **(d)** um parágrafo apontando o **conceito que existe no domínio e ainda não tem nome nenhum** — ele está na conversa, e é o mais importante de todos.

## 🧠 Revisão

[8 questões de múltipla escolha](revisao/README.md) para conferir se os conceitos ficaram sólidos. Responda sem consultar a aula — depois volte e corrija.

## ✅ Entrega

```bash
git add aula-07/
git commit -m "Resolve exercícios da aula 07 (especificação e histórias)"
git push
```

---

⬅️ [Aula 06 — Elicitação](../aula-06-elicitacao/README.md) | ➡️ [Aula 08 — Análise, priorização e validação](../aula-08-analise-priorizacao-validacao/README.md)
