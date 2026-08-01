# Aula 05 — Revisão: Múltipla Escolha

> 🎯 8 questões sobre a [Aula 05 — O Que É um Requisito](../README.md). Só uma alternativa está correta em cada uma.

**Sem gabarito, de propósito.** Cada questão termina com a seção da aula onde a resposta está. Responda **tudo primeiro**, sem consultar — só depois volte às seções indicadas e corrija.

---

### Q-A05-01

O que distingue um requisito de um desejo?

- **a)** O requisito está escrito em documento aprovado, e o desejo é verbal;
- **b)** o requisito veio do cliente, e o desejo veio da equipe;
- **c)** o requisito é escrito de modo que duas pessoas diferentes cheguem à mesma conclusão sobre se ele foi cumprido;
- **d)** o requisito tem prioridade definida, e o desejo ainda não foi priorizado.

↩︎ *Aula 05, seção 1 — A frase que precisa aguentar peso*

---

### Q-A05-02

*"As senhas devem ser armazenadas com hash e sal."* Como se classifica esse requisito, e por quê?

- **a)** Não-funcional: é uma restrição sobre como a autenticação guarda o dado, e não uma nova ação com entrada e saída observáveis;
- **b)** funcional, porque trata de segurança, e segurança é uma função do sistema;
- **c)** funcional, porque descreve algo que o sistema faz com a senha;
- **d)** não é requisito: é decisão de implementação e não deveria estar no documento.

↩︎ *Aula 05, seção 2 — Funcional × não-funcional*

---

### Q-A05-03

Qual é o atalho que resolve quase sempre a classificação entre funcional e não-funcional?

- **a)** Se envolve interface com o usuário, é funcional;
- **b)** se aparece no contrato, é funcional; se aparece no anexo técnico, é não-funcional;
- **c)** se tem número ou unidade de medida, é não-funcional;
- **d)** se dá para escrever um caso de uso para aquilo, é funcional — o não-funcional atravessa vários casos de uso e não vira nenhum deles sozinho.

↩︎ *Aula 05, seção 2 — Funcional × não-funcional*

---

### Q-A05-04

Por que os requisitos não-funcionais quase sempre são derivados do contexto, e não coletados na conversa?

- **a)** Porque o cliente não tem vocabulário técnico para descrevê-los;
- **b)** porque o cliente pede funcionalidade e supõe que o resto vem junto — ninguém chega dizendo que quer acessibilidade e conformidade com a LGPD;
- **c)** porque eles só podem ser definidos depois que a arquitetura for escolhida;
- **d)** porque a norma da instituição já os define, dispensando a conversa.

↩︎ *Aula 05, seção 3 — Os não-funcionais que ninguém pede*

---

### Q-A05-05

Ao passar a lista de verificação de não-funcionais, você conclui que "retenção e trilha de auditoria" não se aplica ao seu sistema. O que fazer?

- **a)** Nada: item que não se aplica simplesmente não entra no documento;
- **b)** escrever por que ele não se aplica — "não se aplica" escrito é uma decisão, "não se aplica" esquecido é uma bomba-relógio;
- **c)** incluir o item mesmo assim, com valores genéricos, para não deixar lacuna;
- **d)** perguntar ao cliente, já que apenas ele pode dispensar um item da lista.

↩︎ *Aula 05, seção 3 — Os não-funcionais que ninguém pede*

---

### Q-A05-06

A coordenação nunca vai abrir a plataforma de reservas, e mesmo assim exige o relatório de ocupação. O que esse caso ilustra?

- **a)** Que requisitos de quem não usa o sistema devem ter prioridade menor;
- **b)** que o relatório deveria ser construído fora do sistema, por não ter usuário interno;
- **c)** que a coordenação precisa ser convencida a usar a plataforma;
- **d)** que interessado não é o mesmo que usuário — e um interessado que não usa pode impor requisito que muda o que o sistema registra desde o primeiro dia.

↩︎ *Aula 05, seção 4 — Interessados e o conflito que eles trazem*

---

### Q-A05-07

Você mapeou todos os interessados e nenhum interesse conflita com outro. O que isso indica?

- **a)** Que o levantamento provavelmente não terminou — conflito é sinal de que se falou com gente suficiente;
- **b)** que o projeto tem escopo bem delimitado e baixo risco;
- **c)** que a etapa de priorização pode ser dispensada;
- **d)** que os interessados foram bem selecionados pela equipe.

↩︎ *Aula 05, seção 4 — Interessados e o conflito que eles trazem*

---

### Q-A05-08

*"Deve funcionar no navegador X, porque é o que os computadores dos laboratórios têm."* Isso é requisito ou solução disfarçada?

- **a)** Solução disfarçada: menciona tecnologia, e todo requisito que cita tecnologia é solução;
- **b)** solução disfarçada, porque congela uma decisão que poderia melhorar depois;
- **c)** é requisito legítimo: a restrição vem de fora, do ambiente que a instituição já tem, e não de uma tela que o cliente imaginou;
- **d)** não é nem um nem outro: é uma observação de contexto, sem lugar no documento.

↩︎ *Aula 05, seção 5 — Requisito × solução: a armadilha*

---

⬅️ [Voltar à Aula 05](../README.md) | ➡️ [Revisão da Aula 06](../../aula-06-elicitacao/revisao/README.md)
