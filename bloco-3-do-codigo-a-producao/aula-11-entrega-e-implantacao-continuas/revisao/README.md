# Aula 11 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 11 — Entrega e implantação contínuas](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

📝 **As respostas vão pelo formulário:** [responder a revisão da Aula 11](https://docs.google.com/forms/d/e/1FAIpQLSf2BsxCT1TVd6J4KIhzQFmVF4XzVHMVZ4VpWbL1e-0KF9yDMw/viewform)

Leia as 8 questões aqui e decida suas respostas antes de abrir o formulário: é **uma resposta por aluno**, com conta Google, e não dá para editar depois de enviar. Ele também pede seu usuário do GitHub. Se o seu nome não estiver na lista da turma, marque a última opção e escreva o nome completo no campo seguinte.

As três últimas são marcadas **[ENADE]**: trazem um **texto-base** com uma situação de projeto, seguido do comando. São mais longas de ler e cobram interpretação, não memória — as alternativas continuam simples, como nas demais.

---

### Q-A11-01

Segundo a aula, a diferença entre entrega contínua e implantação contínua é que:

- **a)** a entrega contínua usa um pipeline automático, e a implantação contínua dispensa o pipeline;
- **b)** a entrega contínua serve para sistemas web, e a implantação contínua, para aplicativos instalados;
- **c)** a implantação contínua exige aprovação manual de cada mudança, e a entrega contínua não exige;
- **d)** na entrega contínua, cada mudança aprovada fica pronta para ir ao ar quando o negócio decidir; na implantação contínua, ela vai ao ar automaticamente.

↩︎ *Aula 11, seção 1 — Pronto não é no ar*

---

### Q-A11-02

Por que a aula recomenda promover o mesmo artefato do ambiente de integração até a produção, em vez de construí-lo de novo em cada ambiente?

- **a)** porque construir de novo ocupa mais espaço nos servidores de produção;
- **b)** porque assim o que vai para a produção é exatamente o que foi testado e aprovado;
- **c)** porque cada ambiente precisa de uma versão diferente do código;
- **d)** porque o artefato construído no próprio servidor de produção fica mais lento.

↩︎ *Aula 11, seção 2 — Os ambientes: o mesmo artefato, outra configuração*

---

### Q-A11-03

Na implantação canário:

- **a)** a versão nova vai primeiro para uma pequena parte dos clientes, é observada e só então é ampliada;
- **b)** a versão nova vai para todos os clientes de uma vez, fora do horário de pico;
- **c)** dois ambientes completos ficam no ar, e todo o tráfego é trocado de um para o outro de uma vez;
- **d)** o sistema é desligado, atualizado e religado durante uma janela de manutenção avisada.

↩︎ *Aula 11, seção 4 — Quatro maneiras de pôr no ar*

---

### Q-A11-04

Uma característica da implantação azul-verde (*blue-green*) é:

- **a)** atualizar os servidores um a um, até que todos rodem a versão nova;
- **b)** liberar a funcionalidade nova apenas para os clientes que pedirem por ela;
- **c)** manter dois ambientes de produção idênticos e trocar o tráfego de um para o outro, o que torna a volta igualmente rápida;
- **d)** dispensar o cuidado com o banco de dados, já que cada ambiente tem o seu próprio banco.

↩︎ *Aula 11, seção 4 — Quatro maneiras de pôr no ar*

---

### Q-A11-05

Segundo a aula, para que serve uma *feature flag* de liberação?

- **a)** para substituir os testes automáticos de uma funcionalidade que ainda não terminou;
- **b)** para guardar no código, de forma permanente, versões alternativas de cada funcionalidade;
- **c)** para separar implantar de liberar: o código vai ao ar desligado e é ligado depois, para quem e quando se decidir;
- **d)** para impedir que o código novo seja integrado ao ramo principal antes de terminado.

↩︎ *Aula 11, seção 5 — Feature flag: no ar não é ligado*

---

### Q-A11-06

**[ENADE]**

Uma empresa de segurança envia com frequência arquivos de conteúdo que o seu programa, instalado em milhões de computadores de clientes, usa para reconhecer ameaças novas. Antes de sair, cada arquivo passa por um validador automático.

Certo dia, um arquivo com defeito passou pelo validador, que também tinha um erro, e foi enviado ao mesmo tempo a todos os computadores ligados. Ao lê-lo, o programa travou o sistema operacional, e as máquinas passaram a reiniciar sem parar. A empresa retirou o arquivo 78 minutos depois, mas milhões de computadores já precisavam de conserto manual, um a um.

Considerando a situação descrita e o conteúdo da aula, a medida que mais reduziria o dano de um defeito parecido no futuro é:

- **a)** enviar cada arquivo de conteúdo primeiro a uma pequena parte dos computadores, observar e só então ampliar;
- **b)** corrigir o validador automático, que deixou o defeito passar, mantendo o envio a todos ao mesmo tempo;
- **c)** enviar os arquivos com menos frequência, reunindo várias mudanças numa só atualização;
- **d)** deixar de enviar arquivos de conteúdo e passar a atualizar o programa inteiro a cada mudança.

↩︎ *Aula 11, seção 3 — Todos de uma vez: o raio da explosão*

---

### Q-A11-07

**[ENADE]**

A diretoria de uma cooperativa de crédito afirma que "o negócio não aceita mudança todo dia" e, por isso, o sistema de atendimento só é atualizado a cada três meses. Cada atualização reúne cerca de 200 mudanças, toma um fim de semana inteiro e, nas três últimas vezes, precisou ser parcialmente desfeita.

Quando um defeito simples é descoberto em produção, a correção espera a próxima atualização trimestral, a menos que se abra um processo de emergência.

Considerando a situação descrita e o conteúdo da aula, a mudança mais adequada é:

- **a)** adotar implantação contínua, levando cada mudança à produção automaticamente, assim que aprovada no pipeline;
- **b)** aumentar o intervalo entre as atualizações para seis meses, para que cada uma seja testada com mais calma;
- **c)** congelar as mudanças nas quatro semanas anteriores a cada atualização trimestral;
- **d)** adotar entrega contínua, mantendo o sistema sempre pronto para ir ao ar em mudanças pequenas, e deixar com o negócio a decisão de quando implantar.

↩︎ *Aula 11, seção 1 — Pronto não é no ar*

---

### Q-A11-08

**[ENADE]**

Para acelerar as entregas, a gerência de um time definiu a meta de "implantar pelo menos cinco vezes por dia" e passou a divulgar o número toda semana. Em dois meses, a frequência de implantação saiu de uma vez por semana para oito vezes por dia.

No mesmo período, a proporção de implantações que precisaram ser revertidas ou corrigidas às pressas subiu de 8% para 30%, e o tempo para recuperar o serviço depois de uma implantação com falha passou de uma hora para dois dias.

Considerando a situação descrita e o conteúdo da aula, a interpretação mais adequada é:

- **a)** o time melhorou, porque a frequência de implantação é a principal métrica do DORA;
- **b)** as métricas se leem em conjunto: a vazão subiu às custas da estabilidade, e a meta de frequência induziu esse comportamento;
- **c)** a taxa de falha subiu porque implantar com frequência é, por natureza, mais arriscado do que implantar pouco;
- **d)** o time deve voltar a implantar uma vez por semana, que era quando a taxa de falha estava mais baixa.

↩︎ *Aula 11, seção 6 — Escolher pelo risco, medir pelo DORA*

---

⬅️ [Voltar à Aula 11](../README.md) | 🏠 [Início](../../../README.md)
