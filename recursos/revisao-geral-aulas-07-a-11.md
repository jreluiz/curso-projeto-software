# Revisão geral — Aulas 07 a 11

### R-01

No aplicativo de uma escola de idiomas, é preciso decidir o que entra primeiro: a rematrícula on-line ou o boletim digital. Segundo a Aula 07 (Quem responde pelo quê), quem toma essa decisão é:

- **a)** o time de desenvolvimento, porque é ele quem vai construir as duas;
- **b)** o gerente de projeto, porque ele responde pelo prazo e pelo custo;
- **c)** o Product Owner, porque ele decide o que se faz e em que ordem;
- **d)** o aluno que reclamar mais alto, porque é ele quem usa o aplicativo.

↩︎ *Aula 07, seção 3 — O Product Owner: o que ele decide*

---

### R-02

No sistema de reservas do restaurante universitário, os alunos usam o sistema todos os dias e querem muito que ele funcione, mas não têm voz em nenhuma decisão do projeto. Na matriz poder × interesse da Aula 07 (Quem responde pelo quê), a estratégia para os alunos é:

- **a)** manter informado, porque têm interesse alto e poder baixo;
- **b)** gerenciar de perto, porque têm interesse alto e poder alto;
- **c)** manter satisfeito, porque têm interesse baixo e poder alto;
- **d)** monitorar, porque têm interesse baixo e poder baixo.

↩︎ *Aula 07, seção 6 — A matriz poder × interesse*

---

### R-03

Dois alunos querem criar um aplicativo de caronas entre colegas do campus. O problema está claro — muita gente vem sozinha de carro —, mas eles não sabem se os colegas topariam dividir a viagem. Segundo a Aula 08 (Descobrir, enxugar, melhorar), a abordagem que responde à dúvida deles é:

- **a)** o Six Sigma, que serve para reduzir a variação de um processo repetido;
- **b)** o MVP, que serve para descobrir se alguém quer a solução;
- **c)** o Lean, que serve para tirar o desperdício de um fluxo que já existe;
- **d)** o Design Thinking, que serve para descobrir qual é o problema certo.

↩︎ *Aula 08, seções 1 e 7 — Três respostas para três perguntas diferentes; Qual usar quando*

---

### R-04

A pedido da diretoria, o time de um sistema de vendas passou um mês construindo um relatório de vendas por região. Seis meses depois, ninguém o abriu nenhuma vez. Entre os sete desperdícios do Lean em software, vistos na Aula 08 (Descobrir, enxugar, melhorar), esse caso é o da:

- **a)** espera, em que um item pronto fica dias parado, aguardando revisão;
- **b)** troca de contexto, em que a mesma pessoa se divide entre três projetos;
- **c)** passagem de bastão, em que quem analisou não é quem constrói;
- **d)** funcionalidade não usada, em que se constrói algo que ninguém usa.

↩︎ *Aula 08, seção 5 — Lean: valor, fluxo e desperdício*

---

### R-05

O time de um sistema de controle de estágios está criando o repositório do projeto. Segundo a Aula 09 (Controle de versão e configuração), qual destes arquivos deve ficar **fora** do repositório?

- **a)** o script que acrescenta uma coluna na tabela de estagiários;
- **b)** o arquivo `.env` com o token de acesso ao serviço de assinatura digital;
- **c)** o `Dockerfile` que descreve o ambiente em que o sistema roda;
- **d)** o arquivo que define o pipeline de verificação do projeto.

↩︎ *Aula 09, seção 2 — Item de configuração: o que entra e o que nunca entra*

---

### R-06

Um time de quatro pessoas mantém o sistema web de uma pizzaria, que roda num servidor do próprio time: existe uma única versão em produção. Segundo a Aula 09 (Controle de versão e configuração), a estratégia de ramificação mais adequada é:

- **a)** o GitFlow, que serve para produtos com várias versões em uso ao mesmo tempo;
- **b)** nenhuma, porque, com uma versão só, o time pode trabalhar sem controle de versão;
- **c)** o GitHub Flow, com ramos curtos e o `main` sempre pronto para ir ao ar;
- **d)** um ramo por funcionalidade, que só volta ao `main` depois de semanas, quando tudo estiver pronto.

↩︎ *Aula 09, seção 4 — Estratégias de ramificação*

---

### R-07

Uma biblioteca de cálculo de frete está na versão 1.4.2 e ganha uma funcionalidade nova, opcional, que não muda nada do que já existia. Seguindo o versionamento semântico da Aula 09 (Controle de versão e configuração), a próxima versão é:

- **a)** 1.5.0, porque funcionalidade nova sem quebra sobe a parte do meio e zera a da direita;
- **b)** 1.4.3, porque toda mudança sobe só a última parte do número;
- **c)** 2.0.0, porque toda funcionalidade nova sobe a primeira parte do número;
- **d)** 1.4.2.1, porque mudanças pequenas ganham uma quarta parte no número.

↩︎ *Aula 09, seção 5 — Versionamento semântico*

---

### R-08

A equipe do sistema de uma biblioteca quer adotar a integração contínua. Segundo a Aula 10 (Integração contínua), isso quer dizer:

- **a)** ter uma ferramenta que roda os testes, mesmo que cada ramo só volte ao principal depois de semanas;
- **b)** integrar cada ramo ao principal no fim da Sprint, depois de testado à mão;
- **c)** rodar todos os testes uma vez por noite e mandar o relatório ao time pela manhã;
- **d)** levar o trabalho de cada pessoa para o `main` todos os dias e deixar uma máquina verificar cada uma dessas integrações.

↩︎ *Aula 10, seção 1 — Integrar todo dia, verificar toda vez*

---

### R-09

No sistema de uma loja virtual, uma integração deixou o pipeline do `main` vermelho: um teste passou a falhar. Segundo a Aula 10 (Integração contínua), o que o time deve fazer?

- **a)** continuar integrando normalmente e deixar a correção para a próxima Sprint;
- **b)** consertar em poucos minutos ou reverter a mudança; até lá, ninguém integra mais nada;
- **c)** apagar o teste que está falhando, e assim o pipeline fica verde de novo;
- **d)** desligar o pipeline até o fim da semana, para não atrasar ninguém.

↩︎ *Aula 10, seção 1 — Integrar todo dia, verificar toda vez*

---

### R-10

O time do sistema de uma transportadora vai montar os testes automáticos seguindo a pirâmide de testes da Aula 10 (Integração contínua). O tipo de teste que deve existir em maior número é:

- **a)** o de unidade, porque é rápido e, quando falha, aponta a regra exata que quebrou;
- **b)** o ponta a ponta, porque percorre o sistema inteiro, do jeito que o cliente usa;
- **c)** o manual, porque uma pessoa percebe defeitos que a máquina não percebe;
- **d)** o de carga, porque simula o sistema no dia de maior movimento.

↩︎ *Aula 10, seção 4 — A pirâmide de testes*

---

### R-11

No sistema de uma loja virtual, toda mudança que passa no pipeline vai para a produção sozinha, sem ninguém apertar botão nenhum. Segundo a Aula 11 (Entrega e implantação contínuas), essa prática se chama:

- **a)** integração contínua, em que o trabalho de todos é juntado e verificado no principal todo dia;
- **b)** entrega contínua, em que o sistema fica sempre pronto e o negócio decide quando ele vai ao ar;
- **c)** implantação contínua, em que cada mudança aprovada no pipeline vai ao ar automaticamente;
- **d)** versionamento semântico, em que cada parte do número da versão tem um significado.

↩︎ *Aula 11, seção 1 — Pronto não é no ar*

---

### R-12

No sistema de inscrições de um vestibular, a comissão testou e aprovou na homologação o pacote identificado como `sha256:7b1e…`. Segundo a Aula 11 (Entrega e implantação contínuas), para pôr o sistema em produção, o time deve:

- **a)** construir o pacote de novo a partir do mesmo commit, já que o código é o mesmo;
- **b)** construir o pacote na máquina do desenvolvedor mais experiente do time;
- **c)** copiar os dados reais da produção para a homologação e repetir os testes;
- **d)** levar à produção o mesmo pacote `sha256:7b1e…`, mudando só a configuração.

↩︎ *Aula 11, seção 2 — Os ambientes: o mesmo artefato, outra configuração*

---

### R-13

No aplicativo de um banco digital, a versão nova vai primeiro para 2% dos clientes. O time compara os erros dela com os da versão antiga e só então amplia para 10%, 50% e, por fim, todos. Segundo a Aula 11 (Entrega e implantação contínuas), essa forma de pôr a versão no ar se chama:

- **a)** implantação direta, em que a versão nova substitui a antiga para todos de uma vez;
- **b)** implantação azul-verde, em que todo o tráfego passa de um ambiente para outro de uma vez;
- **c)** implantação canário, em que a versão nova vai primeiro para uma pequena parte dos clientes e é observada;
- **d)** GitFlow, em que o trabalho se junta num ramo `develop` antes de chegar ao `main`.

↩︎ *Aula 11, seção 4 — Quatro maneiras de pôr no ar*

---

### R-14

No aplicativo de uma pizzaria, o código do pagamento por Pix foi para a produção na terça, desligado por uma feature flag. Na sexta, a flag foi ligada para os clientes, sem nenhuma implantação nova. Segundo a Aula 11 (Entrega e implantação contínuas), a feature flag serviu para:

- **a)** separar implantar de liberar: o código foi ao ar desligado e só foi ligado quando se decidiu;
- **b)** substituir os testes automáticos do Pix, que ainda não estavam prontos;
- **c)** impedir que o código do Pix entrasse no ramo principal antes de terminado;
- **d)** acelerar o pipeline, pulando a verificação do código do Pix.

↩︎ *Aula 11, seção 5 — Feature flag: no ar não é ligado*

---

⬅️ [Voltar ao plano de aulas](../README.md)
