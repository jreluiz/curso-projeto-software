---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 12'
---

<style>
/* Paleta do Bloco 3, com os mesmos papéis:
   verde = está certo / restaurado · vermelho = falha / perigo · âmbar = atenção
   índigo e violeta = categorias neutras · cinza-azulado = contexto */
section {
  --teal: #0f766e; --teal-s: #e7f2f0;
  --ind: #4338ca;  --ind-s: #e0e7ff;
  --amb: #b45309;  --amb-s: #fef3c7;
  --red: #b91c1c;  --red-s: #fee2e2;
  --grn: #15803d;  --grn-s: #dcfce7;
  --vio: #7c3aed;  --vio-s: #ede9fe;
  --sky: #0369a1;  --sky-s: #e0f2fe;
  --sla: #334155;  --sla-s: #f1f5f9;
}
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 18px 24px; }
.grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px; }
.grid4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
.card { border: 3px solid var(--sla); background: var(--sla-s); border-radius: 14px;
        padding: 18px 22px; font-size: 25px; line-height: 1.38; }
.card b.t { display: block; font-size: 28px; margin-bottom: 6px; }
.card .num { display: block; font-size: 60px; font-weight: 800; line-height: 1.05; margin-bottom: 6px; }
.card .pe { display: block; margin-top: 10px; font-size: 22px; color: #475569; }
.card ul { margin: 6px 0 0; padding-left: 24px; }
.card li { font-size: 24px; margin: 4px 0; }
.grid4 .card { font-size: 22px; padding: 14px 16px; }
.grid4 .card b.t { font-size: 25px; }
.teal { border-color: var(--teal); background: var(--teal-s); } .teal .num, .teal b.t { color: var(--teal); }
.ind  { border-color: var(--ind);  background: var(--ind-s);  } .ind .num,  .ind b.t  { color: var(--ind); }
.amb  { border-color: var(--amb);  background: var(--amb-s);  } .amb .num,  .amb b.t  { color: var(--amb); }
.red  { border-color: var(--red);  background: var(--red-s);  } .red .num,  .red b.t  { color: var(--red); }
.grn  { border-color: var(--grn);  background: var(--grn-s);  } .grn .num,  .grn b.t  { color: var(--grn); }
.vio  { border-color: var(--vio);  background: var(--vio-s);  } .vio .num,  .vio b.t  { color: var(--vio); }
.sky  { border-color: var(--sky);  background: var(--sky-s);  } .sky .num,  .sky b.t  { color: var(--sky); }
.legenda { font-size: 25px; margin-top: 18px; }
.chip { display: inline-block; border-radius: 999px; padding: 1px 14px; font-weight: 700;
        font-size: 21px; color: #fff; vertical-align: 2px; }
.chip.grn { background: var(--grn); } .chip.red { background: var(--red); } .chip.amb { background: var(--amb); }
.chip.ind { background: var(--ind); } .chip.vio { background: var(--vio); } .chip.sla { background: var(--sla); }
.chip.sky { background: var(--sky); }

/* linha do tempo */
.linha { display: flex; align-items: stretch; gap: 10px; margin-top: 8px; }
.passo { flex: 1; min-width: 0; border: 3px solid; border-radius: 12px; padding: 12px 12px; font-size: 21px; line-height: 1.3; }
.passo .hora { display: block; font-size: 26px; font-weight: 800; margin-bottom: 4px; }
.seta { align-self: center; font-size: 28px; color: #64748b; font-weight: 700; }
.p-sla { border-color: var(--sla); background: var(--sla-s); } .p-ind { border-color: var(--ind); background: var(--ind-s); }
.p-amb { border-color: var(--amb); background: var(--amb-s); } .p-red { border-color: var(--red); background: var(--red-s); }
.p-grn { border-color: var(--grn); background: var(--grn-s); } .p-vio { border-color: var(--vio); background: var(--vio-s); }
.p-teal { border-color: var(--teal); background: var(--teal-s); } .p-sky { border-color: var(--sky); background: var(--sky-s); }

/* painel de monitoramento escuro */
.dash { background: #0f172a; border-radius: 14px; padding: 16px; display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.tile { background: #1e293b; border-radius: 10px; padding: 12px 16px; color: #cbd5e1; font-size: 20px; }
.tile .v { display: block; font-size: 46px; font-weight: 800; color: #4ade80; line-height: 1.1; }
.tile .ok { color: #4ade80; font-weight: 700; }

/* barras horizontais */
.barras .lin { display: flex; align-items: center; gap: 18px; margin: 12px 0; font-size: 24px; }
.barras .rot { width: 230px; flex: none; font-weight: 700; text-align: right; }
.barras .bar { height: 44px; border-radius: 8px; flex: none; }

/* rastro em cascata: serviço · trilho do tempo · duração */
.wf { display: grid; grid-template-columns: 380px 1fr 90px; gap: 10px 14px; align-items: center; font-size: 22px; }
.wf .tr { position: relative; height: 34px; background: #f1f5f9; border-radius: 6px; }
.wf .tr i { position: absolute; top: 4px; bottom: 4px; border-radius: 5px; }
.wf .d { font-family: Menlo, Consolas, monospace; font-weight: 700; text-align: right; }
.wf .sub { padding-left: 28px; color: #475569; }

/* barra de orçamento / composição */
.orc { display: flex; height: 58px; border-radius: 12px; overflow: hidden; font-size: 22px; font-weight: 700; color: #fff; }
.orc span { display: flex; align-items: center; justify-content: center; }

/* documento */
.doc { border: 2px solid #cbd5e1; border-radius: 12px; background: #fff; padding: 12px 22px;
       font-size: 21px; line-height: 1.4; box-shadow: 0 5px 0 #e2e8f0; }
.doc .h { font-weight: 800; font-size: 23px; margin-bottom: 6px; }
.doc .it { margin: 3px 0; }
.doc .rod { color: #64748b; font-size: 18px; margin-top: 6px; }

/* papéis do incidente, compactos ao lado do runbook */
.papeis { display: grid; gap: 10px; }
.papeis .card { padding: 10px 18px; font-size: 22px; }
.papeis .card b.t { font-size: 25px; margin-bottom: 2px; }

/* quadrante 2×2 */
.quad { display: grid; grid-template-columns: 170px 1fr 1fr; gap: 10px; font-size: 22px; line-height: 1.3; }
.quad div { border-radius: 10px; padding: 14px 16px; }
.quad .h { background: var(--sla); color: #fff; font-weight: 700; text-align: center; display: flex; align-items: center; justify-content: center; }
.quad .v { background: transparent; }

/* código escuro */
.cod { background: #1e1e1e; color: #e6e6e6; border-radius: 12px; padding: 14px 20px; white-space: pre;
       font-family: Menlo, Consolas, monospace; font-size: 20px; line-height: 1.55; }
.cod .k { color: #9cdcfe; } .cod .s { color: #d69d78; } .cod .n { color: #b6cea8; }
</style>

<!-- _class: capa -->

<div class="emoji">🔭</div>

# Operação: Observabilidade e Manutenção

## Aula 12 · Bloco 3 — Do Código à Produção

<div class="meta">Está no ar. Como saber se está tudo bem — e o que fazer quando não está?</div>

---

## 🎯 Nesta aula

1. **Monitorar a máquina não é observar o serviço**
2. **Logs, métricas e rastros** — cada um para uma pergunta
3. **SLO**: quanto de falha é aceitável, e quando acordar alguém
4. **Incidente**: restaurar primeiro, entender depois
5. **Postmortem sem culpa**
6. **Manutenção**, evolução e **dívida técnica**

---

## O painel verde

<div class="grid2">
<div class="dash">
<div class="tile">processador<span class="v">30%</span></div>
<div class="tile">memória<span class="v">40%</span></div>
<div class="tile">servidores no ar<span class="v">4 / 4</span></div>
<div class="tile">situação<span class="v">✓</span><span class="ok">tudo normal</span></div>
</div>
<div class="card red"><span class="num">1 em 3</span>pagamentos por Pix <b>não confirma</b> — há dois dias.<span class="pe">Quem descobriu: o dono do restaurante, lendo as reclamações no Instagram.</span></div>
</div>

<p class="legenda">O painel respondeu tudo o que alguém perguntou a ele. <b>Ninguém tinha perguntado se os clientes conseguiam pagar.</b></p>

---

## Monitorar × observar

<div class="grid2">
<div class="card sla"><b class="t">Monitoramento</b>painéis e alertas para as perguntas <b>que se sabia de antemão</b><span class="pe"><i>"o servidor está de pé?"</i></span></div>
<div class="card teal"><b class="t">Observabilidade</b>responder perguntas <b>que ninguém previu</b>, sem escrever e implantar código novo<span class="pe"><i>"por que só o Pix de um banco falha, e só depois das 19h?"</i></span></div>
</div>

<p class="legenda">O termo vem da teoria de controle (Kálmán, 1960): o quanto o estado interno de um sistema se deduz <b>do que ele emite</b>. A definição para software é de Charity Majors.</p>

> 🔎 **A pergunta que orienta tudo:** o que eu preciso saber para responder *"o serviço está bom?"* **sem perguntar a ninguém**?

---

## Instrumentar o negócio, não só a máquina

<div class="linha">
<div class="passo p-sla"><span class="hora">pedido criado</span></div>
<div class="seta">→</div>
<div class="passo p-amb"><span class="hora">pagamento</span>confirmado ou recusado — e por quê</div>
<div class="seta">→</div>
<div class="passo p-ind"><span class="hora">cozinha</span>pedido na fila</div>
<div class="seta">→</div>
<div class="passo p-grn"><span class="hora">entrega</span>concluída</div>
</div>

<div class="grid2" style="margin-top:22px">
<div class="card grn"><b class="t">O Pix falhando</b>apareceria em <b>15 minutos</b>, e não em dois dias</div>
<div class="card vio"><b class="t">A funcionalidade não usada</b>da Aula 08 aparece: o relatório por bairro foi aberto <b>3 vezes em um ano</b></div>
</div>

<p class="legenda">Medir uso é o que transforma <i>"acho que ninguém usa"</i> numa decisão: manter, melhorar ou remover.</p>

---

## Três sinais, três perguntas

<div class="grid3">
<div class="card ind"><b class="t">📜 Log</b>um evento, com hora e detalhes<span class="pe"><i>o que aconteceu com este pedido, exatamente?</i><br><br>custo: cresce com o volume</span></div>
<div class="card amb"><b class="t">📈 Métrica</b>um número agregado ao longo do tempo<span class="pe"><i>como está o sistema, e como estava ontem?</i><br><br>custo: baixo e fixo</span></div>
<div class="card vio"><b class="t">🧵 Rastro</b>o caminho de uma requisição por todos os serviços<span class="pe"><i>onde o tempo foi gasto, ou o erro aconteceu?</i><br><br>custo: médio — guarda-se uma amostra</span></div>
</div>

<p class="legenda">Nenhum substitui os outros. O padrão aberto para emiti-los é o <b>OpenTelemetry</b> (2019): instrumenta-se uma vez, e os sinais vão para qualquer ferramenta.</p>

---

## O log estruturado

<div class="cod">{<span class="k">"hora"</span>: <span class="s">"2026-11-21T19:42:07Z"</span>, <span class="k">"evento"</span>: <span class="s">"pagamento_recusado"</span>,
 <span class="k">"pedido"</span>: <span class="n">4471</span>, <span class="k">"meio"</span>: <span class="s">"pix"</span>, <span class="k">"provedor"</span>: <span class="s">"banco-x"</span>,
 <span class="k">"motivo"</span>: <span class="s">"tempo_esgotado"</span>, <span class="k">"versao"</span>: <span class="s">"2.6.0"</span>, <span class="k">"rastro"</span>: <span class="s">"a3f9c21e"</span>}</div>

<p class="legenda"><i>"Quantos Pix foram recusados por tempo esgotado, por banco, desde a 2.6.0?"</i> vira <b>consulta</b>, não investigação. O campo <code>versao</code> liga a produção à baseline da Aula 09.</p>

> ⚠️ **Log não é lugar de dado pessoal.** Sem nome, telefone, CPF — o identificador do pedido basta. No prontuário, diagnóstico em log é dado de saúde copiado, e a LGPD vale para a cópia. E log costuma ser lido por mais gente que o banco: lembre a Aula 10.

---

## A média esconde

<div class="barras">
<div class="lin"><span class="rot">média</span><span class="bar" style="width:117px;background:#94a3b8"></span><span>1,8 s — <i>parece ótimo</i></span></div>
<div class="lin"><span class="rot">p50 (mediana)</span><span class="bar" style="width:78px;background:var(--grn)"></span><span>1,2 s — metade é mais rápida</span></div>
<div class="lin"><span class="rot">p95</span><span class="bar" style="width:260px;background:var(--amb)"></span><span>4 s</span></div>
<div class="lin"><span class="rot">p99</span><span class="bar" style="width:780px;background:var(--red)"></span><span>12 s</span></div>
</div>

<p class="legenda">Tempo de confirmação do pedido no delivery. <b>Um em cada cem clientes espera 12 segundos</b> — e desiste. Tempo se mede em <b>percentis</b>.</p>

> 💡 O SRE do Google alerta para a cadeia: o **pior 1%** de um serviço interno vira o tempo **típico** de quem está na ponta.

---

## O rastro: o que aconteceu com este pedido?

<div class="wf">
<div><b>pedido</b> · recebe e valida</div><div class="tr"><i style="left:0;width:1%;background:var(--ind)"></i></div><div class="d">0,2 s</div>
<div><b>pagamento</b> · autoriza no provedor</div><div class="tr"><i style="left:1%;width:97%;background:var(--red)"></i></div><div class="d">37,5 s</div>
<div class="sub">└ provedor externo, 3 tentativas</div><div class="tr"><i style="left:2%;width:96%;background:#f87171"></i></div><div class="d">37,1 s</div>
<div><b>cozinha</b> · entra na fila</div><div class="tr"><i style="left:98%;width:1%;background:var(--amb)"></i></div><div class="d">0,1 s</div>
<div><b>cliente</b> · recebe o aviso</div><div class="tr"><i style="left:98.5%;width:1.5%;background:var(--grn)"></i></div><div class="d">0,4 s</div>
</div>

<p class="legenda">Pedido 4471 · rastro <code>a3f9c21e</code> · 38,4 s no total. Em vez de <i>"está lento"</i>: <b>"o provedor de Pix do banco X leva 37 s, e o nosso código tenta três vezes"</b>.</p>

<p class="legenda">É a resposta à pergunta que a <b>Aula 04</b> deixou na arquitetura orientada a eventos.</p>

---

## Por onde começar: os quatro sinais de ouro

<div class="grid4">
<div class="card ind"><b class="t">Latência</b>quanto tempo leva para atender<span class="pe">p95 da confirmação</span></div>
<div class="card sky"><b class="t">Tráfego</b>quanta demanda chega<span class="pe">pedidos por minuto</span></div>
<div class="card red"><b class="t">Erros</b>a proporção que falha<span class="pe">pagamentos recusados por erro nosso</span></div>
<div class="card amb"><b class="t">Saturação</b>o recurso mais apertado, perto do limite<span class="pe">conexões ocupadas no banco</span></div>
</div>

<p class="legenda">A recomendação é do livro de SRE do Google para qualquer serviço novo: <b>se só der para medir quatro coisas, meça estas</b>.</p>

---

## SLI, SLO, SLA

<div class="grid3">
<div class="card ind"><b class="t">SLI · indicador</b>uma proporção de eventos bons<span class="pe">Pix confirmados em até 30 s ÷ pedidos com Pix</span></div>
<div class="card teal"><b class="t">SLO · objetivo</b>o alvo, numa janela de tempo<span class="pe">99,5% nos últimos 30 dias — <b>o time persegue</b></span></div>
<div class="card amb"><b class="t">SLA · acordo</b>um contrato, com consequência<span class="pe">o provedor devolve parte da tarifa abaixo de 99% — <b>mais folgado que o SLO</b></span></div>
</div>

<p class="legenda">Quem promete 99% em contrato quer o próprio alvo em 99,5%: <b>para descobrir o problema antes de pagar a multa</b>.</p>

---

## Por que não 100%?

<div class="grid4">
<div class="card sla"><span class="num">99%</span>7 h 12 min fora do ar em 30 dias</div>
<div class="card teal"><span class="num">99,5%</span>3 h 36 min</div>
<div class="card ind"><span class="num">99,9%</span>43 min</div>
<div class="card vio"><span class="num">99,99%</span>4 min 19 s</div>
</div>

<p class="legenda">O livro de SRE do Google: <b>100% quase nunca é o alvo certo</b>. É impossível, cada "nove" custa muito mais que o anterior — e o cliente nem percebe, porque o próprio celular falha mais que isso.</p>

---

## O orçamento de erro

<div class="orc">
<span style="width:60%;background:var(--amb)">18 pedidos já falharam</span>
<span style="width:40%;background:var(--grn)">12 ainda cabem</span>
</div>

<p class="legenda">Delivery: 6.000 pedidos com Pix por mês, SLO de 99,5% → <b>30 pedidos por mês podem falhar</b>. É isso o orçamento.</p>

<div class="grid2">
<div class="card grn"><b class="t">Enquanto há orçamento</b>o time implanta à vontade — com as estratégias da Aula 11</div>
<div class="card red"><b class="t">Quando o orçamento acaba</b>param as funcionalidades novas; o esforço vai para a confiabilidade</div>
</div>

<p class="legenda">Uma discussão de opinião — <i>"estamos indo rápido demais?"</i> — vira <b>uma conta combinada antes</b>.</p>

---

## Alerta é para acordar alguém

<div class="grid2">
<div class="card red"><b class="t">🔔 Alerta — exige ação, agora</b><ul>
<li>Pix confirmados abaixo de 95% por 10 min</li>
<li>o ritmo de falhas esgota o orçamento do mês <b>em dois dias</b></li>
</ul><span class="pe">pelo <b>sintoma</b> que o cliente sente</span></div>
<div class="card sla"><b class="t">📊 Painel — sem ação imediata</b><ul>
<li>processador acima de 80%</li>
<li>um pedido isolado que demorou</li>
<li>o orçamento acabando em seis meses</li>
</ul><span class="pe">a <b>causa</b>, para quem investiga</span></div>
</div>

> ⚠️ **"Todo alerta precisa exigir ação"** — livro de SRE. Alerta irrelevante treina o time a silenciar o canal, e o alerta importante chega no meio dos outros. É o teste instável da Aula 10, de novo.

---

## Incidente, problema, mudança

<div class="grid3">
<div class="card red"><b class="t">Incidente</b>interrupção não planejada, ou queda de qualidade<span class="pe">os Pix não confirmam</span></div>
<div class="card amb"><b class="t">Problema</b>a causa de um ou mais incidentes<span class="pe">o provedor demora, e o nosso código desiste cedo</span></div>
<div class="card ind"><b class="t">Mudança</b>qualquer alteração no que está em produção<span class="pe">a 2.6.0, às 19h40</span></div>
</div>

<p class="legenda">Vocabulário do ITIL (leitura <i>Governança</i>). O incidente é o <b>risco que se materializou</b> (leitura <i>Risco</i>).</p>

> 🔎 Cerca de **70%** das interrupções vêm de uma mudança. A primeira pergunta é a da Aula 09: **o que mudou?**

---

## O mesmo sábado, bem conduzido

<div class="linha">
<div class="passo p-sla"><span class="hora">19h40</span>a 2.6.0 vai ao ar num canário de 5%</div>
<div class="seta">→</div>
<div class="passo p-red"><span class="hora">19h52</span><b>alerta</b>: canário 9 pontos abaixo, por 10 min</div>
<div class="seta">→</div>
<div class="passo p-ind"><span class="hora">19h53</span>Bruno <b>declara o incidente</b> e assume o comando</div>
<div class="seta">→</div>
<div class="passo p-amb"><span class="hora">19h55</span><i>o que mudou?</i> — a 2.6.0, há 15 min</div>
<div class="seta">→</div>
<div class="passo p-grn"><span class="hora">19h56</span><b>canário a 0%</b> — às 20h01, tudo normal</div>
</div>

<div class="grid4" style="margin-top:22px">
<div class="card amb"><b class="t">Alerta</b>pelo sintoma</div>
<div class="card ind"><b class="t">Critério</b>de volta, escrito antes</div>
<div class="card sky"><b class="t">Volta pronta</b>o canário da Aula 11</div>
<div class="card grn"><b class="t">Restaurar</b>antes de entender</div>
</div>

<p class="legenda">Às 19h56, <b>ninguém sabia qual era o defeito</b>. Não precisava saber: a causa ficou para segunda-feira.</p>

---

## Do alerta ao aprendizado

![w:1140](img/incidente.svg)

<p class="legenda"><b>Restaurar primeiro, entender depois.</b> Procurar o defeito com o sistema fora do ar é gastar o tempo do cliente na curiosidade do time.</p>

<div class="grid4">
<div class="card grn"><b class="t">Reverter</b>o artefato anterior está guardado</div>
<div class="card grn"><b class="t">Desligar a flag</b>da funcionalidade nova</div>
<div class="card grn"><b class="t">Trocar o tráfego</b>de volta para o azul</div>
<div class="card grn"><b class="t">Zerar o canário</b>todos na versão anterior</div>
</div>

---

## O plano de volta cabe em quatro perguntas

| Pergunta | No delivery |
|---|---|
| **quando decidimos voltar?** | pedidos confirmados 2 pontos abaixo da versão anterior, por 10 min |
| **quem decide?** | quem estiver de plantão, sem consultar ninguém |
| **como se volta?** | canário a 0%; o banco de dados não foi alterado |
| **quanto leva?** | cerca de 3 minutos |

> ⚠️ **A primeira linha é a que sempre falta.** Sem critério escrito, a decisão de voltar é tomada **por desgaste**: tenta-se consertar, espera-se mais um pouco — e a conversa sobre reverter só acontece depois de uma hora.

---

## Papéis e runbook

<div class="grid2">
<div class="papeis">
<div class="card ind"><b class="t">Comandante</b>coordena, decide, delega — <b>não põe a mão no sistema</b></div>
<div class="card amb"><b class="t">Operação</b>age no sistema</div>
<div class="card sky"><b class="t">Comunicação</b>avisa o dono e os clientes, para ninguém interromper quem opera</div>
</div>
<div class="doc">
<div class="h">Runbook — pedidos confirmados abaixo do normal</div>
<div class="it">1. A queda é geral ou de um meio só?</div>
<div class="it">2. Houve implantação ou mudança de flag nas últimas 2 h? → <b>volte a mudança</b> e confira em 5 min</div>
<div class="it">3. O provedor de pagamento está com incidente? → ligue <b>"pagamento-somente-na-entrega"</b> e avise o dono</div>
<div class="it">4. Nada disso: declare incidente e chame a segunda pessoa</div>
<div class="rod">Última revisão: 2026-11-10 · Dono: Ana</div>
</div>
</div>

<p class="legenda">Papéis do modelo do Google, inspirado nos bombeiros. O runbook é <b>item de configuração</b> da Aula 09.</p>

---

## Tempo de recuperação = descobrir + decidir + agir

<div class="orc">
<span style="width:50%;background:var(--amb)">descobrir</span>
<span style="width:30%;background:var(--ind)">decidir</span>
<span style="width:20%;background:var(--grn)">agir</span>
</div>

<div class="grid3" style="margin-top:22px">
<div class="card amb"><b class="t">Descobrir</b>encurta com a <b>observabilidade</b> — o alerta pelo sintoma</div>
<div class="card ind"><b class="t">Decidir</b>encurta com o <b>critério escrito</b> e o plano de volta</div>
<div class="card grn"><b class="t">Agir</b>encurta com as <b>estratégias da Aula 11</b> — volta em minutos</div>
</div>

<p class="legenda">Quando o <b>tempo de recuperação</b> do DORA está alto, é por um desses três que se começa.</p>

---

## 31/01/2017: o banco de dados errado

<div class="linha">
<div class="passo p-sla"><span class="hora">23h30 UTC</span>um engenheiro do <b>GitLab</b> reconstrói a réplica de um banco sobrecarregado</div>
<div class="seta">→</div>
<div class="passo p-red"><span class="hora">rm -rf</span>apaga a pasta de dados — no servidor <b>principal</b>, não na réplica</div>
<div class="seta">→</div>
<div class="passo p-red"><span class="hora">o backup</span>falhava havia tempo; o e-mail de aviso era <b>rejeitado</b></div>
<div class="seta">→</div>
<div class="passo p-amb"><span class="hora">a sorte</span>uma cópia manual de 6 h antes, feita para testes</div>
<div class="seta">→</div>
<div class="passo p-grn"><span class="hora">ao vivo</span>a recuperação transmitida no YouTube</div>
</div>

<div class="grid3" style="margin-top:22px">
<div class="card red"><span class="num">300 GB</span>apagados em um ou dois segundos</div>
<div class="card amb"><span class="num">6 h</span>de dados perdidos — 5 mil projetos, 700 contas</div>
<div class="card sla"><span class="num">18 h</span>com o GitLab.com fora do ar</div>
</div>

---

## Backup que nunca foi restaurado é uma hipótese

<div class="grid2">
<div class="card red"><b class="t">O que falhou em silêncio</b><ul>
<li>o backup diário, por incompatibilidade de versão</li>
<li>o aviso de falha, rejeitado pelo servidor de e-mail</li>
<li>os outros mecanismos, que não cobriam aquele servidor</li>
</ul></div>
<div class="card grn"><b class="t">O que o postmortem listou</b><ul>
<li>replicação frágil</li>
<li><b>backups que ninguém testava</b></li>
<li>falta de dono para a restauração</li>
</ul><span class="pe">publicado 10 dias depois — sem buscar culpado</span></div>
</div>

<p class="legenda">É o painel verde da abertura em outra roupa: <b>um mecanismo que falha sem que ninguém fique sabendo</b>.</p>

---

## Postmortem sem culpa

<div class="grid2">
<div class="card teal"><b class="t">O que ele procura</b>as <b>causas contribuintes</b>, sem acusar pessoa ou time — e parte de que <b>todos agiram com boa intenção</b>, com o que sabiam na hora<span class="pe">livro de SRE do Google</span></div>
<div class="card ind"><b class="t">Por que funciona</b>quando o erro é punido, as pessoas <b>escondem informação</b>, e o próximo incidente demora mais para ser entendido<span class="pe">John Allspaw, Etsy, 2012 — a cultura justa</span></div>
</div>

<p class="legenda">Trocar o engenheiro do GitLab deixaria tudo no lugar: o comando destrutivo à mão, o principal parecido com a réplica, o backup mudo. <b>O próximo engenheiro cansado encontraria o mesmo sistema.</b></p>

> ⚠️ **"Erro humano" é o começo da investigação, não o fim.** A pergunta seguinte: por que o sistema permitiu que a falta de atenção de uma pessoa derrubasse tudo?

---

## O que um postmortem contém

<div class="grid2">
<div class="doc">
<div class="h">Postmortem — Pix não confirmado, 21/11</div>
<div class="it"><b>Resumo</b> — duas frases: o que houve, qual o impacto</div>
<div class="it"><b>Impacto</b> — 14 pedidos, 21 min, metade do orçamento</div>
<div class="it"><b>Linha do tempo</b> — com hora: começo, alerta, volta</div>
<div class="it"><b>Causas contribuintes</b> — quase nunca há uma só</div>
<div class="it"><b>O que funcionou</b> — para manter</div>
<div class="it"><b>Ações</b> — cada uma com <b>dono e prazo</b>, no backlog</div>
</div>
<div>
<p style="font-size:24px;margin-top:0"><b>Quando escrever</b> — os gatilhos do SRE:</p>
<p><span class="chip red">dano visível ao cliente</span> <span class="chip red">qualquer perda de dados</span> <span class="chip amb">volta ou troca de tráfego</span> <span class="chip amb">resolução demorada</span> <span class="chip vio">falha de monitoramento</span></p>
<p style="font-size:22px">Incidentes que <b>se repetem</b> são um <b>problema</b>: é ali que o Six Sigma da Aula 08 cabe — na operação, com repetição e medição.</p>
</div>
</div>

---

## O sistema que não muda fica pior

<div class="grid2">
<div class="card amb"><b class="t">Mudança contínua</b>um sistema em uso precisa ser adaptado o tempo todo, ou fica cada vez menos satisfatório<span class="pe">→ a manutenção <b>não é opcional</b></span></div>
<div class="card red"><b class="t">Complexidade crescente</b>a cada mudança, a complexidade aumenta — a menos que alguém trabalhe para reduzi-la<span class="pe">→ e o custo dela <b>cresce</b></span></div>
</div>

<p class="legenda">Duas das leis de Meir Lehman, dos anos 1970 — ainda a melhor descrição do que acontece depois da entrega.</p>

> ⚠️ **Quando o projeto acaba, alguém precisa ficar com o sistema.** Sem dono, sem plantão e sem runbook, o primeiro incidente leva dias, e não minutos.

---

## Os quatro tipos de manutenção

<div class="grid4">
<div class="card red"><b class="t">Corretiva</b>consertar defeito<span class="pe">o frete arredondado errado</span></div>
<div class="card sky"><b class="t">Adaptativa</b>acompanhar o ambiente: lei, integração, plataforma<span class="pe">o provedor de Pix muda a API</span></div>
<div class="card grn"><b class="t">Perfectiva</b>melhorar ou acrescentar o que se pede<span class="pe">o filtro por bairro</span></div>
<div class="card vio"><b class="t">Preventiva</b>reduzir o risco futuro<span class="pe">testar a restauração do backup</span></div>
</div>

<div class="barras" style="margin-top:18px">
<div class="lin"><span class="rot">perfectiva</span><span class="bar" style="width:600px;background:var(--grn)"></span><span>≈ 60%</span></div>
<div class="lin"><span class="rot">corretiva</span><span class="bar" style="width:170px;background:var(--red)"></span><span>≈ 17% — Lientz e Swanson, fim dos anos 1970</span></div>
</div>

<p class="legenda">⚠️ Contrato que cobre <b>só a corretiva</b> deixa de fora a maior parte do trabalho.</p>

---

## Dívida técnica

<div class="quad">
<div class="v"></div><div class="h">imprudente</div><div class="h">prudente</div>
<div class="h">deliberada</div><div class="card red" style="font-size:22px"><i>"não temos tempo para pensar no desenho"</i></div><div class="card grn" style="font-size:22px"><i>"duplicamos o frete para sexta, e unificamos na semana 3"</i> — <b>registrada, com dono</b></div>
<div class="h">inadvertida</div><div class="card red" style="font-size:22px"><i>"o que é separar em camadas?"</i></div><div class="card amb" style="font-size:22px"><i>"agora que construímos, sabemos como deveria ter sido"</i></div>
</div>

<p class="legenda">Cunningham (1992): um pouco de dívida acelera, <b>desde que paga logo</b>; o juro é o tempo perdido a cada mudança. O quadrante é de Fowler (2009). Só o verde é uma <b>decisão</b>, no sentido da Aula 07.</p>

<p class="legenda">No bloco: a flag que ficou (Aula 11), o teste em quarentena para sempre (Aula 10) — e a funcionalidade que ninguém usa: <b>remover também é manutenção</b>.</p>

---

## Traduzir para quem paga

| No vocabulário técnico | No vocabulário do dono do restaurante |
|---|---|
| *"o frete está duplicado em três lugares"* | *"cada mudança no frete leva uma semana em vez de um dia"* |
| *"precisamos refatorar antes"* | *"duas funcionalidades agora e nenhuma em março, ou uma agora e quatro até março"* |
| *"a biblioteca de pagamento está desatualizada"* | *"em março ela para de receber correção de segurança, no meio do pagamento"* |

<p class="legenda"><b>A dívida só disputa prioridade quando é traduzida em tempo, dinheiro ou risco.</b> E nem toda se paga: sistema que será desligado em um ano não justifica reescrever o frete.</p>

---

## O bloco inteiro em uma volta

![w:1140](img/ciclo-do-bloco.svg)

<p class="legenda">O que se aprende em produção — o incidente, a funcionalidade que ninguém usa, a dívida que cobra juros — volta como <b>item do backlog</b>, e a próxima mudança percorre o mesmo caminho.</p>

---

<!-- _class: lead -->

## 🏁 Doze aulas, um fio só

**A mudança é o objeto de trabalho
da gestão de projetos.**

O escopo muda, o plano muda, o time muda,
o sistema muda depois de entregue —
e alguém precisa conduzir cada mudança.

📚 As **leituras complementares** continuam o caminho.
