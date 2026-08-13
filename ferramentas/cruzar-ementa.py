#!/usr/bin/env python3
"""
Cruza os 48 tópicos da ementa oficial contra o conteúdo das 16 aulas.

    python3 ferramentas/cruzar-ementa.py

Existe porque foi este cruzamento que motivou a reformulação de 13/08/2026:
a versão anterior do curso cobria 16 dos 48 tópicos, com a Unidade 3 zerada.

⚠️ DUAS ARMADILHAS, aprendidas na prática:

1. **Presença de palavra não é cobertura de tópico.** Na primeira rodada, 5
   dos 19 "cobertos" eram falso positivo: "risco" como palavra comum, `UI`
   como nome de participante num diagrama, "quatro valores" falando de
   atributo. O script aponta candidatos; o veredito se lê no contexto.

2. **Ausência de palavra não é ausência de tópico.** Na rodada final, 3
   tópicos apareceram como ausentes só porque a aula usa outro vocabulário:
   "matriz probabilidade × impacto" em vez de "matriz de risco", "como se
   levanta risco" em vez de "mapeamento". Os regexes abaixo já foram
   ajustados ao vocabulário real do curso — se uma aula for reescrita com
   outras palavras, ajuste-os junto.

Cada tópico vive em EXATAMENTE UMA aula, por desenho da grade (3 tópicos por
aula). Concentração numa aula só é o esperado, não um aviso.
"""

import re, pathlib, collections

RAIZ = pathlib.Path('/Users/jreluiz/PycharmProjects/curso-projeto-software')
arquivos = sorted(RAIZ.glob('bloco-*/aula-*/README.md'))
textos = {}
for f in arquivos:
    aula = re.search(r'aula-(\d+)', str(f)).group(1)
    textos[aula] = f.read_text(encoding='utf-8').lower()

TOPICOS = [
 ("U1","Equipe do projeto e matriz de responsabilidades", r"matriz de responsabilidade|\braci\b|equipe do projeto"),
 ("U1","Importância da gestão de projetos", r"gerir um projeto|gest(ã|a)o de projeto|gerenciamento de projeto|gerir um projeto de software"),
 ("U1","Problemas na gestão de projetos, conflitos", r"conflito"),
 ("U1","Ciclo de vida clássico", r"cascata"),
 ("U1","Ciclo de vida incremental e iterativo", r"incremental|iterativ"),
 ("U1","Ciclo de vida preditivo e adaptativo", r"preditivo|adaptativo"),
 ("U1","Processo de encerramento e avaliação", r"encerramento"),
 ("U1","Processo de execução e controle", r"execu(ç|c)(ã|a)o e controle|monitoramento e controle"),
 ("U1","Processo de iniciação e planejamento", r"inicia(ç|c)(ã|a)o|termo de abertura"),
 ("U1","Decisões sobre a arquitetura de software", r"\badr\b|decis(ã|a)o de arquitetura|decis(õ|o)es de arquitetura"),
 ("U1","Estilos e padrões arquitetônicos", r"camadas|\bmvc\b|monolito|microsservi"),
 ("U1","O que é arquitetura de software", r"arquitetura de software|o que é arquitetura|decis(õ|o)es difíceis de"),
 ("U2","Manifesto Ágil", r"manifesto"),
 ("U2","Princípios da metodologia ágil", r"princ(í|i)pios? (do|da|de) (ágil|agilidade|manifesto)|doze princ"),
 ("U2","Valores da metodologia ágil", r"quatro valores|valores do manifesto"),
 ("U2","Artefatos do Scrum", r"artefato do scrum|artefatos do scrum|product backlog|sprint backlog|incremento"),
 ("U2","Eventos do Scrum", r"sprint|daily|retrospectiva|planning|review"),
 ("U2","Responsabilidades do Scrum", r"scrum master|product owner|time de desenvolvimento|dev team"),
 ("U2","Design Thinking em projetos de TI", r"design thinking"),
 ("U2","Lean e Six Sigma", r"\blean\b|six sigma"),
 ("U2","MVP — Minimum Viable Product", r"\bmvp\b|produto m(í|i)nimo vi(á|a)vel"),
 ("U2","Papel do gerente de projetos", r"gerente de projeto"),
 ("U2","Papel do Product Owner", r"product owner"),
 ("U2","Responsabilidade dos stakeholders", r"stakeholder|interessad"),
 ("U3","Mapeamento de risco", r"como se levanta risco|levanta risco|identificar risco|registro de riscos"),
 ("U3","Matriz de risco", r"matriz de risco|matriz probabilidade|probabilidade × impacto"),
 ("U3","Natureza do risco", r"\brisco"),
 ("U3","Maturidade em projeto de software", r"maturidade|\bcmmi\b|mps\.?br"),
 ("U3","Métricas de qualidade", r"m(é|e)trica"),
 ("U3","Sistema de qualidade do software", r"sistema de qualidade|iso ?9|iso ?25|garantia da qualidade|\bsqa\b"),
 ("U3","Documentação como elemento de qualidade", r"documenta(ç|c)(ã|a)o"),
 ("U3","Por que e quando documentar", r"documentar"),
 ("U3","Riscos pela ausência de documentação", r"aus(ê|e)ncia de documenta|sem documenta(ç|c)(ã|a)o"),
 ("U3","Ferramentas para modelos ágeis", r"\bjira\b|trello|azure boards|quadro kanban"),
 ("U3","Ferramentas para modelos sequenciais", r"gantt|ms project|\beap\b|\bwbs\b|cronograma"),
 ("U3","Gestão da comunicação", r"gest(ã|a)o da comunica|plano de comunica"),
 ("U4","Controle de versão", r"controle de vers(ã|a)o|versionamento"),
 ("U4","Processos de entrega contínua", r"entrega cont(í|i)nua"),
 ("U4","Rastreamento de mudanças e configuração", r"ger(ê|e)ncia de configura|gest(ã|a)o de configura|rastreabilidade"),
 ("U4","Continuous Integration / Continuous Deployment", r"integra(ç|c)(ã|a)o cont(í|i)nua|ci/cd"),
 ("U4","Gestão de mudanças e observabilidade", r"observabilidade"),
 ("U4","Manutenção e evolução do software", r"manuten(ç|c)(ã|a)o|evolu(ç|c)(ã|a)o do software"),
 ("U4","Análise e projeto de interfaces", r"projeto de interface|interface de usu(á|a)rio|\bui\b"),
 ("U4","Elementos do projeto da experiência do usuário", r"experi(ê|e)ncia do usu(á|a)rio|\bux\b"),
 ("U4","Projeto de interação de usuário", r"projeto de intera|fluxo de intera|fluxo, estado e retorno"),
 ("U4","Paradigmas ESG", r"\besg\b|environmental, social"),
 ("U4","ITIL, COBIT, PMI e PMBOK", r"\bitil\b|\bcobit\b|\bpmbok\b|\bpmi\b"),
 ("U4","Governança de TI", r"governan(ç|c)a"),
]

print(f"{'':2} {'TÓPICO':52} {'AULAS':22} STATUS")
print("─"*104)
resumo = collections.Counter()
por_unidade = collections.defaultdict(lambda: [0,0,0])
for uni, nome, rx in TOPICOS:
    hits = {a: len(re.findall(rx, t)) for a, t in textos.items()}
    hits = {a: n for a, n in hits.items() if n}
    total = sum(hits.values())
    aulas = ",".join(sorted(hits))
    if total == 0:
        st, idx = "❌ AUSENTE", 2
    elif total <= 2:
        st, idx = "⚠️  MENÇÃO", 1
    else:
        st, idx = "✅ COBERTO", 0
    resumo[st] += 1
    por_unidade[uni][idx] += 1
    print(f"{uni:2} {nome:52} {aulas:22} {st} ({total})")

print("─"*104)
for u in ("U1","U2","U3","U4"):
    c, m, a = por_unidade[u]
    print(f"{u}: ✅ {c:2}   ⚠️ {m:2}   ❌ {a:2}   (de 12)")
print(f"\nTOTAL: ✅ {resumo['✅ COBERTO']}   ⚠️ {resumo['⚠️  MENÇÃO']}   ❌ {resumo['❌ AUSENTE']}   (de {len(TOPICOS)})")
