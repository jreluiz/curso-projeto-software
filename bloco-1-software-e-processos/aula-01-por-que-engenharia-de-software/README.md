# Aula 01 — Por Que Engenharia de Software Existe

> 🎯 Objetivos: distinguir um programa de um produto de software, reconhecer as causas recorrentes de fracasso em projetos e identificar os papéis de quem faz software chegar ao usuário.
> 🎬 Slides da aula: [apresentacao-01-por-que-engenharia-de-software.pdf](apresentacao/apresentacao-01-por-que-engenharia-de-software.pdf)

## 1. O programa do fim de semana

Um aluno de Sistemas de Informação se cansa de mandar e-mail para a secretaria toda vez que precisa de uma sala de estudo. No sábado, ele escreve isto:

```
programa reserva_salas
  lê o arquivo salas.txt
  mostra as salas livres
  pergunta qual sala e qual horário
  grava a linha no arquivo
```

Na segunda-feira o programa funciona. Ele mostra as salas, aceita a reserva, grava. O aluno está certo: **isso é um programa que funciona.**

Agora a secretaria quer usar de verdade. E a lista de perguntas começa:

- E se duas pessoas reservarem a mesma sala no mesmo segundo?
- E se faltar luz no meio da gravação?
- Quem pode cancelar a reserva de quem?
- Como a manutenção interdita uma sala que já tem três reservas?
- Onde isso roda quando o aluno se formar e levar o notebook embora?
- Quem conserta quando quebrar, daqui a dois anos, e ele não trabalhar mais aqui?

Nenhuma dessas perguntas é sobre programação. **Todas são sobre engenharia**, e é a distância entre a primeira coluna e a segunda que este curso percorre.

## 2. Programa × produto de software

| | Programa | Produto de software |
|---|---|---|
| Usuários | quem escreveu | pessoas que você nunca vai conhecer |
| Entrada | a que o autor imaginou | qualquer uma, inclusive a maliciosa |
| Erro | o autor descobre e conserta | precisa ser tratado, registrado e explicado |
| Documentação | a memória do autor | outra pessoa precisa conseguir manter |
| Testes | "rodei e funcionou" | repetíveis, automatizados, executados a cada mudança |
| Instalação | na máquina dele | em ambientes que ele não controla |
| Vida útil | até resolver o problema | anos, mudando o tempo todo |
| Custo | o fim de semana | **muito mais que o fim de semana** |

Fred Brooks, em *O Mítico Homem-Mês*, estimou o "muito mais": transformar um programa em **produto** custa cerca de **três vezes** o programa original; integrá-lo a um **sistema** que conversa com outros custa outras três. O produto de sistema sai por volta de **nove vezes** o esforço do programa que funcionava no sábado.

> 💡 O número exato importa menos que a ordem de grandeza. Quando alguém disser *"mas isso é simples, eu faço num fim de semana"*, essa pessoa não está errada sobre o programa — está falando de outra coisa. Ela geralmente **tem razão** sobre o fim de semana, e é esse o problema: o fim de semana é 11% do trabalho.

> 📖 Sommerville trata dessa distinção logo na abertura, ao definir o que é software e o que é engenharia de software.

## 3. Por que projetos falham

Software fracassa muito, e quase nunca pelo motivo que a intuição sugere. Estas são as causas que aparecem em toda pesquisa sobre o assunto, em ordem de frequência:

**Requisitos.** O time construiu direito a coisa errada. Alguém entendeu "reserva" como intenção, outro como uso confirmado, e ninguém percebeu antes da entrega. É a causa número um, com folga — e é por isso que um bloco inteiro deste curso é dedicado a ela.

**Escopo que cresce sem negociação.** Cada pedido novo parece pequeno. Ninguém diz não, ninguém tira nada, ninguém remarca o prazo. O prazo continua sendo o mesmo prazo, agora com o dobro de trabalho dentro.

**Comunicação.** Quatro pessoas que se falam trocam 6 pares de informação; dez pessoas trocam 45. Times grandes não são proporcionalmente mais rápidos, e a partir de certo ponto ficam mais lentos. É também de Brooks a conclusão desconfortável: **acrescentar gente a um projeto atrasado atrasa mais o projeto**.

**Prazo decidido antes do trabalho.** A data veio de uma reunião, não de uma estimativa. Como a data não muda, o que cede é a qualidade — sempre, e sempre invisível no começo.

**Qualidade adiada.** Testar no fim, revisar no fim, integrar no fim. Tudo que é adiado chega junto, na pior semana possível.

> ⚠️ **Nenhuma dessas causas é "os programadores não sabiam programar".** A competência técnica individual é a parte do problema que a indústria mais resolveu e menos usa como explicação. O que falha é o que acontece **entre** as pessoas.

## 4. O custo da mudança ao longo do tempo

Consertar um erro custa mais quanto mais tarde ele for descoberto. Não é intuição — é aritmética de retrabalho: cada artefato produzido em cima do erro precisa ser refeito.

| Onde o erro foi descoberto | O que precisa ser refeito | Custo relativo |
|---|---|---|
| Requisitos | uma frase no documento | 1× |
| Projeto | o diagrama e o documento | ~5× |
| Codificação | o código, o diagrama e o documento | ~10× |
| Testes | tudo acima, mais os testes já escritos | ~20× |
| Produção | tudo acima, mais dado errado no ar, correção emergencial e a confiança do cliente | **50× ou mais** |

Um exemplo concreto: descobrir na conversa com a secretaria que *"reserva" e "uso confirmado" são coisas diferentes* custa uma pergunta. Descobrir isso depois de o sistema estar no ar custa migrar dados, reescrever relatórios, reeducar usuários e explicar por que os números de ocupação do último período estavam errados.

> 💡 **A curva é a razão de ser deste curso inteiro.** Todo esforço gasto lá na esquerda — perguntar, modelar, revisar, escrever a decisão — é comprado com desconto. Não é burocracia; é o mesmo trabalho, pago mais barato.

> ⚠️ Cuidado com a leitura oposta: a curva **não** diz "planeje tudo antes". Ela diz "descubra cedo". Descobrir cedo às vezes exige construir um pedaço e mostrar — que é justamente o argumento das Aulas 02 e 03.

## 5. Atributos de qualidade

Perguntar "o software está bom?" não leva a lugar nenhum enquanto ninguém disser **bom em quê**. Qualidade não é uma coisa: são várias, e elas competem entre si.

| Atributo | A pergunta que ele responde |
|---|---|
| **Correção** | faz o que foi especificado? |
| **Confiabilidade** | continua funcionando ao longo do tempo, sob uso real? |
| **Desempenho** | responde rápido o suficiente, com a carga esperada? |
| **Usabilidade** | a pessoa certa consegue usar sem treinamento heroico? |
| **Segurança** | resiste a quem quer usá-lo de má-fé? |
| **Manutenibilidade** | outra pessoa consegue mudar isso daqui a dois anos? |
| **Portabilidade** | roda em outro ambiente sem ser reescrito? |
| **Acessibilidade** | serve a quem usa leitor de tela, teclado, alto contraste? |

O que torna isso engenharia, e não uma lista de boas intenções, é que **os atributos se contradizem**:

- Mais segurança quase sempre custa usabilidade (toda verificação a mais é um passo a mais);
- Mais desempenho frequentemente custa manutenibilidade (código otimizado é código mais difícil de ler);
- Mais portabilidade custa desempenho (a camada que abstrai o ambiente cobra pedágio).

> 💡 Por isso a pergunta profissional nunca é *"como faço isso ficar bom?"*, e sim **"quais atributos importam mais neste sistema, e o que estou disposto a perder nos outros?"**. No sistema-guia, um aluno procurando sala no corredor pesa **desempenho e usabilidade**; a interdição de manutenção pesa **correção**. Não são o mesmo sistema para as mesmas pessoas.

## 6. Quem faz software

Um sistema em produção envolve gente com responsabilidades distintas. Vale conhecer todas — inclusive porque, num time pequeno, a mesma pessoa acumula várias:

- **Analista de requisitos / analista de negócio** — descobre e escreve o que o sistema precisa fazer. Conversa com quem entende do problema e traduz para quem entende de solução;
- **Arquiteto** — decide a estrutura: quais partes existem, como conversam, onde os dados ficam. Responde pelas decisões caras de reverter;
- **Projetista / desenvolvedor** — decide como cada parte é organizada por dentro e a constrói;
- **Analista de testes / QA** — projeta como se prova que aquilo funciona, e onde vai quebrar;
- **Gerente de projeto ou Product Owner** — responde por prazo, escopo e prioridade; decide o que **não** será feito agora;
- **Pessoal de operação / DevOps** — coloca no ar, monitora, responde quando cai às três da manhã;
- **Usuário e demais interessados** — para quem tudo isso existe, e sem quem nada disso se valida.

> 🧩 **Ponte com POO:** o papel de **projetista** é o que mais encosta no que você está vendo em Programação Orientada a Objetos. Decidir quais classes existem e o que cada uma sabe fazer é projeto de software — e as Aulas 11 e 13 voltam exatamente a isso.

> ⚠️ Erro de programação aparece em minutos: não compila, quebra o teste, some no *log*. **Erro de requisito ou de projeto aparece meses depois**, quando o sistema não consegue responder a uma pergunta simples porque foi construído de um jeito que nunca permitiria. Não existe correção emergencial para isso.

## 7. Responsabilidade profissional

Software decide coisas sobre pessoas: quem consegue a sala, quem entra na fila, quem recebe o benefício, quem é sinalizado como suspeito. Isso põe quem constrói numa posição de responsabilidade que não termina no código.

Três compromissos que valem desde o primeiro projeto:

- **Dado dos outros não é seu.** Coletar só o necessário, guardar pelo tempo necessário, mostrar a quem tem motivo para ver. No Brasil isso tem nome e força de lei: **LGPD**;
- **Excluir alguém é uma decisão, mesmo quando não intencional.** Um sistema que só funciona bem com internet rápida, tela grande e visão perfeita escolheu seus usuários sem dizer;
- **Competência inclui dizer o que você não sabe.** Estimar um prazo que você sabe impossível, ou garantir uma segurança que você não verificou, é falha profissional — não otimismo.

> 💡 ACM e IEEE mantêm um código de ética de engenharia de software desde 1999, e o princípio que abre o documento é simples: agir de forma consistente com o **interesse público**. Vale a leitura de dez minutos em algum momento do curso.

## 🏋️ Exercícios da aula

Na pasta `aula-01/` do seu repositório:

1. **`ex01.md`** — pegue o programa da seção 1 e transforme-o em produto **no papel**: liste tudo que precisaria ser acrescentado para a secretaria usar de verdade. Organize em quatro grupos (tratamento de erro · documentação · testes · instalação e operação) e estime, para cada grupo, **quantas vezes o esforço original** ele representa. Feche com o seu total e compare com o 9× de Brooks — se você chegou a um número muito menor, explique o que decidiu não fazer;
2. **`ex02.md`** — escolha **três** fracassos de software reais e documentados (Ariane 5, Therac-25, Knight Capital, healthcare.gov, o rastreamento de contatos do Reino Unido em 2020, entre outros). Para cada um, escreva em até 6 linhas: o que aconteceu, e **qual das causas da seção 3** melhor explica o caso. Se você achar que a causa não está na lista, proponha uma nova e defenda;
3. **`ex03.md`** — a tabela de custo da seção 4 diz que o erro descoberto em produção custa 50× o erro descoberto em requisitos. Escreva **a história** desse 50× para um caso do sistema-guia: escolha um mal-entendido plausível entre a secretaria e quem constrói o sistema, e narre o que exatamente precisaria ser refeito em cada fase. Termine com a pergunta que teria evitado tudo;
4. **`ex04.md`** — leia os [interessados do sistema-guia](../../recursos/sistema-guia.md#3-quem-são-os-interessados) e monte uma tabela com os **sete papéis** da seção 6. Para cada papel, escreva quem seria essa pessoa neste projeto e **uma decisão que só ela pode tomar**. Onde um papel não existir na instituição, diga quem acabaria assumindo e o risco disso;
5. **Desafio 🌶️ `ex05.md`** — alguém com autoridade sobre o orçamento diz: *"não precisa de projeto nem de documento, isso aí um estagiário faz num fim de semana."* Escreva a resposta que você daria — **em no máximo 20 linhas**, sem jargão, começando por **reconhecer onde essa pessoa tem razão**. Depois, em 5 linhas, proponha um teste concreto e barato que resolveria a discussão com evidência em vez de opinião. Um bom engenheiro convence com custo, não com susto.

## 🧠 Revisão

[8 questões de múltipla escolha](revisao/README.md) para conferir se os conceitos ficaram sólidos. Responda sem consultar a aula — depois volte e corrija.

## ✅ Entrega

```bash
git add aula-01/
git commit -m "Resolve exercícios da aula 01 (por que engenharia de software existe)"
git push
```

---

🏠 [Voltar ao plano de aulas](../../README.md) | ➡️ [Aula 02 — Ciclo de vida e modelos de processo](../aula-02-ciclo-de-vida-e-processos/README.md)
