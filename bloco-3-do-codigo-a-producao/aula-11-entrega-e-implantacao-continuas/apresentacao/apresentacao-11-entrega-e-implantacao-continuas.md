---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 11'
---

<style>
/* Paleta das Aulas 09–11, com os mesmos papéis:
   verde = está certo / passa · vermelho = quebra / risco alto · âmbar = atenção
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
.card .num { display: block; font-size: 64px; font-weight: 800; line-height: 1.05; margin-bottom: 6px; }
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
.passo { flex: 1; min-width: 0; border: 3px solid; border-radius: 12px; padding: 14px 14px; font-size: 22px; line-height: 1.32; }
.passo .hora { display: block; font-size: 27px; font-weight: 800; margin-bottom: 6px; }
.seta { align-self: center; font-size: 30px; color: #64748b; font-weight: 700; }
.p-sla { border-color: var(--sla); background: var(--sla-s); } .p-ind { border-color: var(--ind); background: var(--ind-s); }
.p-amb { border-color: var(--amb); background: var(--amb-s); } .p-red { border-color: var(--red); background: var(--red-s); }
.p-grn { border-color: var(--grn); background: var(--grn-s); } .p-vio { border-color: var(--vio); background: var(--vio-s); }
.p-teal { border-color: var(--teal); background: var(--teal-s); } .p-sky { border-color: var(--sky); background: var(--sky-s); }

/* ambientes: ambiente · pergunta · quem usa */
.estagios { display: grid; grid-template-columns: 250px 1fr 260px; gap: 12px 18px; align-items: center; font-size: 24px; }
.est { color: #fff; font-weight: 700; border-radius: 10px; padding: 12px 12px; text-align: center; }
.est.sla { background: var(--sla); } .est.ind { background: var(--ind); } .est.vio { background: var(--vio); }
.est.teal { background: var(--teal); }
.quem { color: var(--sla); font-style: italic; }

/* canário: etapas com barra de proporção */
.canario { display: flex; align-items: center; gap: 6px; margin-top: 10px; }
.etapa { border: 3px solid var(--grn); background: var(--grn-s); border-radius: 12px; padding: 12px 10px;
         text-align: center; width: 170px; flex: none; }
.etapa .pct { display: block; font-size: 46px; font-weight: 800; color: var(--grn); line-height: 1.05; }
.etapa .trilha { display: block; height: 14px; background: #dbeafe; border-radius: 7px; margin-top: 8px; overflow: hidden; }
.etapa .trilha i { display: block; height: 100%; background: var(--grn); }
.etapa .quem2 { display: block; font-size: 19px; color: var(--sla); margin-top: 6px; }
.obs { flex: 1; text-align: center; font-size: 20px; color: var(--sla); line-height: 1.2; }
.obs b { display: block; font-size: 30px; color: #64748b; }
.volta { margin-top: 14px; border: 3px dashed var(--red); background: var(--red-s); border-radius: 12px;
         padding: 10px 18px; font-size: 23px; text-align: center; }

/* matriz probabilidade × impacto */
.matriz { display: grid; grid-template-columns: 170px repeat(3, 1fr); gap: 8px; font-size: 22px; line-height: 1.3; }
.matriz div { border-radius: 10px; padding: 12px 12px; text-align: center; display: flex; align-items: center; justify-content: center; }
.matriz .h { background: var(--sla); color: #fff; font-weight: 700; }
.matriz .v { background: transparent; }
.matriz .d { background: var(--grn-s); border: 3px solid var(--grn); }
.matriz .g { background: var(--amb-s); border: 3px solid var(--amb); }
.matriz .c { background: var(--red-s); border: 3px solid var(--red); }

/* código escuro */
.cod { background: #1e1e1e; color: #e6e6e6; border-radius: 12px; padding: 14px 20px; white-space: pre;
       font-family: Menlo, Consolas, monospace; font-size: 22px; line-height: 1.55; }
.cod .k { color: #6aa9e9; } .cod .s { color: #d69d78; } .cod .f { color: #ddd9a0; } .cod .hl { color: #86efac; font-weight: 700; }
</style>

<!-- _class: capa -->

<div class="emoji">🚦</div>

# Entrega e Implantação Contínuas

## Aula 11 · Bloco 3 — Do Código à Produção

<div class="meta">Quem decide que vai, quando vai — e para quantos clientes de cada vez</div>

---

## 🎯 Nesta aula

1. **Pronto não é no ar**: entrega contínua × implantação contínua
2. Os **ambientes**: o mesmo artefato, outra configuração
3. **Todos de uma vez**: o raio da explosão
4. **Quatro maneiras de pôr no ar** — e o banco de dados
5. **Feature flag**: no ar não é ligado
6. **Escolher pelo risco**, medir pelo DORA

---

## Três decisões, três momentos

<div class="linha">
<div class="passo p-vio"><span class="hora">publicar</span>sexta, 18h: a v2.5.0 fica pronta, com tag e CHANGELOG<br><br><b>quem decide:</b> o time</div>
<div class="seta">→</div>
<div class="passo p-sky"><span class="hora">implantar</span>terça, 10h: a v2.5.0 roda em produção, com o cupom <b>desligado</b><br><br><b>quem decide:</b> o time, ou o pipeline</div>
<div class="seta">→</div>
<div class="passo p-grn"><span class="hora">liberar</span>quarta: o cupom ligado para 10% dos clientes<br><br><br><b>quem decide:</b> o negócio</div>
</div>

<p class="legenda">A separação veio da Aula 09. Quando as três acontecem no mesmo instante, <b>cada problema de uma vira problema das outras</b>.</p>

---

## Entrega contínua × implantação contínua

![w:1140](img/entrega-implantacao.svg)

<div class="grid2">
<div class="card amb"><b class="t">Entrega contínua</b>o sistema está <b>sempre pronto</b>; ir ao ar é um botão, apertado quando o negócio decide</div>
<div class="card teal"><b class="t">Implantação contínua</b>toda mudança que passa no pipeline <b>vai ao ar sozinha</b> — a regra foi decidida antes</div>
</div>

<p class="legenda">Fowler: para fazer implantação contínua, <b>é preciso</b> fazer entrega contínua. O teste: <i>"põe no ar a versão de agora"</i> — dá para fazer já, com segurança?</p>

---

<!-- _class: lead -->

## "O negócio não aceita mudança todo dia"

A frase recusa a **implantação** contínua —
não a **entrega** contínua.

O **prontuário** integra todo dia e está sempre pronto.
O comitê aprova uma **tag**, uma vez por mês,
e a implantação vira um botão numa terça de manhã.

O **delivery** pode ir sozinho ao ar —
menos de sexta a domingo, das 18h às 23h.

---

## Mudança pequena é mudança segura

<div class="grid2">
<div class="card red"><b class="t">A cada três meses</b><ul>
<li><b>200</b> mudanças em cada implantação</li>
<li>se der errado, a causa está entre 200, de 20 pessoas</li>
<li>voltar desfaz três meses de trabalho</li>
<li>o time pratica <b>4 vezes por ano</b></li>
</ul></div>
<div class="card grn"><b class="t">Todo dia</b><ul>
<li><b>3</b> mudanças em cada implantação</li>
<li>a causa está entre 3, de ontem, de quem lembra</li>
<li>voltar desfaz um dia</li>
<li>o time pratica <b>todo dia</b></li>
</ul></div>
</div>

<p class="legenda">É o ramo longo da Aula 09 e as <b>mudanças pequenas</b> do DORA na Aula 10. A implantação ideal é um <b>não-evento</b>.</p>

---

## Os ambientes até a produção

<div class="estagios">
<div class="est sla">desenvolvimento</div><div>funciona isolado, na máquina de quem escreveu?</div><div class="quem">quem programa</div>
<div class="est ind">integração</div><div>funciona junto com o resto? — o pipeline da Aula 10</div><div class="quem">a máquina</div>
<div class="est vio">homologação</div><div>funciona numa cópia fiel da produção? O cliente aprova?</div><div class="quem">time, cliente, comitê</div>
<div class="est teal">produção</div><div>funciona para quem usa de verdade?</div><div class="quem">os clientes</div>
</div>

<p class="legenda">O caminho inteiro, automatizado, é o <b>pipeline de implantação</b> de Humble e Farley. Entre um ambiente e o próximo há um <b>portão</b> — automático no delivery; no prontuário, o último é o comitê.</p>

---

## Promover o artefato — não reconstruí-lo

![w:1140](img/promocao.svg)

<p class="legenda">O artefato é o mesmo do começo ao fim; o que muda é a <b>configuração</b>, que mora fora dele (Aula 09). Se a homologação aprovou o <code>sha256:9f2c…</code>, é ele que vai à produção — <b>e dá para conferir</b>.</p>

> ⚠️ **Reconstruir para a produção é testar uma coisa e implantar outra.**

---

## Homologação que não parece produção não homologa nada

<div class="grid4">
<div class="card ind"><b class="t">Dados</b>50 pedidos de teste contra 400 mil reais</div>
<div class="card amb"><b class="t">Carga</b>ninguém testa com o movimento de sábado à noite</div>
<div class="card vio"><b class="t">Integrações</b>simulador de pagamento contra o serviço de verdade</div>
<div class="card sky"><b class="t">Versões</b>um banco de dados na homologação, outro na produção</div>
</div>

<p class="legenda"><span class="chip red">LGPD</span> No prontuário, <b>dado real de paciente nunca vai para a homologação</b> — nem "para testar o volume". Gera-se ou anonimiza-se.</p>

> 💡 **A última verificação sempre acontece em produção.** A pergunta é: com quantos clientes?

---

## 19/07/2024: um arquivo para todos de uma vez

<div class="linha">
<div class="passo p-sla"><span class="hora">04h09 UTC</span>a CrowdStrike envia um <b>arquivo de conteúdo</b> ao seu programa de proteção</div>
<div class="seta">→</div>
<div class="passo p-amb"><span class="hora">21 ≠ 20</span>o arquivo define 21 campos; o programa espera 20 — e o validador tinha um erro</div>
<div class="seta">→</div>
<div class="passo p-red"><span class="hora">tela azul</span>o Windows trava, reinicia, trava de novo</div>
<div class="seta">→</div>
<div class="passo p-amb"><span class="hora">05h27</span>o arquivo é retirado, 78 minutos depois</div>
<div class="seta">→</div>
<div class="passo p-red"><span class="hora">dias</span>cada máquina travada precisa de conserto <b>manual</b></div>
</div>

<p class="legenda">Não era código: era <b>conteúdo</b> — como o arquivo da Cloudflare na Aula 09. E chegou <b>a todos os computadores ligados, ao mesmo tempo</b>.</p>

---

## O tamanho do estrago

<div class="grid3">
<div class="card red"><span class="num">8,5 mi</span>de computadores com Windows afetados, pela estimativa da Microsoft</div>
<div class="card amb"><span class="num">&lt; 1%</span>das máquinas com Windows — concentrado em quem depende delas para funcionar</div>
<div class="card sla"><span class="num">78 min</span>no ar; o conserto, máquina a máquina, levou dias</div>
</div>

<p class="legenda">Companhias aéreas cancelaram voos, hospitais adiaram atendimentos, bancos e emissoras de TV ficaram fora do ar.</p>

> 💡 **O que a empresa anunciou depois:** distribuir o conteúdo **de forma escalonada, começando por um canário**, e dar aos clientes **controle sobre quando** as atualizações chegam.

---

## Mudança é a maior causa de interrupção

<div class="grid2">
<div class="card red"><span class="num">≈ 70%</span>das interrupções de serviço se devem a <b>mudanças num sistema em produção</b><span class="pe">livro de SRE do Google, 2016</span></div>
<div class="card grn"><b class="t">O que mais reduz o dano</b><ul>
<li><b>implantar aos poucos</b> — esta aula</li>
<li>detectar problemas rápido — Aula 12</li>
<li>voltar atrás com segurança — Aula 12</li>
</ul></div>
</div>

<p class="legenda">O <b>raio da explosão</b>: quantos clientes uma mudança defeituosa atinge antes que alguém perceba. O defeito vai acontecer, apesar dos testes — <b>o raio é uma escolha de projeto</b>.</p>

---

## Quatro maneiras de pôr no ar

<div class="grid4">
<div class="card red"><b class="t">Direta</b>a versão nova substitui a antiga de uma vez<span class="pe">raio: <b>todos</b><br>volta: reimplantar a anterior</span></div>
<div class="card amb"><b class="t">Gradual</b>os servidores são atualizados aos poucos<span class="pe">raio: <b>cresce a cada leva</b><br>volta: parar e reverter</span></div>
<div class="card sky"><b class="t">Azul-verde</b>dois ambientes; o tráfego troca de uma vez<span class="pe">raio: todos, depois de testada no real<br>volta: <b>segundos</b></span></div>
<div class="card grn"><b class="t">Canário</b>uma fatia dos clientes primeiro, observada<span class="pe">raio: <b>a fatia</b><br>volta: tirar o canário</span></div>
</div>

<p class="legenda">Do mais barato ao mais trabalhoso. <b>Combinar é o normal</b>: a estratégia se escolhe por mudança, não uma vez para sempre.</p>

---

## Azul-verde: a volta em segundos

![w:900](img/azul-verde.svg)

<p class="legenda">A versão nova sobe no ambiente ocioso e é verificada <b>com a infraestrutura da produção</b>. O azul nunca é desligado: se algo der errado, o roteador troca de volta. Na próxima implantação, os papéis se invertem.</p>

---

## Canário: alguns primeiro, todos depois

<div class="canario">
<div class="etapa"><span class="pct">1%</span><span class="trilha"><i style="width:4%"></i></span><span class="quem2">funcionários</span></div>
<div class="obs"><b>→</b>observa<br>30 min</div>
<div class="etapa"><span class="pct">5%</span><span class="trilha"><i style="width:7%"></i></span><span class="quem2">amostra</span></div>
<div class="obs"><b>→</b>observa<br>1 hora</div>
<div class="etapa"><span class="pct">25%</span><span class="trilha"><i style="width:25%"></i></span><span class="quem2">amostra</span></div>
<div class="obs"><b>→</b>observa<br>1 dia</div>
<div class="etapa"><span class="pct">100%</span><span class="trilha"><i style="width:100%"></i></span><span class="quem2">todos</span></div>
</div>

<div class="volta">⛔ <b>Critério violado em qualquer etapa → volta a 0%</b></div>

<p class="legenda">O critério se escreve <b>antes</b>: <i>"se os pedidos confirmados no canário ficarem 2 pontos abaixo da versão atual, ou os erros de pagamento dobrarem, volta"</i>. Sem ele, avança-se por otimismo e volta-se por desgaste.</p>

---

## O banco de dados não volta tão fácil

![w:1140](img/expandir-contrair.svg)

<p class="legenda">No canário e no azul-verde, <b>a versão antiga e a nova rodam juntas sobre o mesmo banco</b>. Renomear <code>endereco</code> de uma vez quebra os 95% que ainda rodam a antiga. Em três implantações, cada passo tem volta.</p>

> ⚠️ **Migração destrutiva não tem canário que desfaça.** Remover, converter, apagar: a decisão de seguir sem volta se toma **antes**, por quem tem autoridade — não às 21h de sábado.

---

## Feature flag: no ar não é ligado

<div class="cod"><span class="k">if</span> (flags.<span class="f">ligada</span>(<span class="s">"pagamento-pix"</span>, cliente)) {
  <span class="k">return</span> <span class="hl">pagarComPix</span>(pedido);
}
<span class="k">return</span> pagarComCartao(pedido);</div>

<div class="linha">
<div class="passo p-sky"><span class="hora">terça</span>o código do Pix vai ao ar <b>desligado</b></div>
<div class="seta">→</div>
<div class="passo p-ind"><span class="hora">quarta</span>ligado para os funcionários</div>
<div class="seta">→</div>
<div class="passo p-amb"><span class="hora">quinta</span>ligado para 5% dos clientes</div>
<div class="seta">→</div>
<div class="passo p-grn"><span class="hora">semana seguinte</span>ligado para todos</div>
</div>

<p class="legenda">Nenhum desses passos é uma implantação — e <b>cada um se desfaz desligando a flag</b>.</p>

---

## Os quatro tipos de flag

<div class="grid2">
<div class="card grn"><b class="t">De liberação · dias a semanas</b>esconder o que não está pronto, ou liberar aos poucos<span class="pe">o Pix, ligado em etapas</span></div>
<div class="card vio"><b class="t">De experimento · o tempo do teste</b>dividir os clientes em grupos e comparar<span class="pe">metade vê o botão "pedir de novo"</span></div>
<div class="card red"><b class="t">De operação · o <i>kill switch</i></b>desligar ou simplificar algo às pressas<span class="pe">se o serviço de mapas cair, o frete volta a ser fixo</span></div>
<div class="card ind"><b class="t">De permissão · meses a anos</b>liberar algo só para um grupo<span class="pe">o relatório de vendas, só para o dono</span></div>
</div>

<p class="legenda">A classificação é de Pete Hodgson (2017). O que separa os tipos é, principalmente, <b>quanto tempo cada flag deve viver</b>.</p>

---

## 12/06/2025: a flag que faltou

<div class="linha">
<div class="passo p-sla"><span class="hora">29/05</span>código novo no <b>Service Control</b>, região por região</div>
<div class="seta">→</div>
<div class="passo p-amb"><span class="hora">sem flag</span>o trecho novo não é executado em nenhuma região; não tem tratamento de erro</div>
<div class="seta">→</div>
<div class="passo p-red"><span class="hora">12/06</span>uma política com <b>campos em branco</b> chega ao mundo todo <b>em segundos</b></div>
<div class="seta">→</div>
<div class="passo p-red"><span class="hora">queda</span>dezenas de produtos do Google — e de quem roda sobre eles</div>
<div class="seta">→</div>
<div class="passo p-grn"><span class="hora">40 min</span>o trecho novo é desligado; a recuperação total leva horas</div>
</div>

<p class="legenda">O primeiro compromisso do relatório: <b>toda mudança em sistema crítico protegida por flag, desligada por padrão</b>.</p>

---

## O que o caso do Google ensina

<div class="grid2">
<div class="card grn"><b class="t">A flag desligada por padrão</b>o código novo teria chegado a todas as regiões <b>sem ser executado</b> — e seria ligado aos poucos</div>
<div class="card red"><b class="t">O dado também é mudança</b>a implantação do código foi gradual; o dado que disparou o defeito, não — chegou ao mundo todo em segundos</div>
</div>

<div class="linha" style="margin-top:22px">
<div class="passo p-amb"><span class="hora">Aula 09</span>Cloudflare: um arquivo de configuração</div>
<div class="passo p-amb"><span class="hora">esta aula</span>CrowdStrike: um arquivo de conteúdo</div>
<div class="passo p-amb"><span class="hora">esta aula</span>Google: uma política replicada</div>
</div>

<p class="legenda">Três vezes no bloco: <b>configuração e dados precisam da mesma cautela que o código</b>.</p>

---

## Flag é dívida com prazo

<div class="grid3">
<div class="card sla"><span class="num">2</span>flags: <b>4</b> combinações possíveis</div>
<div class="card amb"><span class="num">10</span>flags: <b>1.024</b> combinações — ninguém testa todas</div>
<div class="card red"><span class="num">1</span>flag reaproveitada bastou para a Knight Capital, na Aula 09</div>
</div>

<div class="grid3" style="margin-top:20px">
<div class="card grn"><b class="t">Dono e data</b>a tarefa de remover entra no backlog no dia da criação</div>
<div class="card grn"><b class="t">Limite</b>o número de flags ativas tem teto, como um estoque</div>
<div class="card grn"><b class="t">Nunca reaproveitar</b>flag velha não ganha significado novo</div>
</div>

---

## Escolher pelo risco da mudança

<div class="matriz">
<div class="v"></div><div class="h">impacto baixo</div><div class="h">impacto médio</div><div class="h">impacto alto</div>
<div class="h">prob. alta</div><div class="g">gradual</div><div class="c">canário</div><div class="c">canário com flag, fora do pico — ou rever a mudança</div>
<div class="h">prob. média</div><div class="d">direta</div><div class="g">gradual ou azul-verde</div><div class="c">canário com flag</div>
<div class="h">prob. baixa</div><div class="d">direta</div><div class="d">direta</div><div class="g"><b>azul-verde ou canário, com a volta pronta</b></div>
</div>

<p class="legenda"><b>Probabilidade</b> cresce com o tamanho e a novidade da mudança. <b>Impacto</b>, com clientes, dinheiro, dado sensível — e <b>irreversibilidade</b>. É a matriz da leitura <i>Risco</i>, e a mesma armadilha: probabilidade baixa com impacto alto <b>não é "direta"</b>.</p>

---

## No delivery

| Mudança | Probabilidade | Impacto | Como implantar |
|---|:---:|:---:|---|
| erro de digitação no cardápio | baixa | baixo | <span class="chip grn">direta</span> a qualquer hora |
| frete por bairro, não por distância | média | médio | <span class="chip amb">azul-verde</span> fora do pico |
| trocar o provedor de pagamento | média | **alto** | <span class="chip red">canário com flag</span> funcionários → 5% → 25% → todos |

<p class="legenda">No pagamento, o provedor antigo fica <b>a um clique</b> até a mudança chegar a 100% e estabilizar.</p>

---

## As cinco métricas DORA

<div class="grid2">
<div class="card ind"><b class="t">Vazão</b><ul>
<li><b>tempo de espera da mudança</b> — do commit à produção</li>
<li><b>frequência de implantação</b></li>
<li><b>tempo de recuperação</b> de implantação com falha</li>
</ul></div>
<div class="card red"><b class="t">Instabilidade</b><ul>
<li><b>taxa de falha de mudança</b> — implantações que exigem reverter ou corrigir às pressas</li>
<li><b>taxa de retrabalho</b> — implantações não planejadas, para corrigir incidente</li>
</ul></div>
</div>

<p class="legenda">Cinco desde 2024: entrou a taxa de retrabalho, e o tempo de recuperação passou para a vazão. A leitura <i>Qualidade que se mede</i> traz as quatro clássicas.</p>

---

## Velocidade e estabilidade andam juntas

<div class="grid2">
<div class="card grn"><b class="t">Desempenho mais alto · DORA 2024</b><ul>
<li>commit → produção em <b>menos de 1 dia</b></li>
<li>recuperação em <b>menos de 1 hora</b></li>
<li>taxa de falha de cerca de <b>5%</b></li>
</ul></div>
<div class="card red"><b class="t">Desempenho mais baixo · DORA 2024</b><ul>
<li>commit → produção em <b>1 a 6 meses</b></li>
<li>recuperação em <b>1 semana a 1 mês</b></li>
</ul></div>
</div>

<p class="legenda">Ano após ano, quem entrega mais rápido tende a ser também <b>mais estável</b> — porque entrega em pedaços pequenos, verificados e com volta.</p>

> ⚠️ **As métricas DORA também viram meta** — o próprio DORA avisa. Leem-se **juntas**, **por aplicação**, para o time comparar a si mesmo — nunca para ranquear times.

---

## O que esta aula deixa no lugar

![w:1000](img/o-que-fica.svg)

<p class="legenda">A versão nova está no ar, para 5% dos clientes, com o critério escrito. Falta <b>enxergar</b> o que acontece em produção — e saber o que fazer quando o critério é violado.</p>

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 12 — Operação: observabilidade e manutenção**

Está no ar.
Como saber se está tudo bem —
e o que fazer quando não está?
