"""Lições do Módulo 03 — extraídas automaticamente de lessons_content.py."""

LESSON_03_01 = {
    "id": "03-01",
    "module_id": "03",
    "title": "Funções com Parâmetros e Retorno",
    "objectives": [
        "Criar funções que recebem informações (parâmetros)",
        "Retornar valores de uma função",
        "Diferenciar parâmetro de argumento",
        "Usar múltiplos parâmetros e retornos",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "topico-1",
            "title": "Parâmetros e Argumentos",
            "content": [
                {"type": "text", "value": "Você já sabe criar funções simples. Agora vamos **aprofundar**: funções que recebem dados, processam e devolvem resultados. Isso é o que torna funções realmente úteis."},
                {"type": "text", "value": "**Parâmetro** é o nome que a função usa internamente (`a`, `b`). **Argumento** é o valor concreto que passamos na chamada (`10`, `5`)."},
                {
                    "type": "code",
                    "caption": "Parâmetro vs Argumento",
                    "value": "def somar(a, b):     # a e b são PARÂMETROS\n    return a + b\n\nsomar(10, 5)         # 10 e 5 são ARGUMENTOS",
                },
                {"type": "text", "value": "Uma função pode receber **quantos parâmetros quiser**, separados por vírgula. E pode **retornar qualquer valor** — número, texto, lista, dicionário."},
                {
                    "type": "code",
                    "caption": "Múltiplos parâmetros",
                    "value": "def apresentar(nome, idade, cidade):\n    return f\"{nome}, {idade} anos, mora em {cidade}\"\n\nresultado = apresentar(\"Gabrielly\", 18, \"São Carlos\")\nprint(resultado)\n# Gabrielly, 18 anos, mora em São Carlos",
                },
                {"type": "text", "value": "Quando uma função **não tem `return`**, ela retorna `None` automaticamente. Isso é diferente de retornar uma string vazia ou zero."},
            ],
            "exercise": {
                "id": "03-01-ex1",
                "title": "Função de boas-vindas",
                "statement": "Crie uma função `boas_vindas(nome)` que retorna a string `Bem-vindo, {nome}!` (usando f-string). Chame com `'Gabrielly'` e imprima o resultado.",
                "starter_code": "def boas_vindas(nome):\n    # retorne a string formatada\n    \n\nprint(boas_vindas('Gabrielly'))",
                "tests": [
                    {"validation": "output_equals", "expected": "Bem-vindo, Gabrielly!"},
                ],
                "hint": "Use f-string: return f\"Bem-vindo, {nome}!\"",
            },
        },
        {
            "id": "topico-2",
            "title": "Retornando Múltiplos Valores",
            "content": [
                {"type": "text", "value": "Uma função Python pode retornar **vários valores** ao mesmo tempo. Quando isso acontece, eles vêm numa **tupla**."},
                {
                    "type": "code",
                    "caption": "Retornando múltiplos valores",
                    "value": "def analisar_notas(nota1, nota2, nota3):\n    soma = nota1 + nota2 + nota3\n    media = soma / 3\n    return soma, media\n\nsoma, media = analisar_notas(8, 7, 9)\nprint(\"Soma:\", soma)      # Soma: 24\nprint(\"Média:\", media)    # Média: 8.0",
                },
                {"type": "text", "value": "Repare que na chamada fazemos **desempacotamento**: `soma, media = analisar_notas(...)`. Cada variável recebe um dos valores retornados."},
                {"type": "text", "value": "**Boa prática:** o nome da função deve deixar claro **o que ela devolve**. `calcular_media()` é melhor que `func1()`. Funções bem nomeadas tornam o código autoexplicativo."},
            ],
            "exercise": {
                "id": "03-01-ex2",
                "title": "Retornando soma e produto",
                "statement": "Crie uma função `calcular(a, b)` que retorna **dois valores**: `a + b` e `a * b`. Chame com `3` e `4`, receba em `soma` e `produto`, e imprima `soma` primeiro e depois `produto`.",
                "starter_code": "def calcular(a, b):\n    # retorne soma e produto\n    \n\nsoma, produto = calcular(3, 4)\nprint(soma)\nprint(produto)",
                "tests": [
                    {"validation": "output_contains_all", "expected": ["7", "12"]},
                    {"validation": "output_line_count", "expected": 2},
                ],
                "hint": "return a + b, a * b",
            },
        },
    ],
    "summary": [
        "Parâmetro é o nome; argumento é o valor passado.",
        "Funções retornam valores com return; sem return, retornam None.",
        "É possível retornar múltiplos valores separados por vírgula.",
    ],
}


LESSON_03_02 = {
    "id": "03-02",
    "module_id": "03",
    "title": "Argumentos Opcionais e Nomeados",
    "objectives": [
        "Criar parâmetros com valores padrão",
        "Chamar funções com argumentos nomeados",
        "Entender a ordem dos parâmetros",
        "Combinar argumentos posicionais e nomeados",
    ],
    "reading_time_minutes": 12,
    "topics": [
        {
            "id": "topico-1",
            "title": "Valores Padrão",
            "content": [
                {"type": "text", "value": "Às vezes, queremos que uma função tenha um **comportamento padrão** caso o usuário não passe aquele valor. Para isso, usamos **parâmetros com valor padrão**."},
                {
                    "type": "code",
                    "caption": "Parâmetro com valor padrão",
                    "value": "def saudar(nome, saudacao=\"Olá\"):\n    return f\"{saudacao}, {nome}!\"\n\nprint(saudar(\"Gabrielly\"))          # Olá, Gabrielly!\nprint(saudar(\"Gabrielly\", \"Oi\"))   # Oi, Gabrielly!",
                },
                {"type": "text", "value": "**Regra importante:** parâmetros com valor padrão **devem vir por último**. Se um parâmetro sem padrão vier depois de um com padrão, o Python dá erro."},
                {
                    "type": "code",
                    "caption": "Ordem correta",
                    "value": "# ✅ Correto\ndef criar_usuario(nome, idade, ativo=True):\n    ...\n\n# ❌ Errado (não compila)\ndef criar_usuario(ativo=True, nome, idade):\n    ...",
                },
                {"type": "text", "value": "**Cuidado com listas como valor padrão!** Elas são mutáveis e mantêm estado entre chamadas. Use `None` e crie a lista dentro da função."},
                {
                    "type": "code",
                    "caption": "O bug clássico da lista padrão",
                    "value": "# ❌ Bug perigoso\ndef adicionar(item, lista=[]):\n    lista.append(item)\n    return lista\n\nadicionar(\"a\")   # ['a']\nadicionar(\"b\")   # ['a', 'b'] — SURPRESA! O padrão foi reutilizado\n\n# ✅ Correto\ndef adicionar(item, lista=None):\n    if lista is None:\n        lista = []\n    lista.append(item)\n    return lista",
                },
            ],
            "exercise": {
                "id": "03-02-ex1",
                "title": "Função com padrão",
                "statement": "Crie uma função `apresentar(nome, cidade='São Paulo')` que retorna a string `{nome} mora em {cidade}`. Chame apenas com `'Gabrielly'` (sem cidade) e imprima o resultado.",
                "starter_code": "def apresentar(nome, cidade='São Paulo'):\n    # retorne a string\n    \n\nprint(apresentar('Gabrielly'))",
                "tests": [
                    {"validation": "output_equals", "expected": "Gabrielly mora em São Paulo"},
                ],
                "hint": "return f\"{nome} mora em {cidade}\"",
            },
        },
        {
            "id": "topico-2",
            "title": "Argumentos Nomeados",
            "content": [
                {"type": "text", "value": "Quando chamamos uma função, podemos usar **o nome do parâmetro** para deixar claro o que estamos passando. Isso se chama **argumento nomeado** (ou keyword argument)."},
                {
                    "type": "code",
                    "caption": "Argumentos nomeados",
                    "value": "def criar_conta(nome, email, ativo=True):\n    return f\"{nome} | {email} | ativo={ativo}\"\n\n# Posicional (ordem importa)\nprint(criar_conta(\"Gabrielly\", \"g@email.com\"))\n\n# Nomeado (ordem NÃO importa)\nprint(criar_conta(email=\"g@email.com\", nome=\"Gabrielly\"))",
                },
                {"type": "text", "value": "**Vantagem:** código mais legível e menos propenso a erros. Quando você vê `criar_conta(email=\"...\")`, sabe exatamente o que está sendo passado."},
                {"type": "text", "value": "**Regra:** argumentos **posicionais** vêm antes dos **nomeados**. Não pode misturar na ordem errada."},
                {
                    "type": "code",
                    "caption": "Misturando posicional e nomeado",
                    "value": "# ✅ Correto\ncriar_conta(\"Gabrielly\", email=\"g@email.com\")\n\n# ❌ Errado (nomeado antes de posicional)\ncriar_conta(nome=\"Gabrielly\", \"g@email.com\")",
                },
            ],
            "exercise": {
                "id": "03-02-ex2",
                "title": "Chamada com nomeados",
                "statement": "Crie uma função `perfil(nome, idade, cidade)` que retorna a string `{nome}, {idade}, {cidade}`. Depois chame a função **usando argumentos nomeados** (fora de ordem): `cidade='Rio'`, `nome='Gabrielly'`, `idade=18`. Imprima o resultado.",
                "starter_code": "def perfil(nome, idade, cidade):\n    return f\"{nome}, {idade}, {cidade}\"\n\n# Chame com argumentos nomeados\nprint()",
                "tests": [
                    {"validation": "output_equals", "expected": "Gabrielly, 18, Rio"},
                ],
                "hint": "print(perfil(cidade='Rio', nome='Gabrielly', idade=18))",
            },
        },
    ],
    "summary": [
        "Parâmetros com valor padrão tornam argumentos opcionais.",
        "Parâmetros com padrão devem vir por último.",
        "Nunca use lista/dict como valor padrão — use None.",
        "Argumentos nomeados deixam o código mais legível.",
    ],
}


LESSON_03_03 = {
    "id": "03-03",
    "module_id": "03",
    "title": "*args e **kwargs",
    "objectives": [
        "Entender o que são argumentos variáveis",
        "Usar *args para receber múltiplos valores posicionais",
        "Usar **kwargs para receber múltiplos valores nomeados",
        "Combinar os dois em uma função",
    ],
    "reading_time_minutes": 12,
    "topics": [
        {
            "id": "topico-1",
            "title": "Recebendo Números Variáveis de Argumentos",
            "content": [
                {"type": "text", "value": "Imagine uma função que soma **qualquer quantidade** de números. Você não sabe de antemão se serão 2, 5 ou 20. Para isso existe **`*args`**."},
                {
                    "type": "code",
                    "caption": "*args — múltiplos posicionais",
                    "value": "def somar_tudo(*numeros):\n    total = 0\n    for n in numeros:\n        total += n\n    return total\n\nprint(somar_tudo(1, 2))              # 3\nprint(somar_tudo(1, 2, 3, 4, 5))     # 15\nprint(somar_tudo(10, 20, 30, 40))    # 100",
                },
                {"type": "text", "value": "O `*` faz com que todos os argumentos posicionais sejam empacotados numa **tupla** chamada `numeros` (o nome pode ser qualquer — `*args` é convenção)."},
                {
                    "type": "code",
                    "caption": "args é uma tupla",
                    "value": "def mostrar(*args):\n    print(type(args))   # <class 'tuple'>\n    print(args)\n\nmostrar(1, 2, 3)   # (1, 2, 3)",
                },
                {"type": "text", "value": "**Caso de uso real:** funções de soma, `print()` (que aceita infinitos valores), `max()`, `min()`, etc."},
            ],
            "exercise": {
                "id": "03-03-ex1",
                "title": "Somar vários números",
                "statement": "Crie uma função `somar(*numeros)` que retorna a soma de todos os números passados. Chame com `(10, 20, 30, 40)` e imprima o resultado.",
                "starter_code": "def somar(*numeros):\n    # some todos os números\n    \n\nprint(somar(10, 20, 30, 40))",
                "tests": [
                    {"validation": "output_equals", "expected": "100"},
                ],
                "hint": "Use sum(numeros) ou um for acumulando",
            },
        },
        {
            "id": "topico-2",
            "title": "**kwargs — Argumentos Nomeados",
            "content": [
                {"type": "text", "value": "Enquanto `*args` empacota valores **posicionais** numa tupla, **`**kwargs`** empacota valores **nomeados** num **dicionário**."},
                {
                    "type": "code",
                    "caption": "**kwargs — múltiplos nomeados",
                    "value": "def mostrar_info(**dados):\n    for chave, valor in dados.items():\n        print(f\"{chave}: {valor}\")\n\nmostrar_info(nome=\"Gabrielly\", idade=18, cidade=\"São Carlos\")\n\n# Saída:\n# nome: Gabrielly\n# idade: 18\n# cidade: São Carlos",
                },
                {"type": "text", "value": "Isso é ótimo quando você quer uma função **flexível** que aceite qualquer combinação de parâmetros nomeados, sem saber quais de antemão."},
                {"type": "text", "value": "**Combinando `*args` e `**kwargs`** — a ordem obrigatória é: parâmetros normais, `*args`, depois `**kwargs`."},
                {
                    "type": "code",
                    "caption": "Combinando tudo",
                    "value": "def funcao(obrigatorio, *args, **kwargs):\n    print(\"Obrigatório:\", obrigatorio)\n    print(\"Posicionais extras:\", args)\n    print(\"Nomeados extras:\", kwargs)\n\nfuncao(\"a\", 1, 2, 3, nome=\"Gabrielly\", idade=18)\n\n# Obrigatório: a\n# Posicionais extras: (1, 2, 3)\n# Nomeados extras: {'nome': 'Gabrielly', 'idade': 18}",
                },
                {"type": "text", "value": "**Aplicação real:** frameworks como FastAPI e Django usam `**kwargs` internamente para passar configurações flexíveis entre funções."},
            ],
            "exercise": {
                "id": "03-03-ex2",
                "title": "Imprimindo informações",
                "statement": "Crie uma função `info(**dados)` que imprime cada chave e valor no formato `chave: valor`, um por linha. Chame com `nome='Gabrielly'` e `idade=18`.",
                "starter_code": "def info(**dados):\n    # percorra dados e imprima chave: valor\n    \n\ninfo(nome='Gabrielly', idade=18)",
                "tests": [
                    {"validation": "output_contains_all", "expected": ["nome: Gabrielly", "idade: 18"]},
                    {"validation": "output_line_count", "expected": 2},
                ],
                "hint": "Use for chave, valor in dados.items(): print(f\"{chave}: {valor}\")",
            },
        },
    ],
    "summary": [
        "*args empacota argumentos posicionais em uma tupla.",
        "**kwargs empacota argumentos nomeados em um dicionário.",
        "Ordem: parâmetros normais → *args → **kwargs.",
    ],
}


LESSON_03_04 = {
    "id": "03-04",
    "module_id": "03",
    "title": "Funções Lambda",
    "objectives": [
        "Entender o que são funções anônimas",
        "Criar lambdas para operações simples",
        "Usar lambdas com sorted(), map() e filter()",
        "Saber quando usar (e quando NÃO usar) lambda",
    ],
    "reading_time_minutes": 10,
    "topics": [
        {
            "id": "topico-1",
            "title": "Funções de Uma Linha",
            "content": [
                {"type": "text", "value": "Uma **lambda** é uma função **anônima** (sem nome) que cabe em uma linha. Serve para operações **simples e pontuais**."},
                {
                    "type": "code",
                    "caption": "Sintaxe da lambda",
                    "value": "# Função normal\ndef dobrar(x):\n    return x * 2\n\n# Mesma coisa como lambda\ndobrar = lambda x: x * 2\n\nprint(dobrar(5))   # 10",
                },
                {"type": "text", "value": "A estrutura é `lambda parametros: expressao`. A expressão é o que a função retorna — **não precisa de `return`**."},
                {"type": "text", "value": "Lambdas brilham quando usadas **dentro de outras funções**. Por exemplo, `sorted()` aceita uma função como critério de ordenação:"},
                {
                    "type": "code",
                    "caption": "Lambda com sorted()",
                    "value": "pessoas = [\n    {\"nome\": \"Gabrielly\", \"idade\": 18},\n    {\"nome\": \"Ana\", \"idade\": 25},\n    {\"nome\": \"João\", \"idade\": 20}\n]\n\n# Ordena por idade\nordenado = sorted(pessoas, key=lambda p: p[\"idade\"])\nprint(ordenado)",
                },
            ],
            "exercise": {
                "id": "03-04-ex1",
                "title": "Lambda de multiplicação",
                "statement": "Crie uma variável `triplo` que recebe uma lambda que retorna o triplo de um número. Chame com `7` e imprima o resultado.",
                "starter_code": "triplo = lambda x: \n\nprint(triplo(7))",
                "tests": [
                    {"validation": "output_equals", "expected": "21"},
                ],
                "hint": "lambda x: x * 3",
            },
        },
        {
            "id": "topico-2",
            "title": "Lambda com map e filter",
            "content": [
                {"type": "text", "value": "Duas funções muito usadas com lambda são **`map()`** (transformar) e **`filter()`** (filtrar). Ambas recebem uma função e uma lista."},
                {
                    "type": "code",
                    "caption": "map() — transformar cada item",
                    "value": "numeros = [1, 2, 3, 4, 5]\n\n# Multiplica cada por 10\ndobrados = list(map(lambda x: x * 10, numeros))\nprint(dobrados)   # [10, 20, 30, 40, 50]",
                },
                {
                    "type": "code",
                    "caption": "filter() — manter só o que passa no teste",
                    "value": "numeros = [1, 2, 3, 4, 5, 6, 7, 8]\n\n# Só os pares\npares = list(filter(lambda x: x % 2 == 0, numeros))\nprint(pares)   # [2, 4, 6, 8]",
                },
                {"type": "text", "value": "**Quando NÃO usar lambda:** se a lógica tem mais de uma linha, ou if/else grandes, ou é usada em vários lugares — aí vale mais uma função normal com `def`."},
                {
                    "type": "code",
                    "caption": "Bom uso vs uso ruim",
                    "value": "# ✅ Bom — operação simples, uso único\nsorted(alunos, key=lambda a: a[\"nota\"])\n\n# ❌ Ruim — lógica complexa vira ilegível\ncalcular = lambda x: x * 2 if x > 0 else x * 3 if x < -5 else 0",
                },
            ],
            "exercise": {
                "id": "03-04-ex2",
                "title": "Filtrando com lambda",
                "statement": "Crie uma lista `numeros = [1, 2, 3, 4, 5, 6]`. Use `filter()` com uma lambda para manter **apenas os números maiores que 3**. Converta o resultado para lista e imprima.",
                "starter_code": "numeros = [1, 2, 3, 4, 5, 6]\n\n# Filtre apenas os maiores que 3\nresultado = list()\nprint(resultado)",
                "tests": [
                    {"validation": "output_equals", "expected": "[4, 5, 6]"},
                ],
                "hint": "list(filter(lambda x: x > 3, numeros))",
            },
        },
    ],
    "summary": [
        "Lambda é uma função anônima de uma linha.",
        "Sintaxe: lambda parametros: expressao.",
        "Ideal para sorted, map, filter em operações simples.",
    ],
}


LESSON_03_05 = {
    "id": "03-05",
    "module_id": "03",
    "title": "List Comprehensions",
    "objectives": [
        "Entender o que são list comprehensions",
        "Criar listas de forma concisa e legível",
        "Adicionar condições dentro da comprehension",
        "Comparar com for + append tradicional",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "topico-1",
            "title": "Criando Listas em Uma Linha",
            "content": [
                {"type": "text", "value": "**List comprehension** é uma forma **elegante** e **rápida** de criar listas a partir de um iterável, em uma única linha."},
                {
                    "type": "text", "value": "Compare a forma tradicional com a comprehension:"},
                {
                    "type": "code",
                    "caption": "Tradicional vs Comprehension",
                    "value": "# ❌ Tradicional (5 linhas)\nquadrados = []\nfor x in range(1, 6):\n    quadrados.append(x ** 2)\nprint(quadrados)   # [1, 4, 9, 16, 25]\n\n# ✅ Comprehension (1 linha)\nquadrados = [x ** 2 for x in range(1, 6)]\nprint(quadrados)   # [1, 4, 9, 16, 25]",
                },
                {"type": "text", "value": "A sintaxe é: `[expressao for item in iteravel]`. É como se fosse um for invertido, dentro de colchetes."},
                {"type": "text", "value": "Você pode adicionar uma **condição (if)** no final para filtrar elementos:"},
                {
                    "type": "code",
                    "caption": "Com condição (if)",
                    "value": "numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n\n# Só os pares\npares = [n for n in numeros if n % 2 == 0]\nprint(pares)   # [2, 4, 6, 8, 10]",
                },
                {"type": "text", "value": "Também funciona com if/else: `[x if cond else y for x in lista]`."},
                {
                    "type": "code",
                    "caption": "Com if/else",
                    "value": "numeros = [1, 2, 3, 4, 5]\n\nrotulos = [\"par\" if n % 2 == 0 else \"ímpar\" for n in numeros]\nprint(rotulos)   # ['ímpar', 'par', 'ímpar', 'par', 'ímpar']",
                },
            ],
            "exercise": {
                "id": "03-05-ex1",
                "title": "Quadrados com comprehension",
                "statement": "Use uma **list comprehension** para criar uma lista chamada `quadrados` com os quadrados dos números de 1 a 5. Imprima o resultado.",
                "starter_code": "# Use list comprehension\nquadrados = \nprint(quadrados)",
                "tests": [
                    {"validation": "output_equals", "expected": "[1, 4, 9, 16, 25]"},
                ],
                "hint": "[x ** 2 for x in range(1, 6)]",
            },
        },
        {
            "id": "topico-2",
            "title": "Aplicações Práticas",
            "content": [
                {"type": "text", "value": "List comprehensions são muito usadas para **transformar** dados. Por exemplo, extrair uma coluna específica de uma lista de dicionários:"},
                {
                    "type": "code",
                    "caption": "Extraindo nomes",
                    "value": "produtos = [\n    {\"nome\": \"Notebook\", \"preco\": 3500},\n    {\"nome\": \"Mouse\", \"preco\": 80},\n    {\"nome\": \"Teclado\", \"preco\": 200}\n]\n\nnomes = [p[\"nome\"] for p in produtos]\nprint(nomes)   # ['Notebook', 'Mouse', 'Teclado']",
                },
                {
                    "type": "text",
                    "value": "Ou **combinar** valores de duas listas usando `zip()`:"},
                {
                    "type": "code",
                    "caption": "Combinando com zip()",
                    "value": "nomes = [\"Gabrielly\", \"Ana\", \"João\"]\nidades = [18, 25, 20]\n\npessoas = [f\"{n} tem {i} anos\" for n, i in zip(nomes, idades)]\nprint(pessoas)\n# ['Gabrielly tem 18 anos', 'Ana tem 25 anos', 'João tem 20 anos']",
                },
                {"type": "text", "value": "**Cuidado com comprehensions muito longas.** Se tiver mais de 2 níveis (for dentro de for dentro de for), volte para o `for` tradicional. **Legibilidade > esperteza.**"},
                {
                    "type": "code",
                    "caption": "Limite da legibilidade",
                    "value": "# ✅ Ainda legível\npares_ao_quadrado = [x**2 for x in range(10) if x % 2 == 0]\n\n# ❌ Ilegível — prefira for tradicional\nmatriz = [[y*2 for y in range(3) if y > 0] for x in range(3) if x != 1]",
                },
            ],
            "exercise": {
                "id": "03-05-ex2",
                "title": "Nomes dos produtos",
                "statement": "Dada a lista `produtos = [{'nome': 'Notebook'}, {'nome': 'Mouse'}, {'nome': 'Teclado'}]`, use uma **list comprehension** para criar uma lista `nomes` com apenas os valores de `'nome'`. Imprima o resultado.",
                "starter_code": "produtos = [\n    {'nome': 'Notebook'},\n    {'nome': 'Mouse'},\n    {'nome': 'Teclado'}\n]\n\n# Extraia os nomes com list comprehension\nnomes = \nprint(nomes)",
                "tests": [
                    {"validation": "output_contains_all", "expected": ["Notebook", "Mouse", "Teclado"]},
                ],
                "hint": "[p['nome'] for p in produtos]",
            },
        },
    ],
    "summary": [
        "List comprehension cria listas em uma linha.",
        "Sintaxe: [expressao for item in iteravel if condicao].",
        "Prefira for tradicional quando ficar ilegível.",
    ],
}


LESSON_03_06 = {
    "id": "03-06",
    "module_id": "03",
    "title": "Tratamento de Erros (try/except)",
    "objectives": [
        "Entender o que são exceções",
        "Usar try/except para capturar erros",
        "Conhecer os principais tipos de erro do Python",
        "Usar else e finally para controle completo",
    ],
    "reading_time_minutes": 15,
    "topics": [
        {
            "id": "topico-1",
            "title": "Capturando Erros",
            "content": [
                {"type": "text", "value": "Até agora, quando algo dá errado, o Python **para o programa** com um traceback. Em aplicações reais, isso não pode acontecer — precisamos **tratar** o erro e continuar."},
                {
                    "type": "code",
                    "caption": "O problema sem tratamento",
                    "value": "numero = int(\"abc\")   # 💥 ValueError!\nprint(\"Isso nunca executa\")",
                },
                {"type": "text", "value": "A solução é o **`try/except`**. Tudo que pode dar erro fica no `try`, e o tratamento no `except`."},
                {
                    "type": "code",
                    "caption": "try/except básico",
                    "value": "try:\n    numero = int(\"abc\")\n    print(numero)\nexcept ValueError:\n    print(\"Isso não é um número válido\")\n\n# Saída: Isso não é um número válido",
                },
                {"type": "text", "value": "**Principais exceções que você vai encontrar:**"},
                {
                    "type": "code",
                    "caption": "Tipos de erro mais comuns",
                    "value": "ValueError       → conversão/valor inválido (ex: int(\"abc\"))\nTypeError        → tipo errado (ex: \"10\" + 5)\nZeroDivisionError → divisão por zero\nKeyError         → chave não existe em dicionário\nIndexError       → índice fora do intervalo\nFileNotFoundError → arquivo não encontrado",
                },
                {"type": "text", "value": "Você pode tratar **vários tipos** de erro diferentes em blocos separados:"},
                {
                    "type": "code",
                    "caption": "Múltiplos except",
                    "value": "try:\n    a = int(input(\"Numerador: \"))\n    b = int(input(\"Denominador: \"))\n    print(a / b)\nexcept ValueError:\n    print(\"Digite apenas números\")\nexcept ZeroDivisionError:\n    print(\"Não é possível dividir por zero\")",
                },
            ],
            "exercise": {
                "id": "03-06-ex1",
                "title": "Tratando conversão inválida",
                "statement": "Use `try/except` para tentar converter a string `'abc'` em inteiro com `int()`. No `except ValueError`, imprima `Erro de conversão`. No `try`, não faça nada além da conversão.",
                "starter_code": "try:\n    numero = int('abc')\nexcept ValueError:\n    # imprima 'Erro de conversão'\n    ",
                "tests": [
                    {"validation": "output_equals", "expected": "Erro de conversão"},
                ],
                "hint": "Use print('Erro de conversão') dentro do except",
            },
        },
        {
            "id": "topico-2",
            "title": "else, finally e Boas Práticas",
            "content": [
                {"type": "text", "value": "O `try/except` tem dois blocos opcionais importantes: **`else`** (executa se NÃO houve erro) e **`finally`** (executa SEMPRE, com ou sem erro)."},
                {
                    "type": "code",
                    "caption": "try/except/else/finally",
                    "value": "try:\n    numero = int(\"10\")\nexcept ValueError:\n    print(\"Erro na conversão\")\nelse:\n    print(\"Conversão bem-sucedida:\", numero)\nfinally:\n    print(\"Isso roda sempre\")\n\n# Conversão bem-sucedida: 10\n# Isso roda sempre",
                },
                {"type": "text", "value": "**`finally`** é muito usado para **liberar recursos** — fechar arquivos, conexões de banco de dados, etc. Independente do que aconteceu, ele executa."},
                {"type": "text", "value": "**Boas práticas:**"},
                {
                    "type": "code",
                    "caption": "Bons e maus usos",
                    "value": "# ❌ Ruim — engole TODOS os erros sem tratamento\ntry:\n    fazer_algo()\nexcept:\n    pass\n\n# ✅ Bom — trata erros específicos e faz algo útil\ntry:\n    fazer_algo()\nexcept ValueError as e:\n    print(f\"Erro de valor: {e}\")\nexcept ConnectionError:\n    print(\"Falha na conexão. Tentando novamente...\")",
                },
                {"type": "text", "value": "O `as e` captura o objeto do erro. Você pode ver a mensagem original com `str(e)` ou `e.args`."},
                {
                    "type": "code",
                    "caption": "Capturando a mensagem do erro",
                    "value": "try:\n    int(\"abc\")\nexcept ValueError as e:\n    print(f\"Mensagem: {e}\")\n\n# Mensagem: invalid literal for int() with base 10: 'abc'",
                },
            ],
            "exercise": {
                "id": "03-06-ex2",
                "title": "Divisão segura",
                "statement": "Crie variáveis `a = 10` e `b = 0`. Use `try/except ZeroDivisionError` para tentar imprimir `a / b`. No `except`, imprima `Divisão por zero não permitida`. No `else`, imprima `Resultado: {resultado}`.",
                "starter_code": "a = 10\nb = 0\n\ntry:\n    resultado = a / b\nexcept ZeroDivisionError:\n    # imprima a mensagem de erro\n    \nelse:\n    # imprima o resultado\n    ",
                "tests": [
                    {"validation": "output_equals", "expected": "Divisão por zero não permitida"},
                ],
                "hint": "print('Divisão por zero não permitida') dentro do except",
            },
        },
    ],
    "summary": [
        "try/except captura erros sem parar o programa.",
        "else executa se não houve erro; finally sempre executa.",
        "Trate exceções específicas, não todas com except vazio.",
    ],
}


LESSON_03_07 = {
    "id": "03-07",
    "module_id": "03",
    "title": "Módulos, Pacotes e pip",
    "objectives": [
        "Entender o que são módulos e pacotes",
        "Importar módulos com import e from",
        "Usar módulos da biblioteca padrão do Python",
        "Instalar bibliotecas externas com pip",
    ],
    "reading_time_minutes": 12,
    "topics": [
        {
            "id": "topico-1",
            "title": "Importando Módulos",
            "content": [
                {"type": "text", "value": "Um **módulo** é um arquivo `.py` com funções, classes e variáveis que podem ser **reutilizados** em outros programas. Um **pacote** é uma pasta com vários módulos."},
                {"type": "text", "value": "A forma mais comum de importar é com **`import`**:"},
                {
                    "type": "code",
                    "caption": "import básico",
                    "value": "import math\n\nprint(math.pi)          # 3.141592653589793\nprint(math.sqrt(16))    # 4.0\nprint(math.ceil(4.2))   # 5",
                },
                {"type": "text", "value": "Você também pode importar **funções específicas** com `from`:"},
                {
                    "type": "code",
                    "caption": "from ... import",
                    "value": "from math import sqrt, pi\n\nprint(sqrt(25))   # 5.0\nprint(pi)         # 3.141592653589793",
                },
                {"type": "text", "value": "Ou dar um **apelido** com `as` (útil para nomes longos):"},
                {
                    "type": "code",
                    "caption": "Apelido com as",
                    "value": "import math as m\nprint(m.sqrt(9))   # 3.0\n\nimport random as rnd\nprint(rnd.randint(1, 6))   # dado de 1 a 6",
                },
            ],
            "exercise": {
                "id": "03-07-ex1",
                "title": "Usando math",
                "statement": "Importe o módulo `math` e use `math.sqrt()` para calcular a raiz quadrada de `144`. Imprima o resultado.",
                "starter_code": "import math\n\n# Calcule a raiz quadrada de 144\nprint()",
                "tests": [
                    {"validation": "output_equals", "expected": "12.0"},
                ],
                "hint": "print(math.sqrt(144))",
            },
        },
        {
            "id": "topico-2",
            "title": "Biblioteca Padrão e pip",
            "content": [
                {"type": "text", "value": "O Python vem com uma **biblioteca padrão gigante** — centenas de módulos prontos para usar. Alguns dos mais úteis:"},
                {
                    "type": "code",
                    "caption": "Módulos essenciais da stdlib",
                    "value": "math      → funções matemáticas\nrandom    → números aleatórios\ndatetime  → datas e horários\njson      → ler/gravar JSON\nos        → sistema operacional\nre        → expressões regulares\ncollections → estruturas extras (Counter, deque)",
                },
                {"type": "text", "value": "**Bibliotecas externas** são instaladas via **`pip`**. Por exemplo, para instalar a biblioteca `requests` (para fazer requisições HTTP):"},
                {
                    "type": "code",
                    "caption": "Instalando com pip",
                    "value": "# No terminal:\npip install requests\n\n# Depois no código:\nimport requests\n\nresposta = requests.get(\"https://api.github.com\")\nprint(resposta.status_code)",
                },
                {"type": "text", "value": "**Boas práticas:** cada projeto deve ter um arquivo `requirements.txt` listando suas dependências. Para gerar:"},
                {
                    "type": "code",
                    "caption": "requirements.txt",
                    "value": "# No terminal:\npip freeze > requirements.txt\n\n# Para instalar tudo depois:\npip install -r requirements.txt",
                },
            ],
            "exercise": {
                "id": "03-07-ex2",
                "title": "Número aleatório",
                "statement": "Importe o módulo `random`. Use a semente `random.seed(42)` para garantir resultado determinístico. Depois, use `random.randint(1, 6)` e imprima o resultado. O valor esperado com seed 42 é `1`.",
                "starter_code": "import random\n\nrandom.seed(42)\n\n# Gere um número de 1 a 6\nnumero = \nprint(numero)",
                "tests": [
                    {"validation": "output_equals", "expected": "1"},
                ],
                "hint": "numero = random.randint(1, 6)",
            },
        },
    ],
    "summary": [
        "Módulos reutilizam código entre arquivos.",
        "import, from ... import e as cobrem todos os casos.",
        "Python tem stdlib gigante; pip instala bibliotecas externas.",
    ],
}


LESSON_03_08 = {
    "id": "03-08",
    "module_id": "03",
    "title": "Ambientes Virtuais (venv)",
    "objectives": [
        "Entender por que usar ambientes virtuais",
        "Criar e ativar um venv",
        "Instalar dependências isoladas por projeto",
        "Saber quando usar venv",
    ],
    "reading_time_minutes": 10,
    "topics": [
        {
            "id": "topico-1",
            "title": "Isolando Dependências",
            "content": [
                {"type": "text", "value": "Imagine que você tem **dois projetos**: um precisa da versão 2.0 da biblioteca `requests`, o outro precisa da versão 1.5. Se você instalar globalmente, vai ter conflito."},
                {"type": "text", "value": "**Ambiente virtual (venv)** é uma pasta isolada que contém uma cópia do Python + as bibliotecas específicas do projeto. Cada projeto tem seu próprio venv."},
                {"type": "text", "value": "**Passo a passo para criar um venv:**"},
                {
                    "type": "code",
                    "caption": "Criando um venv",
                    "value": "# No terminal, dentro da pasta do projeto:\npython -m venv venv\n\n# Ativar no Windows:\nvenv\\Scripts\\activate\n\n# Ativar no Mac/Linux:\nsource venv/bin/activate",
                },
                {"type": "text", "value": "Quando ativo, você vê **`(venv)`** no início do prompt do terminal. A partir daí, qualquer `pip install` instala **só no venv**."},
                {
                    "type": "code",
                    "caption": "Usando o venv ativo",
                    "value": "(venv) C:\\projeto> pip install requests\n\n# Instalou só neste venv\n(venv) C:\\projeto> python main.py",
                },
                {"type": "text", "value": "Para **desativar**, digite `deactivate`. Para **remover**, é só apagar a pasta `venv`."},
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "venv isola dependências por projeto.",
        "Criar: python -m venv venv.",
        "Ativar no Windows: venv\\Scripts\\activate.",
        "Nunca commite a pasta venv — coloque no .gitignore.",
    ],
}


LESSON_03_09 = {
    "id": "03-09",
    "module_id": "03",
    "title": "Manipulação de Arquivos e JSON",
    "objectives": [
        "Ler e escrever arquivos de texto",
        "Usar o gerenciador de contexto with",
        "Trabalhar com JSON (gravar e ler)",
        "Persistir dados entre execuções do programa",
    ],
    "reading_time_minutes": 15,
    "topics": [
        {
            "id": "topico-1",
            "title": "Lendo e Escrevendo Arquivos",
            "content": [
                {"type": "text", "value": "Programas precisam **guardar informações** entre execuções — logs, configurações, dados do usuário. Para isso usamos arquivos."},
                {"type": "text", "value": "A forma correta usa **`with`**, que fecha o arquivo automaticamente mesmo se der erro:"},
                {
                    "type": "code",
                    "caption": "Escrevendo um arquivo",
                    "value": "with open(\"nota.txt\", \"w\", encoding=\"utf-8\") as arquivo:\n    arquivo.write(\"Olá, mundo!\\n\")\n    arquivo.write(\"Segunda linha\\n\")",
                },
                {
                    "type": "code",
                    "caption": "Lendo um arquivo",
                    "value": "with open(\"nota.txt\", \"r\", encoding=\"utf-8\") as arquivo:\n    conteudo = arquivo.read()\n    print(conteudo)\n\n# Olá, mundo!\n# Segunda linha",
                },
                {"type": "text", "value": "Os **modos** mais importantes são:"},
                {
                    "type": "code",
                    "caption": "Modos de abertura",
                    "value": "\"r\"  → leitura (padrão) — erro se não existir\n\"w\"  → escrita — SOBRESCREVE o arquivo\n\"a\"  → append — adiciona no final\n\"x\"  → cria novo — erro se existir",
                },
                {"type": "text", "value": "Você também pode ler **linha por linha** (útil para arquivos grandes):"},
                {
                    "type": "code",
                    "caption": "Lendo linha por linha",
                    "value": "with open(\"nota.txt\", \"r\", encoding=\"utf-8\") as arquivo:\n    for linha in arquivo:\n        print(linha.strip())",
                },
            ],
            "exercise": {
                "id": "03-09-ex1",
                "title": "Escrevendo em arquivo",
                "statement": "No sandbox, use `with open('teste.txt', 'w')` para escrever a string `Python é incrível`. Depois, leia o arquivo e imprima seu conteúdo.",
                "starter_code": "with open('teste.txt', 'w', encoding='utf-8') as arquivo:\n    # escreva 'Python é incrível'\n    \n\nwith open('teste.txt', 'r', encoding='utf-8') as arquivo:\n    print(arquivo.read())",
                "tests": [
                    {"validation": "output_equals", "expected": "Python é incrível"},
                ],
                "hint": "arquivo.write('Python é incrível')",
            },
        },
        {
            "id": "topico-2",
            "title": "Trabalhando com JSON",
            "content": [
                {"type": "text", "value": "**JSON** (JavaScript Object Notation) é o formato padrão para troca de dados na web. Ele parece um dicionário Python, e o Python converte um no outro facilmente."},
                {
                    "type": "code",
                    "caption": "Exemplo de JSON",
                    "value": "{\n    \"nome\": \"Gabrielly\",\n    \"idade\": 18,\n    \"cursos\": [\"Python\", \"React\"]\n}",
                },
                {"type": "text", "value": "Para **gravar** um dicionário em JSON, use `json.dump()` com `with`:"},
                {
                    "type": "code",
                    "caption": "Escrevendo JSON",
                    "value": "import json\n\nusuario = {\n    \"nome\": \"Gabrielly\",\n    \"idade\": 18,\n    \"cursos\": [\"Python\", \"React\"]\n}\n\nwith open(\"usuario.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(usuario, f, ensure_ascii=False, indent=2)",
                },
                {"type": "text", "value": "Para **ler**, use `json.load()`:"},
                {
                    "type": "code",
                    "caption": "Lendo JSON",
                    "value": "with open(\"usuario.json\", \"r\", encoding=\"utf-8\") as f:\n    usuario = json.load(f)\n\nprint(usuario[\"nome\"])    # Gabrielly\nprint(usuario[\"cursos\"])  # ['Python', 'React']",
                },
                {"type": "text", "value": "**Dica profissional:** sempre use `ensure_ascii=False` para preservar acentos e emojis, e `indent=2` para deixar o JSON legível."},
            ],
            "exercise": {
                "id": "03-09-ex2",
                "title": "Converter dicionário para JSON",
                "statement": "Importe `json`. Use `json.dumps()` para converter o dicionário `{'nome': 'Gabrielly', 'idade': 18}` em uma string JSON. Imprima o resultado (sem espaços).",
                "starter_code": "import json\n\ndados = {'nome': 'Gabrielly', 'idade': 18}\n\n# Converta para JSON\nresultado = \nprint(resultado)",
                "tests": [
                    {"validation": "output_contains_all", "expected": ["Gabrielly", "18"]},
                ],
                "hint": "json.dumps(dados, ensure_ascii=False)",
            },
        },
    ],
    "summary": [
        "Use with open() para ler/escrever arquivos com segurança.",
        "Modos: r (leitura), w (escrita), a (append).",
        "json.dump() grava; json.load() lê arquivos JSON.",
    ],
}


LESSON_03_10 = {
    "id": "03-10",
    "module_id": "03",
    "title": "Programação Orientada a Objetos (POO)",
    "objectives": [
        "Entender o conceito de classes e objetos",
        "Criar classes com atributos e métodos",
        "Usar o método __init__ para inicializar objetos",
        "Aplicar herança e boas práticas de POO",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "topico-1",
            "title": "Classes e Objetos",
            "content": [
                {"type": "text", "value": "Até agora criamos programas com **funções soltas**. POO é uma forma de **organizar o código** agrupando dados e comportamentos em **objetos**."},
                {"type": "text", "value": "Uma **classe** é o **molde**; um **objeto** é o que você cria a partir desse molde. Por exemplo: `Cachorro` é a classe, `rex` é o objeto."},
                {
                    "type": "code",
                    "caption": "Primeira classe",
                    "value": "class Pessoa:\n    def __init__(self, nome, idade):\n        self.nome = nome\n        self.idade = idade\n\n    def apresentar(self):\n        return f\"Sou {self.nome} e tenho {self.idade} anos\"\n\n# Criando objetos (instâncias)\ngabrielly = Pessoa(\"Gabrielly\", 18)\njoao = Pessoa(\"João\", 25)\n\nprint(gabrielly.apresentar())\nprint(joao.apresentar())",
                },
                {"type": "text", "value": "O método **`__init__`** é chamado automaticamente ao criar o objeto. É onde definimos os **atributos iniciais** (dados do objeto)."},
                {"type": "text", "value": "O **`self`** representa o próprio objeto. É sempre o primeiro parâmetro dos métodos de instância. Pense nele como \"eu mesmo\"."},
                {
                    "type": "code",
                    "caption": "Atributos e métodos",
                    "value": "gabrielly = Pessoa(\"Gabrielly\", 18)\n\n# Atributos (dados)\nprint(gabrielly.nome)    # Gabrielly\nprint(gabrielly.idade)   # 18\n\n# Métodos (comportamentos)\nprint(gabrielly.apresentar())",
                },
            ],
            "exercise": {
                "id": "03-10-ex1",
                "title": "Sua primeira classe",
                "statement": "Crie uma classe `Carro` com `__init__` recebendo `marca` e `ano`, guardando em `self.marca` e `self.ano`. Adicione um método `descricao()` que retorna `{marca} - {ano}`. Crie um objeto com `'Fiat'` e `2020`, e imprima o resultado de `descricao()`.",
                "starter_code": "class Carro:\n    def __init__(self, marca, ano):\n        # guarde marca e ano em self\n        \n    \n    def descricao(self):\n        # retorne 'marca - ano'\n        \n\ncarro = Carro('Fiat', 2020)\nprint(carro.descricao())",
                "tests": [
                    {"validation": "output_equals", "expected": "Fiat - 2020"},
                ],
                "hint": "self.marca = marca, self.ano = ano. No método: return f\"{self.marca} - {self.ano}\"",
            },
        },
        {
            "id": "topico-2",
            "title": "Herança e Boas Práticas",
            "content": [
                {"type": "text", "value": "**Herança** permite que uma classe **herde** atributos e métodos de outra. Isso evita repetição e organiza hierarquias."},
                {
                    "type": "code",
                    "caption": "Herança entre classes",
                    "value": "class Animal:\n    def __init__(self, nome):\n        self.nome = nome\n\n    def fazer_som(self):\n        return \"...\"\n\n\nclass Cachorro(Animal):\n    def fazer_som(self):\n        return \"Au au!\"\n\n\nclass Gato(Animal):\n    def fazer_som(self):\n        return \"Miau!\"\n\n\nrex = Cachorro(\"Rex\")\nmimi = Gato(\"Mimi\")\n\nprint(rex.nome, rex.fazer_som())     # Rex Au au!\nprint(mimi.nome, mimi.fazer_som())   # Mimi Miau!",
                },
                {"type": "text", "value": "A classe `Cachorro` **herda** de `Animal` (o `Animal` entre parênteses). Ela ganha o `__init__` e o `nome`, e **sobrescreve** o `fazer_som()`."},
                {"type": "text", "value": "**Princípios de POO que você vai usar sempre:**"},
                {
                    "type": "code",
                    "caption": "Princípios essenciais",
                    "value": "1. Encapsulamento → agrupar dados + comportamentos\n2. Herança        → reutilizar código entre classes\n3. Polimorfismo   → mesma interface, comportamentos diferentes\n4. Abstração      → esconder complexidade, expor o essencial",
                },
                {"type": "text", "value": "**Onde POO aparece no mundo real:** Django (models), FastAPI (schemas Pydantic), SQLAlchemy (ORM), bibliotecas de UI. POO é a base de frameworks profissionais."},
                {"type": "text", "value": "**Dica final:** não exagere. POO não é obrigatória em todo projeto. Use quando faz sentido — quando há **entidades com dados e comportamentos**."},
            ],
            "exercise": {
                "id": "03-10-ex2",
                "title": "Herança na prática",
                "statement": "Crie uma classe `Animal` com `__init__(self, nome)` que guarda `self.nome`. Crie `Cachorro` herdando de `Animal` e sobrescreva o método `falar()` para retornar `'Au au'`. Crie um cachorro chamado `'Rex'` e imprima o resultado de `falar()`.",
                "starter_code": "class Animal:\n    def __init__(self, nome):\n        self.nome = nome\n\n\nclass Cachorro(Animal):\n    def falar(self):\n        # retorne 'Au au'\n        \n\nrex = Cachorro('Rex')\nprint(rex.falar())",
                "tests": [
                    {"validation": "output_equals", "expected": "Au au"},
                ],
                "hint": "return 'Au au' dentro do método falar()",
            },
        },
    ],
    "summary": [
        "Classe é o molde; objeto é a instância.",
        "__init__ inicializa atributos; self representa o objeto.",
        "Herança reutiliza código entre classes relacionadas.",
        "POO organiza projetos grandes e é base de frameworks.",
    ],
}


