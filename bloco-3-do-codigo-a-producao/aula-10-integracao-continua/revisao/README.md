# Aula 10 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 10 — Integração contínua](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

As três últimas são marcadas **[ENADE]**: trazem um **texto-base** com uma situação de projeto, seguido do comando. São mais longas de ler e cobram interpretação, não memória — as alternativas continuam simples, como nas demais.

---

### Q-A10-01

Segundo a aula, o que caracteriza a integração contínua?

- **a)** o uso de uma ferramenta que executa os testes automaticamente sempre que alguém envia código;
- **b)** a integração de cada ramo de funcionalidade ao principal no fim da Sprint, depois de testado;
- **c)** integrar o trabalho de todos no ramo principal pelo menos uma vez por dia, verificando cada integração automaticamente;
- **d)** a execução de todos os testes do sistema durante a noite, com um relatório para o time pela manhã.

↩︎ *Aula 10, seção 1 — Integrar todo dia, verificar toda vez*

---

### Q-A10-02

Uma integração deixou o pipeline do `main` vermelho. Segundo a aula, o que o time deve fazer?

- **a)** consertar em minutos ou reverter a mudança, antes de integrar qualquer outra coisa;
- **b)** continuar integrando normalmente e incluir a correção no planejamento da próxima Sprint;
- **c)** desativar o teste que falhou, para que o pipeline volte a ficar verde;
- **d)** esperar a próxima execução do pipeline, já que a falha pode ter sido passageira.

↩︎ *Aula 10, seção 1 — Integrar todo dia, verificar toda vez*

---

### Q-A10-03

Um pipeline tem uma verificação de estilo do código, que leva 15 segundos, e uma bateria de testes de integração, que leva 4 minutos. Pelo princípio de falhar cedo, a verificação de estilo deve:

- **a)** rodar depois dos testes de integração, que verificam coisas mais importantes;
- **b)** rodar só uma vez por dia, para não atrasar as integrações;
- **c)** sair do pipeline, porque um problema de estilo não é defeito;
- **d)** rodar antes dos testes de integração, porque é mais barata e, quando falha, avisa em segundos.

↩︎ *Aula 10, seção 3 — O pipeline: a esteira de verificações*

---

### Q-A10-04

Por que a pirâmide de testes recomenda muito mais testes de unidade do que testes ponta a ponta?

- **a)** porque os testes de unidade verificam o sistema inteiro, do jeito que o usuário o usa;
- **b)** porque os testes de unidade são rápidos e apontam onde está o defeito, e os ponta a ponta são lentos e frágeis;
- **c)** porque os testes de unidade tornam desnecessários os testes de integração;
- **d)** porque os testes ponta a ponta não encontram nenhum defeito que os de unidade não encontrem.

↩︎ *Aula 10, seção 4 — A pirâmide de testes*

---

### Q-A10-05

Um teste passa e falha com o mesmo código, sem que nada tenha mudado entre uma execução e outra. Segundo a aula, a conduta adequada é:

- **a)** executá-lo de novo sempre que falhar, até que passe;
- **b)** tirá-lo do conjunto que barra a integração, com um responsável e um prazo para corrigi-lo ou apagá-lo;
- **c)** mantê-lo barrando a integração até que alguém descubra a causa, ainda que leve semanas;
- **d)** trocá-lo por um teste ponta a ponta, que verifica o sistema de forma mais completa.

↩︎ *Aula 10, seção 4 — A pirâmide de testes*

---

### Q-A10-06

**[ENADE]**

Uma loja virtual tem um pipeline que, a cada integração, instala as bibliotecas de que o sistema precisa, sempre na versão mais recente disponível. Numa segunda-feira, sem que ninguém tivesse alterado o código, o build passou a falhar.

O time descobriu que uma biblioteca de formatação de datas, usada indiretamente por outra biblioteca do projeto, havia publicado no domingo uma versão nova, com uma mudança incompatível. Na máquina de um dos desenvolvedores, que tinha instalado as bibliotecas meses antes, o sistema continuava funcionando.

Considerando a situação descrita e o conteúdo da aula, a medida mais adequada é:

- **a)** proibir o uso de bibliotecas de terceiros no projeto, para que o build não dependa de ninguém de fora;
- **b)** passar a construir o sistema na máquina do desenvolvedor em que ele ainda funciona, e publicar a partir dela;
- **c)** desligar o build automático até que a biblioteca de datas publique uma correção;
- **d)** fixar a versão exata de cada biblioteca, inclusive das indiretas, num arquivo versionado junto com o código.

↩︎ *Aula 10, seção 2 — O build: o mesmo resultado em qualquer máquina*

---

### Q-A10-07

**[ENADE]**

Milhares de repositórios usavam em seus pipelines um componente gratuito, publicado por terceiros e referenciado pelo nome de uma versão, como `componente@v45`. Um invasor obteve a credencial da conta que mantinha o componente, alterou o código e fez os nomes de versão já existentes passarem a apontar para a versão alterada.

Na execução seguinte, sem que ninguém mexesse nos repositórios afetados, os pipelines passaram a rodar o código do invasor, que escreveu nos registros de execução as senhas e chaves de acesso disponíveis no pipeline. Em repositórios públicos, esses registros podiam ser lidos por qualquer pessoa.

Considerando a situação descrita e o conteúdo da aula, a lição mais adequada para quem usa componentes de terceiros no pipeline é:

- **a)** referenciar cada componente pelo hash do commit, que não pode ser movido, e dar ao pipeline só as permissões de que ele precisa;
- **b)** abandonar o pipeline e voltar a conferir cada integração manualmente, sem componentes de terceiros;
- **c)** apagar os registros de execução que expuseram as senhas, o que encerra o vazamento;
- **d)** referenciar sempre a versão mais recente de cada componente, para receber as correções mais cedo.

↩︎ *Aula 10, seção 5 — A verificação que barra a mudança*

---

### Q-A10-08

**[ENADE]**

A coordenação de um projeto determinou que nenhuma mudança seria integrada enquanto a cobertura de testes do sistema estivesse abaixo de 90%. Em três semanas, a cobertura subiu de 58% para 92%. No mesmo período, o número de defeitos encontrados na homologação não se alterou.

Ao revisar os testes novos, o time encontrou muitos que executavam o código sem conferir o resultado, e outros que testavam apenas trechos triviais, como métodos que só devolvem um valor guardado.

Considerando a situação descrita e o conteúdo da aula, a interpretação mais adequada é:

- **a)** a meta foi baixa demais, e deveria subir para 100%, o que obrigaria a testar também o código difícil;
- **b)** a cobertura alta mostra que os testes estão bons, e os defeitos da homologação têm outra origem;
- **c)** a cobertura virou meta e deixou de medir: subiu sem que os testes passassem a conferir mais;
- **d)** o time agiu de má-fé ao escrever testes fáceis, e precisa ser substituído por outro mais comprometido.

↩︎ *Aula 10, seção 6 — A métrica que vira meta*

---

⬅️ [Voltar à Aula 10](../README.md) | 🏠 [Início](../../../README.md)
