---
marp: true
theme: trilha
paginate: true
lang: pt-BR
footer: '🏗️ Curso de Projeto de Software · Aula 08'
---

<style>
/* Paleta da aula — cada abordagem tem a sua cor, do primeiro ao último slide:
   violeta = Design Thinking · índigo = MVP · teal = Lean · azul = Six Sigma
   verde = está certo · vermelho = erro, desperdício · âmbar = atenção, espera
   cinza-azulado = contexto */
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
.grid4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }
.card { border: 3px solid var(--sla); background: var(--sla-s); border-radius: 14px;
        padding: 18px 22px; font-size: 25px; line-height: 1.38; }
.card b.t { display: block; font-size: 28px; margin-bottom: 6px; }
.card .num { display: block; font-size: 60px; font-weight: 800; line-height: 1.05; margin-bottom: 8px; }
.card .pe { display: block; margin-top: 10px; font-size: 22px; color: #475569; }
.teal { border-color: var(--teal); background: var(--teal-s); } .teal .num, .teal b.t { color: var(--teal); }
.ind  { border-color: var(--ind);  background: var(--ind-s);  } .ind .num,  .ind b.t  { color: var(--ind); }
.amb  { border-color: var(--amb);  background: var(--amb-s);  } .amb .num,  .amb b.t  { color: var(--amb); }
.red  { border-color: var(--red);  background: var(--red-s);  } .red .num,  .red b.t  { color: var(--red); }
.grn  { border-color: var(--grn);  background: var(--grn-s);  } .grn .num,  .grn b.t  { color: var(--grn); }
.vio  { border-color: var(--vio);  background: var(--vio-s);  } .vio .num,  .vio b.t  { color: var(--vio); }
.sky  { border-color: var(--sky);  background: var(--sky-s);  } .sky .num,  .sky b.t  { color: var(--sky); }
.legenda { font-size: 25px; margin-top: 18px; }
.fonte { font-size: 19px; color: #64748b; margin-top: 6px; }
.chip { display: inline-block; border-radius: 999px; padding: 1px 14px; font-weight: 700;
        font-size: 21px; color: #fff; vertical-align: 2px; }
.chip.vio { background: var(--vio); } .chip.ind { background: var(--ind); } .chip.teal { background: var(--teal); }
.chip.amb { background: var(--amb); } .chip.red { background: var(--red); } .chip.grn { background: var(--grn); }

/* a pergunta de cada abordagem */
.card .perg { display: block; font-style: italic; font-size: 26px; margin-bottom: 12px; }

/* as cinco etapas, com as duas voltas do teste */
.ciclo { display: grid; grid-template-columns: repeat(4, 206px 26px) 206px; margin: 18px auto 0; width: max-content; }
.et { border: 3px solid var(--vio); background: var(--vio-s); border-radius: 10px; padding: 12px 4px;
      text-align: center; font-weight: 800; font-size: 22px; grid-row: 1; }
.et small { display: block; font-weight: 400; font-size: 21px; margin-top: 4px; line-height: 1.3; }
.et.cheia { background: var(--vio); color: #fff; }
.sa { grid-row: 1; align-self: center; text-align: center; font-size: 28px; color: var(--vio); font-weight: 800; }
.volta { grid-row: 2; align-self: start; position: relative; border: 3px dashed var(--amb); border-top: none; border-radius: 0 0 12px 12px; }
.volta::before { content: "▲"; position: absolute; left: -11px; top: -12px; color: var(--amb); font-size: 17px; line-height: 1; }
.volta span { position: absolute; bottom: -15px; left: 50%; transform: translateX(-50%); background: #fdfdfb;
              padding: 0 10px; font-size: 22px; color: var(--amb); font-weight: 700; white-space: nowrap; }
.v1 { grid-column: 5 / 10; height: 42px; margin: 0 123px 0 103px; }
.v2 { grid-column: 3 / 10; height: 100px; margin: 0 83px 0 103px; }

/* linha de etapas */
.linha { display: flex; align-items: stretch; gap: 8px; margin-top: 8px; }
.passo { flex: 1; border: 3px solid; border-radius: 12px; padding: 12px 14px; font-size: 21px; line-height: 1.3; }
.passo .hora { display: block; font-size: 26px; font-weight: 800; margin-bottom: 6px; }
.passo .sai { display: block; margin-top: 10px; padding-top: 8px; border-top: 2px dashed rgba(51,65,85,.35); font-weight: 600; }
.seta { align-self: center; font-size: 28px; color: #64748b; font-weight: 700; }

/* campo → valor (as três partes do MVP) */
.partes { display: grid; grid-template-columns: 270px 1fr; gap: 14px 18px; align-items: stretch; font-size: 26px; margin-top: 10px; }
.campo { color: #fff; font-weight: 700; border-radius: 10px; padding: 14px 14px; display: flex; align-items: center; justify-content: center; text-align: center; }
.campo.ind { background: var(--ind); } .campo.amb { background: var(--amb); } .campo.red { background: var(--red); }
.campo.grn { background: var(--grn); }
.valor { border: 2px solid #cbd5e1; background: #fff; border-radius: 10px; padding: 12px 18px; line-height: 1.35; }

/* pedido × problema */
.pp { display: grid; grid-template-columns: 200px 1fr 44px 360px; gap: 14px 12px; align-items: stretch; font-size: 25px; margin-top: 6px; }
.pp .def { border: 2px solid #cbd5e1; background: #fff; border-radius: 10px; padding: 12px 18px; line-height: 1.35; display: flex; align-items: center; }
.pp .sx { align-self: center; text-align: center; font-size: 30px; color: #64748b; font-weight: 700; }
.pp .cons { border: 3px solid; border-radius: 10px; padding: 12px 16px; line-height: 1.35; display: flex; align-items: center; }
.pp .cons.red { border-color: var(--red); background: var(--red-s); } .pp .cons.grn { border-color: var(--grn); background: var(--grn-s); }
.pp .obs { grid-column: 1 / -1; text-align: center; font-size: 23px; color: var(--vio); font-weight: 600; padding: 2px 0; }
.pp .cab { font-size: 20px; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }

/* a frase de definição, com as lacunas */
.frase { font-size: 30px; line-height: 1.9; text-align: center; margin: 6px 0 22px; }
.lac { border: 3px dashed var(--vio); background: var(--vio-s); border-radius: 10px; padding: 2px 14px; font-weight: 700; color: var(--vio); }

/* duplo diamante */
.dd { display: flex; align-items: center; justify-content: center; margin-top: 18px; }
.ponta { width: 80px; font-size: 21px; font-weight: 700; color: #475569; text-align: center; line-height: 1.2; }
.dia { width: 490px; text-align: center; }
.dia .cap { font-weight: 800; font-size: 26px; margin-bottom: 8px; }
.losango { position: relative; height: 290px; clip-path: polygon(0 50%, 50% 0, 100% 50%, 50% 100%); }
.losango .dentro { position: absolute; inset: 6px; clip-path: polygon(0 50%, 50% 0, 100% 50%, 50% 100%);
                   display: grid; grid-template-columns: 1fr 1fr; align-items: center; }
.losango .dentro::after { content: ""; position: absolute; left: 50%; top: 8%; bottom: 8%; border-left: 3px dashed rgba(51,65,85,.45); }
.losango .dentro div { font-size: 23px; line-height: 1.3; }
.losango .dentro div:first-child { padding-left: 52px; } .losango .dentro div:last-child { padding-right: 52px; }
.losango.vio { background: var(--vio); } .losango.vio .dentro { background: var(--vio-s); }
.losango.ind { background: var(--ind); } .losango.ind .dentro { background: var(--ind-s); }

/* escala do mais barato ao mais caro */
.escala { height: 14px; border-radius: 7px; margin: 8px 0 6px; background: linear-gradient(90deg, #86efac, #fbbf24, #f87171); }
.escala-rot { display: flex; justify-content: space-between; font-size: 20px; font-weight: 700; color: #475569; margin-bottom: 10px; }
.card.mini { font-size: 21px; padding: 14px 16px; line-height: 1.32; }
.card.mini b.t { font-size: 24px; }
.card.mini .pe { font-size: 20px; }

/* os sete desperdícios */
.card.dsp { font-size: 20px; padding: 12px 14px; line-height: 1.3; }
.card.dsp .fab { display: block; font-size: 17px; text-transform: uppercase; letter-spacing: 1px; color: #64748b; font-weight: 700; }
.card.dsp b.t { font-size: 23px; margin: 2px 0 4px; }

/* fluxo em dias, na proporção */
.fluxo { display: flex; gap: 4px; margin-top: 14px; }
.seg { border-radius: 8px; padding: 12px 6px; font-size: 22px; text-align: center; line-height: 1.25; color: #fff; }
.seg b { font-size: 26px; }
.seg.trab { background: var(--teal); }
.seg.esp { background: repeating-linear-gradient(45deg, var(--amb-s), var(--amb-s) 12px, #fde68a 12px, #fde68a 24px);
           border: 3px solid var(--amb); color: var(--amb); }
.chave { border: 3px solid #94a3b8; border-top: none; height: 16px; margin: 6px 2px 4px; border-radius: 0 0 10px 10px; }
.chave-rot { text-align: center; font-size: 22px; color: #475569; font-weight: 600; margin-bottom: 14px; }

/* a média engana: tempos de resposta, em dias */
.plot { display: grid; grid-template-columns: 120px 960px; margin: 6px auto 0; width: max-content; }
.plot .rot { font-size: 26px; font-weight: 800; display: flex; align-items: center; }
.pista { position: relative; height: 100px; border-bottom: 2px solid #cbd5e1; }
.pista .d { position: absolute; width: 24px; height: 24px; border-radius: 50%; transform: translateX(-50%); }
.pista .d.o { background: var(--teal); } .pista .d.s { background: var(--sky); } .pista .d.x { background: var(--red); }
.pista .prazo { position: absolute; left: 66.67%; top: 0; bottom: -2px; border-left: 4px solid var(--red); }
.pista .media { position: absolute; left: 31.11%; top: 0; bottom: -2px; border-left: 3px dashed #475569; }
.pista .tx { position: absolute; top: 2px; font-size: 19px; font-weight: 700; white-space: nowrap; }
.eixo { position: relative; height: 34px; font-size: 19px; color: #64748b; }
.eixo span { position: absolute; top: 4px; transform: translateX(-50%); }
</style>

<!-- _class: capa -->

<div class="emoji">🔍</div>

# Descobrir, Enxugar, Melhorar

## Aula 08 · Bloco 2 — Metodologias de Gestão

<div class="meta">Quatro abordagens, três perguntas — e usar a errada é caro</div>

---

## 🎯 Nesta aula

1. Três abordagens para **três perguntas diferentes**
2. **Design Thinking** — as cinco etapas e o duplo diamante
3. **MVP** — o menor produto que ensina alguma coisa
4. O que MVP **não é**
5. **Lean** — valor, fluxo e desperdício
6. **Six Sigma** e o DMAIC
7. Qual usar **quando**

---

## Cada uma responde a uma pergunta

<div class="grid3">
<div class="card vio"><b class="t">Design Thinking</b><span class="perg">não sabemos qual é o problema certo</span>produz uma <b>definição do problema</b> que ninguém tinha enunciado<span class="pe">achados e perdidos</span></div>
<div class="card ind"><b class="t">MVP</b><span class="perg">não sabemos se alguém quer isto</span>produz uma <b>decisão</b>: seguir, ou mudar de direção<span class="pe">marketplace de serviços</span></div>
<div class="card teal"><b class="t">Lean e Six Sigma</b><span class="perg">sabemos o que fazer, e fazemos mal</span>produz um fluxo <b>mais curto</b> e <b>mais previsível</b><span class="pe">Ouvidoria municipal</span></div>
</div>

<p class="legenda">Há produtos que passam pelas três, <b>nessa ordem</b>. Usar a terceira antes das duas primeiras é que não funciona.</p>

---

<!-- _class: lead -->

## ⚠️ O erro mais caro

é usar Lean
onde a pergunta era MVP.

Otimizar a construção de algo
que ninguém quer produz desperdício
com excelente indicador de eficiência.

---

## Design Thinking: as cinco etapas

Parte de uma suspeita: **o problema que o cliente enuncia raramente é o problema dele** — ele já traduziu a dor numa solução. Em projeto de TI, entra **antes do backlog**.

<div class="ciclo">
<div class="et cheia">EMPATIA<small>observar quem vive o problema</small></div><div class="sa">→</div>
<div class="et">DEFINIÇÃO<small>o problema numa frase</small></div><div class="sa">→</div>
<div class="et">IDEAÇÃO<small>muitas alternativas</small></div><div class="sa">→</div>
<div class="et">PROTOTIPAÇÃO<small>a versão mais barata</small></div><div class="sa">→</div>
<div class="et">TESTE<small>com quem vive o problema</small></div>
<div class="volta v1"><span>a ideia não serve</span></div>
<div class="volta v2"><span>o problema era outro</span></div>
</div>

<p class="legenda">O teste manda de volta para a definição — <b>e é isso que o torna útil</b>.</p>

---

## O que se faz em cada etapa

<div class="linha">
<div class="passo" style="border-color:var(--vio);background:var(--vio-s)"><span class="hora">Empatia</span>acompanhar alguém fazendo a tarefa, onde ela acontece<span class="sai">o que fazem, não o que dizem</span></div>
<div class="seta">→</div>
<div class="passo" style="border-color:var(--vio);background:#fff"><span class="hora">Definição</span>uma frase: <i>quem</i> precisa <i>de quê</i>, <i>porque</i>…<span class="sai">uma definição que ninguém tinha enunciado</span></div>
<div class="seta">→</div>
<div class="passo" style="border-color:var(--vio);background:#fff"><span class="hora">Ideação</span>quantidade primeiro, sem julgar; depois, votar<span class="sai">opções que não viriam na 1ª conversa</span></div>
<div class="seta">→</div>
<div class="passo" style="border-color:var(--vio);background:#fff"><span class="hora">Protótipo</span>tela no papel, ou o serviço feito à mão<span class="sai">algo para mostrar — e jogar fora</span></div>
<div class="seta">→</div>
<div class="passo" style="border-color:var(--vio);background:#fff"><span class="hora">Teste</span>cinco pessoas, uma por vez, sem ninguém explicar nada<span class="sai">o que estava errado na definição</span></div>
</div>

<p class="legenda">As quatro últimas se fazem em sala. <b>A empatia exige sair da sala</b> — é a única que não se pode pular.</p>

---

## Empatia: pergunte sobre o passado

<div class="grid2">
<div class="card red"><b class="t">⛔ Não serve</b><i>"Você usaria um aplicativo para isso?"</i><span class="pe" style="font-size:24px">Quase todo mundo diz que sim, por educação — e não usa. A pergunta sobre o futuro mede gentileza.</span></div>
<div class="card grn"><b class="t">✅ Serve</b><i>"Conte a última vez que isso aconteceu com você."</i><span class="pe" style="font-size:24px">E, melhor que perguntar: <b>observar</b>. A observação mostra o que a pessoa faz sem perceber.</span></div>
</div>

<p class="legenda">💡 É justamente a etapa que some quando a oficina é marcada <b>para caber numa tarde</b>.</p>

---

## Achados e perdidos: o pedido não é o problema

<div class="pp">
<div></div><div class="cab">a definição</div><div></div><div class="cab">o que o time constrói</div>
<div class="campo red">o pedido</div><div class="def"><span>"queremos um sistema para <b>cadastrar</b> itens perdidos"</span></div><div class="sx">→</div><div class="cons red">formulário e listagem</div>
<div class="obs">↓ uma manhã na portaria: o item quase sempre está lá — quem procura <b>não sabe descrevê-lo</b> ↓</div>
<div class="campo grn">o problema</div><div class="def"><span><b>pareamento</b> sob descrição ambígua</span></div><div class="sx">→</div><div class="cons grn">busca por características, foto do item, portaria sugere candidatos</div>
</div>

<p class="legenda">Mesmo orçamento, <b>resultados incomparáveis</b> — e só um dos dois resolve a dor.</p>

---

## Definição: da frase à pergunta

<div class="frase"><span class="lac">quem</span> precisa de <span class="lac">quê</span>, porque <span class="lac">o que se descobriu</span></div>

A frase vira uma pergunta que abre a ideação — ***"como poderíamos…?"*** — sem já trazer a resposta:

<div class="grid2">
<div class="card red"><b class="t">Já escolheu a solução</b><i>"Como poderíamos <b>cadastrar</b> os itens?"</i><span class="pe">a resposta veio dentro da pergunta: um formulário</span></div>
<div class="card grn"><b class="t">Deixa espaço</b><i>"Como poderíamos ajudar alguém a <b>reconhecer</b> o que perdeu?"</i><span class="pe">uma foto, uma vitrine na portaria — ou nenhum sistema</span></div>
</div>

---

## Abrir e fechar: o duplo diamante

<div class="dd">
<div class="ponta">o<br>pedido</div>
<div class="dia"><div class="cap" style="color:var(--vio)">1º · o PROBLEMA</div>
<div class="losango vio"><div class="dentro"><div><b>abre</b><br>empatia</div><div><b>fecha</b><br>definição</div></div></div></div>
<div class="dia"><div class="cap" style="color:var(--ind)">2º · a SOLUÇÃO</div>
<div class="losango ind"><div class="dentro"><div><b>abre</b><br>ideação</div><div><b>fecha</b><br>protótipo<br>e teste</div></div></div></div>
<div class="ponta">a<br>solução</div>
</div>

<p class="legenda">O erro mais comum é <b>pular o primeiro diamante</b>: tratar o pedido como definição e já gerar soluções para um problema que ninguém verificou.</p>
<p class="fonte">Proposto pelo Design Council britânico, em meados dos anos 2000.</p>

---

## 2009: as fotos de Nova York

<div class="linha">
<div class="passo" style="border-color:var(--sla);background:var(--sla-s)"><span class="hora">US$ 200</span>por semana de receita, e sem crescer</div>
<div class="seta">→</div>
<div class="passo" style="border-color:var(--amb);background:var(--amb-s)"><span class="hora">os anúncios</span>de Nova York, a cidade que importava: <b>fotos ruins</b>, de celular</div>
<div class="seta">→</div>
<div class="passo" style="border-color:var(--vio);background:var(--vio-s)"><span class="hora">porta em porta</span>em vez de um e-mail com dicas: <b>câmera alugada</b> — e ouvir os anfitriões</div>
<div class="seta">→</div>
<div class="passo" style="border-color:var(--grn);background:var(--grn-s)"><span class="hora">× 2</span>a receita semanal, <b>uma semana depois</b></div>
</div>

<p class="legenda">Airbnb. A empatia aconteceu <b>fora da sala</b>, na casa de quem usava o produto — e o protótipo <b>não tinha uma linha de código</b>: era uma câmera alugada.</p>
<p class="fonte">Fonte: Joe Gebbia, cofundador, à First Round Review.</p>

---

<!-- _class: lead -->

## ⚠️ Design Thinking não é

dinâmica de post-it.

Se depois da oficina
ninguém mudou de ideia sobre nada,

ou o problema já estava claro,
ou a etapa de **empatia**
não foi feita para valer.

---

## MVP: o menor produto que ensina alguma coisa

<div class="grid3">
<div class="card ind"><b class="t">Produto</b>algo que alguém <b>usa de verdade</b> — não uma tela para mostrar</div>
<div class="card ind"><b class="t">Mínimo</b>pequeno o bastante para ser <b>barato</b></div>
<div class="card ind"><b class="t">Viável</b>completo o bastante para produzir <b>aprendizado real</b></div>
</div>

<p class="legenda">Eric Ries, <i>A startup enxuta</i> (2011): o MVP permite <b>aprender o máximo sobre os clientes com o mínimo de esforço</b>. O que ele entrega não é funcionalidade — é aprendizado.</p>
<p class="fonte"><i>Enxuta</i> é a tradução de <i>lean</i>: o mesmo enxugar do título desta aula.</p>

---

## Construir, medir, aprender

Cada volta termina numa **decisão**: perseverar na ideia, ou **mudar de direção** — o que as startups chamam de *pivotar*.

![w:1140](img/ciclo-mvp.svg)

<p class="legenda">Percorre-se nesse sentido, mas <b>planeja-se ao contrário</b>: o que precisamos aprender → o que medir → o menor produto que gera essa medida.</p>

---

## As três partes obrigatórias — no marketplace

<div class="partes">
<div class="campo ind">Hipótese</div><div class="valor">prestadores autônomos aceitam pagar comissão em troca de encontrar clientes</div>
<div class="campo amb">Como medir</div><div class="valor">30 prestadores cadastrados e 10 serviços concluídos em 8 semanas</div>
<div class="campo red">Critério de decisão</div><div class="valor">menos de 5 serviços concluídos → o problema não é encontrar cliente; <b>mudamos de direção</b></div>
</div>

<p class="legenda"><b>A terceira quase nunca existe</b> — e precisa ser combinada <b>antes</b>, com quem paga. Depois do resultado, qualquer régua parece escolhida para justificar o que já se queria.</p>

---

<!-- _class: lead -->

## Se você não consegue completar

*"se acontecer X,
a gente muda de direção"*,

**não é MVP** —
é a entrega 1 de 8,
com nome bonito.

---

## Qual número decide?

<div class="grid2">
<div class="card red"><span class="num">30 cadastros</span><b>Métrica de vaidade:</b> só sobe, é bom de mostrar — e não diz se a hipótese está certa. Cadastrar-se é grátis.</div>
<div class="card grn"><span class="num">10 serviços</span><b>Métrica que decide:</b> concluídos, com comissão paga. É o comportamento que a hipótese prevê.</div>
</div>

<p class="legenda">Por isso o critério de decisão do marketplace usa <b>os serviços concluídos</b>, e não os cadastros.</p>

---

## Quatro jeitos de fazer um MVP

<div class="escala"></div>
<div class="escala-rot"><span>mais barato</span><span>mais caro</span></div>

<div class="grid4">
<div class="card mini ind"><b class="t">Página ou vídeo</b>descreve o produto que ainda não existe e mede quem pede para entrar<span class="pe">testa o <b>interesse</b> — não o uso</span></div>
<div class="card mini ind"><b class="t">Concierge</b>o serviço é feito à mão, e o cliente <b>sabe</b> disso<span class="pe">testa se o serviço <b>resolve</b> o problema</span></div>
<div class="card mini ind"><b class="t">Mágico de Oz</b>parece pronto; por trás, é tudo manual — e o cliente <b>não sabe</b><span class="pe">testa se as pessoas <b>usam e pagam</b></span></div>
<div class="card mini ind"><b class="t">Uma função só</b>o produto real, com a única função que a hipótese precisa<span class="pe">testa o <b>uso de verdade</b></span></div>
</div>

<p class="legenda">O marketplace pode começar como <b>concierge</b>: formulário, grupo de mensagens e os fundadores intermediando à mão — sem o fluxo de disputa, a parte mais cara.</p>

---

## Dois MVPs de antes de o nome ficar famoso

<div class="grid2">
<div class="card ind"><span class="num">5 mil → 75 mil</span>inscritos na lista de espera do <b>Dropbox</b>, numa noite — por causa de um <b>vídeo</b> de poucos minutos, com o produto ainda inacabado<span class="pe">2008 · vídeo</span></div>
<div class="card vio"><span class="num">0 pares</span>em estoque na <b>Zappos</b>, em 1999: fotos de sapatos de lojas da cidade; a cada pedido, o fundador ia à loja, comprava e enviava<span class="pe">1999 · Mágico de Oz</span></div>
</div>

<p class="legenda">Os dois testaram a hipótese <b>antes</b> de construir a parte cara — sincronizar arquivos sem falhar, e um estoque de sapatos.</p>

---

## O que MVP não é

| Chamam de MVP | É na verdade |
|---|---|
| a primeira fatia do plano | **entrega incremental** — legítima, e não testa nada |
| a versão com menos funcionalidades | **escopo reduzido** |
| o protótipo de tela | **protótipo** — ninguém usa de verdade |
| a versão feita às pressas | **dívida técnica** |

**Incremental supõe o plano certo e o executa em pedaços. O MVP suspeita do plano e o testa.**

---

## Lean: o que o cliente não pagaria para ter?

Vem do sistema de produção da **Toyota**, no Japão do pós-guerra — sem dinheiro para estoque. O nome *lean*, enxuto, veio em 1990.

<div class="grid3">
<div class="card teal"><b class="t">Valor</b>o que o cliente reconhece e pagaria para ter — <b>quem define é ele</b>, não o time</div>
<div class="card teal"><b class="t">Fluxo de valor</b>o caminho inteiro, do pedido à entrega — com as etapas <b>e as filas</b> entre elas</div>
<div class="card red"><b class="t">Desperdício</b>tudo o que, nesse caminho, consome tempo ou esforço <b>sem virar valor</b> — e sai</div>
</div>

---

## Os sete desperdícios em software

<div class="grid4">
<div class="card dsp teal"><span class="fab">na fábrica: estoque</span><b class="t">Trabalho parcialmente feito</b>cinco itens começados, nenhum entregue</div>
<div class="card dsp red"><span class="fab">superprodução</span><b class="t">Funcionalidade não usada</b>o relatório que ninguém abre — <b>a mais cara e a menos visível</b></div>
<div class="card dsp teal"><span class="fab">processamento extra</span><b class="t">Processo extra</b>o documento que ninguém lê, a aprovação que ninguém confere</div>
<div class="card dsp teal"><span class="fab">transporte</span><b class="t">Troca de contexto</b>a pessoa em três projetos, produzindo pouco em todos</div>
<div class="card dsp amb"><span class="fab">espera</span><b class="t">Espera</b>item pronto há seis dias esperando revisão</div>
<div class="card dsp teal"><span class="fab">movimentação</span><b class="t">Passagem de bastão</b>quem analisou não é quem constrói — e o que se sabia se perde</div>
<div class="card dsp teal"><span class="fab">defeito</span><b class="t">Defeito e retrabalho</b>o que volta porque não estava na Definição de Pronto</div>
<div class="card dsp" style="background:#fff;border-style:dashed"><b class="t" style="color:var(--sla)">De onde vem</b>Mary e Tom Poppendieck, 2003: os sete da fábrica, traduzidos para o software</div>
</div>

<p class="legenda" style="font-size:23px">Ninguém reclama de um relatório que não usa: ele só aparece se alguém <b>medir o uso</b> — Aula 12.</p>

---

## O fluxo que revela a espera

<div class="fluxo">
<div class="seg trab" style="flex:2">Análise<br><b>2 dias</b></div>
<div class="seg esp" style="flex:4">espera<br><b>4 dias</b></div>
<div class="seg trab" style="flex:1">Revisão<br><b>1</b></div>
<div class="seg esp" style="flex:3">espera<br><b>3 dias</b></div>
<div class="seg trab" style="flex:1">Publicar<br><b>1</b></div>
</div>
<div class="chave"></div>
<div class="chave-rot">11 dias: o prazo que o cliente percebe</div>

<div class="grid3">
<div class="card teal"><span class="num">4 dias</span>de trabalho</div>
<div class="card amb"><span class="num">7 dias</span>de espera — sem esforço de ninguém</div>
<div class="card red"><span class="num">36%</span>eficiência do fluxo: 4 ÷ 11</div>
</div>

<p class="legenda">Contratar para as etapas de trabalho <b>quase não muda nada</b>. Atacar a espera corta o prazo pela metade.</p>

---

## Puxar, em vez de empurrar

<div class="grid2">
<div class="card red"><b class="t">Empurrar</b>cada etapa joga o que terminou na fila da seguinte e começa outra coisa.<span class="pe" style="font-size:24px">As filas crescem — e ninguém percebe, porque <b>todo mundo está ocupado</b>.</span></div>
<div class="card grn"><b class="t">Puxar</b>com um <b>limite de trabalho em andamento</b>, a etapa seguinte puxa quando tem espaço.<span class="pe" style="font-size:24px">Com a fila cheia, para-se de começar — e vai-se <b>ajudar a terminar</b>.</span></div>
</div>

<p class="legenda">O time <b>começa menos e termina mais</b>. A pergunta do Lean não é <i>"todo mundo está ocupado?"</i> — é <b><i>"o item está andando?"</i></b></p>

---

## Six Sigma: o problema é a variação

Nasceu na **Motorola**, em 1986. Sigma (σ) é o desvio-padrão: um processo "seis sigma" varia tão pouco que tem no máximo **3,4 defeitos por milhão**.

<div class="grid2">
<div class="card teal"><b class="t">Lean</b>ataca o <b>desperdício</b><span class="pe" style="font-size:24px"><i>o que aqui não vira valor?</i><br>exige ver o fluxo inteiro</span></div>
<div class="card sky"><b class="t">Six Sigma</b>ataca a <b>variação</b><span class="pe" style="font-size:24px"><i>por que o resultado oscila tanto?</i><br>exige dados suficientes para medir</span></div>
</div>

<p class="legenda">Juntos, são o <b>Lean Six Sigma</b>: primeiro se tira o que sobra, depois se estabiliza o que ficou.</p>

---

## A média engana — a Ouvidoria em operação

Prazo legal de resposta: **30 dias** (Lei 13.460/2017). Dois órgãos, com a **mesma média** de 14 dias:

<div class="plot">
<div class="rot" style="color:var(--teal)">Obras</div>
<div class="pista">
<span class="media"></span><span class="prazo"></span>
<span class="tx" style="left:32.5%;color:#475569">média · 14 dias</span><span class="tx" style="left:68%;color:var(--red)">prazo · 30 dias</span>
<span class="d o" style="left:24.44%;bottom:6px"></span>
<span class="d o" style="left:26.67%;bottom:6px"></span><span class="d o" style="left:26.67%;bottom:32px"></span>
<span class="d o" style="left:28.89%;bottom:6px"></span><span class="d o" style="left:28.89%;bottom:32px"></span>
<span class="d o" style="left:31.11%;bottom:6px"></span><span class="d o" style="left:31.11%;bottom:32px"></span><span class="d o" style="left:31.11%;bottom:58px"></span>
<span class="d o" style="left:33.33%;bottom:6px"></span><span class="d o" style="left:33.33%;bottom:32px"></span>
<span class="d o" style="left:35.56%;bottom:6px"></span>
<span class="d o" style="left:37.78%;bottom:6px"></span>
</div>
<div class="rot" style="color:var(--sky)">Saúde</div>
<div class="pista">
<span class="media"></span><span class="prazo"></span>
<span class="d s" style="left:4.44%;bottom:6px"></span>
<span class="d s" style="left:6.67%;bottom:32px"></span>
<span class="d s" style="left:11.11%;bottom:6px"></span>
<span class="d s" style="left:13.33%;bottom:32px"></span>
<span class="d s" style="left:17.78%;bottom:6px"></span>
<span class="d s" style="left:20%;bottom:32px"></span>
<span class="d s" style="left:22.22%;bottom:6px"></span>
<span class="d s" style="left:26.67%;bottom:6px"></span>
<span class="d s" style="left:33.33%;bottom:6px"></span>
<span class="d s" style="left:44.44%;bottom:6px"></span>
<span class="d x" style="left:75.56%;bottom:6px"></span>
<span class="d x" style="left:88.89%;bottom:6px"></span>
</div>
<div></div>
<div class="eixo"><span style="left:0%">0</span><span style="left:22.22%">10</span><span style="left:44.44%">20</span><span style="left:66.67%">30</span><span style="left:88.89%">40 dias</span></div>
</div>

<p class="legenda">O cidadão não recebe a média: <b>recebe o caso dele</b>. A Saúde passa do prazo em 1 de cada 6 — e a média não mostra.</p>

---

## DMAIC: o roteiro do Six Sigma

<div class="linha">
<div class="passo" style="border-color:var(--sky);background:var(--sky-s)"><span class="hora">Definir</span><i>qual é o problema, em número?</i><span class="sai">1 em 6 da Saúde passa dos 30 dias</span></div>
<div class="seta">→</div>
<div class="passo" style="border-color:var(--sky);background:var(--sky-s)"><span class="hora">Medir</span><i>quanto, onde, quando?</i><span class="sai">seis meses, por órgão, canal e assunto</span></div>
<div class="seta">→</div>
<div class="passo" style="border-color:var(--sky);background:var(--sky-s)"><span class="hora">Analisar</span><i>o que explica a variação?</i><span class="sai">as que foram ao órgão errado e voltaram à triagem</span></div>
<div class="seta">→</div>
<div class="passo" style="border-color:var(--sky);background:var(--sky-s)"><span class="hora">Melhorar</span><i>que mudança ataca a causa?</i><span class="sai">assuntos por órgão na triagem</span></div>
<div class="seta">→</div>
<div class="passo" style="border-color:var(--sky);background:var(--sky-s)"><span class="hora">Controlar</span><i>como garantir que não volta?</i><span class="sai">reencaminhamento toda semana, com alerta</span></div>
</div>

<p class="legenda">⚠️ <b>Six Sigma exige processo estável e repetido.</b> Cabe na <b>operação</b> — chamados, implantações, incidentes —, não no projeto único que constrói o sistema.</p>

---

## Qual usar quando

![w:1040](img/qual-usar.svg)

<p class="legenda">A saída que mais se esquece: quem entrega bem <b>não precisa de nenhuma das três</b>.</p>

---

<!-- _class: lead -->

## ⚠️ As três podem adiar decisão

Uma oficina marcada para daqui a três semanas,
num projeto que já sabe o problema,
é procrastinação com boa apresentação.

O teste: **que decisão vai mudar**
com o resultado?
Se ninguém nomeia uma, é ritual.

---

<!-- _class: lead -->

## ➡️ Próxima aula

**Aula 09 — Controle de versão e configuração**

Fecha o Bloco 2.

O Bloco 3 sai do plano e entra no código:
o que mudou, quem mudou —
e como voltar ao que funcionava.
