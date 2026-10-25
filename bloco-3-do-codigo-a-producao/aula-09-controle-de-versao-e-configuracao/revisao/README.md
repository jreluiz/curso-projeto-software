# Aula 09 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 09 — Controle de versão e configuração](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

📝 **As respostas vão pelo formulário:** [responder a revisão da Aula 09](https://docs.google.com/forms/d/e/1FAIpQLScutlhyfPrDPpml8WzM1M_pX1R6FpqBbcaPc8jJYnYeLQ9GgQ/viewform)

Leia as 8 questões aqui e decida suas respostas antes de abrir o formulário: é **uma resposta por aluno**, com conta Google, e não dá para editar depois de enviar. Ele também pede seu usuário do GitHub. Se o seu nome não estiver na lista da turma, marque a última opção e escreva o nome completo no campo seguinte.

As três últimas são marcadas **[ENADE]**: trazem um **texto-base** com uma situação de projeto, seguido do comando. São mais longas de ler e cobram interpretação, não memória — as alternativas continuam simples, como nas demais.

---

### Q-A09-01

O time do delivery está criando o repositório do projeto. Qual destes arquivos deve ficar **fora** dele?

- **a)** o script que acrescenta a coluna `cupom` na tabela de pedidos;
- **b)** o arquivo `.env` com a senha do banco de dados de produção;
- **c)** o arquivo que define o raio máximo de entrega em cada ambiente;
- **d)** o `Dockerfile` que descreve o ambiente em que a aplicação roda.

↩︎ *Aula 09, seção 2 — Item de configuração: o que entra e o que nunca entra*

---

### Q-A09-02

Segundo a aula, o que o controle de versão responde e uma cópia de segurança (*backup*) não responde?

- **a)** se existe uma cópia recuperável do projeto caso o computador se perca;
- **b)** qual é o tamanho total do projeto e quanto espaço ele ocupa;
- **c)** quantos arquivos o projeto tinha na data da última cópia;
- **d)** o que mudou entre duas versões, quem mudou, quando e por quê.

↩︎ *Aula 09, seção 1 — Três perguntas que só o histórico responde*

---

### Q-A09-03

Um sistema está na versão **3.7.2** e ganha uma funcionalidade nova, opcional, que não altera nada do que já existia. Pelo versionamento semântico, a próxima versão é:

- **a)** 3.8.0;
- **b)** 3.7.3;
- **c)** 4.0.0;
- **d)** 3.8.2.

↩︎ *Aula 09, seção 5 — Versionamento semântico*

---

### Q-A09-04

Segundo a pesquisa do DORA citada na aula, que prática de ramificação está associada a melhor desempenho de entrega?

- **a)** manter um ramo de desenvolvimento separado do principal, integrado ao fim de cada ciclo;
- **b)** criar um ramo por funcionalidade e integrá-lo só quando a funcionalidade estiver completa;
- **c)** manter três ou menos ramos ativos e integrar no tronco pelo menos uma vez por dia;
- **d)** congelar o código antes de cada versão, para estabilizar a integração.

↩︎ *Aula 09, seção 4 — Estratégias de ramificação*

---

### Q-A09-05

A diferença entre o CHANGELOG e o log de commits, segundo a aula, é que:

- **a)** o CHANGELOG é escrito para quem usa e opera o sistema, agrupando por versão as mudanças relevantes; o log registra cada alteração, para quem desenvolve;
- **b)** o CHANGELOG é uma cópia do log de commits, organizada por data, para facilitar a busca;
- **c)** o log de commits é o registro oficial para a auditoria, e o CHANGELOG é opcional e informal;
- **d)** o CHANGELOG lista só as correções de defeitos, e o log lista as funcionalidades novas.

↩︎ *Aula 09, seção 6 — Release e CHANGELOG*

---

### Q-A09-06

**[ENADE]**

Uma empresa que protege sites contra acessos automatizados gera, a cada cinco minutos, um arquivo de configuração com as características que seu sistema usa para reconhecer robôs, e o distribui imediatamente a todos os seus servidores. O programa que lê esse arquivo aceita no máximo 200 características; o arquivo costuma ter cerca de 60.

Certo dia, uma alteração de permissões num banco de dados fez a consulta que monta o arquivo devolver linhas duplicadas. O arquivo dobrou de tamanho, ultrapassou o limite, e os servidores passaram a falhar — alternando entre funcionar e falhar a cada nova geração do arquivo. Nenhuma linha de código havia sido alterada.

Considerando a situação descrita e o conteúdo da aula, a lição de gerência de configuração mais adequada ao caso é:

- **a)** proibir alterações de permissões no banco de dados, que foram a origem do problema;
- **b)** aumentar o limite do programa para muito acima do tamanho esperado do arquivo;
- **c)** tratar o arquivo gerado como item de configuração, validado antes de distribuído e liberado com a mesma cautela de uma mudança de código;
- **d)** gerar o arquivo com menos frequência, para reduzir a chance de uma geração defeituosa.

↩︎ *Aula 09, seção 2 — Item de configuração: o que entra e o que nunca entra*

---

### Q-A09-07

**[ENADE]**

Uma corretora instalou manualmente uma nova versão do seu sistema de negociação em oito servidores. Por um descuido, o técnico atualizou apenas sete. A versão nova reaproveitava um sinalizador que, anos antes, ativava uma função desativada, mas nunca removida do código.

Quando o sinalizador foi ligado, os sete servidores atualizados se comportaram como esperado, e o oitavo ressuscitou a função antiga, que passou a enviar ordens sem parar. O prejuízo, em menos de uma hora, ameaçou a sobrevivência da empresa.

Considerando a situação descrita e o conteúdo da aula, o que faltou, do ponto de vista da gerência de configuração, foi:

- **a)** um ramo de correção emergencial preparado com antecedência para a função antiga;
- **b)** um número de versão maior na release, indicando que a mudança quebrava compatibilidade;
- **c)** um CHANGELOG detalhado, descrevendo o novo uso do sinalizador;
- **d)** saber e conferir qual baseline estava em cada servidor antes de ligar a mudança.

↩︎ *Aula 09, seção 3 — Baseline: o retrato aprovado do sistema*

---

### Q-A09-08

**[ENADE]**

Um time de três pessoas mantém o sistema web de pedidos de um restaurante, que tem uma única versão em produção. O time adotou um ramo `develop`, onde as funcionalidades são integradas, e só leva o `develop` ao `main` a cada três semanas, depois de uma rodada de testes manuais.

Cada integração ao `main` tem custado dois dias de conflitos e correções. Defeitos simples, como um erro no cálculo do frete, esperam até três semanas para chegar aos clientes, a menos que se abra um ramo de emergência.

Considerando a situação descrita e o conteúdo da aula, a mudança de estratégia mais adequada é:

- **a)** acrescentar um ramo de release para estabilizar cada versão antes de ela chegar ao `main`;
- **b)** adotar ramos curtos, integrados ao `main` pelo menos uma vez por dia, como no GitHub Flow ou no desenvolvimento baseado em tronco;
- **c)** aumentar o intervalo entre integrações para seis semanas, reduzindo o número de rodadas de conflito;
- **d)** designar uma pessoa para cuidar exclusivamente dos conflitos de integração.

↩︎ *Aula 09, seção 4 — Estratégias de ramificação*

---

⬅️ [Voltar à Aula 09](../README.md) | 🏠 [Início](../../../README.md)
