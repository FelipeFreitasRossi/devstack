"""
lessons_content.py
==================
Conteúdo das lições do Módulo 01 — Lógica de Programação.

Cada lição tem uma lista de "topics", cada tópico tem "content" (blocos
de texto/código) e um "exercise" opcional com validação.
"""

from app.analytics import CURRICULUM

LESSON_01_01 = {
    "id": "01-01",
    "module_id": "01",
    "title": "Fundamentos da Programação",
    "objectives": [
        "Entender o que é programação e por que ela move o mundo moderno",
        "Saber como um computador executa instruções passo a passo",
        "Compreender o que é um algoritmo e como pensar como programador",
        "Diferenciar código, programa e algoritmo com exemplos reais",
        "Entender a indentação em Python e por que ela é obrigatória",
        "Escrever seus primeiros comandos em Python",
    ],
    "reading_time_minutes": 34,
    "topics": [
        {
            "id": "topico-1",
            "title": "O que é Programar?",
            "content": [
                {"type": "text", "value": "Antes de escrever uma linha de código, você precisa entender **o que é programação**. Não é decorar comandos — é aprender a resolver problemas dando instruções claras para um computador executar."},
                {"type": "text", "value": "Pense no aplicativo do banco que você usa todo dia. Quando você faz um Pix de R$ 50, existe uma sequência enorme de instruções acontecendo em milissegundos: validar sua senha, verificar o saldo, registrar a transação, notificar o destinatário. **Tudo isso é programação.**"},
                {"type": "text", "value": "Computadores são incrivelmente rápidos, mas não pensam sozinhos. Eles fazem **exatamente** o que mandamos — nem mais, nem menos. Se você errar uma vírgula, ele erra com você."},
                {"type": "text", "value": "**Programar é transformar problemas do mundo real em instruções que o computador consegue executar.**"},
                {
                    "type": "code",
                    "caption": "Seu primeiro contato com código Python",
                    "value": "print(\"Olá, mundo!\")\n\n# O computador lê essa linha e escreve na tela:\n# Olá, mundo!",
                },
                {"type": "text", "value": "Uma única linha `print(...)` já é programação. É pouco, mas é o mesmo princípio que roda por trás de sistemas gigantes como Netflix, iFood e Uber."},
            ],
            "exercise": {
                "id": "01-01-ex1",
                "title": "Calcular idade",
                "statement": "Crie uma variável `ano_atual` com o valor `2026` e uma variável `ano_nascimento` com o valor `2008`. Calcule a `idade` subtraindo o ano de nascimento do ano atual e imprima o resultado.",
                "starter_code": "ano_atual = 2026\nano_nascimento = 2008\n\n# Calcule a idade e imprima\nidade = \nprint(idade)",
                "tests": [
                    {"validation": "output_equals", "expected": "18"},
                    {"validation": "output_not_contains", "value": "-"},
                ],
                "hint": "Use o operador `-` para subtrair: idade = ano_atual - ano_nascimento",
            },
        },
        {
            "id": "topico-2",
            "title": "Indentação — O Espaço no Começo da Linha",
            "content": [
                {"type": "text", "value": "Antes de continuar, você precisa entender um dos conceitos **mais importantes do Python**: a **indentação**. É provavelmente a primeira coisa que vai te confundir, mas depois que entender, nunca mais erra."},
                {"type": "text", "value": "**Indentação é o espaço em branco no começo da linha.** Em muitas linguagens (Java, C, JavaScript), a indentação é só estética — o código funciona com ou sem ela. **No Python, ela é obrigatória.** É a forma que o Python usa para saber onde um bloco de código começa e termina."},
                {"type": "text", "value": "Olhe a diferença entre esses dois códigos:"},
                {
                    "type": "code",
                    "caption": "Sem indentação (fora de bloco)",
                    "value": "print(\"Olá\")\nprint(\"Mundo\")",
                },
                {
                    "type": "code",
                    "caption": "Com indentação (dentro de um bloco)",
                    "value": "if True:\n    print(\"Olá\")\n    print(\"Mundo\")",
                },
                {"type": "text", "value": "No primeiro, as duas linhas estão no **mesmo nível** — o Python executa as duas direto. No segundo, as linhas `print` estão **dentro do bloco do if** por causa dos 4 espaços no começo. Isso muda completamente o comportamento."},
                {"type": "text", "value": "**A regra é simples:** sempre que uma linha termina com `:` (dois pontos), a próxima linha precisa estar **indentada** (com espaço no começo). Isso indica que aquelas linhas pertencem ao bloco que acabou de ser aberto."},
                {
                    "type": "code",
                    "caption": "Linhas terminando em : abrem blocos",
                    "value": "if idade >= 18:\n    print(\"Maior de idade\")   # dentro do if\n\nfor i in range(3):\n    print(i)                 # dentro do for\n\ndef saudacao():\n    print(\"Olá\")             # dentro da função",
                },
                {"type": "text", "value": "**Quantos espaços usar?** O padrão oficial do Python (PEP 8) é **4 espaços**. Não use Tab, use 4 espaços. A maioria dos editores (como o VS Code) insere 4 espaços automaticamente quando você aperta Tab."},
                {
                    "type": "code",
                    "caption": "Indentação correta vs errada",
                    "value": "# ✅ CORRETO\nif idade >= 18:\n    print(\"Maior de idade\")\n    print(\"Pode dirigir\")\n\n# ❌ ERRADO (vai dar erro)\nif idade >= 18:\nprint(\"Maior de idade\")   # faltou a indentação",
                },
                {"type": "text", "value": "Se você esquecer a indentação, o Python vai te mostrar um erro: **`IndentationError: expected an indented block`**. Não entre em pânico — é só adicionar os 4 espaços no começo da linha."},
                {"type": "text", "value": "**Por que o Python funciona assim?** Porque sem indentação, o Python não teria como saber o que está dentro ou fora de um bloco. A indentação **é** a sintaxe do Python. É uma escolha da linguagem — e depois que você se acostuma, o código fica muito mais legível."},
                {
                    "type": "code",
                    "caption": "Exemplo visual: dentro vs fora do bloco",
                    "value": "if idade >= 18:\n    print(\"Linha 1 — dentro do if\")\n    print(\"Linha 2 — dentro do if\")\n\nprint(\"Linha 3 — FORA do if\")\n\n# As linhas 1 e 2 só executam se idade >= 18.\n# A linha 3 executa sempre.",
                },
                {"type": "text", "value": "**Resumo rápido:** sempre que uma linha termina com `:`, a próxima linha precisa começar com 4 espaços. Se a linha seguinte volta a ficar sem espaço, significa que o bloco terminou."},
            ],
            "exercise": {
                "id": "01-01-ex2",
                "title": "Praticando indentação",
                "statement": "Crie uma variável `idade = 20`. Use um `if` para verificar se `idade >= 18`. Dentro do bloco do if, imprima `'Maior de idade'`. **Atenção: não esqueça da indentação de 4 espaços!**",
                "starter_code": "idade = 20\n\nif idade >= 18:\n# imprima 'Maior de idade' aqui (com 4 espaços de indentação)\n",
                "tests": [
                    {"validation": "output_equals", "expected": "Maior de idade"},
                ],
                "hint": "A linha do print precisa começar com 4 espaços:     print('Maior de idade')",
            },
        },
        {
            "id": "topico-3",
            "title": "Pensando como Programador",
            "content": [
                {"type": "text", "value": "Agora que você já sabe escrever código e entende a indentação, vamos falar sobre a diferença entre **saber escrever código** e **saber programar**. Programar é, antes de tudo, **resolver problemas**."},
                {"type": "text", "value": "Imagine que você precisa calcular a média de três notas de um aluno. Antes de escrever qualquer código, você pensa na solução passo a passo:"},
                {
                    "type": "code",
                    "caption": "Algoritmo — cálculo de média (sem código ainda)",
                    "value": "1. Receber a primeira nota\n2. Receber a segunda nota\n3. Receber a terceira nota\n4. Somar as três notas\n5. Dividir o resultado por 3\n6. Mostrar a média",
                },
                {"type": "text", "value": "Isso é um **algoritmo**: uma sequência organizada de passos para resolver um problema. Você usa algoritmos todos os dias — escovar os dentes, seguir uma receita, dar instruções a alguém."},
                {"type": "text", "value": "A grande sacada é: **primeiro pensamos na solução, depois escrevemos o código**. Muitos iniciantes erram porque tentam programar direto, sem pensar no fluxo."},
                {
                    "type": "code",
                    "caption": "Só depois traduzimos para Python",
                    "value": "nota1 = 8\nnota2 = 7\nnota3 = 9\n\nmedia = (nota1 + nota2 + nota3) / 3\nprint(media)   # 8.0",
                },
                {"type": "text", "value": "Perceba que o código é só a **tradução** do pensamento. Se o pensamento está certo, o código flui naturalmente."},
                {
                    "type": "code",
                    "caption": "Outro algoritmo do dia a dia — sair de casa",
                    "value": "1. Verificar se está chovendo\n2. Se estiver chovendo, levar guarda-chuva\n3. Caso contrário, sair sem guarda-chuva",
                },
                {"type": "text", "value": "Algoritmos podem ter **decisões** (if) e **repetições** (loops). Você vai aprender isso em detalhes nos próximos módulos."},
            ],
            "exercise": {
                "id": "01-01-ex3",
                "title": "Calcular total da compra",
                "statement": "Imagine que uma pessoa comprou 3 produtos de R$ 20 cada. Crie duas variáveis: `preco` com o valor `20` e `quantidade` com o valor `3`. Calcule o `total` multiplicando os dois e imprima o resultado.",
                "starter_code": "preco = 20\nquantidade = 3\n\n# Calcule o total e imprima\ntotal = \nprint(total)",
                "tests": [
                    {"validation": "output_equals", "expected": "60"},
                ],
                "hint": "Use o operador `*` para multiplicar: total = preco * quantidade",
            },
        },
    ],
    "summary": [
        "Programar é traduzir problemas do mundo real em instruções para o computador.",
        "Indentação é o espaço no começo da linha e é OBRIGATÓRIA em Python.",
        "Sempre que uma linha termina com `:`, a próxima precisa ter 4 espaços de indentação.",
        "Primeiro pensamos na solução, depois escrevemos o código.",
    ],
}


# ============================================================================
# LIÇÃO 01-03 — Variáveis e Constantes (2 tópicos)
# ============================================================================
LESSON_01_03 = {
    "id": "01-03",
    "module_id": "01",
    "title": "Variáveis e Constantes",
    "objectives": [
        "Entender o que são variáveis e por que usamos",
        "Criar e nomear variáveis corretamente em Python",
        "Alterar valores de variáveis durante a execução",
        "Diferenciar variáveis de constantes",
        "Usar variáveis em cálculos matemáticos",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "topico-1",
            "title": "O que é uma Variável?",
            "content": [
                {"type": "text", "value": "Uma **variável** é um espaço na memória do computador que guarda uma informação. Pense nela como uma **caixa etiquetada**: você dá um nome, coloca um valor dentro e pode trocar esse valor quando quiser."},
                {
                    "type": "code",
                    "caption": "Visualizando uma variável",
                    "value": "┌───────────────┐\n│    idade      │   ← nome da variável\n├───────────────┤\n│      18       │   ← valor armazenado\n└───────────────┘",
                },
                {"type": "text", "value": "Em Python, criamos uma variável simplesmente atribuindo um valor a um nome:"},
                {
                    "type": "code",
                    "caption": "Criando uma variável",
                    "value": "idade = 18\n\n# idade → nome da variável\n# 18    → valor armazenado\n# =     → operador de atribuição",
                },
                {"type": "text", "value": "Podemos armazenar diferentes tipos de informação em variáveis: textos, números inteiros, números decimais, etc."},
                {
                    "type": "code",
                    "caption": "Vários tipos de variáveis",
                    "value": "nome = \"Felipe\"\nidade = 18\naltura = 1.75\n\nprint(nome)\nprint(idade)\nprint(altura)",
                },
                {"type": "text", "value": "**Boas práticas para nomear variáveis:** use nomes descritivos (não `x`), comece com letra minúscula, use underline para separar palavras (`nome_completo`), evite acentos e caracteres especiais."},
                {
                    "type": "code",
                    "caption": "Bons vs maus nomes",
                    "value": "# Bons nomes\nnome_completo = \"Felipe Rossi\"\nidade_usuario = 25\n\n# Ruins\nx = \"Felipe Rossi\"     # não descreve\nNomeCompleto = \"...\"  # CamelCase não é padrão em Python",
                },
            ],
            "exercise": {
                "id": "01-03-ex1",
                "title": "Crie suas primeiras variáveis",
                "statement": "Crie três variáveis: `nome` com o valor `'Felipe'`, `idade` com o valor `18` e `cidade` com o valor `'São Carlos'`. Depois, imprima cada uma em uma linha separada (na ordem: nome, idade, cidade).",
                "starter_code": "# Crie as três variáveis\nnome = \nidade = \ncidade = \n\n# Imprima cada uma em uma linha\nprint(nome)\nprint(idade)\nprint(cidade)",
                "tests": [
                    {"validation": "output_equals", "expected": "São Carlos"},
                    {"validation": "output_line_count", "expected": 3},
                ],
                "hint": "nome = 'Felipe' (com aspas), idade = 18 (sem aspas), cidade = 'São Carlos'",
            },
        },
        {
            "id": "topico-2",
            "title": "Alterando Valores e Constantes",
            "content": [
                {"type": "text", "value": "Uma variável pode ter seu valor **alterado** durante a execução do programa. É justamente por isso que ela se chama **variável**: o valor pode variar."},
                {
                    "type": "code",
                    "caption": "Alterando o valor de uma variável",
                    "value": "idade = 18\nprint(idade)   # 18\n\nidade = 19\nprint(idade)   # 19 (o valor anterior foi substituído)",
                },
                {"type": "text", "value": "Também podemos usar variáveis em **cálculos matemáticos**:"},
                {
                    "type": "code",
                    "caption": "Variáveis em cálculos",
                    "value": "numero1 = 10\nnumero2 = 5\n\nresultado = numero1 + numero2\nprint(resultado)   # 15",
                },
                {"type": "text", "value": "Isso torna nossos programas muito mais úteis, porque podemos trabalhar com dados que mudam."},
                {"type": "text", "value": "**Constantes** são valores que, por convenção, **não devem mudar** durante a execução. O Python não tem uma palavra-chave específica para constantes, então usamos nomes em **LETRAS MAIÚSCULAS** para indicar essa intenção."},
                {
                    "type": "code",
                    "caption": "Constantes em Python",
                    "value": "PI = 3.14159\nTAXA_JUROS = 0.10\nIMPOSTO = 0.27\n\n# Ao ver uma variável em MAIÚSCULAS,\n# o programador sabe que ela não deve ser alterada.",
                },
                {
                    "type": "code",
                    "caption": "Exemplo prático — cálculo com imposto",
                    "value": "preco = 100\nIMPOSTO = 0.10\n\nvalor_imposto = preco * IMPOSTO\ntotal = preco + valor_imposto\n\nprint(total)   # 110.0",
                },
            ],
            "exercise": {
                "id": "01-03-ex2",
                "title": "Cálculo com variáveis",
                "statement": "Crie duas variáveis: `numero1 = 10` e `numero2 = 5`. Calcule o `resultado` somando os dois valores e imprima o resultado.",
                "starter_code": "numero1 = 10\nnumero2 = 5\n\n# Calcule a soma e imprima\nresultado = \nprint(resultado)",
                "tests": [
                    {"validation": "output_equals", "expected": "15"},
                ],
                "hint": "resultado = numero1 + numero2",
            },
        },
    ],
    "summary": [
        "Variável é um espaço nomeado que guarda um valor.",
        "Use nomes descritivos em minúsculas com underline.",
        "Constantes usam MAIÚSCULAS por convenção.",
    ],
}


# ============================================================================
# LIÇÃO 01-04 — Tipos de Dados
# ============================================================================
LESSON_01_04 = {
    "id": "01-04",
    "module_id": "01",
    "title": "Tipos de Dados",
    "objectives": [
        "Conhecer os principais tipos de dados do Python",
        "Trabalhar com textos (str), inteiros (int), decimais (float) e booleanos (bool)",
        "Usar a função type() para descobrir o tipo de um valor",
        "Converter valores entre tipos diferentes",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "topico-1",
            "title": "Os 4 Tipos Básicos",
            "content": [
                {"type": "text", "value": "Cada valor em Python tem um **tipo**. O tipo diz ao Python como ele deve tratar aquele dado — se é texto, número inteiro, número decimal ou verdadeiro/falso."},
                {
                    "type": "code",
                    "caption": "Tipos primitivos em ação",
                    "value": "\"Felipe\"  → texto        (str)\n18        → inteiro      (int)\n1.75      → decimal      (float)\nTrue      → booleano     (bool)",
                },
                {"type": "text", "value": "**Strings (str)** representam textos. Ficam entre aspas simples ou duplas — dá no mesmo."},
                {
                    "type": "code",
                    "caption": "Strings",
                    "value": "nome = \"Felipe\"\ncidade = 'São Carlos'\n\n# Aspas simples e duplas funcionam igual.",
                },
                {"type": "text", "value": "**Inteiros (int)** são números sem casas decimais."},
                {
                    "type": "code",
                    "caption": "Inteiros",
                    "value": "idade = 18\nquantidade = 10\nano = 2026",
                },
                {"type": "text", "value": "**Decimais (float)** são números com casas decimais. Sempre usam ponto (não vírgula) em Python."},
                {
                    "type": "code",
                    "caption": "Floats",
                    "value": "altura = 1.75\npreco = 29.90\ntemperatura = 25.5",
                },
                {"type": "text", "value": "**Booleanos (bool)** representam dois estados: `True` (verdadeiro) ou `False` (falso). Usados para decisões."},
                {
                    "type": "code",
                    "caption": "Booleanos",
                    "value": "maior_de_idade = True\nesta_chovendo = False\nusuario_logado = True",
                },
            ],
            "exercise": {
                "id": "01-04-ex1",
                "title": "Descobrir o tipo de cada valor",
                "statement": "Crie quatro variáveis: `texto = 'Olá'`, `inteiro = 42`, `decimal = 3.14` e `logico = True`. Depois, imprima `type()` de cada uma, uma por linha (na ordem: texto, inteiro, decimal, logico).",
                "starter_code": "texto = 'Olá'\ninteiro = 42\ndecimal = 3.14\nlogico = True\n\n# Imprima o tipo de cada uma\nprint(type(texto))\nprint(type(inteiro))\nprint(type(decimal))\nprint(type(logico))",
                "tests": [
                    {"validation": "output_contains_all", "expected": ["str", "int", "float", "bool"]},
                ],
                "hint": "Basta usar print(type(variavel)) para cada uma",
            },
        },
        {
            "id": "topico-2",
            "title": "Conversão de Tipos",
            "content": [
                {"type": "text", "value": "Às vezes precisamos **transformar** um tipo em outro. Por exemplo, o `input()` sempre retorna texto (str), mesmo que o usuário digite um número."},
                {
                    "type": "code",
                    "caption": "O problema do input()",
                    "value": "idade = input(\"Digite sua idade: \")\n\n# Se o usuário digitar 18,\n# idade será a STRING \"18\", não o número 18.",
                },
                {"type": "text", "value": "Para transformar texto em número, usamos as funções de conversão: `int()`, `float()`, `str()` e `bool()`."},
                {
                    "type": "code",
                    "caption": "Convertendo tipos",
                    "value": "idade_texto = \"18\"\nidade_numero = int(idade_texto)\n\nprint(idade_numero + 2)   # 20",
                },
                {
                    "type": "code",
                    "caption": "input() com conversão direta",
                    "value": "idade = int(input(\"Digite sua idade: \"))\n\n# Agora idade já é um número inteiro",
                },
                {"type": "text", "value": "**Atenção:** se você tentar converter algo que não é número (`int(\"abc\")`), o Python vai dar erro. Sempre valide ou trate o erro."},
                {
                    "type": "code",
                    "caption": "Conversões mais comuns",
                    "value": "int(\"25\")       # 25    (texto → inteiro)\nfloat(\"3.14\")   # 3.14  (texto → decimal)\nstr(42)         # \"42\"  (número → texto)\nint(3.99)       # 3     (decimal → inteiro, trunca)",
                },
            ],
            "exercise": {
                "id": "01-04-ex2",
                "title": "Converter texto em número",
                "statement": "Crie uma variável `idade_texto` com o valor `'25'` (texto). Converta para número inteiro usando `int()` e guarde em `idade`. Depois calcule `idade_futura = idade + 5` e imprima o resultado.",
                "starter_code": "idade_texto = '25'\n\n# Converta para inteiro\nidade = \n\n# Calcule a idade futura\nidade_futura = \nprint(idade_futura)",
                "tests": [
                    {"validation": "output_equals", "expected": "30"},
                ],
                "hint": "Use int(idade_texto) para converter e idade + 5 para somar",
            },
        },
    ],
    "summary": [
        "Tipos básicos: str (texto), int (inteiro), float (decimal), bool (lógico).",
        "type() mostra o tipo de qualquer valor.",
        "int(), float() e str() convertem entre tipos.",
    ],
}


# ============================================================================
# LIÇÃO 01-05 — Operadores Aritméticos
# ============================================================================
LESSON_01_05 = {
    "id": "01-05",
    "module_id": "01",
    "title": "Operadores Aritméticos",
    "objectives": [
        "Realizar as quatro operações básicas em Python",
        "Usar operadores especiais (//, %, **)",
        "Entender a ordem de precedência dos operadores",
        "Combinar operadores em expressões complexas",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "topico-1",
            "title": "Operadores Básicos",
            "content": [
                {"type": "text", "value": "Python tem sete operadores aritméticos. Os quatro primeiros você já conhece da matemática:"},
                {
                    "type": "code",
                    "caption": "Os 4 operadores básicos",
                    "value": "10 + 5    # 15  (soma)\n10 - 5    # 5   (subtração)\n10 * 5    # 50  (multiplicação)\n10 / 5    # 2.0 (divisão)",
                },
                {"type": "text", "value": "Repare que a **divisão sempre retorna um decimal** (float), mesmo quando o resultado é inteiro. `10 / 5` retorna `2.0`, não `2`."},
                {"type": "text", "value": "Existem ainda três operadores **especiais** que você vai usar muito:"},
                {
                    "type": "code",
                    "caption": "Os 3 operadores especiais",
                    "value": "10 // 3   # 3    (divisão inteira — descarta o resto)\n10 % 3    # 1    (resto da divisão)\n2 ** 3    # 8    (potência — 2 elevado a 3)",
                },
                {"type": "text", "value": "O operador `%` (resto) é muito útil para saber se um número é **par ou ímpar**: se `numero % 2` for igual a `0`, é par."},
                {
                    "type": "code",
                    "caption": "Descobrindo se um número é par",
                    "value": "numero = 10\nprint(numero % 2)   # 0 → par\n\nnumero = 7\nprint(numero % 2)   # 1 → ímpar",
                },
            ],
            "exercise": {
                "id": "01-05-ex1",
                "title": "Operações com dois números",
                "statement": "Crie duas variáveis: `a = 15` e `b = 4`. Calcule e imprima, nesta ordem: `soma` (a + b), `subtracao` (a - b) e `multiplicacao` (a * b). Imprima cada resultado em uma linha separada.",
                "starter_code": "a = 15\nb = 4\n\n# Calcule as três operações\nsoma = \nsubtracao = \nmultiplicacao = \n\n# Imprima cada uma em uma linha\nprint(soma)\nprint(subtracao)\nprint(multiplicacao)",
                "tests": [
                    {"validation": "output_contains_all", "expected": ["19", "11", "60"]},
                    {"validation": "output_line_count", "expected": 3},
                ],
                "hint": "soma = a + b, subtracao = a - b, multiplicacao = a * b",
            },
        },
        {
            "id": "topico-2",
            "title": "Ordem das Operações",
            "content": [
                {"type": "text", "value": "Python segue as mesmas regras matemáticas de **precedência** que você aprendeu na escola. A ordem é:"},
                {
                    "type": "code",
                    "caption": "Ordem de precedência",
                    "value": "1. Parênteses ( )\n2. Potência **\n3. Multiplicação *, Divisão /, // e %\n4. Soma + e Subtração -",
                },
                {
                    "type": "code",
                    "caption": "Sem parênteses",
                    "value": "resultado = 10 + 5 * 2\nprint(resultado)   # 20\n\n# Passo a passo:\n# 5 * 2 = 10\n# 10 + 10 = 20",
                },
                {
                    "type": "code",
                    "caption": "Com parênteses (força a ordem)",
                    "value": "resultado = (10 + 5) * 2\nprint(resultado)   # 30\n\n# Agora:\n# 10 + 5 = 15\n# 15 * 2 = 30",
                },
                {"type": "text", "value": "**Dica profissional:** use parênteses mesmo quando não for obrigatório. Isso deixa o código mais legível e evita bugs."},
            ],
            "exercise": {
                "id": "01-05-ex2",
                "title": "Descobrir o resto",
                "statement": "Crie uma variável `numero = 17`. Calcule o `resto` da divisão desse número por `5` usando o operador `%` e imprima o resultado.",
                "starter_code": "numero = 17\n\n# Calcule o resto da divisão por 5\nresto = \nprint(resto)",
                "tests": [
                    {"validation": "output_equals", "expected": "2"},
                ],
                "hint": "Use o operador %: resto = numero % 5",
            },
        },
    ],
    "summary": [
        "Operadores básicos: + (soma), - (subtração), * (multiplicação), / (divisão).",
        "Operadores especiais: // (divisão inteira), % (resto), ** (potência).",
        "A precedência segue a matemática: parênteses > potência > * / > + -",
    ],
}


# ============================================================================
# LIÇÃO 01-06 — Operadores Lógicos e Relacionais
# ============================================================================
LESSON_01_06 = {
    "id": "01-06",
    "module_id": "01",
    "title": "Operadores Lógicos e Relacionais",
    "objectives": [
        "Comparar valores com os operadores relacionais",
        "Entender True e False como resultado de comparações",
        "Combinar múltiplas condições com and, or e not",
        "Construir expressões lógicas complexas",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "topico-1",
            "title": "Comparando Valores",
            "content": [
                {"type": "text", "value": "**Operadores relacionais** comparam dois valores e retornam sempre `True` ou `False`. São a base para a tomada de decisão nos programas."},
                {
                    "type": "code",
                    "caption": "Os 6 operadores relacionais",
                    "value": "10 == 10   # True   (igual)\n10 != 5    # True   (diferente)\n10 > 5     # True   (maior)\n10 < 5     # False  (menor)\n10 >= 10   # True   (maior ou igual)\n10 <= 5    # False  (menor ou igual)",
                },
                {"type": "text", "value": "**Cuidado comum:** `=` é atribuição (guarda valor), `==` é comparação (pergunta se é igual). Não confunda!"},
                {
                    "type": "code",
                    "caption": "O resultado é sempre booleano",
                    "value": "idade = 15\nresultado = idade >= 18\n\nprint(resultado)   # False\nprint(type(resultado))   # <class 'bool'>",
                },
            ],
            "exercise": {
                "id": "01-06-ex1",
                "title": "Comparando dois números",
                "statement": "Crie duas variáveis: `a = 10` e `b = 20`. Calcule e imprima `a > b` e depois `a < b`, um resultado por linha. Ambos devem aparecer como `True` ou `False`.",
                "starter_code": "a = 10\nb = 20\n\n# Compare e imprima\nprint(a > b)\nprint(a < b)",
                "tests": [
                    {"validation": "output_equals", "expected": "True"},
                    {"validation": "output_line_count", "expected": 2},
                ],
                "hint": "Só imprimir as comparações: print(a > b) e print(a < b)",
            },
        },
        {
            "id": "topico-2",
            "title": "Combinando Condições",
            "content": [
                {"type": "text", "value": "**Operadores lógicos** combinam várias condições em uma só. Python tem três:"},
                {
                    "type": "code",
                    "caption": "Os 3 operadores lógicos",
                    "value": "and  →  retorna True se AMBAS forem verdadeiras\nor   →  retorna True se PELO MENOS UMA for verdadeira\nnot  →  INVERTE o valor (True vira False e vice-versa)",
                },
                {
                    "type": "code",
                    "caption": "and — todas precisam ser verdadeiras",
                    "value": "idade = 20\ntem_documento = True\n\npode_dirigir = idade >= 18 and tem_documento\nprint(pode_dirigir)   # True",
                },
                {
                    "type": "code",
                    "caption": "or — basta uma ser verdadeira",
                    "value": "tem_dinheiro = False\ntem_cartao = True\n\npode_pagar = tem_dinheiro or tem_cartao\nprint(pode_pagar)   # True",
                },
                {
                    "type": "code",
                    "caption": "not — inverte o resultado",
                    "value": "esta_chovendo = True\n\nprint(not esta_chovendo)   # False",
                },
                {"type": "text", "value": "**Exemplo real:** uma pessoa pode entrar em uma festa se tiver **18 anos ou mais E** estiver na lista. Já para pagar a entrada, precisa ter **dinheiro OU** cartão."},
                {
                    "type": "code",
                    "caption": "Expressão complexa",
                    "value": "idade = 20\nna_lista = True\ntem_ingresso = False\n\n# Usa and + or + not juntos\npode_entrar = (idade >= 18 and na_lista) or tem_ingresso\nprint(pode_entrar)   # True",
                },
            ],
            "exercise": {
                "id": "01-06-ex2",
                "title": "Pode dirigir?",
                "statement": "Crie as variáveis `idade = 20` e `tem_cnh = True`. Calcule `pode_dirigir` (precisa ter 18 anos ou mais E ter CNH) usando o operador `and`. Imprima o resultado. A saída deve ser `True`.",
                "starter_code": "idade = 20\ntem_cnh = True\n\n# Calcule e imprima\npode_dirigir = \nprint(pode_dirigir)",
                "tests": [
                    {"validation": "output_equals", "expected": "True"},
                ],
                "hint": "pode_dirigir = idade >= 18 and tem_cnh",
            },
        },
    ],
    "summary": [
        "Operadores relacionais: ==, !=, >, <, >=, <=",
        "Sempre retornam True ou False.",
        "Operadores lógicos: and (todas), or (pelo menos uma), not (inverte).",
    ],
}


# ============================================================================
# LIÇÃO 01-07 — Estruturas Condicionais (if/else)
# ============================================================================
LESSON_01_07 = {
    "id": "01-07",
    "module_id": "01",
    "title": "Estruturas Condicionais (if/else)",
    "objectives": [
        "Usar if para executar código condicionalmente",
        "Combinar if, elif e else para múltiplos caminhos",
        "Entender a importância da indentação em Python",
        "Tomar decisões no código com base em dados",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "topico-1",
            "title": "Tomando Decisões com if",
            "content": [
                {"type": "text", "value": "Até agora, nossos programas sempre executavam **todas as linhas** na ordem. Com **condicionais**, o programa pode escolher quais linhas executar."},
                {"type": "text", "value": "O `if` significa **\"se isso for verdadeiro, execute este bloco\"**. Ele só executa o bloco se a condição for `True`."},
                {
                    "type": "code",
                    "caption": "if simples",
                    "value": "idade = 20\n\nif idade >= 18:\n    print(\"Você é maior de idade\")",
                },
                {"type": "text", "value": "**Atenção à indentação!** Em Python, o bloco do `if` precisa estar indentado (4 espaços). A indentação diz ao Python onde o bloco começa e termina."},
                {
                    "type": "code",
                    "caption": "Indentação correta vs incorreta",
                    "value": "# Correto\nif idade >= 18:\n    print(\"Maior de idade\")\n\n# Errado (vai dar erro)\nif idade >= 18:\nprint(\"Maior de idade\")   # falta indentação",
                },
                {"type": "text", "value": "Quando a condição é `False`, o bloco **não executa** e o Python pula direto para a próxima linha fora do `if`."},
            ],
            "exercise": {
                "id": "01-07-ex1",
                "title": "Verificar maioridade",
                "statement": "Crie uma variável `idade = 20`. Use `if` para verificar se `idade >= 18`. Se for verdadeiro, imprima `'Maior de idade'`. Não precisa de else.",
                "starter_code": "idade = 20\n\nif idade >= 18:\n    # imprima 'Maior de idade'\n    ",
                "tests": [
                    {"validation": "output_equals", "expected": "Maior de idade"},
                ],
                "hint": "Use print('Maior de idade') dentro do if",
            },
        },
        {
            "id": "topico-2",
            "title": "Múltiplos Caminhos com elif e else",
            "content": [
                {"type": "text", "value": "O `else` cobre o caso **contrário** do `if`. Se a condição do `if` for falsa, o `else` executa."},
                {
                    "type": "code",
                    "caption": "if / else",
                    "value": "idade = 15\n\nif idade >= 18:\n    print(\"Maior de idade\")\nelse:\n    print(\"Menor de idade\")",
                },
                {"type": "text", "value": "Quando existem **três ou mais possibilidades**, usamos `elif` (abreviação de \"else if\"). Cada `elif` testa uma nova condição, e o `else` final cobre o resto."},
                {
                    "type": "code",
                    "caption": "if / elif / else",
                    "value": "nota = 8\n\nif nota >= 9:\n    print(\"Excelente\")\nelif nota >= 7:\n    print(\"Bom\")\nelif nota >= 6:\n    print(\"Aprovado\")\nelse:\n    print(\"Reprovado\")",
                },
                {"type": "text", "value": "**Importante:** o Python testa as condições de cima para baixo e para na **primeira verdadeira**. Por isso a ordem importa."},
                {
                    "type": "code",
                    "caption": "Combinando com operadores lógicos",
                    "value": "idade = 20\nautorizado = True\n\nif idade >= 18 and autorizado:\n    print(\"Acesso permitido\")\nelse:\n    print(\"Acesso negado\")",
                },
            ],
            "exercise": {
                "id": "01-07-ex2",
                "title": "Aprovado ou reprovado",
                "statement": "Crie uma variável `nota = 7`. Se `nota >= 6`, imprima `'Aprovado'`. Senão, imprima `'Reprovado'`.",
                "starter_code": "nota = 7\n\nif nota >= 6:\n    # imprima Aprovado\n    \nelse:\n    # imprima Reprovado\n    ",
                "tests": [
                    {"validation": "output_equals", "expected": "Aprovado"},
                ],
                "hint": "Use print('Aprovado') dentro do if e print('Reprovado') dentro do else",
            },
        },
    ],
    "summary": [
        "if executa um bloco se a condição for True.",
        "else executa quando o if é False.",
        "elif permite testar várias condições em sequência.",
    ],
}


# ============================================================================
# LIÇÃO 01-08 — Estruturas de Repetição
# ============================================================================
LESSON_01_08 = {
    "id": "01-08",
    "module_id": "01",
    "title": "Estruturas de Repetição (for/while)",
    "objectives": [
        "Entender o conceito de loop (repetição)",
        "Usar for com range para repetições controladas",
        "Usar while para repetir até uma condição mudar",
        "Saber quando usar cada tipo de loop",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "topico-1",
            "title": "O Loop for",
            "content": [
                {"type": "text", "value": "Imagine que você precisa imprimir `\"Olá\"` cinco vezes. Você poderia escrever cinco `print()`. Mas imagine se precisasse imprimir 100 vezes? Ou 1 milhão?"},
                {"type": "text", "value": "**Loops** automatizam tarefas repetitivas. O `for` é usado quando você sabe **quantas vezes** quer repetir algo."},
                {
                    "type": "code",
                    "caption": "for com range",
                    "value": "for i in range(5):\n    print(\"Olá\")\n\n# Imprime 'Olá' cinco vezes",
                },
                {"type": "text", "value": "A função `range()` cria uma sequência de números. `range(5)` gera: 0, 1, 2, 3, 4. **Sempre começa em 0 e para antes do número final.**"},
                {
                    "type": "code",
                    "caption": "for mostrando os índices",
                    "value": "for i in range(5):\n    print(i)\n\n# Imprime:\n# 0\n# 1\n# 2\n# 3\n# 4",
                },
                {"type": "text", "value": "Podemos personalizar o range com **início** e **fim**: `range(1, 6)` gera 1, 2, 3, 4, 5."},
                {
                    "type": "code",
                    "caption": "range personalizado",
                    "value": "for i in range(1, 6):\n    print(i)\n\n# Imprime de 1 a 5",
                },
                {"type": "text", "value": "Também podemos percorrer **coleções** (como listas) com `for`:"},
                {
                    "type": "code",
                    "caption": "Percorrendo uma lista",
                    "value": "frutas = [\"maçã\", \"banana\", \"uva\"]\n\nfor fruta in frutas:\n    print(fruta)",
                },
            ],
            "exercise": {
                "id": "01-08-ex1",
                "title": "Contar de 1 a 5",
                "statement": "Use um `for` com `range` para imprimir os números de `1` a `5`, um por linha (5 linhas no total).",
                "starter_code": "# Use for com range\nfor i in :\n    print(i)",
                "tests": [
                    {"validation": "output_line_count", "expected": 5},
                    {"validation": "output_contains_all", "expected": ["1", "5"]},
                ],
                "hint": "Use range(1, 6) — começa em 1 e para antes do 6",
            },
        },
        {
            "id": "topico-2",
            "title": "O Loop while",
            "content": [
                {"type": "text", "value": "O `while` repete enquanto uma **condição for verdadeira**. É usado quando você **não sabe** quantas vezes vai repetir, só sabe quando parar."},
                {
                    "type": "code",
                    "caption": "while básico",
                    "value": "contador = 1\n\nwhile contador <= 5:\n    print(contador)\n    contador = contador + 1\n\n# Imprime de 1 a 5",
                },
                {"type": "text", "value": "**Cuidado com loop infinito!** Se a condição nunca ficar falsa, o programa roda para sempre. No exemplo acima, o `contador = contador + 1` é essencial para o loop terminar."},
                {
                    "type": "code",
                    "caption": "Loop infinito (NÃO faça isso)",
                    "value": "contador = 1\n\nwhile contador <= 5:\n    print(contador)\n    # O contador nunca muda — loop infinito!",
                },
                {"type": "text", "value": "Podemos usar `break` para **interromper** um loop antes do fim:"},
                {
                    "type": "code",
                    "caption": "break — saindo do loop",
                    "value": "for i in range(10):\n    if i == 5:\n        break\n    print(i)\n\n# Imprime: 0, 1, 2, 3, 4",
                },
                {"type": "text", "value": "**Quando usar cada um:** `for` → quando sabe o número de repetições. `while` → quando quer repetir até uma condição mudar."},
            ],
            "exercise": {
                "id": "01-08-ex2",
                "title": "Contar com while",
                "statement": "Use um `while` para imprimir os números de `1` a `5`, um por linha. Não esqueça de incrementar o contador para evitar loop infinito.",
                "starter_code": "contador = 1\n\nwhile contador <= 5:\n    print(contador)\n    # incremente o contador\n    ",
                "tests": [
                    {"validation": "output_line_count", "expected": 5},
                    {"validation": "output_contains_all", "expected": ["1", "5"]},
                ],
                "hint": "Use contador = contador + 1 (ou contador += 1) dentro do while",
            },
        },
    ],
    "summary": [
        "for repete um número conhecido de vezes.",
        "while repete enquanto uma condição for verdadeira.",
        "Cuidado com loops infinitos: garanta que a condição vai ficar falsa.",
    ],
}


# ============================================================================
# LIÇÃO 01-09 — Listas
# ============================================================================
LESSON_01_09 = {
    "id": "01-09",
    "module_id": "01",
    "title": "Listas",
    "objectives": [
        "Criar e acessar listas em Python",
        "Adicionar, remover e alterar elementos",
        "Percorrer listas com for",
        "Entender o conceito de índices",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "topico-1",
            "title": "O que são Listas",
            "content": [
                {"type": "text", "value": "Uma **lista** armazena **vários valores** em uma única variável. Em Python, listas ficam entre colchetes `[ ]`."},
                {
                    "type": "code",
                    "caption": "Criando uma lista",
                    "value": "frutas = [\"maçã\", \"banana\", \"uva\"]",
                },
                {"type": "text", "value": "Cada elemento tem uma **posição** (índice). **Atenção:** em Python, o primeiro índice é `0`, não 1."},
                {
                    "type": "code",
                    "caption": "Índices da lista",
                    "value": "Índice:    0        1        2\n           ↓        ↓        ↓\nfrutas = [\"maçã\", \"banana\", \"uva\"]",
                },
                {
                    "type": "code",
                    "caption": "Acessando elementos",
                    "value": "frutas = [\"maçã\", \"banana\", \"uva\"]\n\nprint(frutas[0])   # maçã\nprint(frutas[1])   # banana\nprint(frutas[-1])  # uva (último elemento)",
                },
                {"type": "text", "value": "O índice `-1` acessa o **último** elemento. `-2` acessa o penúltimo, e assim por diante."},
                {
                    "type": "code",
                    "caption": "Alterando um elemento",
                    "value": "frutas = [\"maçã\", \"banana\", \"uva\"]\nfrutas[1] = \"morango\"\n\nprint(frutas)   # [\"maçã\", \"morango\", \"uva\"]",
                },
            ],
            "exercise": {
                "id": "01-09-ex1",
                "title": "Acessando uma lista",
                "statement": "Crie uma lista `numeros` com os valores `[10, 20, 30, 40, 50]`. Imprima o primeiro elemento (índice 0) e o último elemento (índice -1), cada um em uma linha.",
                "starter_code": "numeros = [10, 20, 30, 40, 50]\n\n# Imprima o primeiro e o último\nprint()\nprint()",
                "tests": [
                    {"validation": "output_equals", "expected": "50"},
                    {"validation": "output_line_count", "expected": 2},
                ],
                "hint": "Use numeros[0] para o primeiro e numeros[-1] para o último",
            },
        },
        {
            "id": "topico-2",
            "title": "Manipulando Listas",
            "content": [
                {"type": "text", "value": "Listas têm **métodos** que permitem modificá-las. Os mais usados são `append()`, `remove()` e `len()`."},
                {
                    "type": "code",
                    "caption": "append() — adicionar no fim",
                    "value": "frutas = [\"maçã\", \"banana\"]\nfrutas.append(\"uva\")\n\nprint(frutas)   # [\"maçã\", \"banana\", \"uva\"]",
                },
                {
                    "type": "code",
                    "caption": "remove() — remover um elemento",
                    "value": "frutas = [\"maçã\", \"banana\", \"uva\"]\nfrutas.remove(\"banana\")\n\nprint(frutas)   # [\"maçã\", \"uva\"]",
                },
                {
                    "type": "code",
                    "caption": "len() — tamanho da lista",
                    "value": "frutas = [\"maçã\", \"banana\", \"uva\"]\nprint(len(frutas))   # 3",
                },
                {"type": "text", "value": "Podemos percorrer uma lista com `for`, acessando cada elemento um por vez:"},
                {
                    "type": "code",
                    "caption": "Percorrendo lista com for",
                    "value": "frutas = [\"maçã\", \"banana\", \"uva\"]\n\nfor fruta in frutas:\n    print(fruta)",
                },
                {"type": "text", "value": "**Listas são uma das estruturas mais usadas em Python.** Você vai usá-las para guardar usuários, produtos, tarefas, resultados e muito mais."},
            ],
            "exercise": {
                "id": "01-09-ex2",
                "title": "Lista de nomes",
                "statement": "Crie uma lista `nomes` com 3 nomes: `'Felipe'`, `'Ana'` e `'João'`. Use um `for` para imprimir cada nome em uma linha separada. Ao final, imprima o tamanho da lista com `len()`.",
                "starter_code": "nomes = ['Felipe', 'Ana', 'João']\n\n# Percorra e imprima cada nome\nfor nome in nomes:\n    print(nome)\n\n# Imprima o tamanho\nprint()",
                "tests": [
                    {"validation": "output_line_count", "expected": 4},
                    {"validation": "output_contains_all", "expected": ["Felipe", "Ana", "João", "3"]},
                ],
                "hint": "Depois do for, use print(len(nomes))",
            },
        },
    ],
    "summary": [
        "Listas guardam vários valores em uma única variável.",
        "Índices começam em 0; -1 acessa o último.",
        "append() adiciona, remove() remove, len() conta.",
    ],
}


# ============================================================================
# LIÇÃO 01-10 — Dicionários
# ============================================================================
LESSON_01_10 = {
    "id": "01-10",
    "module_id": "01",
    "title": "Dicionários",
    "objectives": [
        "Entender o conceito de chave-valor",
        "Criar e acessar dicionários em Python",
        "Modificar, adicionar e remover informações",
        "Percorrer dicionários com for",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "topico-1",
            "title": "Chaves e Valores",
            "content": [
                {"type": "text", "value": "Enquanto uma lista usa **índices numéricos** (0, 1, 2...), um **dicionário** usa **chaves personalizadas** para acessar valores. Cada elemento é um par **chave → valor**."},
                {
                    "type": "code",
                    "caption": "Criando um dicionário",
                    "value": "pessoa = {\n    \"nome\": \"Felipe\",\n    \"idade\": 18,\n    \"cidade\": \"São Carlos\"\n}",
                },
                {"type": "text", "value": "Pense num dicionário como uma **agenda telefônica**: o nome é a chave, o telefone é o valor."},
                {
                    "type": "code",
                    "caption": "Acessando valores pela chave",
                    "value": "pessoa = {\"nome\": \"Felipe\", \"idade\": 18}\n\nprint(pessoa[\"nome\"])    # Felipe\nprint(pessoa[\"idade\"])   # 18",
                },
                {"type": "text", "value": "**Diferença chave:** em listas, você acessa por posição (`lista[0]`). Em dicionários, você acessa pela **chave** (`dic[\"nome\"]`)."},
                {
                    "type": "code",
                    "caption": "Alterando um valor",
                    "value": "pessoa = {\"nome\": \"Felipe\", \"idade\": 18}\n\npessoa[\"idade\"] = 19\nprint(pessoa[\"idade\"])   # 19",
                },
            ],
            "exercise": {
                "id": "01-10-ex1",
                "title": "Dicionário de produto",
                "statement": "Crie um dicionário `produto` com duas chaves: `'nome'` com o valor `'Notebook'` e `'preco'` com o valor `3500`. Depois, imprima apenas o valor de `'nome'` (deve sair só `Notebook`).",
                "starter_code": "produto = {\n    'nome': ,\n    'preco': \n}\n\nprint(produto['nome'])",
                "tests": [
                    {"validation": "output_equals", "expected": "Notebook"},
                ],
                "hint": "'nome': 'Notebook' (com aspas) e 'preco': 3500 (sem aspas)",
            },
        },
        {
            "id": "topico-2",
            "title": "Manipulando Dicionários",
            "content": [
                {"type": "text", "value": "Podemos **adicionar** novas chaves, **modificar** existentes e **remover** usando `del`."},
                {
                    "type": "code",
                    "caption": "Adicionando e modificando",
                    "value": "pessoa = {\"nome\": \"Felipe\"}\n\npessoa[\"idade\"] = 18          # adiciona\npessoa[\"nome\"] = \"Felipe R.\"   # modifica\n\nprint(pessoa)",
                },
                {
                    "type": "code",
                    "caption": "Removendo uma chave",
                    "value": "pessoa = {\"nome\": \"Felipe\", \"idade\": 18}\n\ndel pessoa[\"idade\"]\nprint(pessoa)   # {\"nome\": \"Felipe\"}",
                },
                {"type": "text", "value": "Para percorrer um dicionário, podemos usar `.items()` que retorna pares (chave, valor):"},
                {
                    "type": "code",
                    "caption": "Percorrendo um dicionário",
                    "value": "pessoa = {\"nome\": \"Felipe\", \"idade\": 18}\n\nfor chave, valor in pessoa.items():\n    print(chave, \"→\", valor)\n\n# nome → Felipe\n# idade → 18",
                },
                {"type": "text", "value": "**Dicionários são usados para representar objetos do mundo real** — um usuário, um produto, uma configuração, um JSON de API. Você vai vê-los em todo lugar em projetos profissionais."},
            ],
            "exercise": {
                "id": "01-10-ex2",
                "title": "Atualizar um dicionário",
                "statement": "Crie um dicionário `aluno` com `'nome': 'Felipe'` e `'nota': 7`. Depois, atualize a `nota` para `9`. Por fim, imprima apenas o valor de `'nota'`.",
                "starter_code": "aluno = {\n    'nome': 'Felipe',\n    'nota': 7\n}\n\n# Atualize a nota para 9\n\n\nprint(aluno['nota'])",
                "tests": [
                    {"validation": "output_equals", "expected": "9"},
                ],
                "hint": "Use aluno['nota'] = 9",
            },
        },
    ],
    "summary": [
        "Dicionários guardam pares chave → valor.",
        "Acesse com dicionario[\"chave\"].",
        "Adicione/modifique atribuindo; delete com del.",
    ],
}


# ============================================================================
# LIÇÃO 01-11 — Funções
# ============================================================================
LESSON_01_11 = {
    "id": "01-11",
    "module_id": "01",
    "title": "Funções",
    "objectives": [
        "Entender o que são funções e por que usá-las",
        "Criar funções com a palavra-chave def",
        "Passar informações com parâmetros",
        "Devolver resultados com return",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "topico-1",
            "title": "Criando Funções",
            "content": [
                {"type": "text", "value": "Uma **função** é um bloco de código com nome que pode ser **chamado quantas vezes você quiser**. Isso evita repetir código e organiza o programa."},
                {"type": "text", "value": "Pense numa função como uma **receita**: você define uma vez, e pode executá-la várias vezes com ingredientes diferentes."},
                {
                    "type": "code",
                    "caption": "Criando a primeira função",
                    "value": "def saudacao():\n    print(\"Olá!\")\n\n# Chamando a função\nsaudacao()   # Olá!\nsaudacao()   # Olá!",
                },
                {"type": "text", "value": "A palavra `def` define uma função. O bloco indentado abaixo é o que ela faz quando é chamada."},
                {"type": "text", "value": "Funções podem **receber informações** através de **parâmetros**:"},
                {
                    "type": "code",
                    "caption": "Função com parâmetro",
                    "value": "def saudacao(nome):\n    print(\"Olá,\", nome)\n\nsaudacao(\"Felipe\")   # Olá, Felipe\nsaudacao(\"Ana\")      # Olá, Ana",
                },
                {"type": "text", "value": "Agora a mesma função serve para qualquer nome. Isso é **reutilização de código**."},
            ],
            "exercise": {
                "id": "01-11-ex1",
                "title": "Função de soma",
                "statement": "Crie uma função chamada `somar` que recebe dois parâmetros (`a` e `b`) e **retorna** a soma deles. Depois, chame `somar(10, 5)` e imprima o resultado.",
                "starter_code": "def somar(a, b):\n    # retorne a soma\n    \n\nresultado = somar(10, 5)\nprint(resultado)",
                "tests": [
                    {"validation": "output_equals", "expected": "15"},
                ],
                "hint": "Dentro da função, use: return a + b",
            },
        },
        {
            "id": "topico-2",
            "title": "Retorno e Reutilização",
            "content": [
                {"type": "text", "value": "O `return` faz a função **devolver um valor** para quem a chamou. Esse valor pode ser guardado numa variável e usado depois."},
                {
                    "type": "code",
                    "caption": "return vs print",
                    "value": "# Com return (devolve o valor)\ndef somar(a, b):\n    return a + b\n\nresultado = somar(3, 5)\nprint(resultado)   # 8\n\n# Sem return (só executa)\ndef somar2(a, b):\n    print(a + b)\n\nx = somar2(3, 5)   # imprime 8\nprint(x)           # None (não retornou nada!)",
                },
                {"type": "text", "value": "**Regra prática:** use `return` quando quer o resultado da função de volta. Use `print` só quando quer mostrar algo na tela."},
                {"type": "text", "value": "**Por que funções são importantes?** Em projetos grandes, o código é dividido em muitas funções pequenas, cada uma com uma responsabilidade única:"},
                {
                    "type": "code",
                    "caption": "Programa organizado em funções",
                    "value": "def cadastrar_usuario():\n    ...\n\ndef fazer_login():\n    ...\n\ndef calcular_total():\n    ...\n\ndef gerar_relatorio():\n    ...\n\n# Cada função faz uma coisa e faz bem.",
                },
                {"type": "text", "value": "Você vai usar funções para **tudo** a partir de agora. É uma das ferramentas mais importantes da programação."},
            ],
            "exercise": {
                "id": "01-11-ex2",
                "title": "Função de multiplicação",
                "statement": "Crie uma função `multiplicar` que recebe dois parâmetros e retorna a multiplicação. Chame com `6` e `7` e imprima o resultado.",
                "starter_code": "def multiplicar(a, b):\n    # retorne a multiplicação\n    \n\nresultado = multiplicar(6, 7)\nprint(resultado)",
                "tests": [
                    {"validation": "output_equals", "expected": "42"},
                ],
                "hint": "Use return a * b dentro da função",
            },
        },
    ],
    "summary": [
        "Funções agrupam código reutilizável com def.",
        "Parâmetros permitem passar informações para a função.",
        "return devolve um valor; print só mostra.",
    ],
}


# ============================================================================
# LIÇÃO 01-12 — Projeto: Calculadora
# ============================================================================
LESSON_01_12 = {
    "id": "01-12",
    "module_id": "01",
    "title": "Projeto: Calculadora",
    "objectives": [
        "Aplicar todos os conceitos do módulo em um projeto real",
        "Combinar variáveis, condicionais, operadores e funções",
        "Construir uma calculadora funcional do zero",
        "Pensar em problemas como um programador",
    ],
    "reading_time_minutes": 20,
    "topics": [
        {
            "id": "topico-1",
            "title": "Projeto Final do Módulo",
            "content": [
                {"type": "text", "value": "Chegou a hora de juntar **tudo** o que você aprendeu no módulo em um projeto real: uma **calculadora funcional**. Vamos usar variáveis, operadores, funções, condicionais e boas práticas."},
                {"type": "text", "value": "**Planejando antes de programar** — como um bom programador, primeiro pensamos na estrutura:"},
                {
                    "type": "code",
                    "caption": "Estrutura da calculadora",
                    "value": "1. Criar funções para cada operação (somar, subtrair, etc.)\n2. Receber os dois números do usuário\n3. Receber qual operação ele quer\n4. Executar a operação correta\n5. Mostrar o resultado",
                },
                {"type": "text", "value": "**Passo 1:** criar uma função para cada operação. Isso organiza o código e permite reaproveitar cada operação:"},
                {
                    "type": "code",
                    "caption": "Funções de operação",
                    "value": "def somar(a, b):\n    return a + b\n\ndef subtrair(a, b):\n    return a - b\n\ndef multiplicar(a, b):\n    return a * b\n\ndef dividir(a, b):\n    if b == 0:\n        return \"Erro: divisão por zero\"\n    return a / b",
                },
                {"type": "text", "value": "Note que em `dividir` adicionamos uma **validação**: não é possível dividir por zero. Isso evita um erro grave no programa."},
                {"type": "text", "value": "**Passo 2:** criar uma função que escolhe qual operação executar com base no que o usuário pediu:"},
                {
                    "type": "code",
                    "caption": "Função principal",
                    "value": "def calcular(a, b, operacao):\n    if operacao == \"+\":\n        return somar(a, b)\n    elif operacao == \"-\":\n        return subtrair(a, b)\n    elif operacao == \"*\":\n        return multiplicar(a, b)\n    elif operacao == \"/\":\n        return dividir(a, b)\n    else:\n        return \"Operação inválida\"",
                },
                {"type": "text", "value": "**Passo 3:** usar tudo junto. Em Python, recebemos os números com `float(input(...))` para permitir decimais:"},
                {
                    "type": "code",
                    "caption": "Usando a calculadora",
                    "value": "a = 10\nb = 5\noperacao = \"/\"\n\nresultado = calcular(a, b, operacao)\nprint(resultado)   # 2.0",
                },
                {"type": "text", "value": "**Por que isso é profissional?** Cada função tem **uma responsabilidade**. Se a divisão estiver com bug, você só olha a função `dividir`. Isso é o princípio **SRP (Single Responsibility Principle)**, base de código limpo."},
                {"type": "text", "value": "Este é apenas o começo da sua jornada. Agora que você domina os fundamentos, poderá aprender a criar sistemas cada vez mais complexos."},
            ],
            "exercise": {
                "id": "01-12-ex1",
                "title": "Construa sua calculadora",
                "statement": "Crie duas funções: `somar(a, b)` que retorna `a + b` e `multiplicar(a, b)` que retorna `a * b`. Depois, chame `somar(10, 5)` e imprima o resultado, e chame `multiplicar(4, 3)` e imprima o resultado. Cada um em uma linha.",
                "starter_code": "def somar(a, b):\n    # retorne a soma\n    \n\ndef multiplicar(a, b):\n    # retorne a multiplicação\n    \n\n# Chame e imprima os resultados\nprint(somar(10, 5))\nprint(multiplicar(4, 3))",
                "tests": [
                    {"validation": "output_contains_all", "expected": ["15", "12"]},
                    {"validation": "output_line_count", "expected": 2},
                ],
                "hint": "somar: return a + b | multiplicar: return a * b",
            },
        },
    ],
    "summary": [
        "Projetos juntam tudo o que você aprendeu no módulo.",
        "Cada função deve ter uma responsabilidade única.",
        "Validar entradas (ex: divisão por zero) evita bugs graves.",
    ],
}

# ============================================================================
# MÓDULO 02 — PYTHON FUNDAMENTOS
# ============================================================================


# ============================================================================
# LIÇÃO 02-01 — Instalando Python e o VS Code
# ============================================================================
LESSON_02_01 = {
    "id": "02-01",
    "module_id": "02",
    "title": "Instalando Python e o VS Code",
    "objectives": [
        "Entender o que é Python e onde ele é usado no mercado",
        "Instalar o Python corretamente no seu sistema",
        "Verificar se a instalação funcionou pelo terminal",
        "Instalar e configurar o VS Code com a extensão Python",
        "Criar e executar o primeiro arquivo .py",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "topico-1",
            "title": "Preparando o Ambiente",
            "content": [
                {"type": "text", "value": "Antes de escrever código, precisamos preparar o **ambiente de desenvolvimento**. É como um carpinteiro que precisa de martelo e serra — nós precisamos de duas ferramentas: **Python** e **VS Code**."},
                {"type": "text", "value": "**Python** é a linguagem que vamos usar. Ele é uma das linguagens mais populares do mundo, usado em **web, automação, IA, ciência de dados, APIs e backend** — por empresas como Google, Instagram, Netflix e Spotify."},
                {"type": "text", "value": "**VS Code** (Visual Studio Code) é o editor onde escrevemos o código. É gratuito, leve e tem extensões que facilitam muito a vida do programador."},
                {"type": "text", "value": "**Passo 1:** baixe o Python em [python.org/downloads](https://www.python.org/downloads/). No Windows, **marque a caixa \"Add Python to PATH\"** antes de clicar em Install. Isso é essencial para o Python funcionar no terminal."},
                {"type": "text", "value": "**Passo 2:** baixe o VS Code em [code.visualstudio.com](https://code.visualstudio.com). Instale com as opções padrão."},
                {"type": "text", "value": "**Passo 3:** abra o VS Code, vá na aba de **Extensões** (ícone de blocos na lateral) e instale a extensão oficial **Python** da Microsoft. Ela adiciona autocomplete, execução e detecção de erros."},
                {"type": "text", "value": "**Passo 4:** abra o **terminal** integrado do VS Code (atalho `Ctrl + '`) e teste se o Python está instalado:"},
                {
                    "type": "code",
                    "caption": "Verificando a instalação",
                    "value": "python --version\n# ou, se não funcionar:\npy --version\n\n# Saída esperada:\n# Python 3.12.x (ou similar)",
                },
                {"type": "text", "value": "**Passo 5:** crie uma pasta chamada `python-curso` no seu computador. Depois abra ela no VS Code (`File → Open Folder`). Crie um arquivo chamado `main.py` e escreva:"},
                {
                    "type": "code",
                    "caption": "Primeiro programa",
                    "value": "print(\"Olá, mundo!\")",
                },
                {"type": "text", "value": "Rode clicando no **▶** no canto superior direito, ou no terminal com `python main.py`. Se aparecer **\"Olá, mundo!\"**, parabéns — seu ambiente está pronto! 🎉"},
                {"type": "text", "value": "**Só para garantir:** para provar que você instalou tudo corretamente, faça o exercício abaixo. Ele vai rodar no **nosso ambiente** (não precisa do seu Python local) e confirmar que a frase aparece corretamente."},
            ],
            "exercise": {
                "id": "02-01-ex1",
                "title": "Verificando o ambiente",
                "statement": "Para confirmar que seu ambiente está funcionando, escreva um `print()` que imprima exatamente a frase `Ambiente configurado com sucesso!`. Este exercício valida automaticamente quando você clicar em Enviar código.",
                "starter_code": "# Escreva o print abaixo\n",
                "tests": [
                    {"validation": "output_equals", "expected": "Ambiente configurado com sucesso!"},
                ],
                "hint": "Use print(\"Ambiente configurado com sucesso!\")",
            },
        },
    ],
    "summary": [
        "Python é o interpretador; VS Code é o editor.",
        "Sempre marque 'Add Python to PATH' na instalação do Windows.",
        "A extensão Python do VS Code dá autocomplete e debug.",
    ],
}


# ============================================================================
# LIÇÃO 02-02 — Primeiro programa: print()
# ============================================================================
LESSON_02_02 = {
    "id": "02-02",
    "module_id": "02",
    "title": "Primeiro programa: print()",
    "objectives": [
        "Entender o que a função print() faz",
        "Exibir textos, números e resultados de cálculos",
        "Combinar múltiplos valores em uma só chamada",
        "Usar quebras de linha com \\n",
        "Escrever comentários no código",
    ],
    "reading_time_minutes": 12,
    "topics": [
        {
            "id": "topico-1",
            "title": "Exibindo Informações",
            "content": [
                {"type": "text", "value": "A função `print()` é a forma mais básica de fazer seu programa **se comunicar com você**. Ela exibe informações no terminal."},
                {
                    "type": "code",
                    "caption": "print() com texto",
                    "value": "print(\"Olá, mundo!\")\nprint(\"Estou aprendendo Python.\")\n\n# Saída:\n# Olá, mundo!\n# Estou aprendendo Python.",
                },
                {"type": "text", "value": "**Textos precisam estar entre aspas** (simples ou duplas — tanto faz). Números não precisam."},
                {
                    "type": "code",
                    "caption": "print() com números e cálculos",
                    "value": "print(10)         # 10\nprint(3.14)       # 3.14\nprint(10 + 5)     # 15\nprint(10 * 5)     # 50\nprint(2 ** 3)     # 8",
                },
                {"type": "text", "value": "Repare que o `print()` consegue **calcular** e mostrar o resultado. Ele aceita qualquer expressão Python dentro dos parênteses."},
                {"type": "text", "value": "Você pode passar **vários valores** separados por vírgula. O `print()` coloca um espaço entre eles automaticamente."},
                {
                    "type": "code",
                    "caption": "Múltiplos valores",
                    "value": "print(\"Nome:\", \"Felipe\")\n# Nome: Felipe\n\nprint(\"Idade:\", 18, \"anos\")\n# Idade: 18 anos",
                },
            ],
            "exercise": {
                "id": "02-02-ex1",
                "title": "Sua primeira mensagem",
                "statement": "Use `print()` para exibir a frase exata: `Estou aprendendo Python` (sem ponto final, sem aspas na saída).",
                "starter_code": "# Escreva um print com a frase pedida\n",
                "tests": [
                    {"validation": "output_equals", "expected": "Estou aprendendo Python"},
                ],
                "hint": "print(\"Estou aprendendo Python\") — não esqueça das aspas!",
            },
        },
        {
            "id": "topico-2",
            "title": "Formatação e Comentários",
            "content": [
                {"type": "text", "value": "O caractere **`\\n`** cria uma **quebra de linha** dentro do texto. Útil quando você quer mostrar várias informações em um só `print()`."},
                {
                    "type": "code",
                    "caption": "Quebrando linhas com \\n",
                    "value": "print(\"Nome: Felipe\\nIdade: 18\\nCidade: São Carlos\")\n\n# Saída:\n# Nome: Felipe\n# Idade: 18\n# Cidade: São Carlos",
                },
                {"type": "text", "value": "**Comentários** são linhas que o Python **ignora**. Servem para explicar o código para você (e para outros programadores). Começam com `#`."},
                {
                    "type": "code",
                    "caption": "Usando comentários",
                    "value": "# Este é um comentário — o Python ignora\nprint(\"Olá!\")   # comentário na mesma linha também funciona\n\n# Comentários ajudam a entender o código depois.",
                },
                {"type": "text", "value": "**Dica profissional:** escreva comentários explicando **o porquê**, não **o quê**. `# soma a + b` é redundante. `# calcula o total antes do imposto` é útil."},
            ],
            "exercise": {
                "id": "02-02-ex2",
                "title": "Apresentação em uma linha",
                "statement": "Use **um único print()** com `\\n` para exibir três linhas exatas:\n```\nNome: Felipe\nIdade: 18\nCurso: Python\n```",
                "starter_code": "# Use \\n para quebrar linhas dentro de um só print()\nprint(\"...\")",
                "tests": [
                    {"validation": "output_line_count", "expected": 3},
                    {"validation": "output_contains_all", "expected": ["Nome: Felipe", "Idade: 18", "Curso: Python"]},
                ],
                "hint": "print(\"Nome: Felipe\\nIdade: 18\\nCurso: Python\")",
            },
        },
    ],
    "summary": [
        "print() exibe textos, números e resultados de cálculos.",
        "Separe valores com vírgula para combinar em uma linha.",
        "\\n quebra linha; # escreve comentários.",
    ],
}


# ============================================================================
# LIÇÃO 02-03 — Variáveis e Tipos em Python
# ============================================================================
LESSON_02_03 = {
    "id": "02-03",
    "module_id": "02",
    "title": "Variáveis e Tipos em Python",
    "objectives": [
        "Criar variáveis e entender a atribuição",
        "Armazenar textos, números e booleanos",
        "Descobrir o tipo de uma variável com type()",
        "Alterar valores de variáveis",
        "Usar variáveis em cálculos",
    ],
    "reading_time_minutes": 12,
    "topics": [
        {
            "id": "topico-1",
            "title": "Guardando Informações",
            "content": [
                {"type": "text", "value": "Uma **variável** é um espaço na memória com um nome, que guarda um valor. Pense numa **caixa etiquetada**: a etiqueta é o nome, o conteúdo é o valor."},
                {
                    "type": "code",
                    "caption": "Criando variáveis",
                    "value": "nome = \"Felipe\"\nidade = 18\naltura = 1.75\nestudando = True",
                },
                {"type": "text", "value": "O sinal `=` significa **atribuição** — \"guarde este valor nesta variável\". Depois de criada, você pode usar a variável em qualquer lugar:"},
                {
                    "type": "code",
                    "caption": "Usando variáveis",
                    "value": "nome = \"Felipe\"\nprint(nome)   # Felipe\n\nidade = 18\nprint(idade)  # 18",
                },
                {"type": "text", "value": "Python tem quatro tipos básicos:"},
                {
                    "type": "code",
                    "caption": "Os 4 tipos básicos",
                    "value": "nome = \"Felipe\"    # str    (texto)\nidade = 18          # int    (inteiro)\naltura = 1.75       # float  (decimal)\nativo = True        # bool   (verdadeiro/falso)",
                },
                {"type": "text", "value": "Para descobrir o tipo de qualquer valor, use a função `type()`:"},
                {
                    "type": "code",
                    "caption": "Descobrindo o tipo",
                    "value": "idade = 18\nprint(type(idade))\n\n# Saída: <class 'int'>",
                },
            ],
            "exercise": {
                "id": "02-03-ex1",
                "title": "Suas primeiras variáveis",
                "statement": "Crie três variáveis: `nome` com o valor `'Gabrielly'`, `idade` com o valor `18` e `altura` com o valor `1.65`. Depois, imprima `nome` e, na linha seguinte, imprima `idade`.",
                "starter_code": "# Crie as variáveis\nnome = \nidade = \naltura = \n\n# Imprima nome e idade\nprint(nome)\nprint(idade)",
                "tests": [
                    {"validation": "output_equals", "expected": "18"},
                    {"validation": "output_line_count", "expected": 2},
                ],
                "hint": "nome = 'Gabrielly' (com aspas), idade = 18 (sem aspas)",
            },
        },
        {
            "id": "topico-2",
            "title": "Alterando e Calculando",
            "content": [
                {"type": "text", "value": "Uma variável pode ter seu valor **alterado** durante a execução. Por isso ela se chama **variável** — o valor pode variar."},
                {
                    "type": "code",
                    "caption": "Alterando valores",
                    "value": "idade = 18\nprint(idade)   # 18\n\nidade = 19\nprint(idade)   # 19 (o valor antigo foi substituído)",
                },
                {"type": "text", "value": "Você também pode usar variáveis em **cálculos matemáticos**. Isso torna os programas muito mais úteis."},
                {
                    "type": "code",
                    "caption": "Variáveis em cálculos",
                    "value": "numero1 = 10\nnumero2 = 5\n\nresultado = numero1 + numero2\nprint(resultado)   # 15",
                },
                {"type": "text", "value": "**Boas práticas de nomes:** use nomes descritivos em minúsculas, com underline para separar palavras. `nome_completo` é melhor que `nc`."},
                {
                    "type": "code",
                    "caption": "Bons vs maus nomes",
                    "value": "# ✅ Bons\nnome_completo = \"Gabrielly Milhor\"\nidade_usuario = 25\n\n# ❌ Ruins\nx = \"Gabrielly Milhor\"      # não descreve\na1 = 25                    # sigla obscura",
                },
            ],
            "exercise": {
                "id": "02-03-ex2",
                "title": "Soma com variáveis",
                "statement": "Crie duas variáveis: `numero1 = 10` e `numero2 = 5`. Calcule `resultado = numero1 + numero2` e imprima o resultado.",
                "starter_code": "numero1 = 10\nnumero2 = 5\n\n# Calcule e imprima\nresultado = \nprint(resultado)",
                "tests": [
                    {"validation": "output_equals", "expected": "15"},
                ],
                "hint": "resultado = numero1 + numero2",
            },
        },
    ],
    "summary": [
        "Variáveis guardam valores com nomes descritivos.",
        "Python descobre o tipo automaticamente (str, int, float, bool).",
        "type() mostra o tipo de qualquer valor.",
    ],
}


# ============================================================================
# LIÇÃO 02-04 — Entrada de dados: input()
# ============================================================================
LESSON_02_04 = {
    "id": "02-04",
    "module_id": "02",
    "title": "Entrada de dados: input()",
    "objectives": [
        "Usar input() para receber dados do usuário",
        "Armazenar a resposta em uma variável",
        "Criar programas interativos",
        "Entender que input() sempre retorna texto",
    ],
    "reading_time_minutes": 10,
    "topics": [
        {
            "id": "topico-1",
            "title": "Programas Interativos",
            "content": [
                {"type": "text", "value": "Até agora nossos programas só **mostravam** coisas. Com `input()`, eles passam a **receber** informações do usuário — e isso muda tudo."},
                {
                    "type": "code",
                    "caption": "Primeiro input()",
                    "value": "nome = input(\"Digite seu nome: \")\n\nprint(\"Olá,\", nome)",
                },
                {"type": "text", "value": "O `input()` faz três coisas: **mostra a mensagem**, **espera o usuário digitar**, e **devolve o texto** digitado. Esse retorno é guardado na variável."},
                {
                    "type": "code",
                    "caption": "Pedindo várias informações",
                    "value": "nome = input(\"Nome: \")\ncidade = input(\"Cidade: \")\n\nprint(\"Nome:\", nome)\nprint(\"Cidade:\", cidade)",
                },
                {"type": "text", "value": "**Ponto crítico:** o `input()` **sempre retorna uma string** (texto), mesmo que o usuário digite um número. Isso vai ser importante na próxima lição."},
            ],
            "exercise": {
                "id": "02-04-ex1",
                "title": "Saudação personalizada",
                "statement": "Peça o nome do usuário com `input(\"Digite seu nome: \")`. Depois, imprima `Olá, ` seguido do nome. Use o print com vírgula (ex: `print(\"Olá,\", nome)`). O resultado deve ser algo como `Olá, Gabrielly`.",
                "starter_code": "nome = input(\"Digite seu nome: \")\n\n# Imprima a saudação\n",
                "tests": [
                    {"validation": "output_contains_all", "expected": ["Olá"]},
                ],
                "hint": "Use print(\"Olá,\", nome)",
            },
        },
    ],
    "summary": [
        "input() mostra mensagem, espera digitação e devolve texto.",
        "Sempre guarde o retorno numa variável.",
        "input() sempre retorna string.",
    ],
}


# ============================================================================
# LIÇÃO 02-05 — Conversão de Tipos
# ============================================================================
LESSON_02_05 = {
    "id": "02-05",
    "module_id": "02",
    "title": "Conversão de Tipos",
    "objectives": [
        "Entender por que precisamos converter tipos",
        "Usar int(), float() e str()",
        "Converter dados recebidos pelo input()",
        "Realizar cálculos com dados do usuário",
    ],
    "reading_time_minutes": 12,
    "topics": [
        {
            "id": "topico-1",
            "title": "Convertendo Valores",
            "content": [
                {"type": "text", "value": "Na aula passada, descobrimos que `input()` sempre retorna **texto (str)**. Se o usuário digitar `18`, o Python recebe `\"18\"` como texto — **não dá para calcular**."},
                {
                    "type": "code",
                    "caption": "O problema",
                    "value": "idade = input(\"Digite sua idade: \")\n\n# Se o usuário digita 18, idade é a STRING \"18\"\n# Fazer idade + 5 daria erro!",
                },
                {"type": "text", "value": "A solução é **converter** com as funções `int()`, `float()` ou `str()`."},
                {
                    "type": "code",
                    "caption": "Convertendo com int()",
                    "value": "idade = int(input(\"Digite sua idade: \"))\n\n# Agora idade é um número inteiro\nidade_futura = idade + 5\nprint(idade_futura)",
                },
                {
                    "type": "text", "value": "Use **`float()`** para números decimais (altura, peso, preço) e **`str()`** para transformar número em texto."},
                {
                    "type": "code",
                    "caption": "As três conversões",
                    "value": "int(\"25\")        # 25    (texto → inteiro)\nfloat(\"1.75\")    # 1.75  (texto → decimal)\nstr(42)          # \"42\"  (número → texto)",
                },
                {"type": "text", "value": "**Cuidado:** se o usuário digitar algo que não é número (`int(\"abc\")`), o Python dá erro. Nós vamos aprender a tratar isso com `try/except` no módulo intermediário."},
            ],
            "exercise": {
                "id": "02-05-ex1",
                "title": "Idade daqui a 5 anos",
                "statement": "Crie uma variável `idade` recebendo `int(input(\"Idade: \"))`. Depois calcule `idade_futura = idade + 5` e imprima o resultado. Como o ambiente de teste não permite input, use uma variável fixa: `idade = int(\"18\")` e depois calcule.",
                "starter_code": "# Simule a conversão (input não funciona no teste)\nidade = int(\"18\")\n\n# Calcule a idade futura\nidade_futura = \nprint(idade_futura)",
                "tests": [
                    {"validation": "output_equals", "expected": "23"},
                ],
                "hint": "idade_futura = idade + 5",
            },
        },
    ],
    "summary": [
        "input() sempre retorna texto.",
        "int() converte texto em inteiro; float() em decimal; str() em texto.",
        "Converta antes de fazer cálculos.",
    ],
}


# ============================================================================
# LIÇÃO 02-06 — Strings: Métodos Principais
# ============================================================================
LESSON_02_06 = {
    "id": "02-06",
    "module_id": "02",
    "title": "Strings: Métodos Principais",
    "objectives": [
        "Trabalhar com strings e seus métodos",
        "Transformar maiúsculas/minúsculas",
        "Remover espaços extras",
        "Substituir e dividir textos",
        "Verificar informações dentro de strings",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "topico-1",
            "title": "Manipulando Textos",
            "content": [
                {"type": "text", "value": "Strings têm **métodos** — funções especiais que agem sobre a própria string. Diferente de funções normais, você chama elas com `.` depois da variável: `nome.upper()`."},
                {
                    "type": "code",
                    "caption": "upper() e lower()",
                    "value": "nome = \"Felipe\"\n\nprint(nome.upper())   # FELIPE\nprint(nome.lower())   # felipe",
                },
                {"type": "text", "value": "**`strip()`** remove espaços em branco no começo e no fim. Muito útil quando o usuário digita sem querer espaços extras."},
                {
                    "type": "code",
                    "caption": "Limpando espaços",
                    "value": "nome = \"  Felipe  \"\nprint(nome.strip())   # \"Felipe\" (sem espaços)",
                },
                {"type": "text", "value": "**`replace()`** substitui um texto por outro dentro da string."},
                {
                    "type": "code",
                    "caption": "Substituindo texto",
                    "value": "texto = \"Eu gosto de Java\"\ntexto = texto.replace(\"Java\", \"Python\")\nprint(texto)   # \"Eu gosto de Python\"",
                },
                {"type": "text", "value": "**`split()`** divide a string em uma lista de palavras."},
                {
                    "type": "code",
                    "caption": "Dividindo texto",
                    "value": "frase = \"Python é muito legal\"\npalavras = frase.split()\nprint(palavras)   # ['Python', 'é', 'muito', 'legal']",
                },
            ],
            "exercise": {
                "id": "02-06-ex1",
                "title": "Nome em maiúsculas",
                "statement": "Crie uma variável `nome = 'gabrielly'` (tudo minúsculo). Use o método `upper()` para transformar em maiúsculas e imprima o resultado.",
                "starter_code": "nome = 'gabrielly'\n\n# Transforme em maiúsculo e imprima\nprint()",
                "tests": [
                    {"validation": "output_equals", "expected": "GABRIELLY"},
                ],
                "hint": "Use nome.upper() dentro do print()",
            },
        },
        {
            "id": "topico-2",
            "title": "Analisando Strings",
            "content": [
                {"type": "text", "value": "**`len()`** retorna o **número de caracteres** de uma string (incluindo espaços)."},
                {
                    "type": "code",
                    "caption": "Contando caracteres",
                    "value": "nome = \"Felipe\"\nprint(len(nome))   # 6",
                },
                {"type": "text", "value": "**`startswith()`** e **`endswith()`** verificam como a string **começa** ou **termina**. Retornam `True` ou `False`."},
                {
                    "type": "code",
                    "caption": "Verificando começo e fim",
                    "value": "arquivo = \"projeto.py\"\n\nprint(arquivo.endswith(\".py\"))     # True\nprint(arquivo.startswith(\"pro\"))    # True",
                },
                {"type": "text", "value": "Também podemos verificar se um texto contém outro usando o operador **`in`**:"},
                {
                    "type": "code",
                    "caption": "Verificando conteúdo",
                    "value": "frase = \"Estou aprendendo Python\"\n\nprint(\"Python\" in frase)   # True\nprint(\"Java\" in frase)     # False",
                },
                {"type": "text", "value": "Esses métodos são muito usados em validação de formulários: verificar se o e-mail tem `@`, se o arquivo termina em `.pdf`, etc."},
            ],
            "exercise": {
                "id": "02-06-ex2",
                "title": "Contar caracteres",
                "statement": "Crie uma variável `palavra = 'programacao'` e imprima o número de caracteres dela usando `len()`.",
                "starter_code": "palavra = 'programacao'\n\n# Imprima o número de caracteres\nprint()",
                "tests": [
                    {"validation": "output_equals", "expected": "11"},
                ],
                "hint": "Use print(len(palavra))",
            },
        },
    ],
    "summary": [
        "upper() e lower() alteram maiúsculas/minúsculas.",
        "strip() remove espaços; replace() substitui; split() divide.",
        "len() conta caracteres; in verifica se contém.",
    ],
}


# ============================================================================
# LIÇÃO 02-07 — Listas, Tuplas e Sets
# ============================================================================
LESSON_02_07 = {
    "id": "02-07",
    "module_id": "02",
    "title": "Listas, Tuplas e Sets",
    "objectives": [
        "Conhecer as três estruturas de coleções do Python",
        "Criar, acessar e modificar listas",
        "Entender quando usar tuplas",
        "Saber o que são sets e quando usá-los",
        "Comparar as diferenças entre elas",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "topico-1",
            "title": "Listas — a Mais Usada",
            "content": [
                {"type": "text", "value": "Uma **lista** guarda **vários valores** em uma única variável. É a estrutura mais usada no dia a dia. Fica entre colchetes `[ ]` e **pode ser alterada**."},
                {
                    "type": "code",
                    "caption": "Criando e acessando listas",
                    "value": "frutas = [\"maçã\", \"banana\", \"uva\"]\n\nprint(frutas[0])    # maçã (primeiro)\nprint(frutas[-1])   # uva (último)\nprint(len(frutas))  # 3",
                },
                {"type": "text", "value": "Índices começam em **0**. O `-1` acessa o último elemento. Use **`append()`** para adicionar e **`remove()`** para remover."},
                {
                    "type": "code",
                    "caption": "Modificando listas",
                    "value": "frutas = [\"maçã\", \"banana\"]\nfrutas.append(\"uva\")         # adiciona no fim\nfrutas.remove(\"banana\")      # remove\n\nprint(frutas)   # [\"maçã\", \"uva\"]",
                },
                {"type": "text", "value": "Percorra listas com **for** — cada elemento é acessado um por vez."},
                {
                    "type": "code",
                    "caption": "Percorrendo uma lista",
                    "value": "frutas = [\"maçã\", \"banana\", \"uva\"]\n\nfor fruta in frutas:\n    print(fruta)",
                },
            ],
            "exercise": {
                "id": "02-07-ex1",
                "title": "Percorrer lista",
                "statement": "Crie uma lista `nomes = ['Gabrielly', 'Ana', 'João']`. Use um `for` para imprimir cada nome em uma linha. No final, imprima o tamanho da lista com `len()`.",
                "starter_code": "nomes = ['Gabrielly', 'Ana', 'João']\n\n# Percorra e imprima cada nome\nfor nome in nomes:\n    print(nome)\n\n# Imprima o tamanho\nprint()",
                "tests": [
                    {"validation": "output_line_count", "expected": 4},
                    {"validation": "output_contains_all", "expected": ["Gabrielly", "Ana", "João", "3"]},
                ],
                "hint": "Depois do for, use print(len(nomes))",
            },
        },
        {
            "id": "topico-2",
            "title": "Tuplas e Sets",
            "content": [
                {"type": "text", "value": "**Tuplas** são parecidas com listas, mas **não podem ser alteradas** depois de criadas. Ficam entre parênteses `( )`. Use quando os dados são fixos, como coordenadas."},
                {
                    "type": "code",
                    "caption": "Tuplas",
                    "value": "coordenadas = (10, 20)\nprint(coordenadas[0])   # 10\n\n# coordenadas[0] = 5  # ❌ erro! Tuplas não podem ser alteradas",
                },
                {"type": "text", "value": "**Sets** são coleções que **não permitem valores repetidos** e **não têm ordem**. Ficam entre chaves `{ }`."},
                {
                    "type": "code",
                    "caption": "Sets eliminam duplicatas",
                    "value": "numeros = {1, 2, 2, 3, 3, 4}\nprint(numeros)   # {1, 2, 3, 4}\n\n# Os valores repetidos desaparecem automaticamente",
                },
                {"type": "text", "value": "**Diferença resumida:**"},
                {
                    "type": "code",
                    "caption": "Comparando as três",
                    "value": "Lista  → [1, 2, 3]     ordenada, alterável, aceita repetição\nTupla  → (1, 2, 3)     ordenada, IMUTÁVEL, aceita repetição\nSet    → {1, 2, 3}     sem ordem, alterável, SEM repetição",
                },
                {"type": "text", "value": "Sets são ótimos para verificar se um valor **já existe** numa coleção. O Python faz isso muito rápido com sets."},
            ],
            "exercise": {
                "id": "02-07-ex2",
                "title": "Set elimina repetidos",
                "statement": "Crie um set `numeros = {1, 2, 2, 3, 3, 3}`. Imprima o tamanho do set com `len()`. Como sets eliminam duplicatas, o resultado deve ser `3`.",
                "starter_code": "numeros = {1, 2, 2, 3, 3, 3}\n\n# Imprima o tamanho\nprint()",
                "tests": [
                    {"validation": "output_equals", "expected": "3"},
                ],
                "hint": "Use print(len(numeros))",
            },
        },
    ],
    "summary": [
        "Lista: ordenada, alterável, aceita repetição.",
        "Tupla: ordenada, imutável.",
        "Set: sem ordem, sem repetição.",
    ],
}


# ============================================================================
# LIÇÃO 02-08 — Dicionários em Python
# ============================================================================
LESSON_02_08 = {
    "id": "02-08",
    "module_id": "02",
    "title": "Dicionários em Python",
    "objectives": [
        "Entender o conceito de chave-valor",
        "Criar, acessar e modificar dicionários",
        "Adicionar e remover informações",
        "Percorrer dicionários com for",
    ],
    "reading_time_minutes": 12,
    "topics": [
        {
            "id": "topico-1",
            "title": "Chave e Valor",
            "content": [
                {"type": "text", "value": "Um **dicionário** guarda pares de **chave → valor**. Enquanto listas usam índices numéricos, dicionários usam **nomes** (chaves) personalizados. Ficam entre chaves `{ }`."},
                {
                    "type": "code",
                    "caption": "Criando um dicionário",
                    "value": "pessoa = {\n    \"nome\": \"Gabrielly\",\n    \"idade\": 18,\n    \"cidade\": \"São Carlos\"\n}",
                },
                {"type": "text", "value": "Para **acessar** um valor, use a chave entre colchetes:"},
                {
                    "type": "code",
                    "caption": "Acessando valores",
                    "value": "print(pessoa[\"nome\"])    # Gabrielly\nprint(pessoa[\"idade\"])   # 18",
                },
                {"type": "text", "value": "**Adicione/modifique** atribuindo à chave, e **remova** com `del`:"},
                {
                    "type": "code",
                    "caption": "Modificando o dicionário",
                    "value": "pessoa = {\"nome\": \"Gabrielly\", \"idade\": 18}\n\npessoa[\"idade\"] = 19          # modifica\npessoa[\"curso\"] = \"Python\"    # adiciona\ndel pessoa[\"nome\"]            # remove\n\nprint(pessoa)   # {\"idade\": 19, \"curso\": \"Python\"}",
                },
            ],
            "exercise": {
                "id": "02-08-ex1",
                "title": "Dicionário de pessoa",
                "statement": "Crie um dicionário `pessoa` com `'nome': 'Gabrielly'` e `'idade': 18`. Depois, imprima apenas o valor de `'nome'`.",
                "starter_code": "pessoa = {\n    'nome': ,\n    'idade': \n}\n\nprint(pessoa['nome'])",
                "tests": [
                    {"validation": "output_equals", "expected": "Gabrielly"},
                ],
                "hint": "'nome': 'Gabrielly' (com aspas) e 'idade': 18 (sem aspas)",
            },
        },
        {
            "id": "topico-2",
            "title": "Percorrendo Dicionários",
            "content": [
                {"type": "text", "value": "Para percorrer um dicionário, use o método **`.items()`**, que retorna pares `(chave, valor)` em cada iteração."},
                {
                    "type": "code",
                    "caption": "Percorrendo com items()",
                    "value": "pessoa = {\"nome\": \"Gabrielly\", \"idade\": 18}\n\nfor chave, valor in pessoa.items():\n    print(chave, \"→\", valor)\n\n# nome → Gabrielly\n# idade → 18",
                },
                {"type": "text", "value": "Dicionários são muito usados no **mundo real** para representar objetos — um usuário, um produto, uma resposta de API em JSON. Você vai encontrar dicionários em todo projeto Python."},
                {
                    "type": "code",
                    "caption": "Exemplo prático — produto",
                    "value": "produto = {\n    \"nome\": \"Notebook\",\n    \"preco\": 3500,\n    \"estoque\": 10\n}\n\n# Alterando estoque\nproduto[\"estoque\"] = 8\n\nprint(produto)",
                },
            ],
            "exercise": {
                "id": "02-08-ex2",
                "title": "Atualizar dicionário",
                "statement": "Crie um dicionário `aluno` com `'nome': 'Gabrielly'` e `'nota': 7`. Atualize a `nota` para `10` e imprima apenas o valor de `'nota'`.",
                "starter_code": "aluno = {\n    'nome': 'Gabrielly',\n    'nota': 7\n}\n\n# Atualize a nota para 10\n\n\nprint(aluno['nota'])",
                "tests": [
                    {"validation": "output_equals", "expected": "10"},
                ],
                "hint": "aluno['nota'] = 10",
            },
        },
    ],
    "summary": [
        "Dicionários guardam pares chave → valor.",
        "Acesse com dic[\"chave\"]; remova com del.",
        "Use .items() para percorrer.",
    ],
}


# ============================================================================
# LIÇÃO 02-09 — Condicionais em Python
# ============================================================================
LESSON_02_09 = {
    "id": "02-09",
    "module_id": "02",
    "title": "Condicionais em Python",
    "objectives": [
        "Tomar decisões no código com if",
        "Cobrir o caso contrário com else",
        "Testar múltiplas condições com elif",
        "Combinar condições com and e or",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "topico-1",
            "title": "Tomando Decisões",
            "content": [
                {"type": "text", "value": "Até agora, todo código rodava linha por linha. Com **condicionais**, o programa pode **escolher** qual caminho seguir, dependendo de uma condição."},
                {"type": "text", "value": "**`if`** executa um bloco **só se a condição for verdadeira**. Lembre-se da regra de indentação: sempre que a linha termina com `:`, o bloco abaixo precisa ter 4 espaços."},
                {
                    "type": "code",
                    "caption": "if simples",
                    "value": "idade = 20\n\nif idade >= 18:\n    print(\"Maior de idade\")",
                },
                {"type": "text", "value": "**`else`** cobre o caso contrário. Se a condição do `if` for falsa, o bloco do `else` executa."},
                {
                    "type": "code",
                    "caption": "if / else",
                    "value": "idade = 15\n\nif idade >= 18:\n    print(\"Maior de idade\")\nelse:\n    print(\"Menor de idade\")",
                },
                {"type": "text", "value": "Os **operadores de comparação** são: `==` (igual), `!=` (diferente), `>` (maior), `<` (menor), `>=` e `<=`."},
                {
                    "type": "code",
                    "caption": "Cuidado: = vs ==",
                    "value": "idade = 18      # atribuição (=)\n\nif idade == 18: # comparação (==)\n    print(\"Tem 18 anos\")",
                },
            ],
            "exercise": {
                "id": "02-09-ex1",
                "title": "Maior ou menor de idade",
                "statement": "Crie a variável `idade = 20`. Use `if` e `else` para imprimir `'Maior de idade'` se idade for maior ou igual a 18, ou `'Menor de idade'` caso contrário.",
                "starter_code": "idade = 20\n\nif idade >= 18:\n    # imprima 'Maior de idade'\n    \nelse:\n    # imprima 'Menor de idade'\n    ",
                "tests": [
                    {"validation": "output_equals", "expected": "Maior de idade"},
                ],
                "hint": "Use print('Maior de idade') dentro do if",
            },
        },
        {
            "id": "topico-2",
            "title": "Múltiplas Condições",
            "content": [
                {"type": "text", "value": "Quando há **três ou mais possibilidades**, usamos **`elif`** (abreviação de \"else if\"). Cada `elif` testa uma nova condição, e o `else` final cobre o resto."},
                {
                    "type": "code",
                    "caption": "if / elif / else",
                    "value": "nota = 8\n\nif nota >= 9:\n    print(\"Excelente\")\nelif nota >= 6:\n    print(\"Aprovado\")\nelse:\n    print(\"Reprovado\")",
                },
                {"type": "text", "value": "**Importante:** o Python testa de cima para baixo e para na **primeira condição verdadeira**. Por isso a ordem dos `elif` importa."},
                {"type": "text", "value": "Você pode **combinar condições** com `and` (todas verdadeiras) e `or` (pelo menos uma verdadeira):"},
                {
                    "type": "code",
                    "caption": "Combinando com and",
                    "value": "idade = 20\nautorizado = True\n\nif idade >= 18 and autorizado:\n    print(\"Acesso permitido\")\nelse:\n    print(\"Acesso negado\")",
                },
                {
                    "type": "code",
                    "caption": "Combinando com or",
                    "value": "tem_dinheiro = False\ntem_cartao = True\n\nif tem_dinheiro or tem_cartao:\n    print(\"Pode pagar\")",
                },
            ],
            "exercise": {
                "id": "02-09-ex2",
                "title": "Classificação de nota",
                "statement": "Crie a variável `nota = 8`. Use `if`/`elif`/`else` para imprimir `'Excelente'` se nota >= 9, `'Aprovado'` se nota >= 6, ou `'Reprovado'` caso contrário.",
                "starter_code": "nota = 8\n\nif nota >= 9:\n    print(\"Excelente\")\nelif nota >= 6:\n    # imprima 'Aprovado'\n    \nelse:\n    print(\"Reprovado\")",
                "tests": [
                    {"validation": "output_equals", "expected": "Aprovado"},
                ],
                "hint": "Use print('Aprovado') dentro do elif",
            },
        },
    ],
    "summary": [
        "if executa se a condição for True; else cobre o resto.",
        "elif testa outras condições em sequência.",
        "Combine com and e or.",
    ],
}


# ============================================================================
# LIÇÃO 02-10 — Loops em Python
# ============================================================================
LESSON_02_10 = {
    "id": "02-10",
    "module_id": "02",
    "title": "Loops em Python",
    "objectives": [
        "Entender o conceito de loop",
        "Usar for com range() e com listas",
        "Usar while para repetir por condição",
        "Interromper loops com break",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "topico-1",
            "title": "O Loop for",
            "content": [
                {"type": "text", "value": "**Loops** automatizam tarefas repetitivas. Em vez de escrever `print(\"Olá\")` cinco vezes, você escreve uma vez e manda o Python repetir."},
                {
                    "type": "code",
                    "caption": "for com range",
                    "value": "for i in range(5):\n    print(\"Olá\")\n\n# Imprime 'Olá' 5 vezes",
                },
                {"type": "text", "value": "**`range()`** gera uma sequência de números. `range(5)` gera 0, 1, 2, 3, 4 (começa em 0 e para antes do número final)."},
                {
                    "type": "code",
                    "caption": "range com início e fim",
                    "value": "for i in range(1, 6):\n    print(i)\n\n# Imprime de 1 a 5",
                },
                {"type": "text", "value": "Também podemos percorrer **listas diretamente** com `for`:"},
                {
                    "type": "code",
                    "caption": "Percorrendo uma lista",
                    "value": "nomes = [\"Gabrielly\", \"Ana\", \"João\"]\n\nfor nome in nomes:\n    print(nome)",
                },
            ],
            "exercise": {
                "id": "02-10-ex1",
                "title": "Contar de 1 a 5",
                "statement": "Use `for` com `range` para imprimir os números de `1` a `5`, um por linha.",
                "starter_code": "# Use for com range\nfor i in :\n    print(i)",
                "tests": [
                    {"validation": "output_line_count", "expected": 5},
                    {"validation": "output_contains_all", "expected": ["1", "5"]},
                ],
                "hint": "Use range(1, 6)",
            },
        },
        {
            "id": "topico-2",
            "title": "O Loop while e o break",
            "content": [
                {"type": "text", "value": "O **`while`** repete **enquanto uma condição for verdadeira**. Use quando **não sabe** quantas vezes vai repetir — só sabe quando parar."},
                {
                    "type": "code",
                    "caption": "while básico",
                    "value": "contador = 1\n\nwhile contador <= 5:\n    print(contador)\n    contador = contador + 1\n\n# Imprime de 1 a 5",
                },
                {"type": "text", "value": "**Cuidado com loop infinito!** Se a condição nunca ficar falsa, o programa trava. No exemplo acima, o `contador = contador + 1` é essencial."},
                {"type": "text", "value": "**`break`** interrompe o loop antes do fim, mesmo que a condição ainda seja verdadeira:"},
                {
                    "type": "code",
                    "caption": "break — saindo do loop",
                    "value": "for i in range(10):\n    if i == 5:\n        break\n    print(i)\n\n# Imprime: 0, 1, 2, 3, 4",
                },
                {"type": "text", "value": "**Quando usar cada um:** `for` quando sabe o número de repetições. `while` quando quer repetir até uma condição mudar (ex: até o usuário digitar a senha correta)."},
                {
                    "type": "code",
                    "caption": "while com input (exemplo de uso real)",
                    "value": "senha = \"\"\n\nwhile senha != \"1234\":\n    senha = input(\"Digite a senha: \")\n\nprint(\"Acesso permitido!\")",
                },
            ],
            "exercise": {
                "id": "02-10-ex2",
                "title": "Contar com while",
                "statement": "Use `while` para imprimir os números de `1` a `5`, um por linha. Lembre de incrementar o contador para evitar loop infinito.",
                "starter_code": "contador = 1\n\nwhile contador <= 5:\n    print(contador)\n    # incremente o contador\n    ",
                "tests": [
                    {"validation": "output_line_count", "expected": 5},
                    {"validation": "output_contains_all", "expected": ["1", "5"]},
                ],
                "hint": "Use contador = contador + 1 (ou contador += 1)",
            },
        },
    ],
    "summary": [
        "for repete um número conhecido de vezes.",
        "while repete enquanto uma condição for verdadeira.",
        "break interrompe um loop.",
    ],
}


# ============================================================================
# LIÇÃO 02-11 — Projeto: Sistema de Cadastro
# ============================================================================
LESSON_02_11 = {
    "id": "02-11",
    "module_id": "02",
    "title": "Projeto: Sistema de Cadastro",
    "objectives": [
        "Aplicar todos os conceitos do módulo em um projeto real",
        "Combinar listas, dicionários, funções, loops e condicionais",
        "Construir um sistema interativo de cadastro",
        "Pensar na arquitetura do programa antes de codar",
    ],
    "reading_time_minutes": 25,
    "topics": [
        {
            "id": "topico-1",
            "title": "Construindo o Sistema",
            "content": [
                {"type": "text", "value": "Chegou o momento de juntar **tudo** o que você aprendeu no módulo. Vamos construir um **sistema de cadastro** que roda no terminal, com menu, cadastro, listagem e saída."},
                {"type": "text", "value": "**Primeiro, o planejamento.** Como todo bom programador, pensamos antes de codar:"},
                {
                    "type": "code",
                    "caption": "Estrutura do sistema",
                    "value": "1. Mostrar menu com opções\n2. Receber escolha do usuário\n3. Se escolher 'cadastrar', pedir dados\n4. Se escolher 'listar', mostrar todos\n5. Se escolher 'sair', encerrar\n6. Repetir até o usuário sair",
                },
                {"type": "text", "value": "**Estrutura de dados:** vamos usar uma **lista** de **dicionários**. Cada usuário é um dicionário com nome e idade; a lista guarda todos eles."},
                {
                    "type": "code",
                    "caption": "A estrutura de dados",
                    "value": "usuarios = []\n\n# Cada usuário será assim:\n# {\"nome\": \"Gabrielly\", \"idade\": 18}",
                },
                {"type": "text", "value": "**Função de cadastro:** pede os dados, cria o dicionário e adiciona na lista."},
                {
                    "type": "code",
                    "caption": "Função de cadastrar",
                    "value": "def cadastrar_usuario():\n    nome = input(\"Nome: \")\n    idade = int(input(\"Idade: \"))\n\n    usuario = {\"nome\": nome, \"idade\": idade}\n    usuarios.append(usuario)\n\n    print(\"Usuário cadastrado com sucesso!\")",
                },
                {"type": "text", "value": "**Função de listar:** percorre a lista e mostra cada usuário. Se a lista estiver vazia, avisa o usuário."},
                {
                    "type": "code",
                    "caption": "Função de listar",
                    "value": "def listar_usuarios():\n    if len(usuarios) == 0:\n        print(\"Nenhum usuário cadastrado.\")\n        return\n\n    for usuario in usuarios:\n        print(\"--------------------\")\n        print(\"Nome:\", usuario[\"nome\"])\n        print(\"Idade:\", usuario[\"idade\"])",
                },
                {"type": "text", "value": "**Menu principal:** um `while True` que mostra as opções e chama a função correta. Usa `break` para sair."},
                {
                    "type": "code",
                    "caption": "O menu principal",
                    "value": "while True:\n    print(\"\\n1 - Cadastrar usuário\")\n    print(\"2 - Listar usuários\")\n    print(\"3 - Sair\")\n\n    opcao = input(\"Escolha uma opção: \")\n\n    if opcao == \"1\":\n        cadastrar_usuario()\n    elif opcao == \"2\":\n        listar_usuarios()\n    elif opcao == \"3\":\n        print(\"Sistema encerrado.\")\n        break\n    else:\n        print(\"Opção inválida.\")",
                },
                {"type": "text", "value": "**Perceba quantos conceitos aparecem juntos:** `input()`, variáveis, dicionários, listas, funções, `if/elif/else`, `while`, `for`. Isso é o que chamamos de **aplicação real**."},
                {"type": "text", "value": "**Desafios para ir além:** adicione uma opção para **buscar** usuário por nome, outra para **excluir**, e adicione **CPF** no cadastro. Cada novo recurso é uma oportunidade de praticar."},
            ],
            "exercise": {
                "id": "02-11-ex1",
                "title": "Construa a função de cadastro",
                "statement": "Crie uma função `criar_usuario(nome, idade)` que retorna um **dicionário** com as chaves `'nome'` e `'idade'`. Depois, chame com `'Gabrielly'` e `18`, e imprima o valor da chave `'nome'` do dicionário retornado.",
                "starter_code": "def criar_usuario(nome, idade):\n    # retorne um dicionário com 'nome' e 'idade'\n    \n\nusuario = criar_usuario('Gabrielly', 18)\nprint(usuario['nome'])",
                "tests": [
                    {"validation": "output_equals", "expected": "Gabrielly"},
                ],
                "hint": "return {'nome': nome, 'idade': idade}",
            },
        },
    ],
    "summary": [
        "Projetos juntam todos os conceitos do módulo.",
        "Estrutura: lista de dicionários guarda os dados.",
        "Menu com while + if/elif/else é padrão em sistemas de terminal.",
    ],
}


# ============================================================================
# BANCO DE LIÇÕES
# ============================================================================
LESSONS: dict[str, dict] = {
    "01-01": LESSON_01_01,
    "01-03": LESSON_01_03,
    "01-04": LESSON_01_04,
    "01-05": LESSON_01_05,
    "01-06": LESSON_01_06,
    "01-07": LESSON_01_07,
    "01-08": LESSON_01_08,
    "01-09": LESSON_01_09,
    "01-10": LESSON_01_10,
    "01-11": LESSON_01_11,
    "01-12": LESSON_01_12,
  # Módulo 02
    "02-01": LESSON_02_01,
    "02-02": LESSON_02_02,
    "02-03": LESSON_02_03,
    "02-04": LESSON_02_04,
    "02-05": LESSON_02_05,
    "02-06": LESSON_02_06,
    "02-07": LESSON_02_07,
    "02-08": LESSON_02_08,
    "02-09": LESSON_02_09,
    "02-10": LESSON_02_10,
    "02-11": LESSON_02_11,
}


# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================
def _flat_lesson_order() -> list[tuple[str, str]]:
    order = []
    for module in CURRICULUM:
        for lesson in module["lessons"]:
            order.append((module["id"], lesson["id"]))
    return order


def get_lesson(lesson_id: str) -> dict | None:
    return LESSONS.get(lesson_id)


def get_adjacent_lesson_ids(lesson_id: str) -> tuple[str | None, str | None]:
    order = _flat_lesson_order()
    ids = [lid for _, lid in order]
    if lesson_id not in ids:
        return None, None
    idx = ids.index(lesson_id)
    prev_id = ids[idx - 1] if idx > 0 else None
    next_id = ids[idx + 1] if idx < len(ids) - 1 else None
    return prev_id, next_id


def validate_submission(exercise: dict, execution_stdout: str) -> dict:
    output = execution_stdout.strip()
    output_lines = [l for l in execution_stdout.splitlines() if l.strip()]

    for test in exercise["tests"]:
        kind = test["validation"]

        if kind == "output_contains_any":
            if not any(exp in output for exp in test["expected"]):
                return {"success": False, "expected": " ou ".join(test["expected"]), "got": output or "(sem saída)"}

        elif kind == "output_contains_all":
            missing = [exp for exp in test["expected"] if exp not in output]
            if missing:
                return {"success": False, "expected": ", ".join(missing), "got": output or "(sem saída)"}

        elif kind == "output_equals":
            last_line = output_lines[-1] if output_lines else ""
            expected_str = str(test["expected"]).strip()
            if last_line.strip() != expected_str:
                return {"success": False, "expected": expected_str, "got": last_line or "(sem saída)"}

        elif kind == "output_not_contains":
            if test["value"] in output:
                return {"success": False, "expected": f"saída sem '{test['value']}'", "got": output}

        elif kind == "output_line_count":
            if len(output_lines) != test["expected"]:
                return {"success": False, "expected": f"{test['expected']} linha(s) de saída", "got": f"{len(output_lines)} linha(s)"}

    return {"success": True}