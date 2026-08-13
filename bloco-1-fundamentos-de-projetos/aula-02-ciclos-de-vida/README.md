# Aula 02 — Ciclos de vida

> 🎯 Objetivos: distinguir o ciclo de vida clássico do incremental e do iterativo, situar um projeto no eixo preditivo–adaptativo e escolher o ciclo para um contexto concreto, defendendo a escolha.
> 🎬 Slides da aula: [apresentacao-02-ciclos-de-vida.pdf](apresentacao/apresentacao-02-ciclos-de-vida.pdf)

## 1. A mesma equipe, dois projetos, duas ordens de trabalho

A mesma fornecedora tem dois contratos em andamento.

No primeiro, a **Ouvidoria municipal**: o escopo veio anexo ao edital, o prazo é de oito meses com multa por atraso, e qualquer mudança exige aditivo contratual que leva de 30 a 60 dias. Ninguém vai descobrir requisito novo no meio — e se descobrir, não vai poder atender.

No segundo, o **marketplace de serviços autônomos**: dois fundadores, seis meses de reserva financeira, e ninguém sabe ainda se alguém quer o produto. O que se aprender no terceiro mês pode mudar o que se constrói no quarto.

Rodar os dois do mesmo jeito seria erro nos dois casos. **O ciclo de vida é a ordem em que o trabalho acontece**, e escolher errado custa caro: planejar tudo antes num projeto incerto é desperdício; improvisar num contrato com multa é irresponsabilidade.

> 💡 **Ciclo de vida não é metodologia, nem ferramenta, nem cultura.** É só a resposta a uma pergunta: *em que ordem fazemos as coisas, e quantas vezes voltamos atrás?*

Esta aula trata de três ciclos e de um eixo. Os três ciclos respondem *em que ordem*; o eixo responde *quanto se decide antes* — e são perguntas independentes, o que é a origem de boa parte da confusão de vocabulário na área.

## 2. O ciclo clássico, e o que ele acertou

O **ciclo clássico** — conhecido como cascata — organiza o trabalho em fases sequenciais, cada uma terminando num documento aprovado que autoriza a seguinte:

```mermaid
flowchart LR
    A[Requisitos] --> B[Projeto]
    B --> C[Construção]
    C --> D[Testes]
    D --> E[Implantação]
```

Ele tem má fama, e boa parte dela é merecida: quando os requisitos estão errados, o erro só aparece na fase de testes, e a essa altura tudo foi construído em cima dele.

Mas **o clássico acertou duas coisas** que sobreviveram a todas as críticas:

- **Existe uma ordem natural** — não se testa o que não foi construído, não se constrói o que não foi decidido. Nenhum ciclo posterior aboliu isso; eles apenas reduziram o tamanho do pedaço;
- **Decisão registrada vale mais que decisão lembrada.** O documento aprovado ao fim de cada fase existe para que ninguém invente, três meses depois, o que ficou combinado.

Ele continua sendo a escolha certa quando **o escopo é conhecido, estável e contratado** — que é exatamente o caso da Ouvidoria.

O custo do ciclo clássico tem nome e hora: é a **descoberta tardia**. O gráfico abaixo é o mesmo em qualquer projeto — o que muda é a inclinação:

```
   custo de corrigir
        │                                              ╱
        │                                        ╱
        │                            ╱
        │              ╱
        │   ╱
        └───────┬────────┬───────────┬────────────┬──────
             requisitos projeto  construção    testes
```

Num ciclo em que os testes só acontecem no fim, **todo erro de requisito é descoberto no ponto mais caro da curva**. Os ciclos das seções seguintes não mudam a curva: eles a percorrem várias vezes, em pedaços menores, para que cada erro custe o que custaria no começo.

> ⚠️ **Cascata não é erro histórico.** O erro é usá-la onde a incerteza é alta. Num projeto com escopo fixo em edital e multa por atraso, adotar um ciclo adaptativo criaria a expectativa de uma flexibilidade que o contrato não permite — e o desapontamento cairia sobre o time.

## 3. Incremental: entregar em pedaços

No ciclo **incremental**, o produto é dividido em partes utilizáveis, e cada entrega acrescenta uma parte nova ao que já existe. O usuário recebe algo que funciona bem antes do fim.

No sistema de empréstimo de equipamentos, um recorte incremental razoável seria:

| Entrega | O que ela contém | Já dá para usar? |
|:---:|---|---|
| 1 | cadastrar item e registrar empréstimo e devolução | sim — substitui a planilha |
| 2 | reserva antecipada e conflito com empréstimo | sim |
| 3 | penalidade automática por atraso | sim |
| 4 | relatórios de uso e itens parados | sim |

Cada linha é **valor que chega ao balcão**, e nenhuma depende das seguintes para funcionar. Esse é o teste: se a entrega 1 não serve para nada sem a 2, o recorte não é incremental — é uma fase com nome de entrega.

> 💡 **O recorte incremental é uma decisão de gestão, não técnica.** Ele responde *"o que resolve mais dor primeiro?"*, e quem sabe isso é quem sofre a dor — no caso, o atendente do balcão.

Repare na ordem escolhida. A penalidade por atraso é o pedido que a chefia mais repete, e mesmo assim ficou em terceiro: sem registro de empréstimo e devolução, **não há como saber que houve atraso**. A ordem incremental é ditada pela dependência real, não pela intensidade do pedido — e explicar isso a quem pediu faz parte do trabalho.

## 4. Iterativo: refazer o mesmo pedaço melhor

No ciclo **iterativo**, volta-se ao que já foi feito para melhorá-lo com o que se aprendeu. A primeira versão da tela de empréstimo existe, foi usada por duas semanas, e a segunda versão nasce do que se descobriu no uso.

A diferença de um para o outro cabe numa frase:

```
   INCREMENTAL   entrega 1     entrega 2     entrega 3
                 ┌───────┐     ┌───────┐     ┌───────┐
                 │  A    │  →  │  A B  │  →  │ A B C │      cresce
                 └───────┘     └───────┘     └───────┘

   ITERATIVO     iteração 1    iteração 2    iteração 3
                 ┌───────┐     ┌───────┐     ┌───────┐
                 │  A    │  →  │  A′   │  →  │  A″   │      melhora
                 └───────┘     └───────┘     └───────┘
```

**Incremental cresce; iterativo melhora.** Um quadro pintado por partes é incremental; um quadro esboçado inteiro e refinado três vezes é iterativo.

Quase todo projeto real usa os dois ao mesmo tempo: entrega partes novas **e** revisita as antigas. O que não existe é o projeto que se diz iterativo e nunca volta a nada — esse é incremental com nome errado.

> ⚠️ **Dizer "somos iterativos" sem nunca revisitar decisão é o disfarce mais comum.** O sintoma é simples de checar: nas últimas três entregas, alguma mexeu em algo já entregue? Se não, o time é incremental — o que é legítimo, desde que ninguém conte com o aprendizado que não está acontecendo.

## 5. Preditivo × adaptativo: um eixo, não dois campos

**Preditivo** e **adaptativo** não são dois métodos concorrentes: são as pontas de um eixo que mede **quanto se decide antecipadamente**.

| | Preditivo | Adaptativo |
|---|---|---|
| **Escopo** | definido no início | refinado ao longo do caminho |
| **Mudança** | tratada como exceção, com controle formal | tratada como esperada |
| **Sucesso é** | entregar o combinado, no prazo e custo | entregar o que resolve, aprendendo no caminho |
| **Exige** | requisitos estáveis e conhecidos | acesso contínuo a quem decide o valor |

A Ouvidoria fica na ponta preditiva por **razões de contrato**, não por preferência. O marketplace fica na adaptativa por **razões de incerteza**. Entre os dois há uma faixa larga onde vive a maioria dos projetos — e o comum é ser **híbrido**: preditivo no que é regulado e conhecido, adaptativo no que é novo.

O sistema da clínica-escola é o exemplo. Ele se parte em duas metades com naturezas opostas:

| Parte do projeto | Ponta do eixo | Por quê |
|---|---|---|
| Controle de acesso e guarda legal do prontuário | **preditiva** | a LGPD e o prazo de guarda não mudam no meio do projeto, e a auditoria externa cobra o que está na norma |
| Rotina de atendimento do aluno e do supervisor | **adaptativa** | ninguém sabe ainda como será o uso na clínica, e a primeira versão vai estar errada em algum ponto |

Gerir as duas metades do mesmo jeito falha duas vezes: a parte legal fica frouxa, e a parte de uso fica engessada num desenho que ninguém validou. **Híbrido não é meio-termo — é aplicar cada regime onde ele cabe**, e dizer por escrito qual é qual.

> ⚠️ **Preditivo não é sinônimo de cascata.** Cascata é um ciclo específico; preditivo é o quanto se decide antes. Um projeto pode ser preditivo e incremental ao mesmo tempo — escopo fechado no início, entregue em quatro pedaços.

## 6. Escolher o ciclo é decisão de projeto

Quatro perguntas resolvem a escolha na primeira semana, e são as mesmas em qualquer projeto:

1. **O escopo é conhecido e estável?** Se sim, o preditivo é viável;
2. **A mudança é barata ou cara?** Contrato com aditivo de 60 dias torna a mudança cara — e o adaptativo, ilusório;
3. **Existe alguém disponível para decidir valor toda semana?** Sem isso, o adaptativo trava, porque ninguém prioriza;
4. **O usuário consegue usar uma parte antes do todo?** Se sim, cabe incremental — e é quase sempre bom que caiba.

As quatro são independentes, e é por isso que a resposta raramente é um nome só. As perguntas 1 e 2 decidem **onde no eixo**; a 3 diz se o adaptativo é executável de verdade; a 4 decide o **formato da entrega**, e vale nos dois regimes.

A resposta é registrada, com o motivo. É o mesmo princípio da matriz da Aula 01: **a decisão precisa ter dono e estar escrita antes de o conflito aparecer** — porque em outubro, com o prazo apertado, alguém vai propor "pular a homologação só desta vez", e a única defesa é o que foi combinado em março.

O registro cabe em meia página. Para a Ouvidoria:

| | |
|---|---|
| **Decisão** | ciclo preditivo, com entrega incremental em três fases |
| **Quem decidiu** | gerente do projeto (**A** na matriz), com a coordenação da ouvidoria consultada |
| **Por quê** | escopo anexo ao edital e estável; mudança exige aditivo de 30 a 60 dias, o que torna o adaptativo inviável na prática |
| **O que se perde** | o que se descobrir sobre o uso real só entra no contrato seguinte |
| **Revisar se** | a prefeitura sinalizar disposição de aditivar por demanda da operação |

A última linha é a que costuma faltar, e é a mais útil: ela diz **em que condição a decisão deixa de valer**. Sem ela, a escolha de março vira dogma em outubro, e ninguém lembra que ela dependia de uma premissa.

> 📖 O Sommerville trata dos modelos de processo de software — cascata, incremental e integração/configuração — no capítulo sobre processos, e discute quando cada um se aplica. O Guia PMBOK trata dos ciclos preditivo, iterativo, incremental e adaptativo na introdução, ao definir o ambiente do projeto.

## 🏋️ Exercícios da aula

Na pasta `aula-02/` do seu repositório:

1. **`ex01.md`** — classifique cada entrega em **incremental** ou **iterativa**: (a) a segunda versão da tela de busca, refeita depois de observar dez atendimentos; (b) o módulo de relatórios, que não existia; (c) o cadastro reescrito para aceitar item sem patrimônio; (d) a reserva antecipada, entregue no terceiro mês; (e) o fluxo de devolução simplificado de cinco para dois passos; (f) a integração com o portal, entregue por último. *Confere assim: três de cada, e o critério é sempre se aquilo já existia — não se foi difícil nem se demorou.*

2. **`ex02.md`** — para cada um dos três projetos, diga onde ele fica no eixo preditivo–adaptativo e **por qual razão**: (a) [Ouvidoria municipal](../../recursos/projetos-para-praticar.md#8-ouvidoria-municipal); (b) [marketplace de serviços autônomos](../../recursos/projetos-para-praticar.md#9-marketplace-de-serviços-autônomos); (c) [prontuário de clínica-escola](../../recursos/projetos-para-praticar.md#10-prontuário-de-clínica-escola). *Confere assim: um em cada ponta e um híbrido — e no híbrido você precisa dizer qual parte é preditiva e qual é adaptativa.*

3. **`ex03.md`** — recorte o sistema de [empréstimo de equipamentos](../../recursos/projetos-para-praticar.md#2-empréstimo-de-equipamentos) em **três entregas incrementais**, na ordem em que você as faria. Para cada uma, escreva a frase que prova que ela é utilizável sozinha. *Confere assim: se alguma entrega precisar da seguinte para servir para alguma coisa, o recorte virou fase — refaça.*

4. **`ex04.md`** — um time afirma ser iterativo. Nas últimas três entregas, produziu: o módulo de relatórios, a integração com o portal e a tela de auditoria. Diga se a afirmação se sustenta, aponte o sintoma que decide a questão e proponha **uma** mudança concreta na próxima entrega que tornaria o time de fato iterativo. *Confere assim: a resposta não depende da qualidade do trabalho do time — só de uma característica das três entregas listadas.*

5. **`ex05.md`** — 🌶️ **Desafio.** Você assume a gestão do projeto da [semana acadêmica](../../recursos/projetos-para-praticar.md#7-semana-acadêmica-com-submissões): equipe voluntária com disponibilidade imprevisível, data do evento imóvel, orçamento comprometido. **Escreva a decisão de ciclo de vida**, respondendo as quatro perguntas da seção 6 e declarando: (i) o ciclo escolhido, e se é híbrido, o que é preditivo e o que é adaptativo; (ii) o recorte da primeira entrega, com o critério que você usou; (iii) **o que se perde** com essa escolha, e qual seria o cenário em que ela se mostraria errada. *Confere assim: o item (iii) precisa nomear um cenário concreto e verificável — "se em setembro só duas pessoas estiverem disponíveis" vale; "se der tudo errado" não vale.*

## 🧠 Revisão

[8 questões de múltipla escolha](revisao/README.md) para conferir se os conceitos ficaram sólidos. Responda sem consultar a aula — depois volte e corrija.

## ✅ Entrega

```bash
git add aula-02/
git commit -m "Resolve exercícios da aula 02 (ciclos de vida)"
git push
```

---

⬅️ [Aula 01 — Por que gerir um projeto](../aula-01-por-que-gerir-um-projeto/README.md) | ➡️ [Aula 03 — Os processos de um projeto](../aula-03-os-processos-de-um-projeto/README.md)
