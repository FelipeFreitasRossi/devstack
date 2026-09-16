"""Lições do Módulo 06 — extraídas automaticamente de lessons_content.py."""

LESSON_06_01 = {
    "id": "06-01", "module_id": "06",
    "title": "Estrutura HTML",
    "objectives": [
        "Entender o que é HTML e por que ele estrutura TODAS as páginas web",
        "Conhecer a estrutura obrigatória de um documento HTML",
        "Saber o que vai no head e o que vai no body",
        "Usar meta tags essenciais para SEO e responsividade",
        "Criar seu primeiro arquivo HTML funcional",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "A Base de Toda Página",
            "content": [
                {"type": "text", "value": "**HTML** (HyperText Markup Language) é a **linguagem de marcação** que estrutura **toda página web que existe**. Google, Instagram, iFood, o site do seu banco — tudo é HTML por baixo."},
                {"type": "text", "value": "**Atenção ao detalhe:** HTML **não é linguagem de programação**. Ele não tem `if`, não tem `for`, não toma decisão. É uma **linguagem de marcação** — o nome já diz. Você **descreve** o conteúdo, e o navegador decide como mostrar."},
                {"type": "text", "value": "Pense assim: se o HTML fosse um **documento do Word**, as tags seriam os estilos (título, negrito, lista). Você marca **o que cada coisa é**, e o navegador renderiza."},
                {"type": "text", "value": "**Por que isso importa?** Porque **toda página começa aqui**. React, Vue, Next.js — todos geram HTML no final. Saber HTML é **pré-requisito** para qualquer coisa no frontend."},
                {"type": "text", "value": "**Tags** são os blocos básicos. Elas vêm entre `<` e `>`, quase sempre em pares (abertura + fechamento). Exemplo: `<h1>Título</h1>`. A tag diz ao navegador **o que aquele conteúdo É** — não como ele aparece."},
                {
                    "type": "code",
                    "caption": "Uma tag em detalhes",
                    "value": "<h1>Olá, mundo!</h1>\n ↑    ↑          ↑\n abertura conteúdo fechamento\n\n# A tag <h1> significa 'título de nível 1'.\n# O navegador já sabe que precisa mostrar grande e em negrito.",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "A Estrutura Mínima",
            "content": [
                {"type": "text", "value": "Todo arquivo HTML segue o **mesmo esqueleto**. Você pode decorar em 5 minutos — e vai usar **para sempre**."},
                {
                    "type": "code",
                    "caption": "Estrutura mínima de um HTML",
                    "value": "<!DOCTYPE html>\n<html lang=\"pt-BR\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Minha Página</title>\n</head>\n<body>\n    <h1>Olá, mundo!</h1>\n</body>\n</html>",
                },
                {"type": "text", "value": "**Vamos destrinchar linha por linha:**"},
                {"type": "text", "value": "**`<!DOCTYPE html>`** — avisa ao navegador que esse é um arquivo HTML5 (a versão moderna). Sem isso, o navegador entra em \"modo de compatibilidade\" com versões antigas e coisas estranhas acontecem."},
                {"type": "text", "value": "**`<html lang=\"pt-BR\">`** — é a **tag raiz**. Tudo fica dentro dela. O `lang` diz o idioma da página — importante para leitores de tela (acessibilidade) e para SEO."},
                {"type": "text", "value": "**`<head>`** — contém **metadados** (informações sobre a página). **Nada disso aparece na tela.** É onde ficam: título da aba, charset, CSS, SEO, favicon."},
                {"type": "text", "value": "**`<body>`** — contém o **conteúdo visível**. Tudo que o usuário vê (textos, imagens, botões) fica aqui dentro."},
                {"type": "text", "value": "**Como testar?** Crie um arquivo `index.html` no VS Code, cole o código acima, e abra no navegador (duplo clique). Você verá **\"Olá, mundo!\"** em negrito grande. Esse é seu primeiro HTML funcionando."},
                {"type": "text", "value": "**Como inspecionar?** Abra o navegador, clique com botão direito → **Inspecionar** → aba **Elements**. Você vê o HTML renderizado. Mude um texto diretamente ali e veja o resultado **em tempo real** — essa é a ferramenta que você vai usar **todos os dias** como dev."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Meta Tags Essenciais",
            "content": [
                {"type": "text", "value": "Meta tags são **informações invisíveis** que dizem ao navegador como se comportar. Existem dezenas, mas **3 são obrigatórias** em qualquer página séria."},
                {
                    "type": "code",
                    "caption": "As 3 meta tags essenciais",
                    "value": "<meta charset=\"UTF-8\">  → acentos funcionam\n<meta name=\"viewport\" content=\"width=device-width\">  → mobile\n<meta name=\"description\" content=\"...\">  → SEO",
                },
                {"type": "text", "value": "**`charset=\"UTF-8\"`** — sem isso, \"Olá\" vira \"OlÃ¡\", \"coração\" vira \"coraÃ§Ã£o\". O UTF-8 é o padrão universal que suporta acentos, emojis e praticamente todos os alfabetos do mundo. **Coloque isso sempre, como primeira linha do `<head>`.**"},
                {"type": "text", "value": "**`viewport`** — sem essa linha, seu site no celular aparece **miniaturizado**, como se fosse uma tela de desktop encolhida. Com ela, o navegador ajusta a largura ao tamanho do dispositivo. É o que torna o site **responsivo**."},
                {"type": "text", "value": "**`description`** — é o texto que aparece no **Google** quando alguém pesquisa seu site. Uma boa descrição aumenta cliques. Máximo ~160 caracteres."},
                {
                    "type": "code",
                    "caption": "Exemplo completo de head profissional",
                    "value": "<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <meta name=\"description\" content=\"Curso de programação do zero ao full stack. Python, React, MongoDB e deploy.\">\n    <title>Devstack — Curso Full Stack</title>\n</head>",
                },
                {"type": "text", "value": "**`<title>`** — é o texto que aparece na **aba do navegador**. Também é usado como título no Google. Deve ser curto (~60 caracteres) e descritivo."},
                {"type": "text", "value": "**Dica profissional:** comece **todo** arquivo HTML com esse `<head>` padrão. É um template que você vai repetir em dezenas de projetos. Automatize no VS Code com o atalho `!` + Tab (se tiver a extensão Emmet, que já vem por padrão)."},
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "HTML é linguagem de marcação, não de programação — ele descreve o conteúdo.",
        "Estrutura: <!DOCTYPE html> + <html> + <head> + <body>.",
        "head = metadados (invisíveis); body = conteúdo visível.",
        "As 3 meta tags obrigatórias: charset UTF-8, viewport e description.",
    ],
}


LESSON_06_02 = {
    "id": "06-02", "module_id": "06",
    "title": "Tags Principais e Textos",
    "objectives": [
        "Usar headings h1 a h6 corretamente",
        "Marcar parágrafos, negrito e ênfase",
        "Criar listas ordenadas e não-ordenadas",
        "Entender a hierarquia semântica e por que ela importa",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "Títulos e Hierarquia",
            "content": [
                {"type": "text", "value": "Toda página séria tem uma **hierarquia de títulos** — como um livro tem capítulos, seções e subseções. Em HTML, isso é feito com as tags `<h1>` até `<h6>`."},
                {
                    "type": "code",
                    "caption": "Os 6 níveis de título",
                    "value": "<h1>Título principal</h1>       ← mais importante\n<h2>Subtítulo</h2>\n<h3>Seção da seção</h3>\n<h4>Sub-seção</h4>\n<h5>Menos importante</h5>\n<h6>O mínimo</h6>              ← menos importante",
                },
                {"type": "text", "value": "**Regra de ouro:** use **apenas UM `<h1>` por página**. Ele representa o **assunto principal** daquela página. Os outros (h2, h3...) criam a hierarquia interna."},
                {"type": "text", "value": "**Por que não pular níveis?** Se você usa h1 e depois h4, o navegador até renderiza, mas **quebra a semântica**. Leitores de tela (para deficientes visuais) usam essa hierarquia para navegar. Google também usa para entender a página."},
                {
                    "type": "code",
                    "caption": "Hierarquia correta vs errada",
                    "value": "# ✅ Correto\n<h1>Curso de Python</h1>\n  <h2>Módulo 1 — Básico</h2>\n    <h3>Variáveis</h3>\n    <h3>Funções</h3>\n  <h2>Módulo 2 — Avançado</h2>\n\n# ❌ Errado\n<h1>Curso de Python</h1>\n<h4>Variáveis</h4>          ← pulou h2 e h3!\n<h2>Funções</h2>",
                },
                {"type": "text", "value": "**Dica profissional:** nunca escolha a tag pelo **tamanho visual**. Use `<h1>` porque **aquilo é o título principal**, não porque você quer grande. O tamanho se ajusta via CSS."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Parágrafos, Ênfase e Destaque",
            "content": [
                {"type": "text", "value": "**`<p>`** marca um **parágrafo** de texto. É a tag mais comum em qualquer página com conteúdo. O navegador adiciona espaço automaticamente entre parágrafos."},
                {
                    "type": "code",
                    "caption": "Parágrafos",
                    "value": "<p>Este é o primeiro parágrafo. Ele contém uma ideia completa.</p>\n\n<p>Este é outro parágrafo. Cada <p> é um bloco separado.</p>",
                },
                {"type": "text", "value": "**Atenção:** se você escrever texto solto no HTML sem `<p>`, ele aparece, mas **não fica semanticamente correto**. O navegador até aceita, mas você perde acessibilidade e SEO."},
                {"type": "text", "value": "Para dar **destaque** ao texto, existem tags com significados específicos. Não use `<b>` e `<i>` sem pensar — eles são visuais. Prefira as tags **semânticas**:"},
                {
                    "type": "code",
                    "caption": "Tags de ênfase semântica",
                    "value": "<strong>Negrito</strong>     → importante (leitor de tela fala mais alto)\n<em>Itálico</em>            → ênfase (leitor de tela entona diferente)\n<mark>Marcado</mark>         → destacado (fundo amarelo)\n<code>código</code>          → trecho de código\n<small>texto pequeno</small> → observação secundária\n<del>riscado</del>           → removido\n<ins>sublinhado</ins>        → inserido",
                },
                {"type": "text", "value": "**Diferença entre `<b>` e `<strong>`:** o `<b>` só deixa **visualmente** negrito. O `<strong>` diz que o conteúdo é **importante semanticamente**. Um leitor de tela lê mais devagar e com ênfase. Use `<strong>`."},
                {"type": "text", "value": "**Mesma regra para `<i>` vs `<em>`:** o `<i>` só deixa itálico; `<em>` dá **ênfase semântica**. Use `<em>`."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Listas Ordenadas e Não-Ordenadas",
            "content": [
                {"type": "text", "value": "Listas são usadas para **agrupar itens relacionados**. Existem dois tipos principais, e cada um tem um significado."},
                {
                    "type": "code",
                    "caption": "Listas não-ordenadas (ul)",
                    "value": "<ul>              <!-- unordered list — com bolinhas -->\n    <li>Item 1</li>\n    <li>Item 2</li>\n    <li>Item 3</li>\n</ul>",
                },
                {
                    "type": "code",
                    "caption": "Listas ordenadas (ol)",
                    "value": "<ol>              <!-- ordered list — com números -->\n    <li>Primeiro passo</li>\n    <li>Segundo passo</li>\n    <li>Terceiro passo</li>\n</ol>",
                },
                {"type": "text", "value": "**`<ul>`** (unordered list) = **ordem não importa**. Use para: menu, lista de features, ingredientes, tags."},
                {"type": "text", "value": "**`<ol>`** (ordered list) = **ordem importa**. Use para: passo a passo, receita, ranking, top 10."},
                {"type": "text", "value": "Dentro de qualquer lista, cada item é marcado com **`<li>`** (list item)."},
                {"type": "text", "value": "**Listas podem ser aninhadas** — uma lista dentro de um item de outra lista. Muito comum em menus com submenus."},
                {
                    "type": "code",
                    "caption": "Lista aninhada",
                    "value": "<ul>\n    <li>Frontend\n        <ul>\n            <li>HTML</li>\n            <li>CSS</li>\n            <li>JavaScript</li>\n        </ul>\n    </li>\n    <li>Backend\n        <ul>\n            <li>Python</li>\n            <li>FastAPI</li>\n        </ul>\n    </li>\n</ul>",
                },
                {"type": "text", "value": "**Erro comum:** esquecer de fechar `<li>`. Diferente de outras tags, o `<li>` é um dos poucos que o navegador consegue inferir o fechamento — mas **sempre feche** para não ter surpresas."},
            ],
            "exercise": {
                "id": "06-02-ex1", "title": "Criando um sumário",
                "statement": "Crie uma lista não-ordenada (`<ul>`) com 3 itens (`<li>`): `HTML`, `CSS`, `JavaScript`. Use `print()` no Python para imprimir o código HTML como string, na ordem exata.",
                "starter_code": "# Simule o HTML de uma <ul> com 3 itens\nhtml = \"<ul>\\n\"\n# adicione os 3 <li> e o </ul>\nprint(html)",
                "tests": [{"validation": "output_contains_all", "expected": ["<ul>", "HTML", "CSS", "JavaScript", "</ul>"]}],
                "hint": "Use concatenação: html += '    <li>HTML</li>\\n'",
            },
        },
    ],
    "summary": [
        "h1 é único por página; h2-h6 criam hierarquia interna.",
        "Não pule níveis — use h1 → h2 → h3 em ordem.",
        "strong/em/mark/code dão destaque semântico (diferente de <b>/<i>).",
        "ul = não ordenada; ol = ordenada; li = item.",
    ],
}


LESSON_06_03 = {
    "id": "06-03", "module_id": "06",
    "title": "Links, Imagens e Caminhos",
    "objectives": [
        "Criar links internos, externos e âncoras",
        "Adicionar imagens com alt obrigatório",
        "Entender caminhos relativos e absolutos",
        "Conhecer os principais formatos de imagem",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "Links — A Alma da Web",
            "content": [
                {"type": "text", "value": "**Links** são o que tornam a web **web** — literalmente. Sem links, tudo seria páginas isoladas. Eles são criados com a tag **`<a>`** (âncora) e o atributo **`href`** (referência)."},
                {
                    "type": "code",
                    "caption": "Anatomia de um link",
                    "value": "<a href=\"https://google.com\">Google</a>\n ↑    ↑                     ↑\n tag  atributo              texto visível",
                },
                {"type": "text", "value": "Existem **4 tipos de links** que você vai usar sempre:"},
                {
                    "type": "code",
                    "caption": "Os 4 tipos de links",
                    "value": "# 1. Link externo (outro site)\n<a href=\"https://google.com\">Google</a>\n\n# 2. Link interno (outra página do seu site)\n<a href=\"/sobre\">Sobre</a>\n<a href=\"/blog/post-1.html\">Post 1</a>\n\n# 3. Âncora (mesma página, rola até um ponto)\n<a href=\"#secao-contato\">Ir para contato</a>\n\n# 4. Email e telefone\n<a href=\"mailto:contato@site.com\">Enviar email</a>\n<a href=\"tel:+5511999999999\">Ligar</a>",
                },
                {"type": "text", "value": "**Âncoras** funcionam assim: você adiciona `id=\"secao-contato\"` em algum elemento lá embaixo, e `<a href=\"#secao-contato\">` rola suavemente até ele. É como um índice clicável."},
                {"type": "text", "value": "**Link externo com `target=\"_blank\"`:** abre em nova aba em vez da mesma. Mas atenção: **nunca** use sem `rel=\"noopener noreferrer\"` — por segurança."},
                {
                    "type": "code",
                    "caption": "Link externo seguro",
                    "value": "<a href=\"https://google.com\" target=\"_blank\" rel=\"noopener noreferrer\">\n    Google (abre em nova aba)\n</a>",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Imagens — Muito Mais que src",
            "content": [
                {"type": "text", "value": "**Imagens** usam a tag **`<img>`** — que é **auto-fechada** (não tem `</img>`). Os dois atributos obrigatórios são `src` (origem) e `alt` (texto alternativo)."},
                {
                    "type": "code",
                    "caption": "Imagens básicas",
                    "value": "<img src=\"logo.png\" alt=\"Logo da empresa\">\n<img src=\"https://site.com/foto.jpg\" alt=\"Foto do produto\">",
                },
                {"type": "text", "value": "**`alt` é OBRIGATÓRIO.** Sempre. Sem exceção. Por dois motivos:"},
                {"type": "text", "value": "**1. Acessibilidade:** leitores de tela leem o `alt` para deficientes visuais. Se a imagem não carrega, é o `alt` que aparece. Um usuário cego **depende** dele para entender a imagem."},
                {"type": "text", "value": "**2. SEO:** o Google não \"vê\" imagens — ele lê o `alt`. Uma descrição boa melhora seu rank na busca de imagens."},
                {"type": "text", "value": "**O que escrever no `alt`?** Descreva **o que a imagem mostra**, não \"imagem de...\". Se é decorativa, use `alt=\"\"` (vazio) para o leitor de tela pular."},
                {
                    "type": "code",
                    "caption": "Alt bom vs ruim",
                    "value": "# ❌ Ruim\n<img src=\"grafico.png\" alt=\"imagem\">\n<img src=\"grafico.png\" alt=\"grafico.png\">\n\n# ✅ Bom\n<img src=\"grafico.png\" alt=\"Gráfico de vendas crescendo 30% em 2024\">\n\n# ✅ Imagem decorativa (só visual)\n<img src=\"linha-decorativa.png\" alt=\"\">",
                },
                {"type": "text", "value": "**Formatos de imagem:** use **`.jpg`** para fotos (compressão boa), **`.png`** para imagens com transparência ou texto, **`.svg`** para ícones e logos (vetorial, escala perfeita), **`.webp`** para melhor performance moderna."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Caminhos Relativos e Absolutos",
            "content": [
                {"type": "text", "value": "Quando você referencia arquivos (imagens, CSS, links), precisa entender **caminhos relativos vs absolutos**. Essa é uma das primeiras confusões de quem começa."},
                {
                    "type": "code",
                    "caption": "A estrutura de pastas importa",
                    "value": "projeto/\n├── index.html\n├── sobre.html\n├── img/\n│   ├── logo.png\n│   └── fundo.jpg\n└── css/\n    └── estilo.css",
                },
                {"type": "text", "value": "**Caminho absoluto:** começa do início (raiz ou URL completa). É sempre o mesmo, não importa onde o arquivo está."},
                {
                    "type": "code",
                    "caption": "Caminhos absolutos",
                    "value": "https://site.com/img/logo.png    ← URL completa\n/img/logo.png                     ← a partir da raiz do site",
                },
                {"type": "text", "value": "**Caminho relativo:** parte da **posição atual** do arquivo HTML. É mais flexível — funciona mesmo se você mover a pasta do projeto."},
                {
                    "type": "code",
                    "caption": "Caminhos relativos",
                    "value": "# Do index.html (na raiz do projeto):\n<img src=\"img/logo.png\">\n<img src=\"img/fundo.jpg\">\n<link rel=\"stylesheet\" href=\"css/estilo.css\">\n<a href=\"sobre.html\">Sobre</a>\n\n# Se estiver dentro de uma subpasta (ex: /blog/post.html):\n<img src=\"../img/logo.png\">    ← ../ sobe um nível",
                },
                {"type": "text", "value": "**`../`** significa **\"voltar um nível de pasta\"**. `./` significa **\"a pasta atual\"**. Esses símbolos são atalhos que você vai usar muito."},
                {"type": "text", "value": "**Regra prática:** use **relativo** quando o arquivo faz parte do seu projeto (é portátil), e **absoluto** quando o arquivo está em outro site (não tem como ser relativo)."},
                {"type": "text", "value": "**Erro comum:** misturar barra errada. Em Windows, o explorador mostra `img\\logo.png` com **barra invertida**. Mas em HTML e URLs, é sempre **barra normal** `/`. Sempre."},
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "<a href> cria links: externo, interno, âncora, mailto/tel.",
        "target=\"_blank\" abre em nova aba (use com rel=\"noopener\").",
        "<img src alt> adiciona imagem — alt é OBRIGATÓRIO.",
        "Caminhos: relativo (../) para arquivos do projeto; absoluto para URLs.",
    ],
}


LESSON_06_04 = {
    "id": "06-04", "module_id": "06",
    "title": "Tabelas e Formulários",
    "objectives": [
        "Criar tabelas com thead, tbody e th",
        "Construir formulários com inputs diversos",
        "Usar labels corretamente para acessibilidade",
        "Entender action, method e tipos de input",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "Tabelas Semânticas",
            "content": [
                {"type": "text", "value": "Tabelas servem para **dados tabulares** — planilhas, comparações, listas com colunas. E existem **3 tags principais** que quase todo mundo esquece: `<thead>`, `<tbody>` e `<tfoot>`."},
                {
                    "type": "code",
                    "caption": "Tabela completa e semântica",
                    "value": "<table>\n    <thead>\n        <tr>\n            <th>Nome</th>\n            <th>Idade</th>\n            <th>Cidade</th>\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>Gabrielly</td>\n            <td>18</td>\n            <td>São Carlos</td>\n        </tr>\n        <tr>\n            <td>Ana</td>\n            <td>25</td>\n            <td>São Paulo</td>\n        </tr>\n    </tbody>\n    <tfoot>\n        <tr>\n            <td colspan=\"3\">Total: 2 pessoas</td>\n        </tr>\n    </tfoot>\n</table>",
                },
                {"type": "text", "value": "**Anatomia da tabela:**"},
                {
                    "type": "code",
                    "caption": "Cada tag tem um papel",
                    "value": "<table>  → a tabela inteira\n<thead>  → cabeçalho (títulos das colunas)\n<tbody>  → corpo (dados)\n<tfoot>  → rodapé (totais, resumos)\n<tr>     → linha (table row)\n<th>     → célula de cabeçalho (bold, centralizado)\n<td>     → célula de dado comum",
                },
                {"type": "text", "value": "**Por que usar thead/tbody e não só tr?** Porque melhora a **semântica** (leitores de tela navegam melhor), facilita o **CSS** (você pode estilizar cabeçalho e corpo separadamente) e ajuda no **SEO**."},
                {"type": "text", "value": "**`colspan` e `rowspan`** permitem que uma célula ocupe **várias colunas ou linhas**. `colspan=\"3\"` = ocupa 3 colunas. `rowspan=\"2\"` = ocupa 2 linhas."},
                {"type": "text", "value": "**⚠️ Cuidado:** **nunca use tabelas para layout**. Isso era prática nos anos 2000, mas hoje é considerado **anti-padrão**. Layout se faz com **Flexbox e Grid** (que você verá depois). Tabelas são **só para dados tabulares**."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Formulários — A Porta de Entrada do Usuário",
            "content": [
                {"type": "text", "value": "Formulários são onde o usuário **interage** com o site: login, cadastro, contato, busca, checkout. Sem eles, a web seria só leitura."},
                {
                    "type": "code",
                    "caption": "Formulário completo",
                    "value": "<form action=\"/cadastrar\" method=\"post\">\n    <label for=\"nome\">Nome:</label>\n    <input type=\"text\" id=\"nome\" name=\"nome\" required>\n\n    <label for=\"email\">Email:</label>\n    <input type=\"email\" id=\"email\" name=\"email\" required>\n\n    <label for=\"senha\">Senha:</label>\n    <input type=\"password\" id=\"senha\" name=\"senha\" minlength=\"8\">\n\n    <button type=\"submit\">Enviar</button>\n</form>",
                },
                {"type": "text", "value": "**`<form>`** envolve tudo. Os dois atributos mais importantes:"},
                {
                    "type": "code",
                    "caption": "action e method",
                    "value": "action=\"/cadastrar\"   → para qual URL enviar os dados\nmethod=\"post\"          → como enviar (GET ou POST)",
                },
                {"type": "text", "value": "**`method=\"GET\"`** manda os dados na URL como query string (`/busca?q=python`). Bom para **buscas**, porque a URL fica compartilhável."},
                {"type": "text", "value": "**`method=\"POST\"`** manda os dados no body (invisível na URL). Use para **login, cadastro, qualquer coisa sensível**."},
                {"type": "text", "value": "**`<label>` é essencial.** Ele conecta o texto ao input via `for`/`id`. Isso melhora a UX (clicar no label foca o input) e é **obrigatório para acessibilidade** (leitores de tela precisam desse vínculo)."},
                {
                    "type": "code",
                    "caption": "Label conectado corretamente",
                    "value": "<label for=\"email\">Email:</label>\n<input type=\"email\" id=\"email\">\n            ↑            ↑\n          conectados pelo id",
                },
                {"type": "text", "value": "**Erro comum:** usar `<label>` sem `for` ou com `for` que não bate com nenhum `id`. Sem essa conexão, o label não faz nada — nem clicável, nem acessível."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Tipos de Input",
            "content": [
                {"type": "text", "value": "O HTML5 trouxe **muitos tipos de input** que já têm validação e teclado especializado no mobile. Usar o tipo certo é **obrigatório** para boa UX."},
                {
                    "type": "code",
                    "caption": "Os tipos mais usados",
                    "value": "<input type=\"text\">      → texto livre\n<input type=\"email\">     → valida formato de email\n<input type=\"password\">  → esconde os caracteres\n<input type=\"number\">    → só números\n<input type=\"tel\">       → teclado numérico no celular\n<input type=\"date\">      → seletor de data\n<input type=\"checkbox\">  → caixa de marcar (múltipla escolha)\n<input type=\"radio\">     → botão de escolha única\n<input type=\"file\">      → upload de arquivo\n<input type=\"color\">     → seletor de cor\n<input type=\"range\">     → slider de valor\n<input type=\"search\">    → campo de busca",
                },
                {"type": "text", "value": "**Por que o tipo importa?** No celular, `type=\"email\"` mostra o teclado com `@`. `type=\"number\"` mostra só números. `type=\"tel\"` mostra teclado numérico. Isso **reduz erros** e melhora a experiência."},
                {"type": "text", "value": "**Validação HTML5 nativa** — sem escrever JavaScript, você já ganha validação:"},
                {
                    "type": "code",
                    "caption": "Atributos de validação",
                    "value": "<input type=\"text\" required>              → obrigatório\n<input type=\"text\" minlength=\"2\">          → mínimo 2 caracteres\n<input type=\"text\" maxlength=\"100\">         → máximo 100\n<input type=\"number\" min=\"1\" max=\"10\">     → entre 1 e 10\n<input type=\"text\" pattern=\"[0-9]{5}\">    → regex (5 dígitos)",
                },
                {"type": "text", "value": "**Mas atenção:** a validação HTML5 é **só a primeira camada**. Um usuário mal-intencionado pode burlar (com DevTools ou via API direta). Você **sempre precisa validar de novo no backend**."},
                {"type": "text", "value": "**Outros elementos de formulário:**"},
                {
                    "type": "code",
                    "caption": "Além do input",
                    "value": "<textarea>texto longo</textarea>      → área de texto multilinha\n<select>\n    <option>Opção 1</option>\n</select>                              → dropdown\n<button type=\"submit\">Enviar</button>   → botão\n<button type=\"button\">Cancelar</button> → botão sem submit",
                },
            ],
            "exercise": {
                "id": "06-04-ex1", "title": "Formulário de cadastro",
                "statement": "Crie um formulário HTML (`<form>`) com 2 campos: email (type=email) e senha (type=password). Cada um com `<label>`. Imprima o código HTML completo (use quebra de linha `\\n`).",
                "starter_code": "html = '<form>\\n'\n# adicione os labels e inputs\nhtml += '</form>'\nprint(html)",
                "tests": [{"validation": "output_contains_all", "expected": ["<form>", "email", "password", "<label>", "</form>"]}],
                "hint": "Adicione: '<label for=\"email\">Email:</label>\\n<input type=\"email\" id=\"email\">\\n'",
            },
        },
    ],
    "summary": [
        "Tabelas usam thead/tbody/th/td — só para dados tabulares.",
        "Forms têm action (URL) e method (GET ou POST).",
        "Labels conectados por for/id são obrigatórios para acessibilidade.",
        "Use o tipo de input certo (email, password, number) — validação grátis.",
        "Validação HTML5 é só a 1ª camada — valide de novo no backend.",
    ],
}


LESSON_06_05 = {
    "id": "06-05", "module_id": "06",
    "title": "HTML Semântico",
    "objectives": [
        "Entender por que semântica importa",
        "Usar header, nav, main, section, article, aside, footer",
        "Diferenciar section de article de div",
        "Estruturar páginas de forma profissional",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "A Evolução do HTML — de div-ite a semântica",
            "content": [
                {"type": "text", "value": "Nos primórdios do HTML, tudo era feito com **`<div>`**. Os desenvolvedores davam classes tipo `class=\"header\"`, `class=\"nav\"`, `class=\"footer\"`. Isso funcionava, mas tinha um problema: **o código não dizia o que cada coisa era** — só o que ela **parecia**."},
                {
                    "type": "code",
                    "caption": "O velho 'div-ite' (❌)",
                    "value": "<div class=\"header\">\n    <div class=\"nav\">...</div>\n</div>\n<div class=\"main\">\n    <div class=\"article\">...</div>\n    <div class=\"sidebar\">...</div>\n</div>\n<div class=\"footer\">...</div>",
                },
                {"type": "text", "value": "Esse código é **difícil de entender**, ruim para leitores de tela, e o Google não sabe o que é o quê."},
                {"type": "text", "value": "O HTML5 resolveu isso com **tags semânticas** — tags que **descrevem o que aquele bloco É**, não como ele parece."},
                {
                    "type": "code",
                    "caption": "O novo padrão (✅)",
                    "value": "<header>\n    <nav>...</nav>\n</header>\n<main>\n    <article>...</article>\n    <aside>...</aside>\n</main>\n<footer>...</footer>",
                },
                {"type": "text", "value": "**A diferença é enorme:** leitores de tela entendem a estrutura, o Google prioriza o conteúdo de `<main>`, e você (6 meses depois) entende o código sem precisar ler tudo."},
                {"type": "text", "value": "**Semântica não é estética.** As tags semânticas **não mudam nada visualmente** por padrão — elas só descrevem. O CSS é que dá a aparência. Você pode ter um `<header>` sem cor de fundo e um `<div>` azul. O valor está no **significado**."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "As Tags Semânticas Essenciais",
            "content": [
                {"type": "text", "value": "São 8 tags que você vai usar **em toda página**. Aprenda os significados:"},
                {
                    "type": "code",
                    "caption": "As 8 tags semânticas principais",
                    "value": "<header>   → topo da página ou seção (logo, título)\n<nav>      → menu de navegação\n<main>     → conteúdo principal (ÚNICO por página)\n<section>  → seção temática (agrupa conteúdo relacionado)\n<article>  → conteúdo independente (faz sentido sozinho)\n<aside>    → conteúdo lateral (relacionado mas secundário)\n<footer>   → rodapé (contatos, links, copyright)\n<figure>   → imagem com legenda\n<figcaption>→ legenda da figure",
                },
                {"type": "text", "value": "**`<main>` é único por página.** Ele contém o conteúdo **principal** — o que realmente importa naquela página. Fora dele ficam header, footer e aside."},
                {"type": "text", "value": "**`<article>` vs `<section>` — a diferença que confunde:**"},
                {
                    "type": "code",
                    "caption": "Article vs Section",
                    "value": "<article>\n    → faz sentido SOZINHO\n    → post de blog, notícia, comentário, produto\n    → você poderia copiar e colar em outro lugar que ainda faz sentido\n\n<section>\n    → agrupamento temático\n    → 'nossas features', 'quem somos', 'planos'\n    → só faz sentido no contexto da página",
                },
                {"type": "text", "value": "**Exemplo prático:** um post de blog é `<article>`. Dentro dele, o texto, os comentários, a seção de \"autor\" — cada um é uma `<section>`. Faz sentido?"},
                {"type": "text", "value": "**Estrutura padrão de página:**"},
                {
                    "type": "code",
                    "caption": "Landing page semântica",
                    "value": "<body>\n    <header>\n        <nav>\n            <a href=\"/\">Logo</a>\n            <ul>\n                <li><a href=\"#features\">Features</a></li>\n                <li><a href=\"#precos\">Preços</a></li>\n            </ul>\n        </nav>\n    </header>\n\n    <main>\n        <section id=\"hero\">\n            <h1>Bem-vindo</h1>\n        </section>\n        <section id=\"features\">\n            <h2>Nossas Features</h2>\n            <article>Feature 1</article>\n            <article>Feature 2</article>\n        </section>\n        <section id=\"precos\">\n            <h2>Planos</h2>\n        </section>\n    </main>\n\n    <footer>\n        <p>&copy; 2025 Meu Site</p>\n    </footer>\n</body>",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Quando usar <div> (e quando não usar)",
            "content": [
                {"type": "text", "value": "Depois de aprender semântica, é comum a pergunta: **\"posso usar `<div>` ainda?\"** A resposta é: **sim, mas só quando não existe tag mais específica**."},
                {
                    "type": "code",
                    "caption": "Quando usar div",
                    "value": "✅ Use <div> quando:\n- É um container puramente para estilo (wrapper)\n- É um agrupamento sem significado semântico\n- Você precisa de um bloco para aplicar flexbox/grid\n\n❌ NÃO use <div> quando:\n- Existe tag semântica pra isso\n- É o header → use <header>\n- É o menu → use <nav>\n- É um post → use <article>",
                },
                {"type": "text", "value": "**Regra prática:** antes de escrever `<div>`, pergunte **\"o que isso é?\"**. Se a resposta for \"é o cabeçalho\", use `<header>`. Se for \"é uma seção de features\", use `<section>`. Se for \"é só um wrapper para centralizar\", use `<div>`."},
                {
                    "type": "code",
                    "caption": "Uso legítimo de div",
                    "value": "<div class=\"container\">\n    <!-- Este div só existe para limitar a largura máxima -->\n    <section>\n        <h2>Título</h2>\n    </section>\n</div>\n\n# O <section> tem significado.\n# O <div class=\"container\"> é só um wrapper de layout.",
                },
                {"type": "text", "value": "**Benefícios de fazer isso direito:**"},
                {
                    "type": "code",
                    "caption": "O que você ganha",
                    "value": "✅ SEO: Google entende melhor o conteúdo prioritário\n✅ Acessibilidade: leitores de tela navegam por regiões\n✅ Manutenção: você entende o código 6 meses depois\n✅ Profissionalismo: código limpo em revisão de PR\n✅ Performance: o navegador sabe o que renderizar primeiro",
                },
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "Tags semânticas descrevem o que cada bloco É, não como parece.",
        "header, nav, main, section, article, aside, footer são as principais.",
        "article = faz sentido sozinho; section = agrupamento temático.",
        "<div> só quando nenhuma tag semântica se aplica (wrappers).",
    ],
}


LESSON_06_06 = {
    "id": "06-06", "module_id": "06",
    "title": "Acessibilidade Web",
    "objectives": [
        "Entender o que é acessibilidade e por que é obrigação",
        "Aplicar as práticas essenciais (alt, labels, contraste)",
        "Conhecer ARIA e quando usar",
        "Testar acessibilidade com ferramentas",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "Acessibilidade Não é Opcional",
            "content": [
                {"type": "text", "value": "**Acessibilidade** (abreviada como **a11y** — porque há 11 letras entre o 'a' e o 'y') é a prática de garantir que **pessoas com deficiências** possam usar seu site. Deficiências visuais, motoras, auditivas, cognitivas."},
                {"type": "text", "value": "**Números que importam:** cerca de **1 bilhão de pessoas** no mundo têm alguma deficiência. Isso é **15% da população global**. Ignorar acessibilidade é ignorar 1 em cada 7 usuários."},
                {"type": "text", "value": "**Além da ética, é lei:** no Brasil, a **Lei Brasileira de Inclusão (LBI)** exige acessibilidade em sites governamentais e de empresas com representação comercial. Internacionalmente, a **WCAG** (Web Content Accessibility Guidelines) é o padrão global."},
                {"type": "text", "value": "**Quem depende de acessibilidade:**"},
                {
                    "type": "code",
                    "caption": "Deficiências e adaptações",
                    "value": "👁️ Visual      → leitores de tela, zoom alto, alto contraste\n🖐️ Motora      → navegação por teclado (sem mouse)\n👂 Auditiva    → legendas, transcrições\n🧠 Cognitiva   → linguagem simples, navegação previsível",
                },
                {"type": "text", "value": "**Bônus inesperado:** sites acessíveis são melhores para **todo mundo**. Um texto com contraste alto ajuda quem está no sol. Legendas ajudam quem está em lugar barulhento. Navegação por teclado ajuda usuários avançados."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "As 6 Práticas Essenciais",
            "content": [
                {"type": "text", "value": "Você não precisa virar especialista em acessibilidade. **HTML semântico + 6 práticas** cobre 90% dos casos."},
                {
                    "type": "code",
                    "caption": "O checklist essencial",
                    "value": "1. alt em TODAS as imagens\n2. Labels em TODOS os inputs\n3. Contraste mínimo 4.5:1 em textos\n4. Navegação por teclado (Tab, Enter)\n5. aria-label em botões só com ícone\n6. Fonte mínima de 16px no mobile",
                },
                {"type": "text", "value": "**1. `alt` em imagens.** Já vimos isso antes. Uma imagem sem `alt` é uma imagem invisível para um usuário cego."},
                {"type": "text", "value": "**2. Labels em inputs.** Cada `<input>` precisa de um `<label for>` correspondente. Sem isso, o usuário cego ouve só \"campo de texto\" e não sabe o que preencher."},
                {"type": "text", "value": "**3. Contraste de cor.** O padrão WCAG AA exige **4.5:1** para textos normais e **3:1** para textos grandes. Ferramentas como **WebAIM Contrast Checker** ajudam a validar."},
                {
                    "type": "code",
                    "caption": "Exemplos de contraste",
                    "value": "❌ Ruim (baixo contraste)\nTexto cinza claro (#ccc) em fundo branco\n\n✅ Bom (alto contraste)\nTexto cinza escuro (#333) em fundo branco\n\n❌ Ruim\nAmarelo (#ffff00) em branco\n\n✅ Bom\nPreto (#000000) em amarelo (#ffff00)",
                },
                {"type": "text", "value": "**4. Navegação por teclado.** Muitas pessoas com deficiência motora **não usam mouse** — usam só teclado. Teste: aperte **Tab** e navegue pela sua página. Você consegue acessar tudo? Se não, tem problema."},
                {"type": "text", "value": "**Ordem do Tab importa.** O navegador segue a **ordem do HTML**. Não coloque elementos importantes só no final do arquivo pensando que \"o CSS posiciona bem\" — quem usa teclado vai sofrer."},
                {"type": "text", "value": "**5. Botões só com ícone precisam de texto.** Se seu botão é só um `<svg>` de X, o leitor de tela não sabe o que é. Adicione `aria-label`:"},
                {
                    "type": "code",
                    "caption": "aria-label em botão de ícone",
                    "value": "<button aria-label=\"Fechar menu\">\n    <svg>...</svg>   <!-- ícone de X, sem texto -->\n</button>\n\n# O usuário cego ouve: 'Fechar menu, botão'",
                },
                {"type": "text", "value": "**6. Fonte mínima de 16px no mobile.** Fontes menores causam zoom involuntário no iOS e dificultam a leitura. Use `16px` como base, aumente se quiser."},
                {"type": "text", "value": "**Testando acessibilidade:**"},
                {
                    "type": "code",
                    "caption": "Ferramentas para testar",
                    "value": "Lighthouse      → aba do DevTools (Ctrl+Shift+P → 'Lighthouse')\naxe DevTools    → extensão de navegador\nWAVE            → wave.webaim.org\nContrast Check  → webaim.org/resources/contrastchecker\nNVDA / VoiceOver → leitores de tela reais (testar manualmente)",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "ARIA — Quando (e Quando Não) Usar",
            "content": [
                {"type": "text", "value": "**ARIA** (Accessible Rich Internet Applications) são atributos que você adiciona no HTML para dar **informações extras** sobre elementos, especialmente quando eles têm comportamento dinâmico que o HTML puro não cobre."},
                {
                    "type": "code",
                    "caption": "Atributos ARIA comuns",
                    "value": "aria-label      → texto alternativo para o elemento\naria-labelledby → aponta para outro elemento que é o rótulo\naria-hidden     → esconde de leitores de tela\naria-expanded   → se um menu está aberto ou fechado\naria-live       → anuncia mudanças dinâmicas\nrole            → define o 'papel' do elemento",
                },
                {"type": "text", "value": "**Mas atenção — regra de ouro do ARIA:**"},
                {
                    "type": "code",
                    "caption": "A primeira regra do ARIA",
                    "value": "❝ Se você pode usar HTML semântico,\n  NÃO use ARIA. ❞\n\nA primeira regra do ARIA (oficial) é:\n'Não use ARIA se um elemento HTML nativo resolve.'",
                },
                {"type": "text", "value": "**Exemplo clássico:** muita gente escreve `<div role=\"button\">`. Isso é **errado**. Use `<button>` de verdade. Motivos:"},
                {
                    "type": "code",
                    "caption": "Por que <button> é melhor que <div role=\"button\">",
                    "value": "✅ <button>\n- Navegável com Tab automaticamente\n- Ativado com Enter e Espaço automaticamente\n- Foco visível por padrão\n- Estilos nativos\n\n❌ <div role=\"button\">\n- Precisa de tabindex=\"0\" manual\n- Precisa de JS pra capturar Enter/Espaço\n- Foco invisível (ou precisa estilizar)\n- Muito mais código pra pouco benefício",
                },
                {"type": "text", "value": "**Quando o ARIA é realmente útil?** Em **componentes dinâmicos** que o HTML não cobre nativamente: modais, abas (tabs), dropdowns customizados, notificações em tempo real, autocomplete."},
                {
                    "type": "code",
                    "caption": "Exemplo — anúncio dinâmico",
                    "value": "<div aria-live=\"polite\">\n    <!-- Este texto é anunciado toda vez que muda -->\n    Item adicionado ao carrinho\n</div>\n\n# O leitor de tela lê a mudança sem precisar de interação.",
                },
                {"type": "text", "value": "**Onde você vai usar ARIA no dia a dia:** principalmente quando criar **componentes React** (modais, dropdowns, tooltips). Frameworks como **Radix UI** e **Headless UI** já implementam ARIA corretamente — bom ponto de partida."},
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "Acessibilidade é obrigação ética e legal — afeta 15% da população.",
        "6 práticas essenciais: alt, labels, contraste, teclado, ARIA, fonte 16px.",
        "HTML semântico resolve 90% dos casos — use ARIA só quando necessário.",
        "Prefira <button> a <div role=\"button\">.",
        "Teste com Lighthouse, axe e leitores de tela reais.",
    ],
}


LESSON_06_07 = {
    "id": "06-07", "module_id": "06",
    "title": "CSS: Seletores e Box Model",
    "objectives": [
        "Conectar CSS ao HTML (externo, interno, inline)",
        "Usar seletores: tag, classe, id, pseudo-classe",
        "Entender o box model (margin, border, padding)",
        "Aplicar box-sizing universal e reset básico",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "CSS — Dando Vida ao HTML",
            "content": [
                {"type": "text", "value": "Se HTML é o **esqueleto** de uma página, o **CSS** (Cascading Style Sheets) é a **pele, roupas e maquiagem**. Ele dá cor, tamanho, espaçamento e posicionamento a tudo."},
                {"type": "text", "value": "**Por que separar HTML de CSS?** Porque cada um tem uma responsabilidade. HTML = estrutura/conteúdo. CSS = apresentação. Se você misturar (colocando estilo direto nas tags), seu código vira uma bagunça impossível de manter."},
                {"type": "text", "value": "Existem **3 formas** de conectar CSS ao HTML, e só uma delas é a recomendada:"},
                {
                    "type": "code",
                    "caption": "As 3 formas de conectar CSS",
                    "value": "# ❌ 1. Inline (na própria tag) — EVITE\n<p style=\"color: red;\">Texto</p>\n\n# ❌ 2. Interno (dentro do HTML) — só para testes\n<head>\n    <style>\n        p { color: red; }\n    </style>\n</head>\n\n# ✅ 3. Externo (arquivo separado) — SEMPRE use este\n<head>\n    <link rel=\"stylesheet\" href=\"styles.css\">\n</head>",
                },
                {"type": "text", "value": "**Por que externo é sempre melhor?** Três motivos:"},
                {
                    "type": "code",
                    "caption": "Vantagens do CSS externo",
                    "value": "1. Reutilização — o mesmo CSS serve para várias páginas\n2. Cache do navegador — carrega mais rápido na 2ª visita\n3. Manutenção — você muda UMA vez e reflete em todo site",
                },
                {"type": "text", "value": "**Estrutura de um arquivo CSS** é simples: cada regra tem um **seletor** e um **bloco de declarações** entre `{}`:"},
                {
                    "type": "code",
                    "caption": "Anatomia de uma regra CSS",
                    "value": "p {\n    color: blue;\n    font-size: 16px;\n}\n\np       → seletor (o que estilizar)\ncolor   → propriedade\nblue    → valor\ncolor: blue;  → declaração\n{ ... } → bloco",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Seletores — Como Escolher o Que Estilizar",
            "content": [
                {"type": "text", "value": "Os **seletores** são como você **mira** os elementos que quer estilizar. Existem vários, mas 6 são essenciais:"},
                {
                    "type": "code",
                    "caption": "Os 6 seletores essenciais",
                    "value": "p { color: blue; }              /* tag */\n.classe { font-size: 16px; }     /* classe */\n#id { margin: 20px; }            /* id */\nbutton:hover { ... }             /* pseudo-classe */\ninput[type=email] { ... }        /* atributo */\n.botao.ativo { ... }             /* múltiplas classes */",
                },
                {"type": "text", "value": "**Seletor de tag** — estiliza TODOS os elementos daquele tipo. Use com cuidado, porque afeta tudo."},
                {
                    "type": "code",
                    "caption": "Seletor de tag",
                    "value": "p {\n    line-height: 1.6;\n}\n\n/* TODOS os <p> da página terão esse line-height */",
                },
                {"type": "text", "value": "**Seletor de classe** — o mais usado. Você adiciona `class=\"nome\"` no HTML e usa `.nome` no CSS. **Pode ser reutilizado em vários elementos.**"},
                {
                    "type": "code",
                    "caption": "Seletor de classe",
                    "value": "/* HTML */\n<button class=\"botao-primario\">Salvar</button>\n<button class=\"botao-primario\">Enviar</button>\n\n/* CSS */\n.botao-primario {\n    background: #f59e0b;\n    color: white;\n}\n\n/* Os DOIS botões ficam laranja. */",
                },
                {"type": "text", "value": "**Seletor de id** — estiliza UM único elemento. O `id` deve ser **único na página** (não pode repetir). Use com moderação — classes são mais flexíveis."},
                {
                    "type": "code",
                    "caption": "Seletor de id",
                    "value": "/* HTML */\n<header id=\"topo\">...</header>\n\n/* CSS */\n#topo {\n    background: black;\n}\n\n/* Só esse header específico. */",
                },
                {"type": "text", "value": "**Pseudo-classes** aplicam estilo em **estados especiais**: `:hover` (mouse em cima), `:focus` (focado), `:active` (clicando), `:disabled`, `:checked`."},
                {
                    "type": "code",
                    "caption": "Pseudo-classes comuns",
                    "value": "button:hover { background: #d97706; }   /* mouse em cima */\ninput:focus { outline: 2px solid blue; } /* focado */\na:visited { color: purple; }             /* link já visitado */\nli:nth-child(2) { color: red; }          /* segundo item */",
                },
                {"type": "text", "value": "**Especificidade — a regra de ouro:** quando dois seletores atingem o mesmo elemento, quem **ganha** é o mais específico. Ordem: `inline` > `#id` > `.classe` > `tag`."},
                {
                    "type": "code",
                    "caption": "Especificidade na prática",
                    "value": "p { color: blue; }          /* perde */\n.destaque { color: green; } /* ganha (mais específico) */\n#titulo { color: red; }     /* ganha de tudo (a menos de inline) */\n\n<p id=\"titulo\" class=\"destaque\">Texto</p>\n/* O texto fica VERMELHO. */",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Box Model — A Caixa de Tudo",
            "content": [
                {"type": "text", "value": "**Esta é a lição mais importante de CSS.** Todo elemento em uma página é uma **caixa retangular**. E toda caixa tem 4 camadas, do conteúdo para fora:"},
                {
                    "type": "code",
                    "caption": "O box model visual",
                    "value": "┌─────────────── margin ───────────────┐\n│  (espaço FORA da caixa)              │\n│  ┌──────────── border ─────────────┐ │\n│  │  (a borda visível)              │ │\n│  │  ┌─────── padding ──────────┐   │ │\n│  │  │  (espaço INTERNO)        │   │ │\n│  │  │  ┌──── conteúdo ─────┐   │   │ │\n│  │  │  │  texto/imagem     │   │   │ │\n│  │  │  └───────────────────┘   │   │ │\n│  │  └──────────────────────────┘   │ │\n│  └─────────────────────────────────┘ │\n└──────────────────────────────────────┘",
                },
                {"type": "text", "value": "**Entendendo as 4 camadas:**"},
                {
                    "type": "code",
                    "caption": "Cada camada tem uma função",
                    "value": "conteúdo → o texto/imagem em si\npadding  → espaço INTERNO (entre conteúdo e borda)\nborder   → a linha visível ao redor\nmargin   → espaço EXTERNO (afasta dos outros elementos)",
                },
                {"type": "text", "value": "**A confusão clássica: padding vs margin.**"},
                {
                    "type": "code",
                    "caption": "Padding vs Margin",
                    "value": "padding: 20px;\n→ Empurra o conteúdo PARA DENTRO da caixa\n→ Se você pinta o fundo, o padding tem a cor de fundo\n→ É parte da caixa\n\nmargin: 20px;\n→ Afasta OUTROS elementos ao redor\n→ Transparente (sem cor de fundo)\n→ É o espaço EXTERNO à caixa",
                },
                {
                    "type": "code",
                    "caption": "Exemplo visual",
                    "value": ".card {\n    background: #f59e0b;   /* laranja */\n    padding: 20px;         /* espaço interno (fica laranja) */\n    margin: 20px;          /* espaço externo (transparente) */\n}\n\n# O padding 'engorda' o card para dentro.\n# O margin 'afasta' o card dos vizinhos.",
                },
                {"type": "text", "value": "**Sintaxe abreviada:**"},
                {
                    "type": "code",
                    "caption": "Formas de escrever",
                    "value": "padding: 10px;                    → todos os lados\npadding: 10px 20px;               → vertical 10, horizontal 20\npadding: 10px 20px 30px 40px;     → top right bottom left (horário)\n\npadding-top: 10px;                → só o topo\npadding-bottom: 10px;\npadding-left: 10px;\npadding-right: 10px;",
                },
                {"type": "text", "value": "**O problema do `box-sizing`:** por padrão, quando você define `width: 200px` em um elemento, **padding e border SOMAM** ao tamanho final. Isso é confuso."},
                {
                    "type": "code",
                    "caption": "O problema",
                    "value": ".caixa {\n    width: 200px;\n    padding: 20px;\n    border: 5px solid black;\n}\n\n/* Você espera 200px de largura.\n   Mas a caixa real fica:\n   200 + 20 + 20 + 5 + 5 = 250px */",
                },
                {"type": "text", "value": "**A solução universal:** aplicar `box-sizing: border-box` em TUDO. Isso faz o `width` incluir padding e border. É um reset padrão em **todo projeto profissional**."},
                {
                    "type": "code",
                    "caption": "Reset universal obrigatório",
                    "value": "*, *::before, *::after {\n    box-sizing: border-box;\n}\n\n* {\n    margin: 0;\n    padding: 0;\n}\n\n/* Coloque isso no TOPO de todo CSS.\n   Com border-box, width: 200px significa 200px reais. */",
                },
                {"type": "text", "value": "**Por que esse reset é padrão?** Porque sem ele, calcular larguras vira caos. Com ele, o navegador faz a conta do jeito que você espera. **Todo projeto sério começa com esse reset.**"},
            ],
            "exercise": {
                "id": "06-07-ex1", "title": "Aplicando box-sizing",
                "statement": "Escreva o CSS universal de reset que aplica `box-sizing: border-box` em todos os elementos. Imprima o código com `print()`.",
                "starter_code": "# Escreva o CSS de reset universal\ncss = \"* {\\n\"\n# complete\nprint(css)",
                "tests": [{"validation": "output_contains_all", "expected": ["*", "box-sizing", "border-box"]}],
                "hint": "css = \"*, *::before, *::after {\\n    box-sizing: border-box;\\n}\"",
            },
        },
    ],
    "summary": [
        "CSS externo (link) é o padrão profissional — evite inline.",
        "Seletores: tag (todos), .classe (reutilizável), #id (único).",
        "Box model: margin (fora) → border → padding (dentro) → conteúdo.",
        "Aplicar * { box-sizing: border-box } no topo de todo CSS.",
    ],
}


LESSON_06_08 = {
    "id": "06-08", "module_id": "06",
    "title": "Flexbox",
    "objectives": [
        "Entender o que é layout unidimensional",
        "Alinhar itens horizontal e verticalmente",
        "Distribuir espaço com justify-content",
        "Criar grids de cards responsivos com flex-wrap",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "t1",
            "title": "Flexbox — O Rei do Alinhamento",
            "content": [
                {"type": "text", "value": "Antes do Flexbox (2012), alinhar coisas no CSS era um pesadelo. Você usava `float`, `table`, `position: absolute` — truques que ninguém entendia e ninguém mantinha."},
                {"type": "text", "value": "**Flexbox** mudou isso. É o sistema de layout **unidimensional** do CSS moderno — trabalha com **linha OU coluna**, nunca as duas ao mesmo tempo (para as duas, usa-se Grid)."},
                {"type": "text", "value": "**Por que 'unidimensional'?** Porque você decide: é uma **fila horizontal** (menu, botões) ou uma **pilha vertical** (formulário, lista)? Flexbox resolve ambos com 3 linhas de CSS."},
                {
                    "type": "code",
                    "caption": "Ativando flexbox",
                    "value": ".container {\n    display: flex;\n}\n\n/* A partir daqui, todos os filhos diretos\n   são organizados em LINHA (padrão). */",
                },
                {"type": "text", "value": "**O caso mais famoso: centralizar qualquer coisa.** Antes do flex, era impossível sem hacks. Hoje, é literalmente 3 linhas:"},
                {
                    "type": "code",
                    "caption": "Centralizar tudo em 3 linhas",
                    "value": ".container {\n    display: flex;\n    justify-content: center;   /* horizontal */\n    align-items: center;       /* vertical */\n    height: 100vh;             /* altura da tela toda */\n}\n\n/* Isso centraliza QUALQUER coisa, horizontal e vertical. */",
                },
                {"type": "text", "value": "**Decore isso.** Esse é o snippet que você vai usar mais que qualquer outro em toda sua carreira de frontend. Centralizar modais, spinners, botões em cards — sempre a mesma receita."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Propriedades do Container",
            "content": [
                {"type": "text", "value": "As propriedades do flexbox se dividem em duas categorias: as que ficam **no container** (pai) e as que ficam **nos itens** (filhos). Vamos começar pelas do container."},
                {
                    "type": "code",
                    "caption": "As 5 propriedades do container",
                    "value": "display: flex;              → ativa o flexbox\nflex-direction: row|column; → direção dos itens\njustify-content: ...;       → alinha no eixo principal\n align-items: ...;          → alinha no eixo cruzado\nflex-wrap: wrap;            → permite quebrar linha\ngap: 16px;                  → espaço entre itens",
                },
                {"type": "text", "value": "**`flex-direction`** — decide o **eixo principal** (main axis):"},
                {
                    "type": "code",
                    "caption": "flex-direction",
                    "value": "row (padrão)     → itens em LINHA (horizontal)\n                    ↓ ↓ ↓\ncolumn           → itens em COLUNA (vertical)\n                    ↓\n                    ↓\n                    ↓",
                },
                {"type": "text", "value": "**`justify-content`** — alinha no **eixo principal** (o que você escolheu em flex-direction):"},
                {
                    "type": "code",
                    "caption": "justify-content",
                    "value": "flex-start    → começo (padrão)\n                [■■■         ]\n\ncenter        → centro\n                [  ■■■       ]\n\nflex-end      → final\n                [       ■■■  ]\n\nspace-between → primeiro e último nas pontas, espaço entre\n                [■       ■   ■]\n\nspace-around  → espaço igual ao redor de cada\n                [ ■   ■   ■ ]\n\nspace-evenly  → espaço IGUAL entre todos\n                [  ■   ■   ■  ]",
                },
                {"type": "text", "value": "**`align-items`** — alinha no **eixo cruzado** (o perpendicular ao principal):"},
                {
                    "type": "code",
                    "caption": "align-items",
                    "value": "flex-start    → topo\nstretch       → estica (padrão)\ncenter        → centro\nflex-end      → base",
                },
                {"type": "text", "value": "**Truque para decorar:** `justify` = eixo **principal**, `align` = eixo **cruzado**. Se você usa `flex-direction: row`, justify é horizontal e align é vertical. Se muda para `column`, **inverte**."},
                {"type": "text", "value": "**`gap`** — espaço **entre** os itens. Não confunda com margin (que afeta as bordas) — gap só cuida do espaço interno entre irmãos."},
                {
                    "type": "code",
                    "caption": "gap economiza código",
                    "value": "/* ❌ Antes (com margin) */\n.item { margin-right: 10px; }\n.item:last-child { margin-right: 0; }\n\n/* ✅ Com gap */\n.container { display: flex; gap: 10px; }\n\n/* Sem exceções, sem last-child. */",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Flexbox na Prática — Grid de Cards",
            "content": [
                {"type": "text", "value": "O caso de uso **mais comum** do Flexbox no dia a dia é criar **grades de cards** que se ajustam sozinhas ao tamanho da tela. Sem media queries, sem JS."},
                {
                    "type": "code",
                    "caption": "Grid de cards responsivo",
                    "value": ".cards {\n    display: flex;\n    flex-wrap: wrap;    /* permite quebrar linha */\n    gap: 20px;\n}\n\n.card {\n    flex: 1 1 280px;    /* cresce, encolhe, base 280px */\n}\n\n/* Cada card tem no mínimo 280px.\n   Se cabem 3 na tela, ficam 3.\n   Se cabem 2, ficam 2.\n   Se só cabe 1, ocupa a tela toda. */",
                },
                {"type": "text", "value": "**Vamos destrinchar o `flex: 1 1 280px`:**"},
                {
                    "type": "code",
                    "caption": "Anatomia do flex: 1 1 280px",
                    "value": "flex: <grow> <shrink> <basis>\n\n1      → pode CRESCER (ocupa espaço extra)\n1      → pode ENCOLHER (se faltar espaço)\n280px  → tamanho BASE (antes de crescer/encolher)",
                },
                {"type": "text", "value": "**O que acontece na prática:** cada card começa com 280px. Se sobrou espaço na linha, os cards crescem para preencher. Se falta espaço, os cards quebram para a próxima linha (por causa do `flex-wrap: wrap`)."},
                {"type": "text", "value": "**Esse é o padrão de grid de cards moderno.** Você vai usar em listagem de produtos, catálogo de cursos, posts de blog, features de landing page. **Decore esses 5 valores:**"},
                {
                    "type": "code",
                    "caption": "O snippet que você vai reusar sempre",
                    "value": ".cards {\n    display: flex;\n    flex-wrap: wrap;\n    gap: 20px;\n}\n\n.card {\n    flex: 1 1 280px;\n}",
                },
                {"type": "text", "value": "**Ajuste do `280px`:** mude conforme o conteúdo. Cards com muito texto precisam de base maior (300px, 350px). Cards com ícones podem ser menores (200px, 220px). Teste e veja."},
                {"type": "text", "value": "**Flexbox vs Grid — quando usar cada um?**"},
                {
                    "type": "code",
                    "caption": "Decisão rápida",
                    "value": "Precisa de LINHA OU COLUNA?\n→ Flexbox\n\nExemplos:\n- Barra de navegação\n- Botões lado a lado\n- Card com ícone + texto\n- Lista vertical\n\nPrecisa de LINHA E COLUNA ao mesmo tempo?\n→ Grid\n\nExemplos:\n- Layout de página (header/main/footer)\n- Grid complexo de produtos\n- Dashboard com widgets",
                },
            ],
            "exercise": {
                "id": "06-08-ex1", "title": "Centralizando com Flexbox",
                "statement": "Escreva o CSS que centraliza um elemento horizontal e verticalmente usando Flexbox. Imprima com `print()`.",
                "starter_code": "# CSS de centralização\ncss = \".container {\\n\"\n# adicione display: flex, justify-content, align-items\nprint(css)",
                "tests": [{"validation": "output_contains_all", "expected": ["display: flex", "justify-content: center", "align-items: center"]}],
                "hint": "Adicione: '    display: flex;\\n    justify-content: center;\\n    align-items: center;\\n'",
            },
        },
    ],
    "summary": [
        "Flexbox é layout unidimensional (linha OU coluna).",
        "display: flex + justify-content + align-items centraliza qualquer coisa.",
        "justify-content controla eixo principal; align-items o cruzado.",
        "flex: 1 1 280px cria grid de cards responsivo sem media query.",
        "gap substitui margin para espaçamento entre itens.",
    ],
}


LESSON_06_09 = {
    "id": "06-09", "module_id": "06",
    "title": "CSS Grid",
    "objectives": [
        "Entender o que é layout bidimensional",
        "Definir colunas e linhas com grid-template",
        "Usar repeat() e minmax() para grids responsivos",
        "Criar layouts com grid-template-areas",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "Grid — Layout Bidimensional",
            "content": [
                {"type": "text", "value": "Se o **Flexbox** é ótimo para **uma direção** (linha OU coluna), o **CSS Grid** domina **as duas ao mesmo tempo** — linha **E** coluna. É o sistema mais poderoso de layout do CSS."},
                {"type": "text", "value": "**Quando usar Grid em vez de Flex?** Quando você precisa pensar em uma **grade** — como uma planilha do Excel. Layouts de página inteira, dashboards, galerias complexas — todos pedem Grid."},
                {
                    "type": "code",
                    "caption": "Grid vs Flex — visualmente",
                    "value": "Flexbox (1D)         Grid (2D)\n─────────────         ─────────────\n[■■■■■■■■■]         [■│■│■]\n                     ─────\n                     [■│■│■]\n                     ─────\n                     [■│■│■]\n\nUma fila            Uma grade",
                },
                {"type": "text", "value": "**Ativação:** `display: grid` (assim como no flex é `display: flex`). Mas a diferença é que no grid você **define as colunas e linhas** explicitamente."},
                {
                    "type": "code",
                    "caption": "Grid básico — 3 colunas iguais",
                    "value": ".container {\n    display: grid;\n    grid-template-columns: 1fr 1fr 1fr;  /* 3 colunas iguais */\n    gap: 20px;\n}",
                },
                {"type": "text", "value": "**A unidade `fr`** (fraction) é o coração do Grid. Significa **\"fração do espaço disponível\"**. `1fr 1fr 1fr` = três colunas iguais. `2fr 1fr` = primeira coluna com o dobro da segunda."},
                {
                    "type": "code",
                    "caption": "Proporções com fr",
                    "value": "grid-template-columns: 1fr 1fr 1fr;   /* 3 iguais (33% cada) */\ngrid-template-columns: 2fr 1fr;       /* 66% e 33% */\ngrid-template-columns: 200px 1fr;     /* fixo + flexível */\ngrid-template-columns: 1fr 2fr 1fr;   /* 25%, 50%, 25% */",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Grid Responsivo com repeat() e minmax()",
            "content": [
                {"type": "text", "value": "Aqui está **o poder real** do Grid: criar layouts responsivos **sem nenhuma media query**. Uma linha de CSS resolve o que antes precisava de 3 breakpoints."},
                {
                    "type": "code",
                    "caption": "O grid responsivo mágico",
                    "value": ".cards {\n    display: grid;\n    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n    gap: 20px;\n}",
                },
                {"type": "text", "value": "**O que essa linha faz?** Vamos destrinchar:"},
                {
                    "type": "code",
                    "caption": "Anatomia do repeat + minmax",
                    "value": "repeat(auto-fit, minmax(280px, 1fr))\n       ↓            ↓            ↓\n    repete     mínimo 280px  máximo 1fr\n\nTraduzindo:\n'Repita quantas colunas couberem,\nsendo que cada uma tem no MÍNIMO 280px\ne no MÁXIMO uma fração do espaço (1fr).'",
                },
                {"type": "text", "value": "**Na prática:** em uma tela grande, cabem 4 cards (4×280 + gaps). Em tablet, cabem 2. Em mobile, cabe 1. **Tudo automático**, sem você escrever uma media query."},
                {"type": "text", "value": "**`auto-fit` vs `auto-fill`** — a diferença que confunde:"},
                {
                    "type": "code",
                    "caption": "auto-fit vs auto-fill",
                    "value": "auto-fit  → colunas vazias COLAPSAM (esticam as existentes)\n            → os cards preenchem toda a largura\n            → MELHOR no dia a dia\n\nauto-fill → colunas vazias FICAM (mesmo sem conteúdo)\n            → os cards ficam do tamanho mínimo\n            → útil quando quer alinhamento previsível",
                },
                {"type": "text", "value": "**Recomendação prática:** use `auto-fit` em **99% dos casos**. É o que faz os cards preencherem a largura toda de forma elegante."},
                {"type": "text", "value": "**Ajuste do `minmax(280px, 1fr)`:** o `280px` é o tamanho **mínimo** de cada card. Ajuste conforme o conteúdo:"},
                {
                    "type": "code",
                    "caption": "Ajustando o mínimo",
                    "value": "minmax(200px, 1fr)  → cards pequenos (ícones, tags)\nminmax(280px, 1fr)  → cards médios (produtos)\nminmax(350px, 1fr)  → cards grandes (posts de blog)\nminmax(400px, 1fr)  → cards enormes (features)",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Layout com Áreas Nomeadas",
            "content": [
                {"type": "text", "value": "Para layouts de **página inteira** (header, sidebar, main, footer), o Grid tem uma feature visual: **`grid-template-areas`**. Você literalmente **desenha** o layout no CSS com texto."},
                {
                    "type": "code",
                    "caption": "Layout clássico com áreas nomeadas",
                    "value": ".layout {\n    display: grid;\n    grid-template-areas:\n        \"header  header\"\n        \"sidebar main\"\n        \"footer  footer\";\n    grid-template-columns: 200px 1fr;\n    grid-template-rows: 60px 1fr 80px;\n    height: 100vh;\n}\n\n.header { grid-area: header; }\n.sidebar { grid-area: sidebar; }\n.main { grid-area: main; }\n.footer { grid-area: footer; }",
                },
                {"type": "text", "value": "**Repare como é visual:** as aspas desenham a grade. `header header` significa que o header ocupa **duas colunas** (a largura toda). `sidebar main` coloca a sidebar à esquerda e o main à direita."},
                {"type": "text", "value": "**Regras do `grid-template-areas`:**"},
                {
                    "type": "code",
                    "caption": "Sintaxe",
                    "value": "1. Cada linha é uma string entre aspas\n2. Cada palavra é o nome de uma área\n3. Palavras repetidas = área que ocupa múltiplas células\n4. '.' significa célula vazia\n5. Todas as linhas precisam ter o mesmo número de colunas\n\n\"header  header\"    → linha 1: header ocupa tudo\n\"sidebar main\"      → linha 2: 2 colunas\n\"footer  footer\"    → linha 3: footer ocupa tudo",
                },
                {"type": "text", "value": "**Mudar o layout é só mudar o desenho.** Quer uma sidebar à direita em vez da esquerda? Uma linha de CSS:"},
                {
                    "type": "code",
                    "caption": "Mudar o layout é trivial",
                    "value": "/* Antes */\ngrid-template-areas:\n    \"header  header\"\n    \"sidebar main\"\n    \"footer  footer\";\n\n/* Depois */\ngrid-template-areas:\n    \"header  header\"\n    \"main    sidebar\"   ← inverti!\n    \"footer  footer\";\n\n/* Só isso. Todo o resto continua igual. */",
                },
                {"type": "text", "value": "**Mobile-first com áreas nomeadas:** mude o layout em mobile para **empilhar tudo** verticalmente:"},
                {
                    "type": "code",
                    "caption": "Layout responsivo com áreas",
                    "value": ".layout {\n    display: grid;\n    grid-template-areas:\n        \"header\"\n        \"main\"\n        \"sidebar\"\n        \"footer\";\n    grid-template-columns: 1fr;\n}\n\n@media (min-width: 768px) {\n    .layout {\n        grid-template-areas:\n            \"header  header\"\n            \"sidebar main\"\n            \"footer  footer\";\n        grid-template-columns: 200px 1fr;\n    }\n}",
                },
                {"type": "text", "value": "**Dica profissional:** para layouts de **dashboard** ou **aplicação web**, `grid-template-areas` é imbatível em clareza. Voltar ao código 6 meses depois e ver o layout desenhado é um alívio."},
            ],
            "exercise": {
                "id": "06-09-ex1", "title": "Grid de 3 colunas",
                "statement": "Escreva o CSS de um grid com 3 colunas iguais usando `repeat()`. Imprima o resultado.",
                "starter_code": "css = \".container {\\n\"\n# adicione display: grid e grid-template-columns com repeat\nprint(css)",
                "tests": [{"validation": "output_contains_all", "expected": ["display: grid", "repeat", "grid-template-columns"]}],
                "hint": "css += '    display: grid;\\n    grid-template-columns: repeat(3, 1fr);\\n}'",
            },
        },
    ],
    "summary": [
        "Grid é layout bidimensional (linha E coluna).",
        "repeat(auto-fit, minmax(280px, 1fr)) cria grid responsivo sem media query.",
        "fr é fração do espaço — 1fr 1fr 1fr = 3 colunas iguais.",
        "grid-template-areas permite desenhar o layout como texto.",
        "Use Grid para layouts de página; Flex para filas ou pilhas.",
    ],
}


LESSON_06_10 = {
    "id": "06-10", "module_id": "06",
    "title": "Cores, Tipografia e Sombras",
    "objectives": [
        "Trabalhar com cores (hex, rgb, hsl)",
        "Aplicar tipografia profissional com escala",
        "Criar profundidade com sombras sutis",
        "Entender espaçamento (whitespace) como parte do design",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "Cores — Formatos e Paletas",
            "content": [
                {"type": "text", "value": "Cor é a **ferramenta mais poderosa** do design visual. Uma paleta bem escolhida faz um site parecer profissional — uma paleta ruim faz parecer amador, mesmo com layout perfeito."},
                {"type": "text", "value": "CSS tem **4 formatos de cor** principais. Você precisa entender os 3 primeiros:"},
                {
                    "type": "code",
                    "caption": "Os formatos de cor",
                    "value": "color: #f59e0b;             /* hex (mais comum) */\ncolor: rgb(245, 158, 11);    /* rgb */\ncolor: rgba(245,158,11,.5);  /* rgb com transparência */\ncolor: hsl(38, 92%, 50%);    /* hsl */",
                },
                {"type": "text", "value": "**Hex (`#RRGGBB`)** — cada par de caracteres é vermelho, verde e azul (de 00 a ff). Exemplo: `#ff0000` = vermelho puro, `#000000` = preto, `#ffffff` = branco. É o formato mais usado no dia a dia."},
                {"type": "text", "value": "**RGB (`rgb(R, G, B)`)** — vermelho, verde e azul de 0 a 255. Equivalente ao hex, mas legível: `rgb(255, 0, 0)` = vermelho."},
                {"type": "text", "value": "**RGBA (`rgba(R, G, B, A)`)** — RGB + **canal alpha** (transparência de 0 a 1). Muito útil para overlays, sombras, hover states."},
                {
                    "type": "code",
                    "caption": "Transparência na prática",
                    "value": "background: rgba(0, 0, 0, 0.5);\n/* Preto com 50% de opacidade. Vê o que está atrás. */\n\nbackground: rgba(245, 158, 11, 0.1);\n/* Laranja bem clarinho. Ótimo para backgrounds de alertas. */",
                },
                {"type": "text", "value": "**HSL (`hsl(H, S%, L%)`)** — Hue (matiz 0-360), Saturation (%), Lightness (%). É o formato **mais intuitivo** para criar paletas:"},
                {
                    "type": "code",
                    "caption": "HSL é ótimo para variações",
                    "value": "hsl(38, 92%, 50%)   → laranja base\nhsl(38, 92%, 40%)   → laranja mais escuro (hover)\nhsl(38, 92%, 60%)   → laranja mais claro\n\n/* Mesmo matiz, mudando só a luminosidade.\n   Isso cria variações harmônicas automaticamente. */",
                },
                {"type": "text", "value": "**Regra prática de paleta:** escolha **3-4 cores no máximo**. Uma primária (marca), uma neutra (texto), uma de fundo, e talvez uma de destaque/alerta. Mais que isso vira carnaval."},
                {
                    "type": "code",
                    "caption": "Paleta exemplo",
                    "value": "--cor-primaria:   #f59e0b;   /* laranja (marca) */\n--cor-texto:      #111827;   /* quase preto */\n--cor-fundo:      #ffffff;   /* branco */\n--cor-sucesso:    #10b981;   /* verde */\n--cor-erro:       #ef4444;   /* vermelho */\n--cor-cinza-100:  #f3f4f6;   /* background leve */\n--cor-cinza-500:  #6b7280;   /* texto secundário */",
                },
                {"type": "text", "value": "**Dica profissional:** use **CSS Variables** (`--nome`) para guardar as cores. Aí você muda em um só lugar e reflete em todo site. Isso é o padrão em qualquer projeto moderno."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Tipografia — Muito Além de Escolher Fonte",
            "content": [
                {"type": "text", "value": "**Tipografia** é a arte de escolher e configurar texto. Um site com tipografia ruim é cansativo de ler — mesmo que tenha cores boas e layout bonito."},
                {"type": "text", "value": "Existem **5 propriedades** de tipografia que você vai usar em todo projeto:"},
                {
                    "type": "code",
                    "caption": "As 5 propriedades essenciais",
                    "value": "font-family: 'Inter', system-ui, sans-serif;\nfont-size: 16px;\nfont-weight: 400;      /* 400 normal, 700 bold */\nline-height: 1.6;      /* altura da linha */\nletter-spacing: -0.01em;",
                },
                {"type": "text", "value": "**`font-family`** — a fonte em si. Use **font stack**: a primeira opção, depois fallbacks. Se a fonte principal não carregar, o navegador usa a próxima."},
                {
                    "type": "code",
                    "caption": "Font stack",
                    "value": "font-family: 'Inter', system-ui, -apple-system, sans-serif;\n\n/* Ordem:\n   1. 'Inter' (fonte customizada)\n   2. system-ui (a fonte do sistema operacional)\n   3. fallback genérico\n*/\n\n/* system-ui é ótimo: usa a fonte nativa do OS.\n   - San Francisco no Mac\n   - Segoe UI no Windows\n   - Roboto no Android */",
                },
                {"type": "text", "value": "**`line-height: 1.6`** — a altura da linha. Valores entre **1.5 e 1.7** são ideais para leitura em tela. Sem isso, o texto fica espremido e cansativo."},
                {"type": "text", "value": "**`font-weight`** — peso da fonte. `400` = normal, `700` = bold. Você pode usar `500` (medium) e `600` (semibold) com fontes variáveis."},
                {"type": "text", "value": "**Escala tipográfica** — este é o conceito que separa amador de profissional. Use uma **escala consistente**, não valores aleatórios."},
                {
                    "type": "code",
                    "caption": "Escala tipográfica profissional",
                    "value": "body   → 16px (base)\nsmall  → 14px\nh4     → 20px\nh3     → 24px\nh2     → 32px\nh1     → 48px\nhero   → 64px\n\n/* Padrão: cada nível multiplica por ~1.25 (escala modular) */",
                },
                {"type": "text", "value": "**Nunca use valores aleatórios** como 17px, 23px, 38px. Isso faz o design parecer amador. Siga uma escala (14, 16, 20, 24, 32, 48, 64 é a mais comum)."},
                {
                    "type": "code",
                    "caption": "Usando rem em vez de px",
                    "value": "html { font-size: 16px; }\n\nbody { font-size: 1rem; }      /* 16px */\nh1   { font-size: 3rem; }      /* 48px */\nh2   { font-size: 2rem; }      /* 32px */\n\n/* 1rem = font-size do html (16px padrão).\n   Vantagem: se o usuário mudar o zoom do navegador,\n   TUDO escala proporcionalmente. */",
                },
                {"type": "text", "value": "**Por que `rem` é melhor que `px`?** Porque respeita **acessibilidade**. Usuários com dificuldades visuais aumentam o font-size padrão do navegador — com `rem`, tudo escala. Com `px`, só o texto que foi declarado em `rem` escala."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Sombras e Whitespace",
            "content": [
                {"type": "text", "value": "**Sombras** são o que dão **profundidade** ao design. Sem elas, tudo parece plano e as coisas ficam grudadas. Com elas, os elementos parecem \"flutuar\" sobre a página."},
                {
                    "type": "code",
                    "caption": "Anatomia de uma sombra",
                    "value": "box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);\n             ↑  ↑  ↑    ↑        ↑        ↑\n             x  y blur spread  cor      opacidade",
                },
                {
                    "type": "code",
                    "caption": "O que cada valor faz",
                    "value": "x       → deslocamento horizontal\n          0    → sombra centralizada\ny       → deslocamento vertical\n          4px  → sombra 'para baixo' (elemento parece elevado)\nblur    → quanto borrada é a sombra\n          6px  → transição suave\nspread  → expansão da sombra\n          -1px → sombra levemente menor que o elemento\ncor+α   → rgba preto com baixa opacidade",
                },
                {"type": "text", "value": "**Boas sombras são sutis.** Iniciantes tendem a fazer sombras muito escuras e borradas — parece anos 2000. Profissionais usam opacidades baixas (0.05 a 0.15)."},
                {
                    "type": "code",
                    "caption": "Sombra profissional",
                    "value": "/* ❌ Sombra amadora (muito dura) */\nbox-shadow: 5px 5px 10px #000;\n\n/* ✅ Sombra profissional (sutil) */\nbox-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),\n            0 2px 4px -1px rgba(0, 0, 0, 0.06);",
                },
                {"type": "text", "value": "**Sombras com hover** — quando o mouse passa, o elemento \"sobe\" (sombra maior):"},
                {
                    "type": "code",
                    "caption": "Elevação no hover",
                    "value": ".card {\n    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);\n    transition: box-shadow 0.3s ease;\n}\n\n.card:hover {\n    box-shadow: 0 20px 25px rgba(0, 0, 0, 0.15);\n}\n\n/* O elemento parece 'subir' quando você passa o mouse. */",
                },
                {"type": "text", "value": "**Whitespace é design.** Este é provavelmente o conceito **mais subestimado** por iniciantes. Espaço em branco **não é desperdício** — é respiro. Layouts apertados parecem ansiosos e amadores."},
                {
                    "type": "code",
                    "caption": "Regra do whitespace",
                    "value": "❌ Apertado demais          ✅ Com respiro\n┌──────────────┐           ┌──────────────────────┐\n│Título         │           │                      │\n│Subtítulo      │           │  Título              │\n│Botão          │           │  Subtítulo           │\n│Conteúdo       │           │                      │\n└──────────────┘           │  [Botão]             │\n                            │                      │\n                            │  Conteúdo...         │\n                            │                      │\n                            └──────────────────────┘",
                },
                {"type": "text", "value": "**Regra prática:** na dúvida, **aumente o espaço**. Padding generoso (24px, 32px, 48px, 64px) faz o layout parecer profissional. Padding mínimo (8px, 12px) faz parecer apertado."},
                {
                    "type": "code",
                    "caption": "Espaçamentos que funcionam",
                    "value": "padding: 16px;    → elementos pequenos (botões, tags)\npadding: 24px;    → cards normais\npadding: 32px;    → cards grandes\npadding: 64px;    → seções de página\npadding: 120px;   → seções hero",
                },
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "Cores: hex (#f59e0b), rgb, rgba (com alpha), hsl.",
        "Paleta com 3-4 cores no máximo — use CSS variables.",
        "Escala tipográfica consistente (14, 16, 20, 24, 32, 48, 64).",
        "Use rem em vez de px para respeitar acessibilidade.",
        "Sombras sutis com rgba(0,0,0,0.1) criam profundidade.",
        "Whitespace generoso faz design parecer profissional.",
    ],
}


LESSON_06_11 = {
    "id": "06-11", "module_id": "06",
    "title": "Gradientes e Transições",
    "objectives": [
        "Criar gradientes lineares, radiais e múltiplos",
        "Aplicar transições suaves em mudanças de estado",
        "Entender timing functions (ease, cubic-bezier)",
        "Animar hover com transform (sem quebrar layout)",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "Gradientes — Cor que Flui",
            "content": [
                {"type": "text", "value": "**Gradiente** é uma transição gradual entre duas ou mais cores. Usado bem, dá profundidade e modernidade ao design. Usado mal, parece coisa dos anos 90."},
                {"type": "text", "value": "Existem **3 tipos** de gradiente em CSS: linear, radial e cônico."},
                {
                    "type": "code",
                    "caption": "Linear gradient",
                    "value": "/* Gradiente linear — em linha reta */\nbackground: linear-gradient(135deg, #f59e0b, #d97706);\n\n/* 135deg = direção (diagonal ↘)\n   #f59e0b = cor inicial\n   #d97706 = cor final */",
                },
                {"type": "text", "value": "**Direções comuns** de gradiente linear:"},
                {
                    "type": "code",
                    "caption": "Direções",
                    "value": "to right   → esquerda → direita\n              (0deg)\n\nto bottom  → topo → base\n              (180deg, padrão)\n\nto bottom right → diagonal ↘\n              (135deg)\n\nto top left → diagonal ↖\n              (315deg)",
                },
                {
                    "type": "code",
                    "caption": "Radial gradient",
                    "value": "background: radial-gradient(circle at top, #fbbf24, #92400e);\n\n/* Círculo começando do topo central */\nbackground: radial-gradient(ellipse at center, #fff, #000);\n\n/* Elipse no centro */",
                },
                {"type": "text", "value": "**Gradientes com múltiplas cores:** basta adicionar mais paradas (stops)."},
                {
                    "type": "code",
                    "caption": "3 cores",
                    "value": "background: linear-gradient(90deg, #f59e0b, #3b82f6, #10b981);\n\n/* Laranja → azul → verde, da esquerda para a direita */",
                },
                {"type": "text", "value": "**Gradientes profissionais são sutis.** O erro mais comum de iniciante é usar cores muito saturadas. Em design moderno, prefira gradientes entre **tons da mesma família** (laranja claro → laranja escuro)."},
                {
                    "type": "code",
                    "caption": "Sutil vs berrante",
                    "value": "/* ❌ Muito saturado */\nbackground: linear-gradient(90deg, #ff0000, #00ff00, #0000ff);\n\n/* ✅ Sutil e moderno */\nbackground: linear-gradient(135deg, #fef3c7, #fbbf24);\n\n/* Mesmo laranja, variando luminosidade. */",
                },
                {"type": "text", "value": "**Textos com gradiente** — truque visual muito usado em headlines:"},
                {
                    "type": "code",
                    "caption": "Texto gradiente",
                    "value": ".titulo {\n    background: linear-gradient(135deg, #f59e0b, #d97706);\n    -webkit-background-clip: text;\n    background-clip: text;\n    -webkit-text-fill-color: transparent;\n    color: transparent;\n}\n\n/* O texto 'recebe' o gradiente como cor. */",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Transições — Movimento Suave",
            "content": [
                {"type": "text", "value": "**`transition`** faz com que mudanças de propriedade aconteçam **suavemente** em vez de instantaneamente. É o que separa UI de site, e site de experiência."},
                {
                    "type": "code",
                    "caption": "Transição básica",
                    "value": ".botao {\n    background: #f59e0b;\n    transition: background 0.3s ease;\n}\n\n.botao:hover {\n    background: #d97706;\n}\n\n/* Sem transition: mudança é INSTANTÂNEA.\n   Com transition: muda suave em 0.3s. */",
                },
                {"type": "text", "value": "**Anatomia do transition:**"},
                {
                    "type": "code",
                    "caption": "transition: <propriedade> <duração> <easing>",
                    "value": "transition: background 0.3s ease;\n             ↑         ↑     ↑\n        propriedade   tempo  timing\n\npropriedade  → qual CSS muda (background, color, transform...)\ntempo        → quanto demora (0.2s, 0.3s, 0.5s)\ntiming       → como acelera/desacelera (ease, linear, ...)",
                },
                {"type": "text", "value": "**Timing functions** — cada uma dá uma sensação diferente ao movimento:"},
                {
                    "type": "code",
                    "caption": "Timing functions",
                    "value": "ease          → padrão, acelera no meio, desacelera no fim\nlinear        → velocidade constante (sem vida)\nease-in       → começa devagar, acelera\nease-out      → começa rápido, desacelera (mais natural)\nease-in-out   → devagar no início e no fim\ncubic-bezier(0.4, 0, 0.2, 1) → padrão Material Design",
                },
                {"type": "text", "value": "**Recomendação:** para **entradas** (elemento aparecendo), use `ease-out`. Para **saídas**, use `ease-in`. Para **interações gerais**, o `cubic-bezier(0.4, 0, 0.2, 1)` do Material Design é excelente."},
                {"type": "text", "value": "**Transições múltiplas** — várias propriedades ao mesmo tempo:"},
                {
                    "type": "code",
                    "caption": "Transição em várias propriedades",
                    "value": ".card {\n    transition: \n        transform 0.3s cubic-bezier(0.4, 0, 0.2, 1),\n        box-shadow 0.3s ease,\n        background 0.3s ease;\n}\n\n/* Cada propriedade com seu próprio tempo e easing. */",
                },
                {"type": "text", "value": "**Durações recomendadas:**"},
                {
                    "type": "code",
                    "caption": "Durações",
                    "value": "0.1s  → micro (mudança de cor de link)\n0.2s  → hover rápido\n0.3s  → hover padrão (mais comum)\n0.5s  → entrada de modal, sidebar\n1.0s  → animações grandes (raro em hover)",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Transform — Animar sem Quebrar Layout",
            "content": [
                {"type": "text", "value": "**`transform`** permite **mover, girar, escalar e inclinar** elementos. É a forma moderna de animar — e a mais performática, porque **não afeta o layout** da página."},
                {
                    "type": "code",
                    "caption": "As 4 funções principais",
                    "value": "transform: translate(10px, 20px);   /* mover */\ntransform: scale(1.1);               /* aumentar 10% */\ntransform: rotate(45deg);            /* girar 45 graus */\ntransform: skew(10deg);              /* inclinar */",
                },
                {"type": "text", "value": "**Por que transform é melhor que margin ou top?** Porque **não recalcula o layout**. Os outros elementos ficam onde estão, e a animação roda na **GPU** — muito mais fluida."},
                {"type": "text", "value": "**Uso clássico: hover com elevação.**"},
                {
                    "type": "code",
                    "caption": "Card com hover elegante",
                    "value": ".card {\n    transition: \n        transform 0.3s cubic-bezier(0.4, 0, 0.2, 1),\n        box-shadow 0.3s ease;\n}\n\n.card:hover {\n    transform: translateY(-4px);\n    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);\n}\n\n/* O card 'sobe' 4px e ganha sombra maior.\n   Parece que flutua. Muito elegante. */",
                },
                {"type": "text", "value": "**Múltiplos transforms** — combine com espaço:"},
                {
                    "type": "code",
                    "caption": "Combinando transforms",
                    "value": "transform: translateY(-4px) scale(1.02);\n/* Sobe E aumenta levemente. */\n\ntransform: rotate(3deg) translateX(10px);\n/* Gira E move. */",
                },
                {"type": "text", "value": "**Atenção:** a ordem importa! `rotate(45deg) translate(10px)` é diferente de `translate(10px) rotate(45deg)`. Primeiro a rotação, depois o deslocamento no eixo **rotacionado**."},
                {"type": "text", "value": "**Transform-origin** — controla o ponto de referência das transformações:"},
                {
                    "type": "code",
                    "caption": "transform-origin",
                    "value": ".elemento {\n    transform-origin: center;      /* padrão */\n    transform-origin: top left;    /* gira a partir do canto sup esq */\n    transform-origin: bottom right;\n}",
                },
                {"type": "text", "value": "**Dica profissional:** para hovers, use sempre **`transform` e `opacity`**. Essas duas propriedades são **aceleradas por GPU** e animam suavemente mesmo em celulares. Evite animar `width`, `height`, `top`, `left` — elas causam **reflow** e travam."},
            ],
            "exercise": {
                "id": "06-11-ex1", "title": "Transição de hover",
                "statement": "Escreva o CSS que aplica uma transição de 0.3s no `transform` de um `.botao`. Imprima com `print()`.",
                "starter_code": "css = \".botao {\\n\"\n# adicione transition\nprint(css)",
                "tests": [{"validation": "output_contains_all", "expected": ["transition", "transform", "0.3s"]}],
                "hint": "css += '    transition: transform 0.3s ease;\\n}'",
            },
        },
    ],
    "summary": [
        "Gradientes lineares e radiais dão profundidade — mantenha sutis.",
        "transition anima mudanças de propriedade.",
        "Timing functions: ease, ease-out (entrada), ease-in (saída).",
        "transform (translate, scale, rotate) é performático (GPU).",
        "Sempre anime transform e opacity — nunca width, height, top, left.",
    ],
}


LESSON_06_12 = {
    "id": "06-12", "module_id": "06",
    "title": "Animações CSS",
    "objectives": [
        "Criar keyframes com @keyframes",
        "Aplicar animações com animation",
        "Diferenciar animation de transition",
        "Respeitar prefers-reduced-motion",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "Animações — Movimento Autônomo",
            "content": [
                {"type": "text", "value": "Enquanto `transition` precisa de um **gatilho** (hover, focus) para rodar, **`animation`** roda **sozinha** — em loop, uma vez, ou com delay. É o que dá **vida própria** aos elementos."},
                {
                    "type": "code",
                    "caption": "Transition vs Animation",
                    "value": "transition              animation\n──────────────────────  ────────────────────\nPrecisa de gatilho      Roda automaticamente\n(hover, focus, JS)      (loop ou uma vez)\n\nSó 2 estados            Múltiplos estados\n(A → B)                 (0%, 25%, 50%, ...)\n\nSimples                  Complexa\n\nEx: mudar cor no hover  Ex: girar infinito, pulsar",
                },
                {"type": "text", "value": "Para criar uma animação, você precisa de **duas coisas**: definir os `@keyframes` (o que acontece) e aplicar com `animation` (onde e como)."},
                {
                    "type": "code",
                    "caption": "Estrutura de uma animação",
                    "value": "/* 1. Define o que acontece */\n@keyframes girar {\n    from { transform: rotate(0deg); }\n    to   { transform: rotate(360deg); }\n}\n\n/* 2. Aplica */\n.icone {\n    animation: girar 2s linear infinite;\n}",
                },
                {"type": "text", "value": "**Entendendo `from` e `to`:** são equivalentes a `0%` e `100%`. Para animações com mais paradas, use percentuais:"},
                {
                    "type": "code",
                    "caption": "@keyframes com percentuais",
                    "value": "@keyframes flutuar {\n    0%   { transform: translateY(0); }\n    50%  { transform: translateY(-10px); }\n    100% { transform: translateY(0); }\n}\n\n/* 0% e 100% iguais = movimento de 'vai e volta'. */",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Aplicando Animações",
            "content": [
                {"type": "text", "value": "A propriedade **`animation`** é um atalho para **8 sub-propriedades**. Vamos entender as 4 mais usadas:"},
                {
                    "type": "code",
                    "caption": "As 4 sub-propriedades mais usadas",
                    "value": "animation: girar 2s linear infinite;\n           ↑      ↑    ↑       ↑\n         nome    dur  timing  iteração\n\nanimation-name      → qual @keyframes usar\nanimation-duration  → quanto tempo dura (1 ciclo)\nanimation-timing-function → easing (linear, ease, ...)\nanimation-iteration-count → quantas vezes (1, 3, infinite)",
                },
                {
                    "type": "code",
                    "caption": "As 8 sub-propriedades completas",
                    "value": "animation-name           → nome do @keyframes\nanimation-duration       → 2s, 500ms\nanimation-timing-function → ease, linear, cubic-bezier\nanimation-delay          → espera antes de começar\nanimation-iteration-count → 1, 3, infinite\nanimation-direction      → normal, reverse, alternate\nanimation-fill-mode      → forwards, backwards, both\nanimation-play-state     → running, paused",
                },
                {"type": "text", "value": "**`animation-fill-mode: forwards`** é uma das mais úteis. Faz o elemento **manter o estado final** após a animação terminar. Sem isso, ele volta ao estado original."},
                {
                    "type": "code",
                    "caption": "Entrada com fade-in",
                    "value": "@keyframes fadeIn {\n    from { opacity: 0; transform: translateY(20px); }\n    to   { opacity: 1; transform: translateY(0); }\n}\n\n.card {\n    animation: fadeIn 0.5s ease-out forwards;\n}\n\n/* O card aparece suavemente, de baixo para cima. */",
                },
                {"type": "text", "value": "**`animation-direction: alternate`** — faz a animação ir e voltar. Excelente para movimentos tipo \"respiração\"."},
                {
                    "type": "code",
                    "caption": "Animação infinita que vai e volta",
                    "value": "@keyframes respirar {\n    from { transform: scale(1); }\n    to   { transform: scale(1.05); }\n}\n\n.coracao {\n    animation: respirar 1s ease-in-out infinite alternate;\n}\n\n/* 'Bate' como coração. */",
                },
                {"type": "text", "value": "**Animações com delay sequencial** — crie efeito cascata em listas:"},
                {
                    "type": "code",
                    "caption": "Efeito cascata",
                    "value": ".item:nth-child(1) { animation-delay: 0s; }\n.item:nth-child(2) { animation-delay: 0.1s; }\n.item:nth-child(3) { animation-delay: 0.2s; }\n.item:nth-child(4) { animation-delay: 0.3s; }\n\n/* Cada item aparece um pouco depois do anterior. */",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Acessibilidade — prefers-reduced-motion",
            "content": [
                {"type": "text", "value": "**Algumas pessoas sentem tontura, enjoo ou até crises com animações.** Isso se chama **distúrbio vestibular**. Sistemas operacionais permitem que o usuário peça para **reduzir movimento** — e você como dev precisa respeitar isso."},
                {"type": "text", "value": "A media query **`prefers-reduced-motion`** detecta essa preferência. Você **desativa** animações quando ela está ativa:"},
                {
                    "type": "code",
                    "caption": "A media query obrigatória",
                    "value": "@media (prefers-reduced-motion: reduce) {\n    *, *::before, *::after {\n        animation-duration: 0.01ms !important;\n        animation-iteration-count: 1 !important;\n        transition-duration: 0.01ms !important;\n        scroll-behavior: auto !important;\n    }\n}",
                },
                {"type": "text", "value": "**O que essa regra faz:** desativa todas as animações e transições. Os `0.01ms` mantêm a propriedade como \"técnica\" (por compatibilidade), mas efetivamente **desliga** o movimento."},
                {"type": "text", "value": "**`!important` aqui é legítimo.** Normalmente evitamos, mas nesta media query é necessário para **sobrescrever qualquer animação específica** que o código tenha definido."},
                {"type": "text", "value": "**Coloque essa media query no final do seu CSS principal.** Ela vira parte do seu \"reset\" e você não precisa mais pensar nisso. Todo projeto profissional tem."},
                {
                    "type": "code",
                    "caption": "Como testar",
                    "value": "Windows:\nConfigurações → Acessibilidade → Efeitos visuais → Desativar animações\n\nMac:\nAcessibilidade → Tela → Reduzir movimento\n\nChrome DevTools:\nCtrl+Shift+P → 'emulate css prefers-reduced-motion'",
                },
                {"type": "text", "value": "**Dica profissional:** comece TODO projeto com essa media query no CSS. Custa 30 segundos e mostra que você se importa com acessibilidade. É o tipo de detalhe que destaca seu portfólio."},
            ],
            "exercise": {
                "id": "06-12-ex1", "title": "Criando keyframes",
                "statement": "Escreva um `@keyframes` chamado `girar` que vai de `rotate(0deg)` até `rotate(360deg)`. Imprima o código CSS.",
                "starter_code": "css = \"@keyframes girar {\\n\"\n# complete com from e to\nprint(css)",
                "tests": [{"validation": "output_contains_all", "expected": ["@keyframes girar", "from", "to", "rotate"]}],
                "hint": "css += '    from { transform: rotate(0deg); }\\n    to { transform: rotate(360deg); }\\n}'",
            },
        },
    ],
    "summary": [
        "@keyframes define a animação; animation aplica.",
        "animation: nome duração timing iteração.",
        "animation-fill-mode: forwards mantém estado final.",
        "animation-direction: alternate faz ir e voltar.",
        "Sempre inclua @media (prefers-reduced-motion: reduce).",
    ],
}


LESSON_06_13 = {
    "id": "06-13", "module_id": "06",
    "title": "Responsividade e Media Queries",
    "objectives": [
        "Entender o que é mobile-first e por que usar",
        "Criar media queries com min-width",
        "Usar unidades relativas (rem, %, vw, clamp)",
        "Aplicar imagens responsivas",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "t1",
            "title": "Mobile-First — A Filosofia Moderna",
            "content": [
                {"type": "text", "value": "Antes de 2010, os sites eram feitos para desktop — e depois **adaptados** para mobile com remendos. Isso gerava código feio e experiências ruins. O mundo virou."},
                {"type": "text", "value": "Hoje, **mais de 60% do tráfego web é mobile**. Em alguns setores (redes sociais, e-commerce), passa de 80%. **Projetar primeiro para o celular não é opção — é obrigação.**"},
                {"type": "text", "value": "**Mobile-first** significa: comece pensando na **tela pequena**. Escreva o CSS básico para mobile. Depois, adicione media queries para **expandir** conforme a tela cresce."},
                {
                    "type": "code",
                    "caption": "Mentalidade mobile-first",
                    "value": "❌ Desktop-first (antigo)\n1. Faz o layout completo para desktop\n2. Adiciona media queries para 'esconder coisas' no mobile\n3. Resultado: código confuso, hierarquia ruim\n\n✅ Mobile-first (moderno)\n1. Faz o essencial para mobile (simples, empilhado)\n2. Adiciona melhorias conforme a tela cresce\n3. Resultado: código limpo, hierarquia clara",
                },
                {"type": "text", "value": "**Por que mobile-first é melhor?** Três motivos:"},
                {
                    "type": "code",
                    "caption": "Vantagens de mobile-first",
                    "value": "1. Conteúdo prioritário — no celular você é OBRIGADO a decidir o que é importante\n2. Performance — o CSS base é enxuto; media queries só adicionam\n3. Manutenção — adicionar features para desktop é 'extra', não 'corte'",
                },
                {"type": "text", "value": "**A regra de ouro:** escreva o CSS para **320px de largura primeiro** (iPhone SE). Depois, adicione `@media (min-width: ...)` para telas maiores."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Media Queries na Prática",
            "content": [
                {"type": "text", "value": "**Media queries** aplicam CSS condicionalmente, baseado em características da tela (largura, orientação, resolução). A mais usada é `min-width` (largura mínima)."},
                {
                    "type": "code",
                    "caption": "Estrutura de uma media query",
                    "value": "@media (min-width: 768px) {\n    .container {\n        padding: 24px;\n    }\n}\n\n/* 'A partir de 768px de largura,\n    o padding vira 24px.' */",
                },
                {"type": "text", "value": "**Mobile-first na prática:** escreva o CSS base (mobile) e adicione media queries **progressivamente**:"},
                {
                    "type": "code",
                    "caption": "CSS mobile-first típico",
                    "value": "/* Base (mobile — 320px+) */\n.container {\n    padding: 16px;\n    font-size: 14px;\n}\n\n/* Tablet (768px+) */\n@media (min-width: 768px) {\n    .container {\n        padding: 24px;\n        font-size: 16px;\n    }\n}\n\n/* Desktop (1024px+) */\n@media (min-width: 1024px) {\n    .container {\n        padding: 32px;\n        max-width: 1200px;\n        margin: 0 auto;\n    }\n}",
                },
                {"type": "text", "value": "**Breakpoints comuns** — valores onde o layout normalmente precisa mudar:"},
                {
                    "type": "code",
                    "caption": "Breakpoints padrão do mercado",
                    "value": "320px   → iPhone SE (mobile pequeno)\n640px   → mobile grande / tablet pequeno\n768px   → tablet\n1024px  → desktop pequeno\n1280px  → desktop grande\n1536px  → desktop muito grande",
                },
                {"type": "text", "value": "**⚠️ Não se apegue aos números.** Os breakpoints devem vir do **conteúdo**, não da moda. Se seu layout quebra em 850px, use `min-width: 850px` como breakpoint — não 768px só porque é \"padrão\"."},
                {"type": "text", "value": "**Boa prática:** sempre **mobile-first** (`min-width`). Evite `max-width` porque força você a pensar desktop-first, o que leva a código pior."},
                {
                    "type": "code",
                    "caption": "min-width vs max-width",
                    "value": "/* ✅ Mobile-first (recomendado) */\n.hero { padding: 32px; }\n@media (min-width: 768px) {\n    .hero { padding: 64px; }\n}\n\n/* ❌ Desktop-first (evite) */\n.hero { padding: 64px; }\n@media (max-width: 767px) {\n    .hero { padding: 32px; }\n}",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Unidades Responsivas e Imagens",
            "content": [
                {"type": "text", "value": "Usar `px` em tudo não é responsivo. **Unidades relativas** escalam com o contexto e respeitam preferências do usuário."},
                {
                    "type": "code",
                    "caption": "As unidades responsivas",
                    "value": "rem     → relativo ao font-size do <html> (padrão 16px)\n          1rem = 16px, 2rem = 32px\n\nem      → relativo ao font-size do PAI\n          cuidado: cascateia\n\n%       → relativo ao tamanho do pai\n          ótimo para larguras\n\nvw/vh   → % da viewport (janela)\n          100vw = largura da tela inteira\n          100vh = altura da tela inteira\n\nch      → largura do caractere '0'\n          ótimo para limitar textos",
                },
                {"type": "text", "value": "**Prefira `rem` para quase tudo:** fontes, paddings, margins, gaps. Só use `%` para larguras fluidas e `vw/vh` para elementos que precisam ocupar a tela toda."},
                {"type": "text", "value": "**`clamp()` — o herói da tipografia responsiva.** Cria um tamanho que **flui** entre um mínimo e um máximo, sem media query."},
                {
                    "type": "code",
                    "caption": "clamp() em ação",
                    "value": "font-size: clamp(1rem, 2vw, 1.5rem);\n\n/* Traduzindo:\n   no mínimo 1rem (16px)\n   idealmente 2vw (2% da viewport)\n   no máximo 1.5rem (24px)\n\n   Em telas pequenas: 16px\n   Em telas médias: cresce proporcionalmente\n   Em telas grandes: para em 24px\n*/\n\nh1 { font-size: clamp(2rem, 6vw, 3.5rem); }",
                },
                {"type": "text", "value": "**`clamp()` é ouro para hero headlines.** O título principal escala de 32px no celular até 56px no desktop — suavemente, sem breakpoint."},
                {"type": "text", "value": "**Imagens responsivas** — a regra mais importante:"},
                {
                    "type": "code",
                    "caption": "Imagens nunca devem transbordar",
                    "value": "img {\n    max-width: 100%;\n    height: auto;\n    display: block;\n}\n\n/* max-width: 100%   → nunca passa do tamanho do pai\n   height: auto      → mantém a proporção\n   display: block    → remove o 'gap' de baixo que imagens inline têm */",
                },
                {"type": "text", "value": "**`srcset` — imagens diferentes por tamanho de tela.** Para performance em sites profissionais:"},
                {
                    "type": "code",
                    "caption": "Imagens adaptativas com srcset",
                    "value": "<img \n    src=\"foto-pequena.jpg\"\n    srcset=\"foto-pequena.jpg 480w,\n            foto-media.jpg 800w,\n            foto-grande.jpg 1600w\"\n    sizes=\"(max-width: 768px) 100vw, 50vw\"\n    alt=\"Descrição\">\n\n/* O navegador escolhe a melhor versão\n   baseado na largura da tela. */",
                },
                {"type": "text", "value": "**Container pattern** — limita a largura máxima do conteúdo em telas gigantes:"},
                {
                    "type": "code",
                    "caption": "Wrapper padrão",
                    "value": ".container {\n    width: 100%;\n    max-width: 1200px;\n    margin: 0 auto;    /* centraliza */\n    padding: 0 16px;   /* respiro nas laterais */\n}\n\n/* Em telas grandes, o conteúdo para em 1200px.\n   Sem isso, textos ficam absurdamente largos. */",
                },
            ],
            "exercise": {
                "id": "06-13-ex1", "title": "Media query básica",
                "statement": "Escreva uma media query que aplica `background: blue` ao body quando a tela tiver `min-width: 768px`. Imprima o CSS completo.",
                "starter_code": "css = \"\"\n# escreva a media query\nprint(css)",
                "tests": [{"validation": "output_contains_all", "expected": ["@media", "min-width: 768px", "background", "blue"]}],
                "hint": "css = '@media (min-width: 768px) {\\n    body { background: blue; }\\n}'",
            },
        },
    ],
    "summary": [
        "Mobile-first: escreva o CSS para 320px, depois expanda com min-width.",
        "Breakpoints comuns: 640, 768, 1024, 1280px.",
        "Use rem, %, vw/vh, clamp() em vez de px fixos.",
        "img { max-width: 100%; height: auto } é obrigatório.",
        "Container com max-width: 1200px; margin: 0 auto centraliza conteúdo.",
    ],
}


LESSON_06_14 = {
    "id": "06-14", "module_id": "06",
    "title": "Projeto: Landing Page",
    "objectives": [
        "Aplicar tudo do módulo em um projeto real",
        "Estruturar HTML semântico do zero",
        "Estilizar com Flexbox e Grid",
        "Deixar responsivo mobile-first",
    ],
    "reading_time_minutes": 30,
    "topics": [
        {
            "id": "t1",
            "title": "Planejando a Landing Page",
            "content": [
                {"type": "text", "value": "Chegou a hora de **juntar tudo** em uma landing page completa. Esse é o tipo de projeto que você vai fazer **a vida toda** — para produtos, cursos, SaaS, freelancer."},
                {"type": "text", "value": "**Por que landing page?** Porque ela é o **cartão de visitas digital** do seu produto. Ela precisa convencer em **5 segundos** — headline clara, prova social, CTA visível."},
                {"type": "text", "value": "**Estrutura clássica de landing page (8 seções):**"},
                {
                    "type": "code",
                    "caption": "As 8 seções padrão",
                    "value": "1. Header com logo e navegação\n2. Hero — título grande + subtítulo + CTA\n3. Features — por que escolher?\n4. Como funciona — 3 passos\n5. Depoimentos — prova social\n6. Preços — planos\n7. FAQ — perguntas frequentes\n8. Footer — contato e copyright",
                },
                {"type": "text", "value": "**Passo 1: estrutura semântica.** Antes de escrever qualquer CSS, monte o HTML com as tags corretas:"},
                {
                    "type": "code",
                    "caption": "Estrutura HTML da landing",
                    "value": "<body>\n    <header>\n        <nav>\n            <a href=\"#\">Logo</a>\n            <ul>\n                <li><a href=\"#features\">Features</a></li>\n                <li><a href=\"#precos\">Preços</a></li>\n                <li><a href=\"#contato\">Contato</a></li>\n            </ul>\n        </nav>\n    </header>\n\n    <main>\n        <section id=\"hero\">...</section>\n        <section id=\"features\">...</section>\n        <section id=\"como-funciona\">...</section>\n        <section id=\"depoimentos\">...</section>\n        <section id=\"precos\">...</section>\n        <section id=\"faq\">...</section>\n    </main>\n\n    <footer>...</footer>\n</body>",
                },
                {"type": "text", "value": "**Repare:** `header`, `nav`, `main`, `section`, `footer` — **tudo semântico**. Nada de `<div class=\"header\">`. Isso é o que separa código profissional de código amador."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "CSS Mobile-First do Header e Hero",
            "content": [
                {"type": "text", "value": "**Passo 2: CSS mobile-first.** Comece com o layout **empilhado**, simples, para celular. Vamos fazer o header e o hero primeiro."},
                {
                    "type": "code",
                    "caption": "Reset universal + variáveis",
                    "value": "*, *::before, *::after {\n    box-sizing: border-box;\n}\n\n* {\n    margin: 0;\n    padding: 0;\n}\n\n:root {\n    --cor-primaria: #f59e0b;\n    --cor-primaria-escura: #d97706;\n    --cor-texto: #111827;\n    --cor-cinza: #6b7280;\n    --cor-fundo: #ffffff;\n    --cor-fundo-claro: #f9fafb;\n}\n\nbody {\n    font-family: 'Inter', system-ui, sans-serif;\n    font-size: 16px;\n    line-height: 1.6;\n    color: var(--cor-texto);\n}",
                },
                {
                    "type": "code",
                    "caption": "Header mobile-first",
                    "value": "header {\n    padding: 16px;\n    border-bottom: 1px solid #e5e7eb;\n}\n\nnav {\n    display: flex;\n    justify-content: space-between;\n    align-items: center;\n    flex-wrap: wrap;\n    gap: 16px;\n}\n\nnav ul {\n    display: flex;\n    gap: 20px;\n    list-style: none;\n}\n\nnav a {\n    text-decoration: none;\n    color: var(--cor-texto);\n    font-weight: 500;\n    transition: color 0.2s;\n}\n\nnav a:hover {\n    color: var(--cor-primaria);\n}",
                },
                {"type": "text", "value": "**Vamos destrinchar o que fizemos:**"},
                {
                    "type": "code",
                    "caption": "Cada decisão tem motivo",
                    "value": "display: flex no nav   → logo e menu lado a lado\njustify-content: space-between → logo à esquerda, menu à direita\nflex-wrap: wrap        → se não couber, quebra no mobile\nlist-style: none       → remove bolinhas do <ul>\ntext-decoration: none  → remove sublinhado dos links\ntransition: color 0.2s → hover suave",
                },
                {
                    "type": "code",
                    "caption": "Hero mobile-first",
                    "value": "#hero {\n    display: flex;\n    flex-direction: column;\n    align-items: center;\n    text-align: center;\n    padding: 64px 16px;\n    gap: 24px;\n}\n\n#hero h1 {\n    font-size: clamp(2rem, 6vw, 3.5rem);\n    line-height: 1.1;\n    font-weight: 700;\n}\n\n#hero p {\n    font-size: 1.125rem;\n    color: var(--cor-cinza);\n    max-width: 600px;\n}\n\n#hero .cta {\n    background: var(--cor-primaria);\n    color: white;\n    padding: 16px 32px;\n    border: none;\n    border-radius: 8px;\n    font-size: 1rem;\n    font-weight: 600;\n    cursor: pointer;\n    transition: background 0.3s, transform 0.3s;\n}\n\n#hero .cta:hover {\n    background: var(--cor-primaria-escura);\n    transform: translateY(-2px);\n}",
                },
                {"type": "text", "value": "**`clamp()` no h1** — o título escala entre 32px e 56px conforme a tela, sem media query. Suave."},
                {"type": "text", "value": "**`gap` no lugar de margin** — mais limpo, sem aquele `margin-bottom: 24px` em cada filho."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Grid de Features Responsivo",
            "content": [
                {"type": "text", "value": "**Passo 3: a seção de features.** Aqui usamos **CSS Grid** com `auto-fit` — a feature que você aprendeu na lição 06-09. Em **3 linhas**, temos um grid que se adapta a qualquer tela."},
                {
                    "type": "code",
                    "caption": "Features — grid responsivo",
                    "value": "#features {\n    display: grid;\n    grid-template-columns: 1fr;   /* 1 coluna no mobile */\n    gap: 24px;\n    padding: 64px 16px;\n    background: var(--cor-fundo-claro);\n}\n\n.feature-card {\n    background: white;\n    padding: 32px;\n    border-radius: 12px;\n    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);\n    transition: transform 0.3s, box-shadow 0.3s;\n}\n\n.feature-card:hover {\n    transform: translateY(-4px);\n    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);\n}\n\n.feature-card h3 {\n    font-size: 1.25rem;\n    margin-bottom: 12px;\n}\n\n.feature-card p {\n    color: var(--cor-cinza);\n}",
                },
                {
                    "type": "code",
                    "caption": "Adicionando as colunas em telas maiores",
                    "value": "@media (min-width: 768px) {\n    #features {\n        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n        padding: 120px 32px;\n    }\n}",
                },
                {"type": "text", "value": "**Repare na mudança:** no mobile é `grid-template-columns: 1fr` (uma coluna). A partir de 768px, muda para **`repeat(auto-fit, minmax(280px, 1fr))`** — que cria automaticamente 2, 3 ou 4 colunas conforme o espaço. **Zero media queries adicionais.**"},
                {"type": "text", "value": "**O `hover` no card** — o pattern `transform: translateY(-4px)` + sombra maior faz o card parecer flutuar. É **o** efeito de hover moderno."},
                {"type": "text", "value": "**Repetindo o pattern para outras seções:**"},
                {
                    "type": "code",
                    "caption": "Preços (mesmo pattern)",
                    "value": "#precos {\n    display: grid;\n    grid-template-columns: 1fr;\n    gap: 24px;\n    padding: 64px 16px;\n}\n\n@media (min-width: 768px) {\n    #precos {\n        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\n        padding: 120px 32px;\n    }\n}\n\n.plano {\n    background: white;\n    padding: 32px;\n    border: 2px solid #e5e7eb;\n    border-radius: 12px;\n    text-align: center;\n}\n\n.plano.destaque {\n    border-color: var(--cor-primaria);\n    transform: scale(1.05);\n}",
                },
                {"type": "text", "value": "**Passo final: checklist de qualidade.** Antes de considerar a landing pronta, verifique:"},
                {
                    "type": "code",
                    "caption": "Checklist final",
                    "value": "✅ HTML semântico (header, nav, main, section, footer)\n✅ Mobile-first (começa em 320px, expande)\n✅ Breakpoints em 768px e 1024px\n✅ Grid responsivo com repeat(auto-fit, minmax())\n✅ CSS variables para cores\n✅ Fonte em rem, não px\n✅ clamp() nos títulos\n✅ Hover com transform + transition\n✅ prefers-reduced-motion no final do CSS\n✅ img { max-width: 100%; height: auto }\n✅ Contraste de cores testado (WebAIM)\n✅ Funciona sem JS (a base)",
                },
                {"type": "text", "value": "**Próximos passos:** com esse projeto pronto, você tem uma **landing page profissional** para mostrar em portfólio. Suba no GitHub Pages ou Vercel e mande o link junto do currículo."},
                {"type": "text", "value": "**Bônus — animação de entrada com GSAP:** quando estiver confortável, adicione animações de scroll com GSAP. Faz os elementos aparecerem suavemente conforme você rola — dá um ar premium ao site."},
            ],
            "exercise": {
                "id": "06-14-ex1", "title": "Grid de features",
                "statement": "Escreva o CSS da seção `#features` que usa Grid com `repeat(auto-fit, minmax(280px, 1fr))` e `gap: 24px`. Imprima o CSS.",
                "starter_code": "css = \"#features {\\n\"\n# adicione display, grid-template-columns, gap\nprint(css)",
                "tests": [{"validation": "output_contains_all", "expected": ["display: grid", "repeat", "auto-fit", "minmax", "gap"]}],
                "hint": "css += '    display: grid;\\n    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));\\n    gap: 24px;\\n}'",
            },
        },
    ],
    "summary": [
        "Landing page = 8 seções: header, hero, features, como funciona, depoimentos, preços, FAQ, footer.",
        "HTML semântico do início ao fim — zero div-ite.",
        "Mobile-first: base em 320px, expande com @media (min-width: 768px).",
        "Grid responsivo com repeat(auto-fit, minmax(280px, 1fr)) resolve features e preços.",
        "Hover com transform + transition + sombra = elegância profissional.",
    ],
}


