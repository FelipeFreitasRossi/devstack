"""Lições do Módulo 01 — extraídas automaticamente de lessons_content.py."""

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


