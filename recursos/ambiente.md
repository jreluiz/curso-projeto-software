# 🛠️ Preparação do Ambiente

> 💡 **Boa notícia:** este curso não exige instalar nada. Um editor de texto, o Git que você já usa e uma conta no GitHub. Nenhum compilador, nenhum banco, nenhum servidor.

A má notícia — que é a mesma coisa dita de outro jeito: **não existe ferramenta para culpar aqui.** O que você entrega é raciocínio escrito, e ele nasce e morre no editor.

## 1. O repositório de exercícios

É onde tudo que você produzir vai morar. Uma pasta por aula, do primeiro ao último dia.

1. No GitHub, crie um repositório **público** chamado `exercicios-projeto-software`, marcando "Add a README file";
2. Clone na sua máquina:

```bash
git clone https://github.com/SEU-USUARIO/exercicios-projeto-software.git
cd exercicios-projeto-software
```

3. Teste o ciclo completo agora, sem esperar a primeira aula:

```bash
mkdir aula-00-teste
echo "# Teste" > aula-00-teste/README.md
git add .
git commit -m "Testa o ciclo de entrega"
git push
```

Se o arquivo apareceu no GitHub, seu ambiente de entrega está pronto.

> ⚠️ Repositório **público**. Se estiver privado, ninguém consegue revisar o seu trabalho — e revisão por par é metade do curso.

### Como nomear as coisas

Uma pasta por aula, um arquivo por exercício, tudo em `.md`:

```
exercicios-projeto-software/
├── aula-01-por-que-engenharia-de-software/
│   ├── ex01.md
│   ├── ex02.md
│   ├── ex03.md
│   ├── ex04.md
│   └── ex05.md          ← o desafio 🌶️
├── aula-10-casos-de-uso/
│   ├── ex01.md
│   ├── ex05-diagrama.puml
│   ├── ex05-diagrama.svg
│   └── ex05.md
└── README.md
```

Minúsculas, sem espaço, sem acento nos **nomes de arquivo** — o conteúdo pode e deve ter acento. Nome de arquivo com espaço quebra link e dá trabalho na linha de comando pelo resto da vida.

## 2. Editor de texto com preview de Markdown

Qualquer editor serve, mas você vai escrever muito Markdown com diagramas dentro. O [VS Code](https://code.visualstudio.com/) resolve os dois:

- `Cmd/Ctrl + Shift + V` abre o **preview** do Markdown, já com os diagramas Mermaid renderizados;
- Instale a extensão **Markdown Preview Mermaid Support** se o diagrama aparecer como texto cru;
- A extensão **markdownlint** avisa quando o Markdown está torto antes de o GitHub mostrar isso para todo mundo.

Alternativas sem instalar nada: escrever direto no editor web do GitHub (a aba *Preview* mostra o Mermaid renderizado) ou usar [StackEdit](https://stackedit.io/).

## 3. Mermaid — os diagramas do dia a dia

Do Bloco 3 em diante você escreve diagramas quase toda aula. Eles são **texto dentro do `.md`**, e o GitHub renderiza sozinho:

````markdown
```mermaid
classDiagram
    Espaco "1" --> "0..*" Reserva : recebe
```
````

```mermaid
classDiagram
    Espaco "1" --> "0..*" Reserva : recebe
```

Se o bloco acima aparece como um diagrama para você aqui nesta página, está tudo certo — é exatamente essa renderização que o professor e os colegas vão ver.

**Onde depurar:** [mermaid.live](https://mermaid.live). Cole o diagrama, veja o erro apontado na hora, corrija, copie de volta. É o lugar certo para brigar com a sintaxe — não no *commit*.

> 💡 Erro que todo mundo comete uma vez: esquecer a palavra `mermaid` depois das três crases. Sem ela o GitHub mostra o código-fonte do diagrama, e a página fica com cara de que você entregou pela metade.

O guia do curso, com um exemplo pronto de cada artefato — matriz RACI, EAP, Gantt, matriz de risco, quadro Kanban e burndown —, está em [artefatos de gestão](artefatos-de-gestao.md).

## 4. O que você **não** precisa instalar

Vale dizer explicitamente, porque a lista costuma assustar quem chega:

| Não é necessário | Por quê |
|---|---|
| IDE pesada (IntelliJ, Eclipse) | Não escrevemos código neste curso |
| Java, Node, Python | Idem |
| Banco de dados | Idem |
| Ferramenta paga de diagrama ou de gestão (Lucidchart, Visio, MS Project) | Tudo aqui é texto versionado |
| Astah, StarUML, Enterprise Architect | Bons programas, mas geram binário que não entra em *diff* |
| PlantUML | Saiu do curso junto com os diagramas de casos de uso |

Se você **quiser** rascunhar em ferramenta gráfica — [draw.io](https://app.diagrams.net/) é gratuito — rascunhe à vontade.

> 📏 **Regra do curso:** rascunhe onde quiser, **entregue em texto**. Imagem não faz *diff*, não recebe comentário de linha no Pull Request e envelhece mal.

## ✅ Checklist final

- [ ] Repositório `exercicios-projeto-software` criado, **público** e clonado;
- [ ] Um commit de teste já apareceu no GitHub;
- [ ] Editor com preview de Markdown funcionando;
- [ ] Um diagrama Mermaid de teste renderizou **no GitHub** — copie o da seção 3 e confira na página, não só no editor;
- [ ] [mermaid.live](https://mermaid.live) salvo nos favoritos;
- [ ] Você abriu o [guia de artefatos de gestão](artefatos-de-gestao.md) e viu os seis exemplos renderizados.

---

🏠 [Voltar ao início](../README.md)
