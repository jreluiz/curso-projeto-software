# Aula 13 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 13 — Versão, mudança e configuração](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

As três últimas são marcadas **[ENADE]**: trazem um **texto-base** com uma situação de projeto, seguido do comando. São mais longas de ler e cobram interpretação, não memória — as alternativas continuam simples, como nas demais.

---

### Q-A13-01

Segundo a aula, a pergunta que revela se há controle de versão de verdade num projeto é:

- **a)** todos os arquivos estão no mesmo repositório?
- **b)** se essa mudança quebrar, quanto tempo até voltar ao que funcionava?
- **c)** a equipe usa a mesma ferramenta de versionamento?
- **d)** há uma cópia de segurança diária do código?

↩︎ *Aula 13, seção 1 — Controle de versão como prática de engenharia*

---

### Q-A13-02

Um integrante afirma que vai "terminar tudo direitinho antes de integrar", mantendo o ramo aberto por três semanas. Sobre essa escolha, a aula sustenta que:

- **a)** é adequada quando a funcionalidade é grande e não pode ser entregue pela metade;
- **b)** reduz o número de integrações e, com isso, o risco total do projeto;
- **c)** adiar não evita o custo da integração: multiplica, porque o conflito cresce com o tempo;
- **d)** é indiferente, desde que a verificação automática rode ao final.

↩︎ *Aula 13, seção 2 — Estratégia de integração: o custo do branch longo*

---

### Q-A13-03

A pergunta que identifica um **item de configuração** é:

- **a)** este arquivo é produzido pela equipe de desenvolvimento?
- **b)** este item está armazenado no repositório do projeto?
- **c)** este item foi citado no termo de abertura do projeto?
- **d)** se isto mudar sozinho, alguma coisa quebra ou alguém se engana?

↩︎ *Aula 13, seção 3 — Gerência de configuração: o que é item de configuração*

---

### Q-A13-04

Sobre o caminho de mudança **emergencial**, a aula estabelece que ele precisa ter escrito:

- **a)** o que autoriza pular e o que obriga a fazer depois, com prazo;
- **b)** a lista de pessoas autorizadas a acioná-lo;
- **c)** o limite de vezes que pode ser usado por mês;
- **d)** a aprovação prévia do patrocinador do projeto.

↩︎ *Aula 13, seção 4 — Baseline e rastreamento de mudança*

---

### Q-A13-05

Um time tem esteira de verificação automática configurada e mantém ramos abertos por três semanas. Segundo a aula, esse time:

- **a)** tem uma ferramenta rodando sobre um processo que ela não muda;
- **b)** pratica integração contínua, uma vez que a verificação roda automaticamente;
- **c)** pratica entrega contínua, mas não integração contínua;
- **d)** precisa apenas aumentar a frequência de execução da esteira.

↩︎ *Aula 13, seção 5 — Integração contínua*

---

### Q-A13-06

**[ENADE]**

O dono de um restaurante recusa a proposta da equipe de desenvolvimento, afirmando que não quer que ninguém mexa no sistema durante o sábado à noite, quando o volume de pedidos é máximo e qualquer interrupção custa vendas.

A equipe havia proposto que o sistema estivesse permanentemente apto a receber uma nova versão, com todo o processo de verificação e empacotamento automatizado, ficando a publicação sujeita a autorização.

Considerando a situação descrita e o conteúdo da aula, a recusa do dono:

- **a)** inviabiliza a proposta, que depende de publicação automática para funcionar;
- **b)** recai sobre a implantação contínua, e não sobre a entrega contínua que foi proposta;
- **c)** é tecnicamente infundada, já que a automação reduz o risco de erro humano;
- **d)** obriga a equipe a abandonar também a integração contínua do trabalho diário.

↩︎ *Aula 13, seção 6 — CI/CD: o que cada sigla entrega*

---

### Q-A13-07

**[ENADE]**

Um sistema de delivery parou de calcular o frete corretamente após uma publicação. A equipe verificou que o código não havia sido alterado naquele dia. Depois de quatro horas de investigação, descobriu-se que uma biblioteca de cálculo geográfico havia sido atualizada automaticamente para uma versão nova, com comportamento diferente.

Nenhum registro indicava qual versão estava em uso antes, e a equipe precisou testar três versões até encontrar a que reproduzia o comportamento anterior.

Considerando a situação descrita e o conteúdo da aula, o que falhou foi:

- **a)** a verificação automática, que deveria ter detectado a mudança de comportamento;
- **b)** o processo de aprovação de mudanças, que não avaliou o impacto da atualização;
- **c)** o controle da versão das bibliotecas como item de configuração do projeto;
- **d)** a comunicação com o fornecedor da biblioteca sobre a mudança de comportamento.

↩︎ *Aula 13, seção 3 — Gerência de configuração: o que é item de configuração*

---

### Q-A13-08

**[ENADE]**

Numa organização, aprovar qualquer alteração em produção exige preenchimento de formulário, análise por comitê e prazo médio de três dias — inclusive para correções de texto em telas.

Após seis meses, uma auditoria interna constatou que a maioria das alterações pequenas era feita diretamente, sem passar pelo processo, e comunicada informalmente depois. O comitê continuava se reunindo e aprovando apenas as mudanças grandes.

Considerando a situação descrita e o conteúdo da aula, o que o caso demonstra é que:

- **a)** a equipe descumpriu deliberadamente o processo estabelecido pela organização;
- **b)** o comitê deveria ter aumentado a frequência das reuniões para reduzir o prazo;
- **c)** processos de mudança devem ser eliminados em favor da confiança na equipe;
- **d)** processo desproporcional ao risco é contornado, e o resultado é não haver processo nem registro.

↩︎ *Aula 13, seção 4 — Baseline e rastreamento de mudança*

---

⬅️ [Voltar à Aula 13](../README.md) | 🏠 [Início](../../../README.md)
