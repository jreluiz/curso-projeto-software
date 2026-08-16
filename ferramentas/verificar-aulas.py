#!/usr/bin/env python3
"""
Verificador da régua do curso-projeto-software.

Portado do curso-modelagem-dados em 12/08/2026, na reformulação pela ementa
oficial. O que mudou em relação ao original: 5 exercícios em vez de 3, e as
listas de vocabulário são as deste curso — o que se barra aqui é o resto da
grade antiga (UML, requisitos, POO), não prática de SQL.

Uso:
    python3 ferramentas/verificar-aulas.py [caminho]
    python3 ferramentas/verificar-aulas.py --gabarito trilha-gabaritos/curso-projeto-software/bloco-1.md
    python3 ferramentas/verificar-aulas.py . --no-mermaid

Confere as métricas do template, a ordem do fechamento, os links e âncoras
relativos, a renderização de todo bloco Mermaid e o formato das questões.

Existe porque um defeito de formato não pego se repete em 16 arquivos.
"""

import os
import re
import subprocess
import sys
import tempfile

# ─────────────────────────────────────────────────────────────────────────────
# Régua (PLANEJAMENTO.md §5 e §6)
# ─────────────────────────────────────────────────────────────────────────────

LINHAS_MIN, LINHAS_MAX = 180, 220   # calibrado com o professor em 13/08/2026
SECOES_MIN, SECOES_MAX = 4, 7
EXERCICIOS = 5          # este curso mantém 5, sendo o 5º o Desafio 🌶️ (§7)
QUESTOES = 8
DIRETAS, ENADE = 5, 3   # 5 diretas + 3 [ENADE]; TODAS com alternativas a–d (§6)

# A "Entrega" deixou de ser seção de fechamento em 16/08/2026: virou a
# subseção "### 📤 Entrega" DENTRO de "## 🏋️ Exercícios da aula", junto do
# enunciado a que ela se refere. O fechamento passou a ter dois itens.
FECHAMENTO = [
    "## 🏋️ Exercícios da aula",
    "## 🧠 Revisão",
]

# Resto da grade antiga — proibido. A reformulação de 12/08/2026 tirou UML,
# engenharia de requisitos e projeto OO da ementa, e o risco real numa
# reformulação é material velho sobreviver por cópia. Estes marcadores são
# inequívocos: se aparecerem, veio de arraste.
#
# `stateDiagram-v2` e `classDiagram` NÃO estão na mesma situação. O primeiro é
# permitido (§5: ciclo de vida, estados de uma mudança); o segundo não, porque
# diagrama de classes saiu com o Bloco 3 antigo.
GRADE_ANTIGA_PROIBIDA = [
    r"@startuml", r"classDiagram", r"erDiagram",
    r"\bGherkin\b", r"\bINVEST\b", r"\bSOLID\b",
    r"\bincluded?\b\s*×\s*\bextends?\b", r"\bmultiplicidade\b",
]

# Assuntos que saíram da ementa mas podem aparecer de passagem numa frase
# legítima ("o requisito funcional que o cliente pediu"). AVISO, não erro:
# cada ocorrência é conferida à mão. O que se quer pegar é a seção inteira
# sobrevivendo, não a menção isolada.
GRADE_ANTIGA_AVISO = [
    r"\bcasos? de uso\b", r"\bdiagrama de classes\b", r"\bhist[óo]ria de usu[áa]rio\b",
    r"\belicita[çc][ãa]o\b", r"\bacoplamento\b", r"\bcoes[ãa]o\b",
    r"\bpadr[ãa]o de projeto\b", r"\bReserva de Espa[çc]os\b",
]

# Vocabulário de curso aberto. AVISO, não erro: "semestre" e "disciplina"
# podem ser domínio legítimo de um exercício (uma escola, uma faculdade), e
# "disciplina da equipe" é uso legítimo num curso de gestão.
VOCAB_AVISO = [r"\bnota\b", r"\bnotas\b", r"\bprova\b", r"\bbimestre\b",
               r"\bdisciplina\b", r"\bsemestre\b"]

# Formatos de enunciado que este curso NÃO usa (decisão de 13/08/2026). Eles
# são o padrão em banco de questões de ENADE e voltam por hábito de quem
# escreve — daí a checagem explícita.
FORMATO_BANIDO = [
    (r"^\s*(I{1,3}|IV|V)\.\s", "afirmativas em algarismo romano"),
    (r"^\s*PORQUE\s*$", "asserção-razão"),
    (r"é correto apenas o que se afirma em", "complementação múltipla"),
    (r"assinale a (opção|alternativa) correta", "comando de asserção-razão"),
]

# CUIDADO: `gabarito` sozinho é falso positivo. Toda revisão abre com
# "Sem gabarito, de propósito" — a palavra é conteúdo legítimo. O que entrega
# a resposta é o gabarito de verdade: "Gabarito: b", "Resposta correta: c".
REVELA_RESPOSTA = [r"\bgabaritos?\s*:", r"\brespostas?\s+corretas?\b",
                   r"\bresposta\s*:\s*[a-eA-E]\b"]

# Alvos que ainda não existem mas estão previstos no plano de construção.
PREVISTO = re.compile(
    r"aula-(0[5-9]|1[0-6])-|bloco-[234]-|apresentacao/|revisao/|trilha-gabaritos/"
    r"|projetos-para-praticar\.md|artefatos-de-gestao\.md"
)


def problemas_de_aula(caminho, texto):
    """Métricas do template de aula (PLANEJAMENTO.md §5)."""
    p = []
    linhas = texto.split("\n")
    n = len(linhas)

    if not (LINHAS_MIN <= n <= LINHAS_MAX):
        p.append(f"{n} linhas (régua: {LINHAS_MIN}–{LINHAS_MAX})")

    secoes = re.findall(r"^## \d+\.", texto, re.M)
    if not (SECOES_MIN <= len(secoes) <= SECOES_MAX):
        p.append(f"{len(secoes)} seções numeradas (régua: {SECOES_MIN}–{SECOES_MAX})")

    # Objetivos na linha 3: "# Aula XX — Título", vazia, "> 🎯 Objetivos:"
    if len(linhas) < 3 or not linhas[2].startswith("> 🎯 Objetivos:"):
        p.append("linha 3 não é '> 🎯 Objetivos:'")

    # Fechamento na ordem exata
    pos = [texto.find(h) for h in FECHAMENTO]
    faltando = [FECHAMENTO[i] for i, x in enumerate(pos) if x == -1]
    if faltando:
        p.append("fechamento sem: " + ", ".join(faltando))
    elif pos != sorted(pos):
        p.append("fechamento fora de ordem (deve ser Exercícios → Revisão)")

    # EXCEÇÃO 3: não existe cabeçalho "### Exercício N" — é lista numerada sob
    # "## 🏋️ Exercícios da aula". Contar as ocorrências de `exNN.md`.
    n_ex = len(set(re.findall(r"`(ex\d\d\.md)`", texto)))
    if n_ex != EXERCICIOS:
        p.append(f"{n_ex} exercícios (régua: {EXERCICIOS})")

    # EXCEÇÃO 2: todo rodapé tem DOIS links. O 🏠 só aparece nas pontas,
    # ocupando a vaga do vizinho que não existe (Aula 01 no lugar do ⬅️,
    # Aula 16 no lugar do ➡️). Exigir 🏠 em todas acusa 14 aulas sem motivo.
    rodape = next((l for l in reversed(linhas) if l.strip()), "")
    if not re.search(r"[⬅️➡️🏠]", rodape):
        p.append("rodapé ausente")
    elif len(re.findall(r"\]\(", rodape)) != 2:
        p.append(f"rodapé com {len(re.findall(r'](', rodape))} links (deve ter 2)")

    for pat in GRADE_ANTIGA_PROIBIDA:
        for m in set(re.findall(pat, texto, re.I)):
            p.append(f"resto da grade antiga: {m!r}")

    return p


def avisos_de_aula(texto):
    a = []
    for pat in VOCAB_AVISO:
        achados = re.findall(pat, texto, re.I)
        if achados:
            a.append(f"vocabulário de turma: {achados[0]!r} ×{len(achados)}")
    for pat in GRADE_ANTIGA_AVISO:
        achados = re.findall(pat, texto, re.I)
        if achados:
            a.append(f"assunto fora da ementa: {achados[0]!r} ×{len(achados)}")
    return a


def problemas_de_revisao(caminho, texto):
    """
    Formato deste curso: 8 questões, TODAS com alternativas a–d simples.

    As 3 últimas são marcadas [ENADE] e diferem por trazerem um TEXTO-BASE
    com uma situação de projeto antes do comando — não pelo número nem pelo
    tipo de alternativa. Decisão do professor em 13/08/2026.

    NÃO se usa asserção-razão nem complementação múltipla: nada de "I, II e
    III", "PORQUE" ou "é correto apenas o que se afirma em". A checagem
    abaixo barra esses formatos, que voltam facilmente por hábito.

    Como as 8 questões têm o mesmo número de alternativas, a distribuição de
    letras é a regra simples da trilha: 2 de cada por aula, 32 no curso.
    """
    p = []
    ids = re.findall(r"^### (Q-A(\d\d)-(\d\d))", texto, re.M)
    if len(ids) != QUESTOES:
        p.append(f"{len(ids)} questões (régua: {QUESTOES})")
    nomes = [i[0] for i in ids]
    if len(set(nomes)) != len(nomes):
        p.append("IDs repetidos: " + ", ".join(sorted(x for x in nomes if nomes.count(x) > 1)))
    numeros = [int(i[2]) for i in ids]
    if numeros and numeros != list(range(1, len(numeros) + 1)):
        p.append(f"IDs fora de sequência: {numeros}")

    # Uma questão vai do seu "### Q-..." até o próximo (ou o fim)
    blocos = re.split(r"^### Q-A\d\d-\d\d\s*$", texto, flags=re.M)[1:]
    n_diretas = n_enade = 0
    for i, b in enumerate(blocos, 1):
        alts = re.findall(r"^- \*\*([a-d])\)\*\*", b, re.M)
        maiusculas = re.findall(r"^- \*\*([A-E])\)\*\*", b, re.M)
        marcada = "[ENADE]" in b
        qid = nomes[i - 1] if i - 1 < len(nomes) else f"#{i}"

        if maiusculas:
            p.append(f"{qid}: alternativas em MAIÚSCULA — este curso usa a–d em todas")
        if len(alts) != 4:
            p.append(f"{qid}: {len(alts)} alternativas a–d (a régua pede 4)")

        for pat, nome in FORMATO_BANIDO:
            if re.search(pat, b, re.M):
                p.append(f"{qid}: formato banido ({nome}) — use texto-base + comando")
                break
        if marcada:
            n_enade += 1
        else:
            n_diretas += 1

        # Negrito dentro do texto da alternativa entrega a resposta (§6).
        for linha in re.findall(r"^- \*\*[a-d]\)\*\*(.*)$", b, re.M):
            if "**" in linha:
                p.append(f"{qid}: negrito dentro do texto de uma alternativa")
                break

    if blocos:
        if n_diretas != DIRETAS:
            p.append(f"{n_diretas} questões diretas (régua: {DIRETAS})")
        if n_enade != ENADE:
            p.append(f"{n_enade} questões [ENADE] (régua: {ENADE})")

    n_ptr = len(re.findall(r"↩︎", texto))
    if n_ptr != QUESTOES:
        p.append(f"{n_ptr} ponteiros ↩︎ (deve haver {QUESTOES}, um por questão)")

    for pat in REVELA_RESPOSTA:
        if re.search(pat, texto, re.I):
            p.append(f"revela resposta: {pat}")

    return p


# ─────────────────────────────────────────────────────────────────────────────
# EXCEÇÃO 1 — âncora do GitHub
# ─────────────────────────────────────────────────────────────────────────────

def ancora(titulo):
    """
    O GitHub converte CADA espaço num hífen e MANTÉM os acentos.

        "## 4. A especificação — onde está"  ->  "#4-a-especificação--onde-está"

    Hífen duplo, porque o travessão sai e deixa dois espaços no lugar.
    NÃO colapsar espaços (re.sub(r'\\s+', '-')) e NÃO remover acentos: as duas
    coisas geram "âncora inexistente" em massa.
    """
    t = titulo.strip().lower()
    t = re.sub(r"[^\w\s-]", "", t, flags=re.UNICODE)  # tira pontuação, mantém acento
    return "#" + t.replace(" ", "-")                   # cada espaço -> um hífen


def ancoras_de(texto):
    return {ancora(m) for m in re.findall(r"^#{1,6}\s+(.*)$", texto, re.M)}


def sem_blocos_de_codigo(texto):
    """
    Tira os blocos cercados antes de procurar link. O template de aula do
    PLANEJAMENTO.md tem `](../aula-XX-1-tema/README.md)` dentro de uma cerca:
    é exemplo, não link, e conferir acusa quatro alvos inexistentes.
    Cobre cercas de 3 ou mais backticks (a de ````markdown aninha uma ```mermaid).
    """
    return re.sub(r"^(`{3,}).*?^\1\s*$", "", texto, flags=re.M | re.S)


def problemas_de_link(caminho, texto, raiz):
    quebrados, previstos = [], []
    base = os.path.dirname(caminho)
    texto = sem_blocos_de_codigo(texto)
    for alvo in re.findall(r"\]\(([^)\s]+)\)", texto):
        if alvo.startswith(("http://", "https://", "mailto:", "#")):
            if alvo.startswith("#") and alvo not in ancoras_de(texto):
                quebrados.append(f"âncora interna inexistente: {alvo}")
            continue
        arquivo, _, frag = alvo.partition("#")
        destino = os.path.normpath(os.path.join(base, arquivo)) if arquivo else caminho
        if not os.path.exists(destino):
            (previstos if PREVISTO.search(alvo) else quebrados).append(alvo)
            continue
        if frag and destino.endswith(".md"):
            with open(destino, encoding="utf-8") as f:
                if "#" + frag not in ancoras_de(f.read()):
                    quebrados.append(f"{arquivo}#{frag} (âncora inexistente)")
    return quebrados, previstos


# ─────────────────────────────────────────────────────────────────────────────
# Mermaid
# ─────────────────────────────────────────────────────────────────────────────

def achar_mmdc(raiz):
    if os.environ.get("MMDC") and os.path.exists(os.environ["MMDC"]):
        return os.environ["MMDC"]
    for c in (os.path.join(raiz, "ferramentas/node_modules/.bin/mmdc"),
              os.path.join(raiz, "node_modules/.bin/mmdc")):
        if os.path.exists(c):
            return c
    from shutil import which
    return which("mmdc")


def renderizar_mermaid(caminho, texto, mmdc, saida):
    """Devolve (ok, total, erros). Bloco que não renderiza aparece como código cru."""
    blocos = re.findall(r"^```mermaid\s*\n(.*?)^```", texto, re.M | re.S)
    if not blocos or not mmdc:
        return 0, len(blocos), []
    ok, erros = 0, []
    nome = os.path.basename(os.path.dirname(caminho)) or "raiz"
    for i, b in enumerate(blocos, 1):
        with tempfile.NamedTemporaryFile("w", suffix=".mmd", delete=False,
                                         encoding="utf-8") as f:
            f.write(b)
            src = f.name
        png = os.path.join(saida, f"{nome}-{i}.png")
        r = subprocess.run([mmdc, "-i", src, "-o", png, "-b", "white"],
                           capture_output=True, text=True)
        os.unlink(src)
        if r.returncode == 0 and os.path.exists(png):
            ok += 1
        else:
            erros.append(f"bloco {i}: {(r.stderr or r.stdout).strip().splitlines()[-1:]}")
    return ok, len(blocos), erros


# ─────────────────────────────────────────────────────────────────────────────
# Gabarito
# ─────────────────────────────────────────────────────────────────────────────

def verificar_gabarito(gab, raiz):
    """Cobertura nos dois sentidos, distribuição de letras e ponteiros."""
    print(f"\n── Gabarito: {os.path.relpath(gab, raiz)}")
    with open(gab, encoding="utf-8") as f:
        linhas = [l for l in f if re.match(r"\s*Q-A\d\d-\d\d\s*\|", l)]

    registro = {}
    for l in linhas:
        campos = [c.strip() for c in l.split("|")]
        if len(campos) < 4:
            print(f"  ✗ linha malformada: {l.strip()!r}")
            continue
        registro[campos[0]] = {"letra": campos[1], "tipo": campos[2], "ptr": campos[3]}

    # Questões reais nos READMEs de revisão
    reais = {}
    for dirpath, _, arquivos in os.walk(raiz):
        if os.path.basename(dirpath) != "revisao" or "README.md" not in arquivos:
            continue
        with open(os.path.join(dirpath, "README.md"), encoding="utf-8") as f:
            texto = f.read()
        aula = os.path.join(os.path.dirname(dirpath), "README.md")
        titulos = {}
        if os.path.exists(aula):
            with open(aula, encoding="utf-8") as f:
                titulos = {n: t for n, t in re.findall(r"^## (\d+)\. (.*)$",
                                                       f.read(), re.M)}
        for qid in re.findall(r"^### (Q-A\d\d-\d\d)", texto, re.M):
            bloco = texto.split(qid, 1)[1].split("### ", 1)[0]
            ptr = re.search(r"↩︎\s*\*(.*?)\*", bloco)
            alts = set(re.findall(r"^- \*\*([a-eA-E])\)\*\*", bloco, re.M))
            reais[qid] = {"ptr": ptr.group(1) if ptr else "", "alts": alts,
                          "titulos": titulos}

    # Um gabarito de bloco cobre só as aulas daquele bloco. Comparar contra o
    # repositório inteiro acusaria as 96 questões dos outros três blocos.
    aulas_do_bloco = {qid[2:5] for qid in registro}
    reais = {q: v for q, v in reais.items() if q[2:5] in aulas_do_bloco}

    falta_gab = sorted(set(reais) - set(registro))
    falta_rev = sorted(set(registro) - set(reais))
    if falta_gab:
        print(f"  ✗ sem linha no gabarito: {', '.join(falta_gab)}")
    if falta_rev:
        print(f"  ✗ no gabarito mas não na revisão: {', '.join(falta_rev)}")

    erros = 0
    for qid, r in sorted(registro.items()):
        if qid not in reais:
            continue
        if r["letra"] not in reais[qid]["alts"]:
            print(f"  ✗ {qid}: gabarito {r['letra']!r} não está entre as "
                  f"alternativas {sorted(reais[qid]['alts'])}")
            erros += 1
        # Ponteiro do gabarito × ↩︎ do README, string a string
        if r["ptr"] and reais[qid]["ptr"] and r["ptr"] != reais[qid]["ptr"]:
            print(f"  ✗ {qid}: ponteiro divergente\n"
                  f"      gabarito: {r['ptr']}\n"
                  f"      revisão : {reais[qid]['ptr']}")
            erros += 1
        # O título citado existe no README da aula, com o número certo?
        m = re.match(r"Aula \d+, seção (\d+) — (.*)", reais[qid]["ptr"])
        if m:
            num, titulo = m.group(1), m.group(2).strip()
            real = reais[qid]["titulos"].get(num)
            if real is None:
                print(f"  ✗ {qid}: aponta para a seção {num}, que não existe")
                erros += 1
            elif real.strip() != titulo:
                print(f"  ✗ {qid}: título divergente\n"
                      f"      ponteiro: {titulo}\n"
                      f"      seção {num}: {real.strip()}")
                erros += 1

    # Distribuição de letras. Como TODAS as questões têm alternativas a–d
    # (decisão de 13/08/2026), a regra é a simples da trilha: exatamente 2 de
    # cada letra por aula. Diretas e [ENADE] contam juntas.
    por_aula = {}
    for qid, r in registro.items():
        por_aula.setdefault(qid[2:5], {})
        aula = por_aula[qid[2:5]]
        aula[r["letra"]] = aula.get(r["letra"], 0) + 1
    total = {}
    for aula, cont in sorted(por_aula.items()):
        for k, v in cont.items():
            total[k] = total.get(k, 0) + v
        fora = {k: cont.get(k, 0) for k in "abcd" if cont.get(k, 0) != 2}
        marca = "✗" if fora else "·"
        print(f"  {marca} {aula}: " +
              " ".join(f"{k}={cont.get(k, 0)}" for k in "abcd") +
              (f"  ← fora de 2 por letra: {fora}" if fora else ""))
        erros += bool(fora)
    print("  · bloco: " + " ".join(f"{k}={total.get(k, 0)}" for k in "abcd") +
          "   (alvo: 8 de cada por bloco, 32 no curso)")

    print(f"  {'✓' if not (erros or falta_gab or falta_rev) else '✗'} "
          f"{len(registro)} questões no gabarito, {len(reais)} na revisão, {erros} erros")
    return erros + len(falta_gab) + len(falta_rev)


# ─────────────────────────────────────────────────────────────────────────────

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    raiz = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    if "--gabarito" in flags:
        sys.exit(1 if verificar_gabarito(os.path.abspath(args[0]), raiz) else 0)

    alvo = os.path.abspath(args[0]) if args else raiz
    mmdc = None if "--no-mermaid" in flags else achar_mmdc(raiz)
    saida = tempfile.mkdtemp(prefix="mermaid-")

    arquivos = []
    if os.path.isfile(alvo):
        arquivos = [alvo]
    else:
        for dirpath, dirnames, nomes in os.walk(alvo):
            dirnames[:] = [d for d in dirnames if d not in
                           (".git", "node_modules", "__pycache__")]
            arquivos += [os.path.join(dirpath, n) for n in nomes if n.endswith(".md")]
    arquivos.sort()

    n_aulas = n_ok = n_rev = n_rev_ok = 0
    tot_links = tot_quebrados = tot_previstos = 0
    tot_mmd = tot_mmd_ok = 0
    falhou = False

    for caminho in arquivos:
        rel = os.path.relpath(caminho, raiz)
        with open(caminho, encoding="utf-8") as f:
            texto = f.read()

        e_aula = re.search(r"aula-\d\d[^/]*/README\.md$", rel) is not None
        e_rev = re.search(r"aula-\d\d[^/]*/revisao/README\.md$", rel) is not None

        problemas, avisos = [], []
        if e_aula:
            n_aulas += 1
            problemas = problemas_de_aula(caminho, texto)
            avisos = avisos_de_aula(texto)
            if not problemas:
                n_ok += 1
        elif e_rev:
            n_rev += 1
            problemas = problemas_de_revisao(caminho, texto)
            if not problemas:
                n_rev_ok += 1

        quebrados, previstos = problemas_de_link(caminho, texto, raiz)
        tot_links += len(re.findall(r"\]\(([^)\s]+)\)", texto))
        tot_quebrados += len(quebrados)
        tot_previstos += len(previstos)

        ok_m, tot_m, erros_m = renderizar_mermaid(caminho, texto, mmdc, saida)
        tot_mmd += tot_m
        tot_mmd_ok += ok_m

        linhas_saida = ([f"  ✗ {x}" for x in problemas] +
                        [f"  ✗ link quebrado: {x}" for x in quebrados] +
                        [f"  ✗ mermaid {x}" for x in erros_m] +
                        [f"  ⚠ {x}" for x in avisos] +
                        [f"  · previsto: {x}" for x in previstos])
        if problemas or quebrados or erros_m:
            falhou = True
        if linhas_saida:
            print(f"\n{rel}")
            print("\n".join(linhas_saida))
        elif e_aula or e_rev:
            n = len(texto.split("\n"))
            print(f"\n{rel}\n  ✓ OK ({n} linhas)")

    print("\n" + "─" * 70)
    print(f"aulas na régua ......... {n_ok}/{n_aulas}")
    print(f"revisões no formato .... {n_rev_ok}/{n_rev}")
    print(f"links relativos ........ {tot_links} conferidos, "
          f"{tot_quebrados} quebrados, {tot_previstos} previstos")
    if mmdc:
        print(f"blocos Mermaid ......... {tot_mmd_ok}/{tot_mmd} renderizam")
        print(f"                         PNGs em {saida}")
    else:
        print("blocos Mermaid ......... NÃO VERIFICADO — instale com:")
        print("                         npm i --prefix ferramentas "
              "@mermaid-js/mermaid-cli")
        print(f"                         ({tot_mmd} blocos encontrados)")
    sys.exit(1 if falhou else 0)


if __name__ == "__main__":
    main()
