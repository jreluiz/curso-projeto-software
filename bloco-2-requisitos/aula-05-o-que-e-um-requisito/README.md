# Aula 05 — O Que É um Requisito

> 🎯 Objetivos: distinguir requisitos funcionais de não-funcionais, identificar interessados e seus conflitos e reconhecer o requisito que chegou disfarçado de solução.
> 🎬 Slides da aula: [apresentacao-05-o-que-e-um-requisito.pdf](apresentacao/apresentacao-05-o-que-e-um-requisito.pdf)

> 📄 Esta aula abre o bloco de requisitos e passa a trabalhar em cima do [sistema-guia](../../recursos/sistema-guia.md). Leia o documento antes de continuar — ele tem duas páginas e é o material de todas as aulas até a 16.

## 1. A frase que precisa aguentar peso

A secretaria pede: *"a gente precisa que dê para reservar sala."*

Essa frase vai atravessar todo o projeto. Alguém vai estimá-la, alguém vai projetar em cima dela, alguém vai testá-la, e daqui a dois anos alguém vai discutir se o sistema cumpre o que prometeu — olhando para ela. **A frase é um contrato**, e a maioria das frases que os clientes dizem não aguenta esse peso.

Repare no que ela não responde:

- Reservar o quê: uma sala qualquer, uma sala específica, um horário recorrente?
- Quem pode reservar? Qualquer pessoa da instituição?
- Com quanta antecedência?
- O que acontece quando duas pessoas pedem a mesma sala no mesmo segundo?
- Reservar é o mesmo que **usar**?

Um **requisito** é uma afirmação sobre o que o sistema deve fazer ou sobre a qualidade com que deve fazer, escrita de modo que **duas pessoas diferentes cheguem à mesma conclusão sobre se ele foi cumprido**. Essa última parte é o que separa requisito de conversa.

> 💡 O teste de sanidade de qualquer requisito cabe em uma pergunta: **"como eu saberia que isto foi cumprido?"**. Se não existe resposta objetiva, você ainda não tem um requisito — tem um desejo, e desejos não se contratam nem se testam.

> 📖 Sommerville dedica dois capítulos a requisitos: um sobre tipos e definição, outro sobre o processo de engenharia de requisitos.

## 2. Funcional × não-funcional

Requisitos vêm em duas naturezas, e confundi-las é o erro mais comum do bloco inteiro:

- **Funcional** — algo que o sistema **faz**. Tem entrada, processamento e saída observável;
- **Não-funcional** — uma **qualidade ou restrição** sobre como ele faz. Atravessa várias funções ao mesmo tempo.

| Exemplo | Tipo | Por quê |
|---|---|---|
| O sistema deve permitir cancelar uma reserva futura | **F** | é uma ação, com resultado observável |
| A busca por espaço livre deve responder em até 2 s com 500 usuários simultâneos | **NF** | é uma qualidade da busca, não uma nova função |
| O sistema deve autenticar o usuário | **F** | tem entrada e saída — dá para escrever um caso de uso |
| As senhas devem ser armazenadas com *hash* e sal | **NF** | é uma restrição sobre como a autenticação guarda dado |
| O sistema deve notificar quem teve a reserva deslocada | **F** | ação |
| A notificação deve chegar em até 5 minutos | **NF** | qualidade da ação acima |

Note que **segurança gera os dois tipos**: "autenticar" é função, "guardar senha com *hash*" é restrição. Classificar pelo **assunto** é a origem do erro; classifique pela **natureza**.

> ⚠️ Atalho que funciona quase sempre: **se você consegue escrever um caso de uso para aquilo, é funcional.** Não-funcional é o que aparece em vários casos de uso ao mesmo tempo e não vira nenhum deles sozinho.

> 🧩 **Ponte com POO:** requisito funcional tende a virar **comportamento** — um método, uma operação. Requisito não-funcional raramente vira um método; ele condiciona **como** os métodos são escritos e como as classes se organizam. É uma das razões de qualidade não se resolver "acrescentando uma classe no fim".

## 3. Os não-funcionais que ninguém pede

Cliente nenhum chega dizendo *"quero acessibilidade e conformidade com a LGPD"*. Ele pede funcionalidade e **supõe** que o resto vem junto. Por isso os não-funcionais quase sempre são **derivados do contexto**, não coletados na conversa.

Volte ao [contexto de uso do sistema-guia](../../recursos/sistema-guia.md#8-contexto-de-uso-e-restrições) e veja como cada observação vira requisito:

| O que se observou | O não-funcional que nasce disso |
|---|---|
| O uso explode na semana de provas | desempenho e disponibilidade sob pico, com número |
| Acesso pelo celular, andando pelo campus, na rede que oscila | resposta em conexão instável; funcionar em tela pequena |
| Há espaços acessíveis e usuários que navegam por leitor de tela | conformidade com diretrizes de acessibilidade |
| Saber quem reservou o quê é dado pessoal | quem pode ver, por quanto tempo se guarda, o que fica registrado |
| O Sistema Acadêmico é legado e cai | comportamento da plataforma quando a fonte externa não responde |
| A equipe de TI tem três pessoas | operação simples; nada que exija plantão especializado |

**A lista de verificação que evita esquecimento.** Em todo sistema, passe por estes itens e, para cada um, **ou escreva um requisito, ou escreva por que ele não se aplica**:

desempenho sob pico · disponibilidade · segurança e controle de acesso · privacidade e dados pessoais · acessibilidade · usabilidade · dispositivos e navegadores suportados · volume de dados · retenção e trilha de auditoria · idioma · operação e monitoramento.

> ⚠️ "Não se aplica" **escrito** é uma decisão. "Não se aplica" **esquecido** é uma bomba-relógio: a diferença entre as duas aparece na auditoria, na reclamação do usuário ou no processo judicial.

## 4. Interessados e o conflito que eles trazem

Requisito não sai do ar: sai de gente. E gente quer coisas diferentes.

Um erro clássico é confundir **interessado** com **usuário**. No sistema-guia, a coordenação provavelmente nunca vai abrir a plataforma — e mesmo assim impõe um requisito (o relatório de ocupação) que muda o que o sistema precisa registrar desde o primeiro dia.

Mapear interessados é responder três perguntas para cada um: **o que ele ganha**, **o que ele teme**, e **o que ele pode vetar**. E então vem a parte que interessa: procurar onde essas respostas se chocam.

| Tensão do sistema-guia | Um lado | O outro |
|---|---|---|
| Prioridade × ordem de chegada | o professor precisa da sala para a banca de amanhã | o grupo reservou há duas semanas e se organizou |
| Manutenção × reserva confirmada | a infraestrutura precisa entrar hoje | alguém vai chegar e achar a sala interditada |
| Reservar fácil × sala vazia | atrito baixo faz as pessoas usarem o sistema | quanto mais fácil, mais gente reserva "por garantia" |

Cada linha dessa tabela **vira um requisito**, porque alguém precisa decidir. `RN-04` e `RN-06` do sistema-guia são exatamente duas dessas decisões já tomadas.

> 💡 **Se todos os interesses concordam, você não terminou o levantamento.** Conflito não é sinal de projeto mal conduzido; é sinal de que você falou com gente suficiente.

## 5. Requisito × solução: a armadilha

O cliente diz:

> *"O sistema deve ter um botão vermelho no canto superior direito para cancelar a reserva."*

Isso parece um requisito e não é. É **uma solução** — a tela que o cliente imaginou enquanto pensava no problema dele. Anotá-la assim custa caro de três formas: congela uma decisão de interface que deveria poder melhorar, esconde a necessidade real e impede descobrir alternativas melhores.

A ferramenta é perguntar **"por quê?"** até chegar na necessidade:

| Rodada | O que se diz |
|---|---|
| Pedido | "quero um botão vermelho no canto superior direito" |
| Por quê? | "porque as pessoas não acham onde cancelar" |
| Por quê isso importa? | "porque quando não acham, elas simplesmente não aparecem" |
| **Requisito** | **"O solicitante deve poder cancelar uma reserva futura de forma que a sala volte a ficar disponível."** |

Repare no que se ganhou: o requisito agora é verificável, não menciona tecnologia, e deixa em aberto **como** resolver — o botão pode virar um link no e-mail de confirmação, que talvez funcione melhor.

> ⚠️ Teste rápido: se o requisito menciona **botão, tela, menu, cor, tabela do banco ou nome de tecnologia**, quase sempre ele é solução disfarçada. A exceção legítima é quando a restrição vem de fora — *"deve funcionar no navegador X, porque é o que os computadores dos laboratórios têm"* é requisito de verdade.

> 💡 Perguntar "por quê" três vezes é o suficiente na maioria dos casos. Perguntar mais que isso costuma levar a "porque a instituição existe", o que é verdade e não ajuda ninguém.

## 6. O custo de descobrir tarde

A Aula 01 mostrou a curva; aqui ela ganha nome e sobrenome. Suponha que ninguém tenha perguntado se **reserva** e **uso confirmado** são a mesma coisa.

| Quando se descobre | O que custa |
|---|---|
| Na conversa | uma pergunta |
| No documento de requisitos | uma frase reescrita |
| No diagrama de classes | uma classe a mais e as associações em volta |
| No código | a estrutura de dados, as telas e os relatórios |
| Em produção | tudo acima, mais migrar dados, corrigir os números de ocupação já divulgados e explicar à coordenação por que o relatório do último período estava errado |

Por isso o resto deste bloco existe: a Aula 06 ensina a **descobrir**, a 07 a **escrever de forma verificável** e a 08 a **priorizar e validar**. Tudo para empurrar erro para a esquerda da tabela.

## 🏋️ Exercícios da aula

Na pasta `aula-05/` do seu repositório:

1. **`ex01.md`** — classifique os 12 requisitos abaixo em **funcional** ou **não-funcional** e escreva uma linha de justificativa para cada. Três deles são polêmicos de propósito: identifique quais e explique a ambiguidade. (a) permitir consultar espaços livres por período; (b) responder à consulta em até 2 s; (c) registrar quem confirmou o uso de cada reserva; (d) manter o registro de reservas por 5 anos; (e) autenticar pelo login institucional; (f) funcionar em telas a partir de 320 px de largura; (g) notificar quem teve reserva deslocada; (h) enviar a notificação em até 5 minutos; (i) impedir reserva acima da capacidade do espaço; (j) estar disponível 99,5% do horário de funcionamento do campus; (k) permitir que a infraestrutura bloqueie um espaço; (l) atender às diretrizes de acessibilidade WCAG nível AA;
2. **`ex02.md`** — os cinco pedidos a seguir chegaram como solução. Para cada um, faça a escada do "por quê" (mínimo duas rodadas) e reescreva como requisito verificável: (a) "quero um botão de exportar para Excel"; (b) "coloca um alerta vermelho piscando quando a sala for interditada"; (c) "precisa de um campo de observação no formulário"; (d) "faz um aplicativo, site não serve"; (e) "quero uma tela de administrador que mostre tudo";
3. **`ex03.md`** — monte o **mapa de interessados** do sistema-guia numa tabela com quatro colunas: interessado · o que ganha · o que teme · o que pode vetar. Inclua pelo menos **um interessado que não aparece** na [seção 3 do documento](../../recursos/sistema-guia.md#3-quem-são-os-interessados) e defenda a inclusão. Depois escolha **duas tensões** e escreva, para cada uma, o requisito que a resolve e **quem sai perdendo** com a sua decisão;
4. **`ex04.md`** — usando apenas o [contexto de uso](../../recursos/sistema-guia.md#8-contexto-de-uso-e-restrições), derive **oito requisitos não-funcionais** numerados (`RNF-01`…`RNF-08`), todos com número, unidade ou critério objetivo. Depois passe a lista de verificação da seção 3 e, para cada item que você **não** transformou em requisito, escreva a frase que justifica a ausência;
5. **Desafio 🌶️ `ex05.md`** — abaixo está a descrição de uma tela do sistema, do jeito que um cliente a desenharia. **Extraia os requisitos implícitos** — os que a tela pressupõe e ninguém escreveu.

   > *Tela "Minhas reservas". No topo, o nome do usuário e um seletor de período. Uma lista com uma linha por reserva, mostrando espaço, dia, horário e uma etiqueta colorida de situação. Cada linha tem um botão "cancelar", que fica cinza em algumas. No rodapé, "mostrando 10 de 47" e as setas de página.*

   Liste no mínimo **12 requisitos** (funcionais e não-funcionais) que essa tela pressupõe, marcando cada um com a evidência que o denuncia. Depois aponte **três perguntas** que a tela deixa sem resposta e que você levaria ao cliente antes de construir qualquer coisa.

## 🧠 Revisão

[8 questões de múltipla escolha](revisao/README.md) para conferir se os conceitos ficaram sólidos. Responda sem consultar a aula — depois volte e corrija.

## ✅ Entrega

```bash
git add aula-05/
git commit -m "Resolve exercícios da aula 05 (o que é um requisito)"
git push
```

---

⬅️ [Aula 04 — Como o software chega ao usuário](../../bloco-1-software-e-processos/aula-04-entrega-continua-e-devops/README.md) | ➡️ [Aula 06 — Elicitação](../aula-06-elicitacao/README.md)
