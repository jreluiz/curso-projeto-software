# Aula 06 — Elicitação: Descobrir o Que o Cliente Precisa

> 🎯 Objetivos: explicar por que perguntar "o que você quer" não basta, escolher a técnica de elicitação adequada a cada situação e conduzir uma entrevista com roteiro.
> 🎬 Slides da aula: [apresentacao-06-elicitacao.pdf](apresentacao/apresentacao-06-elicitacao.pdf)

## 1. A pergunta que não funciona

Você marca a reunião com a secretaria e faz a pergunta óbvia: *"o que vocês querem no sistema?"*

A resposta vem, e é curta: *"a gente quer parar de responder e-mail de reserva."*

Trinta minutos depois a reunião acabou, você tem uma página de anotações e nenhuma das perguntas que importam foi respondida. Isso não acontece porque a secretaria é má informante. Acontece por três razões estruturais:

- **Ninguém consegue descrever o que faz automaticamente.** Quem executa um processo há seis anos parou de enxergá-lo. As exceções, que são a parte cara, viraram reflexo;
- **O cliente responde na linguagem da solução que ele imagina**, não na do problema que ele tem — foi a armadilha da Aula 05;
- **O que ele lembra é o que aconteceu recentemente.** O caso raro e caro — a interdição de manutenção em cima de três reservas — não vem à cabeça numa sala de reunião.

Por isso a palavra técnica não é *coleta*, é **elicitação**: em inglês, *elicit* significa **extrair**, trazer à tona algo que está lá mas não sai sozinho. Requisito não é colhido como fruta madura; é escavado.

> 💡 A pergunta que rende dez vezes mais que "o que você quer": **"me mostra como você faz isso hoje."** Ela troca opinião por observação — e opinião sobre o futuro é a informação menos confiável que existe.

> 📖 Sommerville trata de elicitação e análise dentro do capítulo sobre engenharia de requisitos, com as técnicas comparadas.

## 2. Entrevista

É a técnica mais usada e a mais malfeita. Duas formas, e a boa entrevista usa as duas:

- **Fechada** — roteiro de perguntas definidas. Garante cobertura, permite comparar respostas de várias pessoas;
- **Aberta** — o entrevistado conduz. Descobre o que você nem sabia que precisava perguntar.

**O que faz uma entrevista funcionar:**

| Faça | Em vez de |
|---|---|
| Preparar roteiro e estudar o domínio antes | chegar e improvisar |
| Perguntar por **exemplos concretos e recentes** | perguntar por regras gerais |
| Pedir para ver o artefato real (a planilha, o e-mail, o caderno) | acreditar na descrição do artefato |
| Perguntar "e quando dá errado?" | mapear só o caminho feliz |
| Repetir com suas palavras e confirmar | anotar e sair |
| Enviar o resumo escrito depois, pedindo correção | confiar na sua memória |

**Perguntas fechadas que induzem** são o defeito mais comum: *"vocês precisam de um relatório mensal, certo?"* recebe "sim" quase sempre — inclusive de quem nunca pensou nisso. Prefira: *"o que a coordenação pede a vocês hoje, e com que frequência?"*.

> ⚠️ Entrevistar **uma pessoa só** é o caminho mais rápido para um sistema que atende uma pessoa só. No sistema-guia, entrevistar a secretaria e não entrevistar a infraestrutura produz um sistema que não sabe interditar sala — e a interdição é justamente a regra que atropela todas as outras.

## 3. Observação e análise de documentos

Quando o entrevistado não consegue descrever o que faz, pare de perguntar e vá olhar.

**Observação** — acompanhe a pessoa fazendo o trabalho real. É a técnica que revela:

- Os passos que ninguém menciona porque são automáticos;
- As gambiarras — o caderno paralelo, a planilha "de verdade", o grupo de mensagens onde as decisões acontecem;
- A frequência real das exceções, que costuma ser muito maior que a lembrada;
- O tempo que cada coisa leva.

> 💡 Toda gambiarra é um requisito não atendido com um post-it colado em cima. Quando você encontra uma, encontrou ouro: alguém já pagou para descobrir que aquilo era necessário.

**Análise de documentos** — o que a organização já escreveu diz muito, e não muda de ideia durante a conversa:

| Documento | O que ele entrega |
|---|---|
| A norma de uso dos espaços | as regras de negócio, já escritas e aprovadas |
| A planilha atual | os dados que realmente importam — as colunas que existem |
| A caixa de e-mails de reserva | o vocabulário do domínio e os casos de exceção reais |
| O calendário letivo | as restrições de tempo que atravessam tudo |
| Relatórios já pedidos | o que a coordenação vai continuar pedindo |

> ⚠️ Documento diz o processo **como deveria ser**; observação mostra **como é**. Quando os dois divergem — e eles divergem —, você achou uma decisão a tomar: consertar o processo ou consertar a norma. Registre a divergência; não escolha sozinho.

## 4. Workshop e prototipação

Duas técnicas para quando o problema não é falta de informação, e sim falta de **acordo** ou de **imaginação**.

**Workshop de requisitos** — reúne interessados diferentes na mesma sala, ao mesmo tempo. Serve exatamente para o que a entrevista individual não faz: **fazer o conflito aparecer na frente de quem pode resolvê-lo**. Se o professor acha que banca tem prioridade e o aluno acha que reserva antiga vale mais, é melhor descobrir isso numa sala com as duas pessoas do que em duas entrevistas separadas e um sistema no meio.

Exige preparo: pauta, alguém facilitando, e regra de encerramento — *"saímos daqui com a decisão escrita"*.

**Prototipação** — construir algo descartável para descobrir. Funciona porque é muito mais fácil criticar do que imaginar:

| Tipo | O que é | Bom para |
|---|---|---|
| Papel / rascunho | telas desenhadas à mão | discutir fluxo em minutos, sem apego |
| Navegável | telas ligadas, sem funcionar por baixo | validar entendimento e sequência |
| Funcional | um pedaço que funciona de verdade | testar viabilidade técnica e desempenho |

> ⚠️ **O risco do protótipo é o cliente achar que ele é o sistema.** *"Já está quase pronto, é só ligar no banco"* — a frase que precede o desastre. Combine em voz alta, antes de mostrar: isto é para jogar fora. Protótipo de papel tem uma virtude que o bonito não tem: ninguém confunde rascunho com produto.

## 5. O cliente que não sabe o que quer

Vai acontecer, e não é má vontade: ele conhece o **problema**, não a **solução** — a solução é o seu ofício, não o dele.

Cinco saídas que funcionam:

1. **Pergunte pelo passado, não pelo futuro.** "Descreva a última vez que deu errado" rende mais que "o que você gostaria";
2. **Ofereça alternativas concretas.** Escolher entre duas opções desenhadas é fácil; inventar do zero é difícil;
3. **Mostre algo errado de propósito.** Um protótipo ligeiramente furado produz correções específicas e imediatas — as pessoas corrigem melhor do que criam;
4. **Pergunte pelos extremos.** "Qual é o pior dia do ano para vocês?" e "o que **nunca** pode acontecer?" delimitam o sistema mais rápido que qualquer lista de funcionalidades;
5. **Anote o que ele **não** quer.** Restrição negativa é informação de altíssima qualidade e quase nunca é registrada.

> 💡 Existe um caso em que o cliente realmente não sabe **e não vai saber**: quando o processo não existe ainda. Aí a resposta honesta é reconhecer a incerteza, construir a menor fatia possível e aprender com o uso — que é exatamente o argumento das Aulas 02 e 03.

## 6. As perguntas que todo analista faz

Um roteiro genérico que funciona em qualquer domínio. Adapte, não decore:

**Sobre o problema**
- Me mostra como isso funciona hoje?
- O que dá errado com mais frequência?
- Qual foi a última vez que isso deu errado feio? O que aconteceu?
- Se nada mudasse, qual seria o custo disso continuar assim?

**Sobre as pessoas**
- Quem mais toca nesse processo?
- Quem reclama quando ele falha?
- Quem precisa aprovar alguma coisa aqui?
- Quem vai ficar incomodado se isso mudar?

**Sobre as regras**
- Isso está escrito em algum lugar?
- Sempre foi assim? Por que virou assim?
- Existe exceção? Quem pode autorizá-la?
- O que acontece se alguém não cumprir?

**Sobre os limites**
- Qual é o pior dia do ano?
- Quantos são, em número?
- O que **nunca** pode acontecer?
- Se você pudesse ter só uma coisa deste sistema, qual seria?

> 💡 A última pergunta da lista é a mais valiosa e a menos feita. A resposta a ela é a sua primeira entrega — e a Aula 08 mostra o que fazer com o resto.

## 🏋️ Exercícios da aula

Na pasta `aula-06/` do seu repositório:

1. **`ex01.md`** — escreva o **roteiro completo** de uma entrevista de 40 minutos com a secretaria sobre a reserva de espaços. Inclua: o objetivo em uma frase, 12 a 15 perguntas em ordem de condução, a marcação de quais são abertas e quais são fechadas, e **duas perguntas de acompanhamento** para cada uma das três perguntas mais importantes. Feche com o que você faria nos últimos 5 minutos;
2. **`ex02.md`** — escolha a técnica mais adequada para cada situação e **justifique descartando as outras**: (a) você precisa saber por que a secretaria mantém uma planilha paralela ao e-mail; (b) o professor e o representante dos alunos discordam sobre prioridade de reserva; (c) você precisa das regras oficiais de uso do auditório; (d) a coordenação não consegue explicar que relatório quer, mas diz que "vai saber quando vir";
3. **`ex03.md`** — abaixo está um trecho da norma de uso dos espaços. **Extraia dele todos os requisitos e regras de negócio** que conseguir, numerados, e marque cada um como F, NF ou RN. Depois liste **as ambiguidades** — os pontos em que a norma admite mais de uma leitura — e escreva a pergunta que você faria para resolver cada uma.

   > *Art. 4º — A utilização dos espaços destina-se prioritariamente às atividades de ensino. Art. 5º — As solicitações serão atendidas por ordem de recebimento, ressalvado o disposto no Art. 4º. Art. 6º — O solicitante deverá comparecer no horário reservado, sob pena de perda do direito de uso. Art. 7º — A Divisão de Infraestrutura poderá interditar espaços a qualquer tempo, mediante comunicação aos interessados. Parágrafo único — Em caso de interdição, será oferecida alternativa sempre que possível.*

4. **`ex04.md`** — você vai passar **duas horas observando** a secretaria num dia comum. Escreva o plano de observação: o que você vai olhar, o que vai anotar, quais três momentos do dia escolheria e por quê. Depois liste **cinco descobertas que só a observação revelaria** e que nem a entrevista nem a norma dariam — para cada uma, explique por que ela escaparia das outras técnicas;
5. **Desafio 🌶️ `ex05.md`** — **conduza uma entrevista de verdade.** Peça a um colega que assuma o papel de um interessado do sistema-guia (secretaria, professor ou infraestrutura) e conduza a entrevista de 20 minutos com o roteiro do `ex01`. Entregue: a transcrição ou o resumo fiel do que foi dito; a lista de requisitos e regras que você extraiu; **três perguntas que você deveria ter feito e não fez** — e o que provavelmente perdeu por isso; e um parágrafo sobre o que mudaria no roteiro para a próxima. A autocrítica vale tanto quanto a entrevista.

## 🧠 Revisão

[8 questões de múltipla escolha](revisao/README.md) para conferir se os conceitos ficaram sólidos. Responda sem consultar a aula — depois volte e corrija.

## ✅ Entrega

```bash
git add aula-06/
git commit -m "Resolve exercícios da aula 06 (elicitação)"
git push
```

---

⬅️ [Aula 05 — O que é um requisito](../aula-05-o-que-e-um-requisito/README.md) | ➡️ [Aula 07 — Especificação: documento e histórias](../aula-07-especificacao-e-historias/README.md)
