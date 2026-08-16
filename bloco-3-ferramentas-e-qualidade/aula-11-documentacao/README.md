# Aula 11 — Documentação

> 🎯 Objetivos: decidir o que documentar a partir de quem lê e de qual decisão o documento apoia, reconhecer documentação como elemento de qualidade e quantificar o custo da ausência.
> 🎬 Slides da aula: [apresentacao-11-documentacao.pdf](apresentacao/apresentacao-11-documentacao.pdf)

## 1. O documento que ninguém leu

O projeto da clínica-escola entregou, junto com o sistema, um documento de sessenta páginas: visão, escopo, arquitetura, dicionário de dados, plano de testes, manual do usuário.

Oito meses depois, ninguém o abriu. Quando a auditoria pediu evidência sobre o controle de acesso, a resposta estava lá — na página 41 — e ninguém sabia. O documento existia e não servia, que é diferente de não existir.

Duas semanas antes, uma decisão sobre onde guardar o prontuário havia sido refeita do zero numa reunião de duas horas, porque a página 12 não fora encontrada.

Os dois episódios têm a mesma causa e desmentem as duas posições habituais sobre o assunto. **Não foi falta de documentação** — ela existia, com sessenta páginas. E **não foi excesso** — se estivesse organizada por pergunta, as sessenta páginas teriam servido.

**A pergunta não é "documentamos ou não?"** — é ***quem lê, e para decidir o quê?*** Um documento sem leitor e sem decisão associada é custo puro, e pior: dá à organização a sensação de que o assunto está resolvido.

> 💡 **O documento de sessenta páginas não falhou por ser longo.** Falhou por não ter sido escrito para nenhuma pergunta específica. Sessenta páginas organizadas por pergunta — *"como se concede acesso?"*, *"por que este banco?"* — teriam sido consultadas.

## 2. Por que documentar: as três razões que se sustentam

Documentação boa responde a pelo menos uma destas três, e é possível dizer qual:

| Razão | Leitor | Exemplo na clínica-escola |
|---|---|---|
| **Decidir depois** | quem chega ao projeto no ano que vem | o ADR sobre bancos separados, com as alternativas descartadas |
| **Operar** | quem usa ou sustenta o sistema | como conceder e revogar acesso de um aluno |
| **Provar** | quem audita, contrata ou fiscaliza | o registro de quem aprovou cada concessão |

Se um documento não serve a nenhuma das três, ele existe por hábito. O manual de sessenta páginas continha as três coisas — misturadas, sem índice por pergunta, e por isso inúteis para os três leitores.

Repare que **os três leitores são pessoas diferentes, com pressas diferentes**: quem chega no ano que vem tem tempo e nenhum contexto; quem opera tem contexto e nenhum tempo; quem audita tem uma lista fechada de perguntas. Escrever para os três de uma vez é escrever para nenhum.

> ⚠️ **"Documentar para o caso de alguém precisar" não é razão.** É a formulação que produz documento genérico: sem leitor definido, escreve-se tudo com o mesmo peso, e quem procura algo específico desiste na terceira página.

As três razões pedem **formatos diferentes**, e é por isso que misturá-las num documento só não funciona:

| Razão | Formato que serve | O que o inutiliza |
|---|---|---|
| decidir depois | meia página por decisão, com alternativas descartadas | virar relatório longo, em que a decisão se perde |
| operar | procedimento numerado, passo a passo | virar texto corrido, que ninguém segue sob pressão |
| provar | registro com data, autor e aprovação | ser reconstituído depois, o que a auditoria detecta |

O manual de sessenta páginas fracassou exatamente aqui: **um formato só para três necessidades incompatíveis.** Quem precisava do procedimento encontrou texto corrido; quem auditava encontrou descrição em vez de registro; quem queria a decisão encontrou a conclusão sem o motivo.

E isso responde a uma dúvida comum: *"posso juntar tudo num documento só?"* Pode, se for um índice que aponta para os três — nunca se for um texto que tenta atender aos três ao mesmo tempo.

## 3. Quando documentar, e quanto

Três critérios decidem, e todos são de gestão:

**Quanto custa redescobrir.** Uma decisão de arquitetura custa duas horas de reunião para ser refeita — e pode ser refeita **errado**, porque a premissa original se perdeu. Meia página evita isso. Já o motivo de um nome de variável não custa nada redescobrir: está no código, e quem precisar dele já está lendo o código.

O critério tem um efeito prático agradável: ele **elimina a maior parte da documentação** que os projetos produzem por hábito. Descrição de tela, listagem de campos, explicação de fluxo óbvio — tudo isso é barato de redescobrir olhando o produto, e caro de manter atualizado.

**Quantas pessoas vão passar por aqui.** Um projeto de três pessoas que se conhecem precisa de menos registro que um de vinte com rotatividade. Documentação é, em boa medida, **comunicação com quem ainda não chegou**.

**Se alguém vai cobrar.** Auditoria, contrato e norma criam obrigação. Aqui não há escolha, e a decisão é só sobre formato e momento — e o momento importa, porque registro produzido depois não vale como evidência.

Os três critérios se aplicam **item a item**, e não ao projeto inteiro. É comum ver a discussão em bloco — *"este projeto documenta ou não?"* —, e ela não tem resposta. O que tem resposta é *"esta decisão vale meia página?"*, repetida algumas dezenas de vezes ao longo do projeto.

| Situação | Documentar |
|---|---|
| decisão cara de reverter (Aula 04) | **sim**, meia página, na hora |
| regra de negócio que ninguém mais lembra de onde veio | **sim**, junto da regra |
| procedimento que a auditoria vai pedir | **sim**, com registro de execução |
| como o código funciona internamente | quase nunca — o código é a fonte |
| o que está óbvio na tela | não |
| o que a norma ou o contrato exigem | **sim**, e no formato que eles pedem |

> 💡 **A regra prática: documente a decisão e a premissa, não a descrição.** A descrição do sistema envelhece sozinha e alguém a encontra lendo o produto. A decisão — e o que foi descartado — não está em lugar nenhum além do documento.

## 4. Documentação como elemento de qualidade

Documentação entra nas duas metades do sistema de qualidade da Aula 10:

- Na **garantia**, ela é o processo escrito que a auditoria verifica: existe procedimento para conceder acesso, e ele foi seguido;
- No **controle**, ela é o critério contra o qual o resultado é conferido: a Definição de Pronto, os critérios de aceite, o registro do que se testou.

E há um efeito indireto que costuma passar batido: **escrever revela o que não se entendeu.** Um requisito que não se consegue escrever de forma verificável não está entendido, e a dificuldade de redação é o sintoma. É mais barato descobrir isso escrevendo do que construindo.

O mesmo vale para decisão. Quem não consegue escrever meia página explicando **por que** escolheu uma alternativa e descartou outra costuma não ter comparado as duas — apenas escolheu a que já conhecia. A folha em branco é o teste mais barato que existe contra decisão por hábito.

> 💡 **É o mesmo princípio do Desafio 🌶️ deste curso.** Defender a escolha por escrito, com o que se perde, não é exercício de redação: é o método que expõe a decisão que não foi tomada de verdade.

> ⚠️ **Documentação errada é pior que documentação ausente.** A ausente ninguém usa; a errada engana quem confia nela. Um documento que descreve um sistema mudado há oito meses vai orientar uma decisão hoje — e a pessoa que decidir não terá como saber que estava desatualizado.

Duas defesas contra isso:

- **Documento perto do que descreve**, versionado junto, para que a mudança de um puxe a revisão do outro;
- **Data e dono visíveis.** Um documento com "atualizado em 03/2026, responsável: Ana" permite ao leitor calibrar a confiança. Sem isso, todo documento parece atual.

A segunda é quase de graça e resolve metade do problema: **o leitor deixa de precisar adivinhar.** Um procedimento datado de dois anos atrás continua sendo consultado, mas com a desconfiança certa — e alguém acaba perguntando se ainda vale, que é exatamente o comportamento desejado.

## 5. O que a ausência custa

O custo da não-documentação não aparece como item de orçamento, e por isso parece zero. Ele aparece **disperso**, em horas de várias pessoas ao longo de meses — o que é a forma mais fácil de um custo passar despercebido. Ele se manifesta assim:

| Sintoma | O que estava faltando |
|---|---|
| a mesma decisão discutida duas vezes, com pessoas diferentes | registro da decisão e das alternativas |
| a pessoa que sabe sai, e o projeto para duas semanas | procedimento operacional escrito |
| a auditoria pede evidência e a organização reconstitui às pressas | registro de execução |
| o time reimplementa uma regra que já existia em outro módulo | nada escrito sobre a regra de negócio |
| a nova pessoa leva três meses para produzir | documentação de entrada, e não de tudo |
| ninguém sabe se aquele campo pode ser removido | registro de qual regra o criou, e para quem |

Na transportadora, o risco **R-02** da Aula 09 — o único conhecedor do legado se aposenta — é literalmente um risco de ausência de documentação. A resposta escolhida lá, gravar sessões com ele, é uma forma barata de documentar: **o formato não precisa ser um documento formal.**

Repare no que a Aula 09 permite fazer aqui: **a ausência de documentação vira um risco com probabilidade, impacto, dono e gatilho**, e passa a ser tratada como qualquer outro risco. É a forma mais eficaz de justificar o esforço a um patrocinador que acha documentação perda de tempo — porque a conversa deixa de ser sobre boas práticas e passa a ser sobre seis semanas de atraso.

E quando o risco se concretiza, o custo aparece inteiro de uma vez: a pessoa saiu, e o que ela sabia não está em lugar nenhum. **Não há como documentar retroativamente o conhecimento de quem já foi embora.**

> 💡 **Documentação também é decisão de custo-benefício, e o benefício é probabilístico.** Você escreve hoje contra a chance de precisar depois. Escrever tudo é caro e certo; escrever nada é barato e arriscado. O trabalho de gestão é escolher onde, e isso se faz pelas três razões da seção 2.

Há um caso em que a conta é sempre favorável, e vale conhecê-lo: **quando o custo de escrever é pago uma vez e o de redescobrir é pago muitas.** O procedimento de concessão de acesso é consultado por cada aluno novo, a cada semestre. Meia página escrita uma vez economiza uma pergunta por semana, indefinidamente.

O caso oposto — escrever uma vez, ler nunca — é o manual de sessenta páginas. A diferença entre os dois não é o assunto: é o número de vezes que alguém vai precisar da informação.

## 6. Documento que se mantém sozinho

Documento desatualiza porque manter custa esforço e ninguém é cobrado por isso. Quatro formas de reduzir esse custo — todas por **escrever menos**, não por disciplina:

| Prática | Por que funciona |
|---|---|
| escrever a **decisão**, não a descrição | decisão não muda sozinha; descrição muda toda semana |
| viver **junto do que descreve**, no mesmo repositório | a mudança de um aparece na revisão do outro |
| **um documento por pergunta**, curto | quem procura acha; quem atualiza sabe o escopo |
| **datar e assinar** | o leitor calibra a confiança sem precisar conferir |

E a decisão mais honesta, quando um documento não é mantido: **apagá-lo**. Um documento morto no repositório é uma armadilha — alguém vai encontrá-lo e acreditar. Removê-lo é melhor que fingir que existe manutenção.

Um exemplo de documento que se mantém quase sozinho, e que este curso usa o tempo todo:

| | |
|---|---|
| **Pergunta** | Como se concede acesso ao prontuário a um aluno? |
| **Leitor** | quem opera a secretaria da clínica, e a auditoria |
| **Atualizado** | 03/2026 · responsável: Ana |
| **Procedimento** | 1. o supervisor solicita por formulário; 2. a coordenação confere a matrícula ativa; 3. o acesso é concedido com prazo do semestre; 4. a revogação é automática na data |
| **Evidência** | cada concessão gera registro com solicitante, aprovador e prazo |

Meia página, uma pergunta, leitor nomeado, data e dono. Ele só desatualiza se o **procedimento** mudar — e quando muda, quem muda sabe que este documento existe, porque ele é curto e tem dono.

> ⚠️ **Nenhuma dessas práticas resolve por si só a documentação que ninguém quis escrever.** Se a organização não reserva tempo para isso no plano, ela será feita às pressas no fim, quando alguém cobrar — e será reconstituição, não registro.

E vale dizer o desconfortável: **o time raramente é cobrado por documentar, e sempre é cobrado por entregar.** Enquanto for assim, nenhuma boa prática se sustenta por convencimento. O que sustenta é a documentação estar **no plano**, com tempo alocado, como qualquer outro entregável da EAP.

> 📖 O Guia PMBOK trata dos documentos do projeto e do registro de decisões na área de integração, e das exigências de registro na área de qualidade. O Sommerville discute documentação de processo e de produto no capítulo sobre gerenciamento de qualidade.

## 🏋️ Exercícios da aula

Na pasta `aula-11/` do seu repositório:

1. **`ex01.md`** — para cada documento, identifique **o leitor** e **a decisão** que ele apoia, ou diga que não há nenhum: (a) o ADR sobre bancos separados; (b) o manual de sessenta páginas da abertura; (c) o procedimento de concessão de acesso; (d) um documento descrevendo cada tela do sistema; (e) o registro de quem aprovou cada acesso; (f) um diagrama do fluxo de atendimento da clínica. *Confere assim: dois dos seis não têm leitor nem decisão associada — e um deles é o que mais gente diria ser indispensável.*

2. **`ex02.md`** — decida **documentar ou não** em cinco situações do projeto de [frota e manutenção](../../recursos/projetos-para-praticar.md#11-frota-e-manutenção-preventiva), justificando por um dos três critérios da seção 3: (a) por que se escolheu processar telemetria em lote; (b) como o sistema calcula a próxima manutenção; (c) o nome dos campos da tela de cadastro; (d) o procedimento de cadastro de um veículo novo; (e) por que o hodômetro manual tem validação de faixa. *Confere assim: um dos cinco é "não documentar" e a justificativa é sempre a mesma — quanto custa redescobrir.*

3. **`ex03.md`** — para cada sintoma da tabela da seção 5, escreva **quanto ele custou** num caso concreto que você invente com números — horas, semanas, pessoas. Depois some e compare com o esforço de escrever o que faltava. *Confere assim: se a sua conta der que documentar custa mais, releia — o exercício não é provar que documentar sempre compensa, e uma das cinco pode mesmo não compensar. Diga qual.*

4. **`ex04.md`** — pegue o manual de sessenta páginas da abertura e **reorganize-o**: proponha a lista de documentos curtos que o substituiria, cada um com título em forma de pergunta, leitor e tamanho estimado. *Confere assim: se a sua lista somar mais de dez documentos, você fatiou demais — e se somar menos de quatro, algum dos três leitores da seção 2 ficou sem nada.*

5. **`ex05.md`** — 🌶️ **Desafio.** Você assume um projeto de oito meses, cinco pessoas, com auditoria externa prevista. O patrocinador diz que "documentação é perda de tempo, o time é bom". **Escreva o mínimo de documentação do projeto**, contendo: (i) a lista do que será escrito, com leitor e razão de cada item; (ii) o que **não** será escrito, e a justificativa de cada exclusão; (iii) **o que se perde** com as exclusões, e em que cenário a decisão se mostraria errada. *Confere assim: a lista do item (ii) precisa ser maior que a do item (i). Se você não excluiu quase nada, não decidiu — só listou tudo o que existe.*

### 📤 Entrega

Estes exercícios são feitos em sala e vão para o **seu repositório** `exercicios-projeto-software`:

```bash
cd ..                 # da pasta da aula para a raiz do repositório
git add aula-11/
git commit -m "Resolve exercícios da aula 11"
git push
```

Confira no navegador que a pasta apareceu em `github.com/SEU-USUARIO/exercicios-projeto-software`.

## 🧠 Revisão

[8 questões de múltipla escolha](revisao/README.md) para conferir se os conceitos ficaram sólidos. Responda sem consultar a aula — depois volte e corrija.

---

⬅️ [Aula 10 — Qualidade que se mede](../aula-10-qualidade-que-se-mede/README.md) | ➡️ [Aula 12 — Ferramentas e comunicação](../aula-12-ferramentas-e-comunicacao/README.md)
