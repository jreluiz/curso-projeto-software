# Aula 10 — Casos de Uso

> 🎯 Objetivos: identificar atores e a fronteira do sistema, escrever a especificação textual de um caso de uso com os três fluxos e decidir entre `include` e `extend`.
> 🎬 Slides da aula: [apresentacao-10-casos-de-uso.pdf](apresentacao/apresentacao-10-casos-de-uso.pdf)

## 1. Onde termina o sistema

Primeira pergunta antes de qualquer desenho: **o que é o sistema e o que é o mundo?**

No sistema-guia, o Sistema Acadêmico está dentro ou fora? A resposta muda tudo: se está dentro, você é responsável por ele; se está fora, você depende dele e precisa decidir o que fazer quando ele cair. Ele está **fora** — e essa é uma decisão de escopo já registrada no documento do cliente.

A linha que separa os dois é a **fronteira do sistema**. Do lado de fora ficam os **atores**:

> **Ator** é um papel externo à fronteira que interage com o sistema.

Três consequências que resolvem a maioria das dúvidas:

- **Ator é papel, não pessoa.** A mesma professora é *Solicitante* quando reserva a sala e *Coordenação* quando pede o relatório. Dois atores, uma pessoa;
- **Ator pode não ser humano.** O Sistema Acadêmico é ator: está fora e interage. Um relógio que dispara rotina às 3h também;
- **O que está dentro nunca é ator.** Banco de dados, servidor, módulo de notificação: são partes do sistema.

| Candidato | É ator? | Por quê |
|---|---|---|
| Aluno | ✅ | usa o sistema por vontade própria |
| Infraestrutura | ✅ | papel distinto, com objetivos próprios |
| Sistema Acadêmico | ✅ | externo, fornece a grade de aulas |
| Serviço de e-mail | ✅ | externo, recebe pedidos do sistema |
| Banco de dados | ❌ | está dentro da fronteira |
| "Sistema" | ❌ | é o próprio sistema; nunca é ator dele mesmo |

> 💡 Um teste rápido: **se você é responsável por consertar quando aquilo quebrar, está dentro.** Se você só pode reclamar com outra pessoa, está fora — e é ator.

> 📖 Bezerra dedica um capítulo a casos de uso, com bastante espaço para a especificação textual e para os relacionamentos entre eles.

## 2. Caso de uso não é tela

Ninguém usa o sistema para "clicar em salvar". Usa para **reservar um espaço** — e essa diferença é todo o conteúdo desta seção. O teste cabe numa frase com lacuna:

> *"O aluno usa o sistema para \_\_\_\_\_\_."*

O que preenche a lacuna é um **objetivo de um ator que produz um resultado de valor observável**, escrito como `verbo + complemento`, no infinitivo. O que não preenche é tela, menu ou clique.

| Escrito errado | Por que está errado | Escrito certo |
|---|---|---|
| Tela de login | é uma tela | Autenticar-se |
| Menu principal | é navegação | *(não é caso de uso nenhum)* |
| Preencher formulário de reserva | é um passo | Reservar espaço |
| Clicar em cancelar | é uma interação | Cancelar reserva |
| Gerenciar reservas | "gerenciar" esconde 4 objetivos diferentes | Reservar · Cancelar · Consultar · Confirmar uso |

> ⚠️ **"Gerenciar X" quase nunca é um caso de uso.** É o nome que se dá quando não se decidiu quais são os objetivos de verdade. Toda vez que a palavra aparecer, quebre em verbos concretos e veja quantos aparecem.

## 3. `include`, `extend` e generalização

Três setas ligam casos de uso, e duas delas são trocadas o tempo todo.

| | Significa | Quem aponta para quem | Exemplo |
|---|---|---|---|
| `include` | o comportamento **sempre** acontece; foi extraído para não repetir | o caso **base** aponta para o incluído | `Reservar espaço` ──include──▶ `Autenticar-se` |
| `extend` | acontece **às vezes**, sob condição | o caso **extensor** aponta para o base | `Reservar com prioridade` ──extend──▶ `Reservar espaço` |
| generalização | um caso é uma variação especializada de outro | o específico aponta para o geral | `Reservar auditório` ─▷ `Reservar espaço` |

A regra que resolve na hora: **leia em voz alta "isto acontece sempre?"**. Sempre → `include`. Só quando ⟨condição⟩ → `extend`, **e a seta vai na direção contrária** da que a intuição pede.

Em PlantUML, o diagrama do sistema-guia fica assim (a sintaxe completa e como gerar o `.svg` estão no [guia de notações](../../recursos/notacoes-uml.md#6-casos-de-uso-em-plantuml)):

![Diagrama de casos de uso da Reserva de Espaços do Campus: Aluno e Infraestrutura sobre cinco casos de uso, com três relacionamentos include e um extend](casos-de-uso-relacionamentos.svg)

> Fonte do diagrama: [`casos-de-uso-relacionamentos.puml`](casos-de-uso-relacionamentos.puml). Editou a fonte? Gere o `.svg` de novo antes de commitar.

> 💡 **Na dúvida, não use nenhuma das três.** Dois casos de uso independentes e bem especificados valem mais que um diagrama cheio de setas que cada leitor interpreta de um jeito. O relacionamento existe para evitar repetição, não para demonstrar conhecimento de notação.

## 4. A especificação textual — onde está o conteúdo

Aqui está o ponto mais importante da aula, e vale dito com todas as letras:

> **O diagrama de casos de uso é o índice. O conteúdo é a especificação textual.**

O diagrama cabe num slide e é feito em dez minutos. Quem vai construir o sistema lê a **especificação** — e é ela que expõe as regras que ninguém tinha percebido. Um diagrama com dez elipses e nenhuma especificação não documenta nada.

Um caso de uso especificado, completo:

---

**UC-02 — Reservar espaço**

| | |
|---|---|
| **Ator principal** | Solicitante (aluno, professor ou setor) |
| **Interessados** | Secretaria (quer parar de mediar); Infraestrutura (precisa poder interditar) |
| **Pré-condições** | Solicitante autenticado; existe pelo menos um espaço cadastrado |
| **Pós-condição de sucesso** | Reserva registrada, o espaço fica indisponível no período e o solicitante é notificado |
| **Gatilho** | O solicitante decide que precisa de um espaço |

**Fluxo principal**

1. O solicitante informa o período desejado, a quantidade de pessoas e os recursos necessários;
2. O sistema consulta a grade de aulas no Sistema Acadêmico e as reservas e bloqueios existentes;
3. O sistema apresenta os espaços livres que atendem à capacidade e aos recursos;
4. O solicitante escolhe um espaço e declara a finalidade;
5. O sistema verifica os limites do solicitante (`RN-02`, `RN-03`) e a compatibilidade do espaço (`RN-08`);
6. O sistema registra a reserva e notifica o solicitante.

**Fluxos alternativos**

- **4a. Finalidade acadêmica em horário ocupado por estudo em grupo** — o sistema informa que a reserva existente será deslocada (`RN-04`), pede confirmação; confirmando, desloca a reserva anterior, notifica o solicitante deslocado e retorna ao passo 5.
- **3a. Nenhum espaço atende exatamente** — o sistema apresenta os espaços que atendem parcialmente, indicando o que falta em cada um; o solicitante pode escolher um deles ou mudar os critérios e voltar ao passo 1.

**Fluxos de exceção**

- **2a. O Sistema Acadêmico não responde** — o sistema informa que a disponibilidade pode estar desatualizada, apresenta apenas o que conhece das próprias reservas e registra o ocorrido. *(comportamento derivado do contexto: o legado cai)*
- **5a. O solicitante já tem 2 reservas futuras** (`RN-03`) — o sistema recusa, informa o limite e lista as reservas existentes com a opção de cancelar uma.
- **5b. O solicitante está suspenso** (`RN-07`) — o sistema recusa e informa a data em que a suspensão termina.
- **6a. Falha ao registrar** — nenhuma reserva é criada, o espaço continua livre e o solicitante é informado de que pode tentar de novo.

---

> ⚠️ **Os fluxos de exceção são onde mora a regra de negócio.** Repare que o fluxo principal acima tem 6 passos e os alternativos e de exceção têm 6 casos — e são eles que citam quase todas as regras. Um caso de uso só com fluxo principal descreve o sistema num dia bom.

> 💡 A técnica para achar exceção: em cada passo do fluxo principal, pergunte **"e se não?"**. E se o serviço externo não responder, e se o limite estourar, e se o usuário fechar a página, e se dois pedidos chegarem juntos.

## 5. Caso de uso × história de usuário

Os dois descrevem o que o usuário quer. Não são concorrentes — servem a momentos diferentes:

| | Caso de uso | História de usuário |
|---|---|---|
| Tamanho | um objetivo completo, com todos os caminhos | uma fatia que cabe num ciclo |
| Detalhe | fluxos escritos, incluindo exceções | um cartão + critérios de aceite |
| Escrito | uma vez, revisado quando o domínio muda | continuamente, e descartado depois |
| Bom para | entender o domínio inteiro e achar exceção | organizar o trabalho e priorizar |
| Fraco em | acompanhar trabalho | dar visão do todo |

Na prática, um caso de uso costuma virar **várias** histórias. O `UC-02` acima renderia, no mínimo: consultar disponibilidade; reservar em horário livre; deslocar reserva por prioridade acadêmica; tratar indisponibilidade do Sistema Acadêmico.

> 💡 Use caso de uso para **entender**, história para **trabalhar**. Times que só usam histórias costumam ter uma visão fragmentada do domínio; times que só usam casos de uso costumam demorar a entregar.

## 6. Granularidade

Qual é o tamanho certo de um caso de uso? O critério é a **sessão**: o que o ator faz em um uso contínuo do sistema, com começo, meio e fim, e que ele consideraria "resolvido" ao sair.

| Grande demais | No ponto | Pequeno demais |
|---|---|---|
| Usar o sistema | Reservar espaço | Digitar a data |
| Gerenciar reservas | Cancelar reserva | Clicar em confirmar |
| Administrar o campus | Bloquear espaço para manutenção | Selecionar o motivo do bloqueio |

> ⚠️ Sinal de granularidade errada: se um caso de uso **não pode ser interrompido sem prejuízo**, ele é um passo, não um caso de uso. Se o ator precisa fazer **outros três** antes de considerar o objetivo atingido, ele é grande demais.

## 🏋️ Exercícios da aula

Na pasta `aula-10/` do seu repositório:

1. **`ex01.md`** — liste **todos os atores** do sistema-guia, classificando cada um em principal (usa para atingir objetivo próprio) ou secundário (é acionado pelo sistema). Para cada um, escreva o objetivo dele em uma frase. Depois escreva o parágrafo que **define a fronteira**: o que está dentro, o que está fora, e a consequência prática de o Sistema Acadêmico estar do lado de fora;
2. **`ex02.md`** — os oito nomes abaixo foram entregues como casos de uso. Diga quais **não são**, explique o defeito de cada um e reescreva: (a) Tela de reservas; (b) Consultar disponibilidade; (c) Gerenciar espaços; (d) Validar formulário; (e) Bloquear espaço para manutenção; (f) Login; (g) Emitir relatório de ocupação; (h) Selecionar sala na lista;
3. **`ex03.md`** — decida entre `include`, `extend` e nenhum dos dois para cada par, justificando com a pergunta "isto acontece sempre?": (a) `Reservar espaço` e `Autenticar-se`; (b) `Reservar espaço` e `Deslocar reserva de menor prioridade`; (c) `Bloquear espaço` e `Notificar afetados`; (d) `Consultar disponibilidade` e `Obter grade de aulas`; (e) `Cancelar reserva` e `Aplicar penalidade por não comparecimento`. Para os que você marcou como `extend`, escreva também a **condição** que dispara a extensão;
4. **`ex04.md`** — especifique **dois casos de uso** do sistema-guia no formato completo da seção 4 (ficha, fluxo principal, alternativos e de exceção). Escolha entre: `Cancelar reserva`, `Confirmar uso`, `Bloquear espaço para manutenção` e `Consultar disponibilidade`. Cada um precisa ter no mínimo **dois fluxos de exceção**, e cada exceção deve citar a regra (`RN-NN`) ou a observação de contexto que a origina;
5. **Desafio 🌶️ `ex05.md`** — o [guia de notações](../../recursos/notacoes-uml.md#6-casos-de-uso-em-plantuml) traz um diagrama de casos de uso do sistema-guia com seis elipses. **Parta dele e vá além:** (a) revise o diagrama — acrescente os casos de uso que faltam, corrija os relacionamentos que você discordar e **justifique cada mudança**; gere o `.svg` e commite os dois arquivos; (b) especifique **três** casos de uso do seu diagrama no formato completo, sendo pelo menos um deles ainda não especificado no `ex04`; (c) escreva meia página respondendo: **o que a especificação textual revelou que o diagrama escondia?** Liste as regras, exceções e perguntas que só apareceram quando você escreveu os fluxos. Se não apareceu nenhuma, você provavelmente escreveu só o caminho feliz — volte e pergunte "e se não?" em cada passo.

## 🧠 Revisão

[8 questões de múltipla escolha](revisao/README.md) para conferir se os conceitos ficaram sólidos. Responda sem consultar a aula — depois volte e corrija.

## ✅ Entrega

```bash
git add aula-10/
git commit -m "Resolve exercícios da aula 10 (casos de uso)"
git push
```

---

⬅️ [Aula 09 — Por que modelar e o que é UML](../aula-09-por-que-modelar-e-uml/README.md) | ➡️ [Aula 11 — Diagrama de classes](../aula-11-diagrama-de-classes/README.md)
