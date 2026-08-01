# 👥 Trabalho em Dupla — Documento de Requisitos via Pull Request

> 📅 **Quando:** Bloco 2, após a [Aula 08](../bloco-2-requisitos/aula-08-analise-priorizacao-validacao/README.md).
> 🎯 **O que se aprende aqui e em nenhum outro lugar:** defender um requisito para alguém que discorda — e reescrevê-lo quando o argumento do outro é melhor.

Escrever requisito sozinho esconde um problema: você nunca descobre que a sua frase só é clara na sua cabeça. Este trabalho existe para que **outra pessoa leia o seu requisito e pergunte "como você testaria isso?"**.

E o Pull Request é o lugar natural para isso. O comentário de linha do GitHub foi feito exatamente para dizer *"'o sistema deve responder rapidamente' — rapidamente quanto, medido como?"*.

## 📋 Formato

- **Dupla**, com um repositório compartilhado;
- **Ninguém commita no `main`.** Todo trabalho entra por Pull Request revisado pelo colega;
- **Mínimo de 3 PRs por pessoa**, com revisão de verdade — "LGTM 👍" não conta como revisão;
- O tema vem do [catálogo de sistemas para praticar](../recursos/sistemas-para-praticar.md) (⭐⭐ ou ⭐⭐⭐) ou é proposto pela dupla.

> ⚠️ A **Reserva de Espaços do Campus** não pode ser escolhida: ela é o [sistema-guia](../recursos/sistema-guia.md), e os requisitos dela estão publicados nas aulas.

## 🛠️ Preparação

```bash
# Aluno A cria o repositório no GitHub e adiciona B como collaborator
# (Settings → Collaborators → Add people)

git clone https://github.com/ALUNO-A/requisitos-<tema>.git
cd requisitos-<tema>

# Cada rodada de trabalho começa assim:
git checkout main
git pull
git checkout -b requisitos-funcionais     # branch com nome do que você vai fazer
# ... escreve ...
git add . && git commit -m "Adiciona os 14 requisitos funcionais"
git push -u origin requisitos-funcionais
# Abre o PR no GitHub e pede a revisão do colega
```

> 📏 Configure a proteção do `main`: **Settings → Branches → Add rule → Require a pull request before merging**. Sem isso, a primeira pressa acaba com o combinado.

## 🔄 As três rodadas

### Rodada 1 — Divisão

| Quem | Entrega | Branch |
|---|---|---|
| **A** | Contexto do sistema · mapa de interessados com conflitos · **requisitos funcionais** numerados | `contexto-e-funcionais` |
| **B** | **Requisitos não-funcionais** numerados e com critério objetivo · glossário do domínio · **regras de negócio** numeradas | `nao-funcionais-e-regras` |

B só pode começar depois que o PR de A estiver aberto — mas **não precisa esperar o merge**. Trabalhar sobre um documento em revisão é realista, e é onde as divergências aparecem.

> 💡 Repare que a divisão não é "cada um faz metade dos requisitos". Ela separa **naturezas diferentes de trabalho**, justamente para que cada um revise algo que não escreveu.

### Rodada 2 — Revisão cruzada

Cada um revisa o PR do outro **com comentários de linha**, cobrindo obrigatoriamente:

- [ ] Cada requisito passa no teste **"como eu saberia que isto foi cumprido?"** (Aula 05);
- [ ] Nenhum requisito é **solução disfarçada** — botão, tela, tecnologia (Aula 05, §5);
- [ ] Nenhum requisito é **composto** — se metade pode estar pronta, são dois (Aula 08, §1);
- [ ] Cada não-funcional tem **número, unidade ou critério**;
- [ ] A [lista de verificação de não-funcionais](../bloco-2-requisitos/aula-05-o-que-e-um-requisito/README.md#3-os-não-funcionais-que-ninguém-pede) foi percorrida, e o que não se aplica está escrito como não se aplicando;
- [ ] O glossário não tem dois termos significando a mesma coisa;
- [ ] Toda regra de negócio é verdadeira **mesmo sem o sistema** — se depende do software, é requisito, não regra.

> 💡 **Uma revisão boa faz perguntas, não dá ordens.** *"Um solicitante pode ter duas reservas no mesmo horário?"* é melhor que *"está errado"* — porque metade das vezes quem está errado é quem pergunta, e a pergunta descobre isso sem custo.

### Rodada 3 — O pedido de mudança

Depois dos merges, **invertam os papéis**. Cada um escreve, para o outro, um **pedido de mudança de escopo** realista — do tipo que um cliente manda no meio do projeto, começando por "aproveitando que vocês estão fazendo…".

Quem recebe responde seguindo os quatro passos da [Aula 08, §6](../bloco-2-requisitos/aula-08-analise-priorizacao-validacao/README.md#6-mudança-de-escopo): entender o pedido, dimensionar, apresentar **duas alternativas com custo explícito**, e registrar a decisão. Depois, atualiza o documento conforme o que foi decidido.

É a rodada que mais ensina: documento bom é o que aguenta um requisito novo sem ser refeito.

## 📦 O que entregar

Estrutura do repositório ao final:

```
requisitos-<tema>/
├── README.md              # a entrega principal (ver abaixo)
├── contexto.md            # o problema, o escopo e o que ficou de fora — com o porquê
├── interessados.md        # quem ganha o quê, quem teme o quê, e onde se chocam
├── requisitos.md          # RF e RNF numerados
├── regras-de-negocio.md   # RN numeradas + glossário do domínio
├── backlog.md             # priorizado, com critérios de aceite dos cinco do topo
├── mudanca-de-escopo.md   # os dois pedidos da Rodada 3 e as respostas
└── divergencias.md        # ⭐ o diferencial deste trabalho
```

### `README.md`

- Nome dos dois integrantes e o que cada um fez, por rodada;
- O sistema em **um parágrafo**, escrito para quem nunca ouviu falar dele;
- Link para os demais arquivos;
- **Link para os PRs** — é a prova de que o processo aconteceu.

### `divergencias.md` — o coração do trabalho

Registre **duas divergências reais** que a dupla teve. Para cada uma:

1. **O ponto** — qual decisão estava em disputa;
2. **O argumento de cada lado** — escrito de forma que os dois se reconheçam;
3. **Como foi resolvido** — quem convenceu quem, e com qual evidência;
4. **O que teria acontecido** se a outra opção tivesse ganhado — um caso concreto que quebraria.

> ⚠️ Se a dupla não teve **nenhuma** divergência, uma das duas coisas aconteceu: ou uma pessoa aceitou tudo sem ler, ou uma pessoa fez o trabalho todo. Nos dois casos o objetivo se perdeu — **provoquem a discussão de propósito**: cada um escolhe um requisito do outro e tenta derrubá-lo.

## ✅ Requisitos obrigatórios

Do documento:

- [ ] Contexto em 3 a 5 parágrafos, **sem nomear telas nem tecnologia**;
- [ ] Escopo com uma tabela do que ficou **de fora e por quê**;
- [ ] Mínimo de **5 interessados**, com pelo menos **um que não usa o sistema**;
- [ ] Tabela de **conflitos** com no mínimo 3 tensões entre interesses;
- [ ] Mínimo de **14 requisitos funcionais** numerados;
- [ ] Mínimo de **8 requisitos não-funcionais**, todos com número, unidade ou critério objetivo;
- [ ] Mínimo de **8 regras de negócio** numeradas;
- [ ] **Glossário** com no mínimo 8 termos do domínio;
- [ ] Backlog ordenado com MoSCoW e **critérios de aceite dos 5 itens do topo**;
- [ ] Uma seção de **questões em aberto** — o que vocês não decidiram, e por quê.

Do processo:

- [ ] Mínimo de **3 PRs por pessoa**, cada um com pelo menos **3 comentários de linha** do colega;
- [ ] Nenhum commit direto no `main`;
- [ ] Pelo menos **um PR em que o autor mudou o documento** por causa da revisão — e o commit que mostra a mudança;
- [ ] Os dois pedidos de mudança de escopo, com as respostas em duas alternativas;
- [ ] `divergencias.md` com duas divergências documentadas.

## 🌶️ Extras para ir além

- Escrever **três casos de uso especificados** com os três fluxos (antecipa a Aula 10);
- Converter os critérios de aceite do topo do backlog para **Gherkin**;
- Montar a **matriz de rastreabilidade** ligando cada regra de negócio aos requisitos que a realizam;
- Entrevistar de verdade **uma pessoa** que viva o problema do seu sistema, e anexar a transcrição — comparando o que vocês supunham com o que ela disse;
- Escrever o mesmo requisito **das duas formas defensáveis** e a comparação honesta — é o exercício mais difícil e o que mais ensina.

## 🧭 Como isso é avaliado

Não é o documento mais longo que vence. Em ordem de peso:

1. **A verificabilidade dos requisitos** — um documento curto em que tudo é testável vale mais que um extenso cheio de "amigável" e "eficiente";
2. **A qualidade da revisão que você fez no colega** — encontrar a ambiguidade alheia prova que você entendeu;
3. **A coerência entre as partes** — glossário, requisitos, regras e backlog precisam usar as mesmas palavras para as mesmas coisas;
4. **O registro da divergência e da mudança de escopo** — é a prova de que houve pensamento, e não divisão de tarefas.

> 📏 **O critério que resume tudo:** uma terceira pessoa consegue ler o documento de vocês e construir o sistema **sem perguntar nada a vocês dois**? Onde ela precisaria perguntar, o documento ainda não está pronto.

---

🏠 [Voltar ao início](../README.md)
