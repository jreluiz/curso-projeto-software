# Aula 08 — Análise, Priorização e Validação

> 🎯 Objetivos: detectar ambiguidade e falta de verificabilidade num documento, priorizar um backlog com critério defensável e validar requisitos com o cliente antes de construir.
> 🎬 Slides da aula: [apresentacao-08-analise-priorizacao-validacao.pdf](apresentacao/apresentacao-08-analise-priorizacao-validacao.pdf)

## 1. O documento que parece pronto

Você tem 40 requisitos escritos. Todo mundo aprovou na reunião — ninguém discordou de nada. Isso deveria ser um alívio e é um sinal de alerta: **concordar não custa nada quando ninguém sabe o que a frase exige.**

Análise de requisitos é ler o próprio documento procurando defeito. Quatro defeitos respondem pela maioria:

**Ambiguidade** — admite mais de uma leitura razoável.

> *"O sistema deve permitir reservar espaços com antecedência."* — Quanta? Mínima ou máxima? As duas?

**Não-verificabilidade** — não dá para responder objetivamente se foi cumprido.

> *"O sistema deve ser fácil de usar."* — Fácil para quem, medido como?

**Requisito composto** — várias verificações numa frase só.

> *"O sistema deve permitir interditar o espaço e notificar os atingidos e exportar o relatório em PDF."* — Quando 60% estiver pronto, o requisito está pronto?

**Requisito que é solução** — a Aula 05 inteira. Continua aparecendo, e a revisão é a última chance de pegá-lo.

Palavras que quase sempre denunciam defeito: *adequado, amigável, rápido, eficiente, robusto, simples, se necessário, quando possível, etc., entre outros, deve tratar adequadamente*.

> 💡 Um teste barato e cruel: **peça a duas pessoas que leiam o requisito e escrevam, separadamente, como testariam.** Se as descrições divergirem, o requisito é ambíguo — e você descobriu isso por dez minutos em vez de por um ciclo de trabalho.

> 📖 Sommerville trata de validação de requisitos, revisões e o que procurar em cada uma, no capítulo de engenharia de requisitos.

## 2. MoSCoW

Todo mundo quer tudo, e não cabe tudo. Priorizar não é ordenar por gosto — é **decidir o que não será feito agora** e conseguir defender isso.

O MoSCoW classifica em quatro faixas:

| Faixa | Significa | Teste |
|---|---|---|
| **M**ust — obrigatório | sem isso, não vale entregar | se faltar, a entrega é cancelada? Se não, não é *must* |
| **S**hould — importante | dói ficar sem, mas há contorno | existe uma alternativa manual aceitável por um tempo? |
| **C**ould — desejável | melhora, e sai fácil se apertar | seria a primeira coisa a cair sem drama? |
| **W**on't — fora **desta** vez | decidido que não entra agora | está registrado por que, e quando se reavalia? |

Aplicado ao sistema-guia, primeira entrega:

- **Must** — consultar disponibilidade; reservar; cancelar; interdição pela infraestrutura (`RN-05` atropela tudo o mais);
- **Should** — confirmação de uso no local; notificação de reserva deslocada;
- **Could** — sugestão automática de espaço alternativo após interdição;
- **Won't (desta vez)** — reserva recorrente; relatório de ocupação da coordenação.

> ⚠️ O **W** é a faixa mais importante e a mais mal usada. Ele **não** significa "nunca"; significa *"não nesta entrega, e está escrito por quê"*. Sem essa faixa, tudo vira *must*, e uma lista em que tudo é obrigatório não priorizou nada.

> 💡 Regra de bolso que segura a conversa: se mais de metade dos itens está em *must*, a priorização não aconteceu — alguém só transcreveu a lista de pedidos.

## 3. Esforço × valor

MoSCoW captura importância; falta o custo. Cruzando os dois eixos aparecem quatro regiões, e o que fazer em cada uma:

| | **Esforço baixo** | **Esforço alto** |
|---|---|---|
| **Valor alto** | **Faça primeiro.** É onde está a entrega que justifica o projeto | **Planeje e quebre.** Vale a pena, mas não cabe inteiro: fatie |
| **Valor baixo** | **Faça se sobrar.** Barato, mas não deixe encher a fila | **Não faça.** E escreva por que não — é a decisão mais atacada depois |

Duas armadilhas moram aqui:

- **Valor é do usuário, não de quem constrói.** "Refatorar o módulo de agenda" pode ter valor altíssimo para o time e nenhum para a secretaria. Isso não quer dizer que não deva ser feito — quer dizer que **não se justifica pelo mesmo argumento**;
- **Esforço é estimativa, e estimativa erra.** Item de esforço alto e incerto merece antes uma investigação curta e cronometrada, não um chute com duas casas decimais.

> 💡 No sistema-guia, "consultar disponibilidade" é o caso raro de valor alto com esforço baixo: resolve sozinho boa parte do problema da seção 1 do documento — a pessoa que atravessa o campus atrás de sala vazia. É por isso que ele é a primeira entrega, e não porque é o primeiro passo do fluxo.

## 4. O backlog

O resultado da priorização é o **backlog do produto**: uma fila **ordenada** de tudo que se quer fazer. Três propriedades que separam backlog de lista de desejos:

- **É ordenado, não agrupado.** Não existem "cinco itens de prioridade alta" — existe um primeiro, um segundo, um terceiro. Empate é priorização não terminada;
- **É detalhado de forma desigual, e isso é correto.** O topo tem critérios de aceite escritos; o fundo tem uma linha. Detalhar o que talvez nunca seja feito é desperdício;
- **É vivo.** Item entra, sai, muda de lugar e é descartado. Backlog que não muda há três meses não está sendo usado para decidir nada.

> ⚠️ Um backlog só tem valor se **uma pessoa responde pela ordem**. Quando a ordem é definida por quem grita mais alto, o efeito é o de não ter backlog — com o custo adicional de manter a planilha.

## 5. Rastreabilidade

Seis meses depois, a norma de uso dos espaços muda: interdição passa a exigir aviso de 24 horas. **O que precisa ser revisto?**

Sem rastreabilidade, a resposta é "vamos procurar". Com rastreabilidade, é uma consulta. Rastrear é manter a ligação entre os artefatos:

```
Regra de negócio  →  Requisito / História  →  Projeto  →  Código  →  Teste
```

Na prática, uma matriz simples resolve:

| RN | Requisito / História | Critério de aceite | Onde é testado |
|---|---|---|---|
| `RN-05` | H-03 — interditar espaço e avisar | CA-03.2, CA-03.5 | Cenário "Interdição atinge reserva confirmada" |
| `RN-04` | H-02 — reservar declarando finalidade | CA-02.3 | Cenário "Banca desloca reserva de estudo" |
| `RN-06` | H-05 — confirmar uso no local | CA-05.1, CA-05.4 | Cenário "Reserva não confirmada em 15 min" |

Ela responde a três perguntas caras:

- **Mudou a norma — o que revisar?** Leia a linha;
- **Este requisito veio de onde?** Requisito sem origem é candidato a escopo que ninguém pediu;
- **Isto está testado?** Linha com a última coluna vazia é risco declarado.

> 💡 Rastreabilidade **completa** custa caro e raramente compensa em projeto pequeno. Rastreabilidade **das regras de negócio e dos requisitos críticos** custa pouco e paga na primeira mudança de norma. Escolha o recorte e escreva qual escolheu.

## 6. Mudança de escopo

A coordenação pede, no meio da construção: *"aproveitando, dá para incluir reserva de equipamento também?"*

As duas respostas ruins são igualmente comuns. **"Sim"** sem discussão: o prazo não muda, o time absorve, a qualidade cede em silêncio. **"Não"** sem discussão: o sistema entrega o que foi combinado em março e não o que a instituição precisa em agosto.

A resposta profissional tem quatro partes:

1. **Entenda o pedido.** É requisito ou solução? Que problema ele resolve? (Aula 05);
2. **Dimensione.** Esforço, impacto no que já está feito, risco;
3. **Apresente o custo em forma de escolha.** *"Cabe, e desloca a confirmação de uso para a entrega seguinte. Ou entra depois, sem deslocar nada. Qual você prefere?"*;
4. **Registre.** O que foi pedido, o que foi decidido, quem decidiu, quando.

> ⚠️ O **inchaço de escopo** (*scope creep*) não acontece por um pedido grande — acontece por doze pedidos pequenos, cada um obviamente razoável, nenhum registrado. O antídoto não é rigidez: é **tornar o custo visível toda vez**.

> 💡 Note que o passo 3 devolve a decisão a quem tem autoridade para tomá-la. Quem constrói não decide escopo; quem constrói informa o custo de cada alternativa — com honestidade, inclusive quando o custo é baixo.

## 7. Validação: fechando o ciclo

**Verificar** é conferir o sistema contra a especificação. **Validar** é conferir a especificação contra a necessidade real. Neste bloco só há especificação — então tudo aqui é validação, e ela acontece **antes** de construir, que é onde ela é barata.

**O roteiro de revisão.** Passe cada requisito por seis perguntas:

| # | Pergunta | Procura |
|---|---|---|
| 1 | Está verificável? | "como eu saberia que foi cumprido?" |
| 2 | É uma coisa só? | requisito composto |
| 3 | É problema ou solução? | tela, botão, tecnologia |
| 4 | De quem veio? | requisito órfão, que ninguém pediu |
| 5 | Conflita com outro? | dois requisitos que não podem ser verdade juntos |
| 6 | O que acontece quando falha? | caminho de exceção esquecido |

**Um requisito passando pelo roteiro.** Como ele chegou da entrevista:

> *"O sistema deve avisar rapidamente quem perdeu a sala e oferecer outra opção adequada."*

| Pergunta | Diagnóstico |
|---|---|
| 1. Verificável? | Não. "Rapidamente" e "adequada" não têm medida |
| 2. Uma coisa só? | Não. Avisar e oferecer alternativa são dois comportamentos |
| 3. Problema ou solução? | Problema — está bem aqui |
| 4. De quem veio? | Da infraestrutura, na entrevista de terça |
| 5. Conflita? | Sim, potencialmente com `RN-05`: e se não houver alternativa? |
| 6. Falha? | Não trata o caso "nenhum espaço equivalente livre" |

Reescrito, vira dois requisitos e uma pergunta ao cliente:

> **RF-14** — O sistema deve notificar o solicitante de toda reserva interrompida por interdição, em até 5 minutos, informando espaço, período e motivo.
> **RF-15** — Ao interromper uma reserva, o sistema deve apresentar ao solicitante os espaços livres no mesmo período com capacidade igual ou superior.
> **Pergunta em aberto** — quando não houver espaço equivalente livre, o sistema deve oferecer horário alternativo, entrar em lista de espera, ou apenas informar? *(a decidir com a secretaria — [questão 3 do sistema-guia](../../recursos/sistema-guia.md#9-o-que-está-em-aberto))*

Note o desfecho: **a validação não terminou com tudo resolvido.** Ela terminou com dois requisitos bons e uma pergunta explícita — que é infinitamente melhor que uma suposição silenciosa.

> 💡 **Como validar com o cliente sem ler 40 requisitos em voz alta:** leve cenários concretos. *"É sexta, 14h. A infraestrutura interdita o B-12. Três grupos tinham reserva. Me conta o que deveria acontecer."* Cliente valida história; ninguém valida lista.

## 🏋️ Exercícios da aula

Na pasta `aula-08/` do seu repositório:

1. **`ex01.md`** — o documento abaixo tem **pelo menos dez defeitos**. Encontre-os, classifique cada um (ambíguo · não-verificável · composto · solução disfarçada · conflitante · sem origem) e reescreva os requisitos.

   > **RF-01** O sistema deve ser rápido e amigável.
   > **RF-02** O sistema deve permitir reservar espaços com antecedência.
   > **RF-03** O sistema deve ter um botão de cancelar na tela principal e enviar e-mail ao usuário.
   > **RF-04** Reservas de estudo em grupo não podem ser canceladas por terceiros.
   > **RF-05** O professor pode assumir qualquer sala quando necessário.
   > **RF-06** O sistema deve tratar adequadamente os casos de erro.
   > **RF-07** O relatório de ocupação deve ser gerado mensalmente em PDF, Excel e enviado por e-mail à coordenação.
   > **RF-08** O sistema deve suportar muitos usuários simultâneos.

2. **`ex02.md`** — pegue as seis histórias do `ex01` da Aula 07 e mais quatro que você criar, e monte um **backlog ordenado de 10 itens**. Entregue: a classificação MoSCoW de cada um; a posição de cada um na matriz esforço × valor; a **ordem final numerada de 1 a 10**; e um parágrafo defendendo as posições 1, 5 e 10. Depois responda: **qual item você teria colocado em *must* e não colocou, e por quê resistiu?**;
3. **`ex03.md`** — monte a **matriz de rastreabilidade** do sistema-guia ligando as 8 regras de negócio (`RN-01` a `RN-08`) às suas histórias e critérios. Toda regra precisa aparecer. Ao final, responda: (a) alguma regra ficou sem nenhuma história? O que isso significa? (b) alguma história não realiza nenhuma regra? Isso é problema? (c) a norma passa a exigir aviso de 24 h para interdição — **liste exatamente o que precisa ser revisto**;
4. **`ex04.md`** — a coordenação envia: *"Aproveitando que vocês estão fazendo o sistema, dá para incluir também a reserva dos equipamentos do almoxarifado? É parecido, deve ser rápido."* Escreva a **resposta completa** seguindo os quatro passos da seção 6: as perguntas que você faria antes de responder; o dimensionamento (o que muda no que já está feito, e por que "é parecido" pode ser enganoso); **duas alternativas com custo explícito**; e o registro da decisão no formato que você usaria. Lembre que [o almoxarifado está fora do escopo](../../recursos/sistema-guia.md#2-escopo) — e que isso não encerra a conversa, apenas informa;
5. **Desafio 🌶️ `ex05.md`** — escolha **um sistema** do [catálogo](../../recursos/sistemas-para-praticar.md) (não o sistema-guia) e escreva o **documento de requisitos completo** dele. Deve conter: contexto e escopo, com o que ficou de fora e por quê; interessados com interesses e conflitos; glossário do domínio; requisitos funcionais numerados; requisitos não-funcionais numerados e com critério objetivo; regras de negócio numeradas; backlog priorizado com MoSCoW; critérios de aceite dos cinco itens do topo; e uma seção de **questões em aberto**. Ao final, aplique o roteiro de seis perguntas da seção 7 ao seu próprio documento e **relate o que você encontrou e corrigiu** — essa última parte vale tanto quanto o documento.

## 🧠 Revisão

[8 questões de múltipla escolha](revisao/README.md) para conferir se os conceitos ficaram sólidos. Responda sem consultar a aula — depois volte e corrija.

## ✅ Entrega

```bash
git add aula-08/
git commit -m "Resolve exercícios da aula 08 (análise, priorização e validação)"
git push
```

---

⬅️ [Aula 07 — Especificação: documento e histórias](../aula-07-especificacao-e-historias/README.md) | ➡️ [Aula 09 — Por que modelar e o que é UML](../../bloco-3-modelagem-e-uml/aula-09-por-que-modelar-e-uml/README.md)
