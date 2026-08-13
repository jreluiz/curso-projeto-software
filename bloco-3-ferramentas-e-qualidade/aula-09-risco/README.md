# Aula 09 — Risco

> 🎯 Objetivos: distinguir risco de problema, escrever risco no formato causa–evento–efeito, posicioná-lo na matriz probabilidade × impacto e escolher a resposta com dono e gatilho.
> 🎬 Slides da aula: [apresentacao-09-risco.pdf](apresentacao/apresentacao-09-risco.pdf)

## 1. Risco não é problema

Na transportadora, a integração com o ERP legado depende de uma pessoa: o único servidor que conhece o sistema, e que **se aposenta em quatro meses**. A documentação está desatualizada há anos.

Isso é **risco**: ainda não aconteceu, pode acontecer, e se acontecer custa caro.

Na mesma empresa, o servidor de relatórios está lento há três semanas e todo mundo reclama. Isso é **problema**: já aconteceu, e o que se faz com ele é resolver.

| | Risco | Problema |
|---|---|---|
| **Quando** | pode acontecer | já aconteceu |
| **O que se faz** | acompanha, com resposta preparada | resolve |
| **Quem cuida** | o dono do risco | quem tem o problema |
| **Some quando** | o evento acontece — ou a janela passa | é resolvido |

A confusão custa das duas formas. Chamar problema de risco adia a solução: fica na planilha, monitorado, enquanto o servidor segue lento. E tratar risco como problema é não fazer nada até ele virar um — que é o modo padrão de operar em boa parte dos projetos.

Há ainda uma terceira categoria, que a gestão de projeto trata à parte: a **oportunidade**. Ela é um evento incerto de efeito **positivo** — o fornecedor pode entregar o ambiente antes do previsto, liberando duas semanas. As mesmas quatro respostas valem, invertidas: explorar, ampliar, compartilhar, aceitar. Este curso trata só das ameaças, que são o caso frequente.

> ⚠️ **Se tudo virar risco, a lista fica longa e ninguém a lê.** Uma lista de 40 riscos é o mesmo que nenhuma: ninguém prioriza 40 coisas. Depurá-la é parte do trabalho.

## 2. A natureza do risco: causa, evento, efeito

*"Risco: integração"* não é risco — é assunto. Não dá para estimar probabilidade nem impacto de um assunto, e por isso ele fica na planilha para sempre.

Um risco bem escrito tem três partes:

```
   CAUSA                       →  EVENTO INCERTO        →  EFEITO
   algo que já é verdade          o que pode acontecer     o que isso custa
```

Aplicado à transportadora:

> **R-01** — Porque a documentação do ERP está desatualizada e há um só conhecedor, **a integração pode levar o dobro do estimado**, atrasando a entrega em cerca de 6 semanas.

A causa é **fato**, o evento é **incerto**, e o efeito é **quantificado**. Com as três partes, a conversa muda: dá para estimar a probabilidade (a causa é forte), dimensionar o impacto (6 semanas contra prazo de 9 meses) e — o mais importante — **atacar a causa**, que é a única parte sobre a qual se pode agir hoje.

> 💡 **Escrever o risco já sugere a resposta.** Se a causa é "documentação desatualizada e um só conhecedor", a resposta aparece sozinha: mapear a integração cedo, e gravar sessões com quem sabe. É por isso que a redação não é formalidade.

Um teste rápido de redação: se o texto do risco tiver **duas causas incertas**, ele são dois riscos e precisa ser partido. *"Se o fornecedor atrasar e a equipe ficar reduzida, o projeto atrasa"* mistura dois eventos com probabilidades diferentes, e não dá para classificar nem responder a nenhum dos dois.

## 3. Como se levanta risco

Riscos não aparecem sozinhos numa reunião em que se pergunta *"alguém vê algum risco?"*. Três fontes que funcionam:

| Fonte | O que ela dá |
|---|---|
| **As premissas do termo de abertura** | toda premissa é um risco: se ela cair, o plano cai. É a fonte mais barata e a mais ignorada |
| **Lições aprendidas de projetos anteriores** | o que deu errado antes tende a dar de novo — é o uso concreto do encerramento da Aula 03 |
| **As pessoas que executam** | quem vai fazer a integração sabe o que preocupa; quem vai operar sabe o que quebra |

E vale percorrer categorias, para não olhar só onde a luz já está acesa: **técnico** (integração, desempenho, tecnologia nova), **de pessoas** (saída, indisponibilidade, competência), **externo** (fornecedor, legislação, clima), **de gestão** (escopo, prazo, comunicação) e **organizacional** (prioridade muda, patrocinador sai).

> ⚠️ **O risco mais perigoso costuma ser organizacional, e é o que menos se escreve.** *"O patrocinador pode perder a eleição e o projeto perder o padrinho"* é constrangedor de registrar, e é exatamente o tipo de coisa que mata projeto — como na assembleia digital, onde a diretoria que contrata pode perder a eleição que o sistema vai apurar.

## 4. A matriz probabilidade × impacto

Com os riscos escritos, é preciso decidir **quais merecem trabalho**. A matriz cruza as duas dimensões:

| | Impacto baixo | Impacto médio | Impacto alto |
|---|---|---|---|
| **Prob. alta** | 🟡 monitorar | 🔴 atacar já | 🔴 atacar já |
| **Prob. média** | 🟢 aceitar | 🟡 monitorar | 🔴 atacar já |
| **Prob. baixa** | 🟢 aceitar | 🟢 aceitar | 🟡 monitorar |

Duas armadilhas de leitura:

**Probabilidade baixa com impacto altíssimo não é "aceitar".** O canto inferior direito é onde moram os riscos que acabam com o projeto — vazamento de dado de saúde na clínica-escola, por exemplo. A matriz manda monitorar, e monitorar aqui significa ter uma resposta pronta, não olhar de vez em quando.

**Impacto não é só prazo.** Ele pode ser custo, reputação, conformidade legal ou segurança de alguém. Na clínica-escola, o impacto de um acesso indevido é jurídico e reputacional, e não se mede em semanas.

> 💡 **Duas escalas de três níveis bastam** para um projeto do tamanho dos deste curso. Escalas de 1 a 10 dão falsa precisão: ninguém distingue um impacto 6 de um 7, e a discussão passa a ser sobre o número em vez de sobre o risco.

Vale combinar o que cada nível significa **antes** de classificar, senão cada pessoa usa uma régua:

| Nível | Probabilidade | Impacto (prazo) |
|---|---|---|
| **baixa / baixo** | seria surpresa | até 1 semana |
| **média / médio** | acontece em projetos assim | 1 a 4 semanas |
| **alta / alto** | é mais provável que não | mais de 4 semanas, ou a data cai |

Com a régua escrita, a classificação vira conversa sobre o projeto. Sem ela, vira negociação sobre adjetivos — e quem tem mais voz na sala classifica os próprios riscos como baixos.

## 5. As quatro respostas ao risco

Para cada risco que merece trabalho, escolhe-se uma resposta:

| Resposta | O que se faz | Exemplo na transportadora |
|---|---|---|
| **Evitar** | mudar o plano para que o risco deixe de existir | não integrar com o ERP; digitar os dados manualmente na fase 1 |
| **Mitigar** | reduzir a probabilidade ou o impacto | mapear a integração no primeiro mês, enquanto o servidor está lá |
| **Transferir** | passar o impacto a outro — contrato, seguro, fornecedor | contratar a integração com a empresa que mantém o ERP |
| **Aceitar** | conviver, conscientemente e por escrito | assumir que o dado manual terá erro, e prever conferência |

As quatro são legítimas, e **aceitar é uma decisão, não uma omissão** — a diferença é que a decisão está escrita, com quem decidiu e sob qual premissa.

> ⚠️ **Evitar é a resposta mais esquecida e às vezes a mais barata.** Muita reunião de risco discute como mitigar algo que o projeto poderia simplesmente não fazer. Antes de perguntar "como reduzimos?", vale perguntar "precisamos mesmo disto agora?".

Toda resposta tem custo, e o custo precisa aparecer:

| Resposta | O que ela custa |
|---|---|
| **Evitar** | escopo, quase sempre. Não integrar significa entregar menos |
| **Mitigar** | esforço agora, para reduzir uma perda que talvez não venha |
| **Transferir** | dinheiro, e a dependência de um terceiro que também pode falhar |
| **Aceitar** | nada agora, tudo depois — se o evento acontecer |

**Transferir não faz o risco sumir.** Contratar a integração com quem mantém o ERP transfere o impacto técnico e cria um risco novo: dependência de um fornecedor com agenda própria. É comum e é aceitável — desde que o risco novo entre na lista, em vez de desaparecer junto com o antigo.

E há uma resposta que não está na lista de propósito: **esperar para ver**. Ela parece aceitar, mas não é — aceitar é uma decisão registrada, com quem decidiu; esperar para ver é a ausência de decisão, e o registro fica vazio.

## 6. Risco sem dono e sem gatilho não existe

Identificar risco é fácil e agradável; responsabilizar é desconfortável. É por isso que tantas matrizes têm vinte riscos bem classificados e nenhum nome ao lado.

O registro completo, que é o artefato desta aula:

| ID | Risco (causa → evento → efeito) | P | I | Resposta | Dono | Gatilho |
|---|---|:---:|:---:|---|---|---|
| R-01 | documentação do ERP desatualizada → integração pode levar o dobro → +6 semanas | alta | alto | mitigar: mapear a integração no 1º mês | Ana | mapeamento não concluído até 30/03 |
| R-02 | único conhecedor se aposenta em 4 meses → conhecimento se perde → retrabalho | alta | alto | mitigar: 4 sessões gravadas com ele | Bruno | agenda não fechada até 15/03 |
| R-03 | motorista digita hodômetro errado → manutenção disparada fora de hora → custo de parada | média | médio | mitigar: validação de faixa no registro | Ana | 3 leituras inconsistentes na semana |
| R-04 | oficina própria tem capacidade limitada → fila de manutenção → veículo parado | média | alto | transferir: contrato com oficina externa | Carla | fila acima de 4 veículos |

Duas colunas fazem a diferença entre gestão e literatura:

**Dono** é uma pessoa, não uma área. "TI" não acompanha risco nenhum; Ana acompanha.

**Gatilho** é o sinal observável de que o risco está virando problema — com número e data. Sem ele, a resposta é acionada quando alguém lembra, que costuma ser tarde. *"Fila acima de 4 veículos"* é gatilho; *"quando a situação piorar"* não é.

> 💡 **O registro de riscos é revisado, não arquivado.** A cada marco: o que saiu (a janela passou), o que entrou, o que mudou de quadrante. Um registro idêntico ao de três meses atrás significa que ninguém o está usando.

E há um destino que todo risco tem, e que quase nunca se registra: **o que aconteceu com ele**. Três finais possíveis:

- **A janela passou** — o servidor se aposentou e as sessões estavam gravadas. O risco sai da lista, e a lição vai para o encerramento;
- **O evento aconteceu** — o risco vira problema, e a resposta preparada é acionada. Se ela funcionou, isso é o melhor resultado possível da gestão de risco;
- **A resposta falhou** — o evento aconteceu e a mitigação não bastou. É a informação mais valiosa para o próximo projeto, e a que menos se escreve.

Registrar o destino é o que transforma gestão de risco em aprendizado organizacional. Sem isso, cada projeto começa a lista do zero, como se ninguém antes tivesse integrado com um legado sem documentação.

> ⚠️ **Risco que virou problema não some do registro.** Ele muda de estado, e o registro passa a mostrar quanto custou de verdade contra quanto se estimou. É assim que a estimativa do próximo projeto melhora.

> 📖 O Guia PMBOK dedica uma área de conhecimento inteira ao risco, com os processos de identificação, análise qualitativa e quantitativa, planejamento de respostas e monitoramento. As quatro respostas a ameaças estão no processo de planejamento de respostas.

## 🏋️ Exercícios da aula

Na pasta `aula-09/` do seu repositório:

1. **`ex01.md`** — classifique cada item em **risco** ou **problema**: (a) o servidor de relatórios está lento há três semanas; (b) o único conhecedor do legado se aposenta em quatro meses; (c) a equipe não conseguiu entregar duas das cinco funcionalidades da iteração; (d) a legislação sobre dado de saúde pode mudar no ano que vem; (e) o fornecedor atrasou a entrega do ambiente em duas semanas; (f) a diretoria pode trocar na próxima eleição. *Confere assim: três de cada, e o critério é sempre se o evento já ocorreu — não se ele é grave nem se há solução conhecida.*

2. **`ex02.md`** — reescreva cinco riscos mal formulados no formato **causa → evento → efeito**, quantificando o efeito: (a) "risco: integração"; (b) "risco: equipe pequena"; (c) "risco: prazo apertado"; (d) "risco: LGPD"; (e) "risco: fornecedor". Use o contexto do [prontuário de clínica-escola](../../recursos/projetos-para-praticar.md#10-prontuário-de-clínica-escola). *Confere assim: em cada um, a causa precisa ser algo que **já é verdade hoje** — se você escreveu uma causa incerta, o risco tem dois eventos e precisa virar dois riscos.*

3. **`ex03.md`** — posicione seis riscos do projeto de [frota e manutenção preventiva](../../recursos/projetos-para-praticar.md#11-frota-e-manutenção-preventiva) na matriz probabilidade × impacto, e diga quais merecem trabalho agora. Um deles precisa ser de **probabilidade baixa e impacto alto**. *Confere assim: o de probabilidade baixa e impacto alto não pode cair em "aceitar" — releia a seção 4 se ele caiu.*

4. **`ex04.md`** — para cada um dos quatro riscos da tabela da seção 6, proponha uma **resposta diferente** da que está lá e diga o que se ganha e o que se perde com a troca. Pelo menos uma das suas propostas precisa ser **evitar**. *Confere assim: a resposta "evitar" sempre custa escopo ou funcionalidade — se a sua não custou nada, você não evitou o risco, só mudou o nome da mitigação.*

5. **`ex05.md`** — 🌶️ **Desafio.** Monte o **registro de riscos** do [prontuário de clínica-escola](../../recursos/projetos-para-praticar.md#10-prontuário-de-clínica-escola), com no mínimo cinco riscos, todas as sete colunas preenchidas, e inclua **um risco organizacional** — daqueles constrangedores de escrever. Depois, escolha **um** risco e escreva um parágrafo defendendo por que ele deve ser atacado antes dos outros, e **o que se perde** ao priorizá-lo. *Confere assim: se todos os seus riscos forem técnicos, releia a seção 3 — o projeto tem comitê de ética, auditoria externa e uma notificação recente por dado exposto.*

## 🧠 Revisão

[8 questões de múltipla escolha](revisao/README.md) para conferir se os conceitos ficaram sólidos. Responda sem consultar a aula — depois volte e corrija.

## ✅ Entrega

```bash
git add aula-09/
git commit -m "Resolve exercícios da aula 09 (risco)"
git push
```

---

⬅️ [Aula 08 — Descobrir, enxugar, melhorar](../../bloco-2-metodologias-de-gestao/aula-08-design-thinking-mvp-lean/README.md) | ➡️ [Aula 10 — Qualidade que se mede](../aula-10-qualidade-que-se-mede/README.md)
