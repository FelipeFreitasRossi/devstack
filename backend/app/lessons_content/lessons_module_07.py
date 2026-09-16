"""Lições do Módulo 07 — extraídas automaticamente de lessons_content.py."""

LESSON_07_01 = {
    "id": "07-01", "module_id": "07",
    "title": "Variáveis e Tipos",
    "objectives": [
        "Entender o papel do JavaScript na web moderna",
        "Usar let, const e saber por que evitar var",
        "Conhecer os tipos primitivos da linguagem",
        "Trabalhar com template literals",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "O que é JavaScript e por que ele é onipresente",
            "content": [
                {"type": "text", "value": "Se HTML é o esqueleto e CSS é a aparência, o **JavaScript (JS)** é o **cérebro**. É a única linguagem que roda **nativamente em todo navegador** — e é por isso que ela domina o frontend há 25 anos."},
                {"type": "text", "value": "**O que JS faz?** Responde a cliques, valida formulários, busca dados de APIs, atualiza a tela sem recarregar, anima elementos, guarda informações no navegador. Tudo que é **interativo** numa página é JavaScript."},
                {"type": "text", "value": "**Onde você encontra JS hoje:**"},
                {
                    "type": "code",
                    "caption": "JS está em todo lugar",
                    "value": "🌐 Navegador     → toda interatividade web\n⚙️ Node.js       → backend (APIs, CLIs, scripts)\n📱 React Native  → apps mobile (iOS/Android)\n🖥️ Electron      → apps desktop (VS Code, Discord, Slack)\n🤖 IA            → bibliotecas como TensorFlow.js",
                },
                {"type": "text", "value": "**A grande diferença com Python:** o JS roda **no navegador do usuário**, não no servidor. Isso significa que o **código é visível** para qualquer um (basta apertar F12). Por isso, **nunca** coloque senhas, chaves de API ou lógica crítica no JS — tudo isso fica no backend."},
                {"type": "text", "value": "**Onde escrever JS?** Duas formas:"},
                {
                    "type": "code",
                    "caption": "Inline vs arquivo externo",
                    "value": "# ❌ Inline (evite)\n<button onclick=\"alert('oi')\">Clique</button>\n\n# ✅ Arquivo externo (padrão)\n<script src=\"script.js\" defer></script>\n\n# O 'defer' faz o script rodar SÓ DEPOIS\n# que o HTML carregar por completo. Sempre use.",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "let, const e por que evitar var",
            "content": [
                {"type": "text", "value": "Em JS, existem **3 formas** de declarar variáveis. Mas no código moderno, você usa apenas **duas**: `let` e `const`. O `var` é legado — tem comportamentos estranhos que causam bugs difíceis de rastrear."},
                {
                    "type": "code",
                    "caption": "let e const",
                    "value": "let nome = \"Gabrielly\";    // pode reatribuir\nconst PI = 3.14;            // NÃO pode reatribuir\n\nnome = \"Ana\";              // ✅ ok\n// PI = 3.15;               // ❌ erro: Assignment to constant variable",
                },
                {"type": "text", "value": "**Regra prática:** use `const` **por padrão**. Só use `let` quando você **sabe** que o valor vai mudar. Esse hábito evita bugs — você não pode reatribuir algo sem querer."},
                {"type": "text", "value": "**Por que evitar `var`?** Três problemas sérios:"},
                {
                    "type": "code",
                    "caption": "Os problemas do var",
                    "value": "1. var tem escopo de função (let/const têm escopo de bloco)\n   → variáveis 'vazam' para fora de if/for\n\n2. var sofre 'hoisting' de forma confusa\n   → você pode usar antes de declarar e não dá erro\n\n3. var permite redeclarar a mesma variável\n   → bugs silenciosos que quebram o código",
                },
                {
                    "type": "code",
                    "caption": "O clássico bug do var em loop",
                    "value": "// ❌ Com var — imprime '5' cinco vezes\nfor (var i = 0; i < 5; i++) {\n    setTimeout(() => console.log(i), 100);\n}\n\n// ✅ Com let — imprime 0, 1, 2, 3, 4\nfor (let i = 0; i < 5; i++) {\n    setTimeout(() => console.log(i), 100);\n}\n\n// 'var' tem escopo de função, então o i é o MESMO em todas as iterações.\n// 'let' tem escopo de bloco, então cada iteração tem seu próprio i.",
                },
                {"type": "text", "value": "**A regra é simples:** esqueça que `var` existe. Use `const` sempre, `let` quando precisar mudar. Vai economizar horas de debug."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Tipos Primitivos e Template Literals",
            "content": [
                {"type": "text", "value": "JS tem **7 tipos primitivos**, mas na prática você usa 5. Diferente do Python, aqui não existe `int` separado de `float` — tudo é `number`."},
                {
                    "type": "code",
                    "caption": "Os tipos primitivos",
                    "value": "let texto    = \"Olá\";        // string\nlet inteiro  = 42;           // number\nlet decimal  = 3.14;         // number (não tem float separado)\nlet ativo    = true;         // boolean\nlet vazio    = null;         // null (intencional)\nlet indef    = undefined;    // undefined (ainda não definido)\n\n// Para descobrir o tipo, use typeof:\nconsole.log(typeof texto);   // 'string'\nconsole.log(typeof 42);      // 'number'",
                },
                {"type": "text", "value": "**`null` vs `undefined`** — parecidos, mas diferentes:"},
                {
                    "type": "code",
                    "caption": "null vs undefined",
                    "value": "let a = null;        // você DECIDIU que está vazio\nlet b;               // ainda não atribuiu → undefined\n\nconsole.log(a);      // null\nconsole.log(b);      // undefined",
                },
                {"type": "text", "value": "**Template literals** são a forma moderna de montar strings. Usa **crase** (`` ` ``) e `${...}` para interpolar valores. É muito mais limpo que concatenação com `+`."},
                {
                    "type": "code",
                    "caption": "Concatenação vs Template literal",
                    "value": "const nome = \"Gabrielly\";\nconst idade = 18;\n\n// ❌ Concatenação antiga (chato)\nconsole.log(\"Olá, \" + nome + \", \" + idade + \" anos\");\n\n// ✅ Template literal (lindo)\nconsole.log(`Olá, ${nome}, ${idade} anos`);",
                },
                {"type": "text", "value": "**Você pode colocar qualquer expressão dentro de `${...}`** — inclusive cálculos, chamadas de função, ternários:"},
                {
                    "type": "code",
                    "caption": "Template literals poderosos",
                    "value": "const preco = 100;\nconst qtd = 3;\n\nconsole.log(`Total: R$ ${preco * qtd}`);        // Total: R$ 300\nconsole.log(`Status: ${preco > 50 ? 'ok' : 'x'}`); // Status: ok\n\n// Quebra de linha direto na string também funciona:\nconsole.log(`\nLinha 1\nLinha 2\n`);",
                },
            ],
            "exercise": {
                "id": "07-01-ex1", "title": "Template literal",
                "statement": "Use JavaScript para imprimir `Olá, meu nome é Felipe`. Use `console.log` com template literal (crase). Para executar como teste, imprima via `print()` no Python a string final esperada.",
                "starter_code": "# simulação de JS para teste\nnome = 'Felipe'\n# use f-string para simular template literal\nprint()",
                "tests": [{"validation": "output_equals", "expected": "Olá, meu nome é Felipe"}],
                "hint": "print(f'Olá, meu nome é {nome}')",
            },
        },
    ],
    "summary": [
        "JS é a linguagem do navegador — só ela roda nativamente em todos.",
        "Use const por padrão; let quando precisar mudar. Evite var.",
        "Tipos: string, number, boolean, null, undefined.",
        "Template literals (crase + ${}) substituem concatenação.",
    ],
}


LESSON_07_02 = {
    "id": "07-02", "module_id": "07",
    "title": "Operadores e Condicionais",
    "objectives": [
        "Usar operadores aritméticos e lógicos",
        "Entender === vs == e por que usar sempre ===",
        "Aplicar if/else if/else",
        "Usar ternário e operador ??",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "Operadores Aritméticos",
            "content": [
                {"type": "text", "value": "Os operadores aritméticos do JS são quase idênticos aos do Python — com uma diferença importante: **não existe `//` (divisão inteira)**."},
                {
                    "type": "code",
                    "caption": "Os operadores",
                    "value": "10 + 5    // 15\n10 - 5    // 5\n10 * 5    // 50\n10 / 5    // 2\n10 % 3    // 1   (resto)\n2 ** 3    // 8   (potência)",
                },
                {"type": "text", "value": "**Truque:** para fazer divisão inteira em JS, use `Math.floor(10 / 3)` → `3`. Existe também `Math.trunc()` que corta a parte decimal."},
                {"type": "text", "value": "**⚠️ Cuidado com o `+`:** ele soma **números** mas **concatena strings**. Se um dos lados for string, o resultado é string."},
                {
                    "type": "code",
                    "caption": "O + faz coisas diferentes",
                    "value": "10 + 5         // 15  (number)\n10 + '5'       // '105' (string!)\n'Olá' + ' ' + 'mundo'  // 'Olá mundo'\n\n// Por isso é importante saber os tipos dos valores.",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "=== vs == — A Regra de Ouro",
            "content": [
                {"type": "text", "value": "Este é **provavelmente o erro #1** de quem vem de Python. JS tem **dois operadores de igualdade**: `==` e `===`. Use **sempre** o `===`."},
                {
                    "type": "code",
                    "caption": "A diferença",
                    "value": "'5' == 5     // true   (converte tipos — PERIGOSO)\n'5' === 5    // false  (compara tipo também — CORRETO)\n\n0 == false   // true   😱\n0 === false  // false  ✅\n'' == false  // true   😱\n'' === false // false  ✅",
                },
                {"type": "text", "value": "**O que o `==` faz?** Ele tenta **converter um lado para o tipo do outro** antes de comparar. Isso causa bugs absurdos — como `'' == false` ser `true`."},
                {"type": "text", "value": "**O `===` (estritamente igual)** compara **tipo E valor**. Sem conversão. Sem surpresa. É o que você quer em 99,9% dos casos."},
                {"type": "text", "value": "**A regra é simples: use `===` e `!==` sempre.** Nunca `==` nem `!=`. Se algum dia você vir um `==` no código, provavelmente é bug."},
                {
                    "type": "code",
                    "caption": "Os operadores relacionais",
                    "value": "10 === 10   // true   (igual estrito)\n10 !== 5    // true   (diferente estrito)\n10 > 5      // true\n10 < 5      // false\n10 >= 10    // true\n10 <= 5     // false",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Condicionais, Ternário e ??",
            "content": [
                {"type": "text", "value": "O `if/else if/else` do JS é **idêntico** ao do Python — com `&&` (and), `||` (or) e `!` (not). A sintaxe usa `{}` em vez de indentação."},
                {
                    "type": "code",
                    "caption": "Condicional básica",
                    "value": "const idade = 18;\n\nif (idade >= 18) {\n    console.log(\"Maior de idade\");\n} else if (idade >= 12) {\n    console.log(\"Adolescente\");\n} else {\n    console.log(\"Criança\");\n}",
                },
                {"type": "text", "value": "**Operadores lógicos:**"},
                {
                    "type": "code",
                    "caption": "&&, || e !",
                    "value": "const idade = 20;\nconst temCnh = true;\n\nif (idade >= 18 && temCnh) {        // AND — os dois true\n    console.log(\"Pode dirigir\");\n}\n\nif (temDinheiro || temCartao) {     // OR — pelo menos um true\n    console.log(\"Pode pagar\");\n}\n\nif (!estaChovendo) {                // NOT — inverte\n    console.log(\"Vamos sair\");\n}",
                },
                {"type": "text", "value": "**Operador ternário** — if/else curto em uma linha:"},
                {
                    "type": "code",
                    "caption": "Ternário",
                    "value": "const idade = 20;\nconst status = idade >= 18 ? \"maior\" : \"menor\";\n\n// Lê-se: SE idade >= 18, use 'maior'; SENÃO, use 'menor'.\n// Estrutura: condição ? valor_se_true : valor_se_false\n\n// Também funciona com chamadas:\nidade >= 18 ? permitir() : bloquear();",
                },
                {"type": "text", "value": "**Ternário aninhado** existe, mas **evite**. Se precisar de 2+ ternários, use if/else normal — é muito mais legível."},
                {"type": "text", "value": "**Operador `||` (OR) para valores padrão:** retorna o **primeiro valor truthy**. Muito usado para defaults."},
                {
                    "type": "code",
                    "caption": "|| e ?? para valores padrão",
                    "value": "// || retorna o primeiro valor TRUTHY\nconst nome = usuario.nome || 'Visitante';\n// Se usuario.nome for '', null, undefined, 0, false → 'Visitante'\n\n// ?? (nullish coalescing) só considera null/undefined\nconst config = valorConfig ?? 'padrão';\n// Se valorConfig for '' ou 0, ainda usa o valor original!\n\n// Diferença importante:\n0 || 'padrão'    // 'padrão' (0 é falsy)\n0 ?? 'padrão'    // 0        (0 não é null/undefined)",
                },
                {"type": "text", "value": "**Quando usar cada um?** Use `??` quando `0` ou `''` forem valores válidos (preços, quantidades). Use `||` quando qualquer valor \"falsy\" deve virar padrão."},
            ],
            "exercise": {
                "id": "07-02-ex1", "title": "Ternário em ação",
                "statement": "Use um ternário JS para decidir entre 'Aprovado' e 'Reprovado' baseado em uma nota >= 7. Simule em Python com if/else e imprima o resultado.",
                "starter_code": "nota = 8\n# simule o ternário JS\nresultado = \nprint(resultado)",
                "tests": [{"validation": "output_equals", "expected": "Aprovado"}],
                "hint": "resultado = 'Aprovado' if nota >= 7 else 'Reprovado'",
            },
        },
    ],
    "summary": [
        "Use === sempre; == faz conversão implícita e causa bugs.",
        "if/else if/else com &&, ||, ! — igual ao Python.",
        "Ternário: condição ? valor_true : valor_false.",
        "?? só considera null/undefined; || considera todos os falsy.",
    ],
}


LESSON_07_03 = {
    "id": "07-03", "module_id": "07",
    "title": "Loops",
    "objectives": [
        "Usar for clássico com contador",
        "Percorrer arrays com for...of",
        "Percorrer objetos com for...in",
        "Escolher o loop certo para cada caso",
    ],
    "reading_time_minutes": 12,
    "topics": [
        {
            "id": "t1",
            "title": "for Clássico — Controle Total",
            "content": [
                {"type": "text", "value": "O `for` clássico é o mais **controlável** — você define o início, a condição e o incremento. É o loop certo quando você **precisa do índice** ou quando vai repetir um número específico de vezes."},
                {
                    "type": "code",
                    "caption": "for clássico",
                    "value": "for (let i = 0; i < 5; i++) {\n    console.log(i);   // 0, 1, 2, 3, 4\n}\n\n// Estrutura: for (inicialização; condição; incremento)\n// - let i = 0     → começa em 0\n// - i < 5         → continua enquanto for menor que 5\n// - i++           → incrementa 1 a cada volta",
                },
                {"type": "text", "value": "**Diferença importante do Python:** o `for` do JS **não tem `range()`**. Você faz o contador manualmente com `let i = 0; i < N; i++`."},
                {
                    "type": "code",
                    "caption": "for ao contrário e com passo",
                    "value": "// De 10 até 1\nfor (let i = 10; i >= 1; i--) {\n    console.log(i);\n}\n\n// De 0 a 10, de 2 em 2\nfor (let i = 0; i <= 10; i += 2) {\n    console.log(i);   // 0, 2, 4, 6, 8, 10\n}",
                },
                {"type": "text", "value": "**Quando usar `for` clássico?** Quando você **precisa do índice** ou vai **modificar o array durante o loop**. Para percorrer valores puros, o `for...of` é mais limpo."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "for...of e for...in",
            "content": [
                {"type": "text", "value": "Existem **duas variantes** do `for` no JS moderno, e é comum confundir. A regra é: **`of` para valores, `in` para chaves**."},
                {
                    "type": "code",
                    "caption": "for...of — percorre VALORES",
                    "value": "const nomes = ['Gabrielly', 'Ana', 'João'];\n\nfor (const nome of nomes) {\n    console.log(nome);\n}\n\n// Saída: Gabrielly, Ana, João\n// Use for...of com arrays, strings, Sets, Maps",
                },
                {
                    "type": "code",
                    "caption": "for...in — percorre CHAVES",
                    "value": "const pessoa = { nome: 'Gabrielly', idade: 18 };\n\nfor (const chave in pessoa) {\n    console.log(chave, '→', pessoa[chave]);\n}\n\n// Saída:\n// nome → Gabrielly\n// idade → 18\n// Use for...in com objetos",
                },
                {"type": "text", "value": "**Como decorar isso?** **`of` = valor**, **`in` = índice/chave**. Pense: \"eu quero **o valor** de cada coisa\" → `of`. \"Eu quero **a chave** de cada coisa\" → `in`."},
                {"type": "text", "value": "**⚠️ Cuidado ao usar `for...in` em arrays:** ele retorna o **índice como string**, o que pode causar bugs. Para arrays, prefira sempre `for...of` ou `forEach`."},
                {
                    "type": "code",
                    "caption": "O perigo do for...in em array",
                    "value": "const arr = [10, 20, 30];\n\nfor (const i in arr) {\n    console.log(i + 1);   // '01', '11', '21' — CONCATENAÇÃO!\n}\n\n// i é a STRING '0', '1', '2'. Não dá pra somar.\n// Para arrays, use for...of:\nfor (const valor of arr) {\n    console.log(valor + 1);   // 11, 21, 31\n}",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "while, do...while e controle",
            "content": [
                {"type": "text", "value": "**`while`** repete enquanto a condição for verdadeira. Use quando **não sabe** quantas vezes vai repetir."},
                {
                    "type": "code",
                    "caption": "while básico",
                    "value": "let contador = 1;\n\nwhile (contador <= 5) {\n    console.log(contador);\n    contador++;   // essencial, senão loop infinito\n}",
                },
                {"type": "text", "value": "**`do...while`** garante que o bloco roda **pelo menos uma vez**, antes de checar a condição."},
                {
                    "type": "code",
                    "caption": "do...while",
                    "value": "let tentativas = 0;\n\ndo {\n    console.log('Tentando...');\n    tentativas++;\n} while (tentativas < 3);\n\n// Roda pelo menos 1 vez, mesmo se a condição já for false no início.",
                },
                {"type": "text", "value": "**`break` e `continue`** controlam o fluxo dentro de loops:"},
                {
                    "type": "code",
                    "caption": "break e continue",
                    "value": "// break — sai do loop imediatamente\nfor (let i = 0; i < 10; i++) {\n    if (i === 5) break;\n    console.log(i);   // 0, 1, 2, 3, 4\n}\n\n// continue — pula para a próxima iteração\nfor (let i = 0; i < 5; i++) {\n    if (i === 2) continue;\n    console.log(i);   // 0, 1, 3, 4\n}",
                },
                {"type": "text", "value": "**Quando usar cada loop?**"},
                {
                    "type": "code",
                    "caption": "Guia de escolha",
                    "value": "for clássico  → quando precisa do ÍNDICE ou controlar incremento\nfor...of      → percorrer VALORES de array/string/Set/Map\nfor...in      → percorrer CHAVES de objeto\nwhile         → repetir até uma condição (sem saber quantas vezes)\ndo...while    → igual ao while, mas roda pelo menos 1 vez",
                },
            ],
            "exercise": {
                "id": "07-03-ex1", "title": "Loop de 1 a 5",
                "statement": "Simule um loop JS em Python que imprima 1, 2, 3, 4, 5. Use `for i in range(1, 6)` e imprima cada um.",
                "starter_code": "for i in :\n    print(i)",
                "tests": [{"validation": "output_line_count", "expected": 5}, {"validation": "output_contains_all", "expected": ["1", "5"]}],
                "hint": "for i in range(1, 6):",
            },
        },
    ],
    "summary": [
        "for clássico: contador manual (let i = 0; i < N; i++).",
        "for...of percorre VALORES; for...in percorre CHAVES.",
        "while repete até condição falsa; do...while roda pelo menos 1 vez.",
        "break sai do loop; continue pula para a próxima iteração.",
    ],
}


LESSON_07_04 = {
    "id": "07-04", "module_id": "07",
    "title": "Funções",
    "objectives": [
        "Conhecer as 3 formas de declarar funções",
        "Usar arrow functions corretamente",
        "Entender parâmetros padrão e rest params",
        "Saber quando usar arrow vs function",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "As 3 Formas de Declarar Funções",
            "content": [
                {"type": "text", "value": "Em JS, existem **3 formas** de declarar funções, e cada uma tem seu comportamento. Entender a diferença evita bugs."},
                {
                    "type": "code",
                    "caption": "As 3 formas",
                    "value": "// 1. Function declaration (hoisted — pode usar antes de declarar)\nfunction somar(a, b) {\n    return a + b;\n}\n\n// 2. Function expression (NÃO hoisted)\nconst somar2 = function(a, b) {\n    return a + b;\n};\n\n// 3. Arrow function (a mais moderna)\nconst somar3 = (a, b) => a + b;",
                },
                {"type": "text", "value": "**Hoisting** é um comportamento do JS onde **declarações** são movidas para o topo do escopo. Por isso você pode chamar `somar(1, 2)` **antes** de definir a função com `function`. Já com `const somar2 = function()...`, isso **não funciona** — você tem que declarar antes de usar."},
                {"type": "text", "value": "**Na prática, use arrow functions** para 90% dos casos. São mais curtas e têm comportamento de `this` mais previsível (que veremos no React)."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Arrow Functions — A Forma Moderna",
            "content": [
                {"type": "text", "value": "**Arrow functions** (funções seta) foram introduzidas no ES6 e viraram o padrão. A sintaxe é mais curta e existem 3 variações dependendo do corpo."},
                {
                    "type": "code",
                    "caption": "As 3 variações de arrow",
                    "value": "// 1. Uma expressão (return implícito)\nconst quadrado = x => x * x;\n\n// 2. Múltiplos parâmetros\nconst somar = (a, b) => a + b;\n\n// 3. Corpo com múltiplas linhas (precisa de {} e return)\nconst maior = (a, b) => {\n    if (a > b) return a;\n    return b;\n};",
                },
                {"type": "text", "value": "**Regras do `return` implícito:** se o corpo é **uma linha só** e **sem chaves `{}`**, o valor da expressão é retornado automaticamente. Se você adiciona `{}`, precisa do `return` explícito."},
                {
                    "type": "code",
                    "caption": "Erro comum: {} sem return",
                    "value": "// ✅ Correto (return implícito)\nconst dobro = x => x * 2;\n\n// ❌ Errado — retorna undefined!\nconst dobro2 = x => { x * 2 };\n\n// ✅ Com {} precisa de return\nconst dobro3 = x => { return x * 2; };",
                },
                {"type": "text", "value": "**Quando NÃO usar arrow function?** Em **métodos de objeto** que precisam do `this` dinâmico — arrow não tem `this` próprio. Mas isso é um caso avançado, você vai entender quando estudar React."},
                {
                    "type": "code",
                    "caption": "Arrow em callback — o caso mais comum",
                    "value": "// ❌ Sem arrow (verboso)\n[1, 2, 3].map(function(x) {\n    return x * 2;\n});\n\n// ✅ Com arrow (limpo)\n[1, 2, 3].map(x => x * 2);",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Parâmetros Padrão e Rest Params",
            "content": [
                {"type": "text", "value": "**Parâmetros padrão** permitem que a função assuma um valor quando o argumento não é passado. Se você não passar, usa o padrão."},
                {
                    "type": "code",
                    "caption": "Parâmetros padrão",
                    "value": "function saudar(nome = 'Visitante') {\n    return `Olá, ${nome}!`;\n}\n\nsaudar();               // Olá, Visitante!\nsaudar('Gabrielly');    // Olá, Gabrielly!",
                },
                {"type": "text", "value": "**Rest params (`...args`)** capturam **quantidade variável** de argumentos em um array. Use quando a função aceita \"N valores\"."},
                {
                    "type": "code",
                    "caption": "Rest params",
                    "value": "function somarTudo(...numeros) {\n    return numeros.reduce((acc, n) => acc + n, 0);\n}\n\nsomarTudo(1, 2, 3, 4);       // 10\nsomarTudo(10, 20);            // 30\nsomarTudo();                  // 0",
                },
                {"type": "text", "value": "**`...` tem dois significados em JS**, e é fácil confundir. No **parâmetro** da função, ele é **rest** (coleta). Em uma **chamada** ou **atribuição**, ele é **spread** (espalha)."},
                {
                    "type": "code",
                    "caption": "Rest vs Spread",
                    "value": "// REST — coleta em array (na DEFINIÇÃO da função)\nfunction log(...args) {\n    console.log(args);   // array\n}\n\n// SPREAD — espalha array em argumentos (na CHAMADA)\nconst nums = [1, 2, 3];\nconsole.log(Math.max(...nums));   // Math.max(1, 2, 3)",
                },
            ],
            "exercise": {
                "id": "07-04-ex1", "title": "Arrow function",
                "statement": "Simule uma arrow function em Python que calcula o dobro de um número. Imprima o resultado de `dobro(7)`.",
                "starter_code": "def dobro(x):\n    return \n\nprint(dobro(7))",
                "tests": [{"validation": "output_equals", "expected": "14"}],
                "hint": "return x * 2",
            },
        },
    ],
    "summary": [
        "3 formas: function declaration, expression, arrow.",
        "Arrow functions são o padrão moderno — mais curtas e limpas.",
        "Uma linha sem {} tem return implícito; com {} precisa de return.",
        "Rest (...args) coleta; spread (...arr) espalha.",
    ],
}


LESSON_07_05 = {
    "id": "07-05", "module_id": "07",
    "title": "Arrays e Objetos",
    "objectives": [
        "Criar e manipular arrays (push, pop, slice, splice)",
        "Criar e acessar objetos",
        "Desestruturar arrays e objetos",
        "Entender a diferença entre mutar e copiar",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "Arrays — Coleções Ordenadas",
            "content": [
                {"type": "text", "value": "**Arrays** em JS são como listas em Python. Guardam vários valores em uma variável, acessados por índice. Índices começam em **0**."},
                {
                    "type": "code",
                    "caption": "Criando e acessando arrays",
                    "value": "const frutas = ['maçã', 'banana', 'uva'];\n\nconsole.log(frutas[0]);       // 'maçã'\nconsole.log(frutas[-1]);      // ❌ NÃO existe em JS (diferente do Python!)\nconsole.log(frutas.length);   // 3\nconsole.log(frutas.at(-1));   // 'uva' (a forma moderna de pegar o último)",
                },
                {"type": "text", "value": "**Atenção:** em JS, `arr[-1]` retorna `undefined` — não é como em Python. Para pegar o último, use `.at(-1)` (ES2022) ou `arr[arr.length - 1]`."},
                {"type": "text", "value": "**Métodos que MUTAM o array** (modificam no lugar):"},
                {
                    "type": "code",
                    "caption": "Métodos mutantes",
                    "value": "const nums = [1, 2, 3];\n\nnums.push(4);        // adiciona no fim    → [1, 2, 3, 4]\nnums.pop();           // remove do fim       → [1, 2, 3]\nnums.unshift(0);      // adiciona no início  → [0, 1, 2, 3]\nnums.shift();         // remove do início    → [1, 2, 3]",
                },
                {"type": "text", "value": "**Métodos que NÃO mutam** (retornam novo array):"},
                {
                    "type": "code",
                    "caption": "Métodos imutáveis",
                    "value": "const arr = [1, 2, 3, 4, 5];\n\narr.slice(1, 3);      // [2, 3]  — novo array (não muta)\narr.slice(-2);        // [4, 5]  — últimos 2\narr.concat([6, 7]);   // [1, 2, 3, 4, 5, 6, 7]\n\n// splice MUTA (é a exceção):\narr.splice(1, 2);     // remove 2 itens a partir do índice 1 — MUTA",
                },
                {"type": "text", "value": "**Como decorar:** **slice** (pedaço) **não muta**. **splice** (emendar) **muta**. Duas letras a mais, mas fazem coisas diferentes."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Objetos — Pares Chave-Valor",
            "content": [
                {"type": "text", "value": "**Objetos** são como dicionários em Python — guardam pares **chave → valor**. Usados para representar entidades: um usuário, um produto, uma configuração."},
                {
                    "type": "code",
                    "caption": "Criando objetos",
                    "value": "const pessoa = {\n    nome: 'Gabrielly',\n    idade: 18,\n    cidade: 'São Carlos',\n    saudar() {\n        return `Olá, eu sou ${this.nome}`;\n    },\n};\n\n// Acessando valores\nconsole.log(pessoa.nome);         // 'Gabrielly'  (notação de ponto)\nconsole.log(pessoa['idade']);     // 18           (notação de colchete)\npessoa.saudar();                  // 'Olá, eu sou Gabrielly'",
                },
                {"type": "text", "value": "**Ponto vs Colchete:** use **ponto** quando a chave é conhecida (`pessoa.nome`). Use **colchete** quando a chave é dinâmica (`pessoa[variavel]`)."},
                {
                    "type": "code",
                    "caption": "Modificando objetos",
                    "value": "const pessoa = { nome: 'Gabrielly' };\n\npessoa.idade = 18;              // adiciona chave\npessoa.nome = 'Ana';            // modifica\ndelete pessoa.idade;            // remove\n\n// Verificar se chave existe:\n'nome' in pessoa                 // true\npessoa.hasOwnProperty('nome')    // true",
                },
                {"type": "text", "value": "**`this` dentro de métodos:** refere-se ao objeto. Em `saudar()`, `this.nome` acessa o `nome` do próprio objeto. Só funciona se você chamar `pessoa.saudar()` — se extrair a função isolada, o `this` quebra."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Desestruturação e Spread",
            "content": [
                {"type": "text", "value": "**Desestruturação** extrai valores de arrays/objetos para variáveis separadas. É um dos recursos mais usados no código moderno."},
                {
                    "type": "code",
                    "caption": "Destructuring de objetos",
                    "value": "const pessoa = { nome: 'Gabrielly', idade: 18, cidade: 'São Carlos' };\n\n// ❌ Sem destructuring\nconst nome = pessoa.nome;\nconst idade = pessoa.idade;\n\n// ✅ Com destructuring\nconst { nome, idade } = pessoa;\n\n// Renomeando:\nconst { nome: nomeCompleto, idade: anos } = pessoa;\n\n// Valor padrão:\nconst { ativo = true } = pessoa;",
                },
                {
                    "type": "code",
                    "caption": "Destructuring de arrays",
                    "value": "const [a, b] = [1, 2];         // a=1, b=2\nconst [primeiro, ...resto] = [1, 2, 3, 4];\n// primeiro=1, resto=[2, 3, 4]",
                },
                {"type": "text", "value": "**Spread (`...`)** — usado para **copiar e combinar** arrays/objetos sem mutar o original. Fundamental em React e Redux."},
                {
                    "type": "code",
                    "caption": "Spread em arrays",
                    "value": "const a = [1, 2, 3];\nconst b = [4, 5, 6];\n\nconst juntos = [...a, ...b];     // [1, 2, 3, 4, 5, 6]\nconst copia = [...a];            // copia rasa (não é a mesma referência)",
                },
                {
                    "type": "code",
                    "caption": "Spread em objetos",
                    "value": "const base = { nome: 'Gabrielly', idade: 18 };\n\n// ✅ Jeito moderno (imutável)\nconst atualizado = { ...base, idade: 19 };\n\n// ❌ Jeito antigo (mutável)\nconst antigo = base;\nantigo.idade = 19;    // MUTA o base também!",
                },
                {"type": "text", "value": "**Por que isso importa?** Em React, **você nunca muta estado diretamente** — sempre cria um novo objeto com spread. Isso é o padrão de **imutabilidade**."},
                {
                    "type": "code",
                    "caption": "Imutabilidade é regra em React",
                    "value": "// ❌ Nunca faça isso em React\nestado.idade = 19;\nsetEstado(estado);   // React não detecta a mudança!\n\n// ✅ Sempre crie novo objeto\nsetEstado({ ...estado, idade: 19 });",
                },
            ],
            "exercise": {
                "id": "07-05-ex1", "title": "Destructuring",
                "statement": "Simule destructuring em Python. Dada a lista `dados = [10, 20, 30]`, atribua a=10, b=20 e c=30. Imprima `a + b + c`.",
                "starter_code": "dados = [10, 20, 30]\na, b, c = dados\nprint()",
                "tests": [{"validation": "output_equals", "expected": "60"}],
                "hint": "print(a + b + c)",
            },
        },
    ],
    "summary": [
        "Arrays: índices começam em 0; use .at(-1) para o último.",
        "push/pop/unshift/shift MUTAM; slice/concat NÃO mutam.",
        "Objetos guardam chave-valor; acesso com .chave ou ['chave'].",
        "Destructuring extrai valores; spread copia e combina.",
        "React trabalha com imutabilidade — sempre crie novo objeto.",
    ],
}


LESSON_07_06 = {
    "id": "07-06", "module_id": "07",
    "title": "DOM — Manipulando Elementos",
    "objectives": [
        "Entender o que é o DOM",
        "Selecionar elementos com querySelector",
        "Alterar texto, HTML, classes e estilos",
        "Criar e remover elementos dinamicamente",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "O que é o DOM",
            "content": [
                {"type": "text", "value": "**DOM** (Document Object Model) é a **representação do HTML em memória**. Quando o navegador carrega uma página, ele transforma o HTML em uma **árvore de objetos** que o JS pode ler e modificar."},
                {"type": "text", "value": "Pense assim: o HTML é o **arquivo texto**. O DOM é esse HTML transformado em uma **estrutura viva** que o JS pode manipular. Quando você muda o DOM, a página atualiza **na hora**, sem recarregar."},
                {
                    "type": "code",
                    "caption": "HTML → DOM",
                    "value": "# HTML (arquivo texto)\n<body>\n    <h1>Olá</h1>\n    <p>Mundo</p>\n</body>\n\n# DOM (árvore em memória)\n         document\n            │\n          body\n         /    \\\n        h1     p\n        │      │\n     'Olá'  'Mundo'",
                },
                {"type": "text", "value": "**`document`** é o ponto de entrada. É o objeto global que representa a página. Todas as manipulações começam em `document.`."},
                {"type": "text", "value": "**Por que isso é revolucionário?** Antes do JS moderno, cada interação exigia **recarregar a página** — enviar formulário, mudar aba, atualizar dados. Com DOM, tudo isso acontece **sem reload**. É o que define uma SPA (Single Page Application)."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Selecionando Elementos",
            "content": [
                {"type": "text", "value": "Antes de mexer em qualquer coisa, você precisa **selecionar** o elemento. Existem vários métodos, mas no dia a dia você usa **`querySelector`** para quase tudo."},
                {
                    "type": "code",
                    "caption": "As formas de selecionar",
                    "value": "// 1. Por ID (raro hoje)\ndocument.getElementById('titulo');\n\n// 2. querySelector — retorna o PRIMEIRO match\ndocument.querySelector('.botao');     // classe\ndocument.querySelector('#titulo');    // id\ndocument.querySelector('h1');         // tag\ndocument.querySelector('form input'); // combinado\n\n// 3. querySelectorAll — retorna TODOS (NodeList)\ndocument.querySelectorAll('.item');   // todos com class='item'",
                },
                {"type": "text", "value": "**`querySelector` usa a mesma sintaxe do CSS** — então tudo que você aprendeu em seletores CSS vale aqui. Isso unifica muito o aprendizado."},
                {"type": "text", "value": "**Diferença entre retorno:** `querySelector` retorna **um elemento** (ou `null`). `querySelectorAll` retorna uma **NodeList** — que você pode percorrer com `forEach`."},
                {
                    "type": "code",
                    "caption": "querySelectorAll + forEach",
                    "value": "const itens = document.querySelectorAll('.item');\n\nitens.forEach(item => {\n    item.classList.add('ativo');\n});",
                },
                {"type": "text", "value": "**⚠️ Erro comum:** se você seleciona antes do HTML carregar, `querySelector` retorna `null` e seu JS quebra. Por isso, sempre coloque `<script>` com **`defer`** ou no **final do `<body>`**."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Modificando Conteúdo",
            "content": [
                {"type": "text", "value": "Com o elemento selecionado, você pode **alterar** ele de várias formas. Vamos ver as principais:"},
                {
                    "type": "code",
                    "caption": "Alterando texto — textContent vs innerHTML",
                    "value": "const titulo = document.querySelector('h1');\n\n// textContent — SÓ texto (seguro contra XSS)\ntitulo.textContent = 'Novo título';\n\n// innerHTML — INTERPRETA HTML (cuidado!)\ntitulo.innerHTML = '<em>Novo</em> título';\n\n// ⚠️ NUNCA use innerHTML com input do usuário:\ntitulo.innerHTML = usuarioInput;   // 🚨 RISCO DE XSS",
                },
                {"type": "text", "value": "**Por que `innerHTML` é perigoso?** Se um usuário mandar `<script>roubarCokies()</script>`, o navegador **executa** esse script. Isso se chama **XSS** (Cross-Site Scripting). Use `textContent` sempre que estiver colocando dados do usuário."},
                {
                    "type": "code",
                    "caption": "Manipulando classes com classList",
                    "value": "const card = document.querySelector('.card');\n\ncard.classList.add('ativo');        // adiciona\ncard.classList.remove('antigo');     // remove\ncard.classList.toggle('aberto');     // adiciona se não tem, remove se tem\ncard.classList.contains('ativo');    // true/false\ncard.classList.replace('a', 'b');    // troca uma pela outra",
                },
                {"type": "text", "value": "**Por que usar `classList` em vez de mexer no `style`?** Porque é mais limpo. O ideal é que o CSS defina as classes e o JS só **troque** a classe. Assim, toda a aparência fica no CSS."},
                {
                    "type": "code",
                    "caption": "Mexendo em style (evite quando puder)",
                    "value": "// Funciona, mas mistura aparência com lógica\ncard.style.color = '#f59e0b';\ncard.style.fontSize = '18px';\ncard.style.display = 'none';   // esconder\n\n// ✅ Prefira classes:\n// CSS: .destaque { color: #f59e0b; font-size: 18px; }\ncard.classList.add('destaque');",
                },
                {
                    "type": "code",
                    "caption": "Criando e removendo elementos",
                    "value": "// Criar\nconst novoP = document.createElement('p');\nnovoP.textContent = 'Novo parágrafo';\nnovoP.classList.add('destaque');\n\n// Inserir no DOM\ndocument.body.appendChild(novoP);   // ou:\ndocument.body.append(novoP);        // aceita vários + strings\n\n// Remover\nnovoP.remove();",
                },
            ],
            "exercise": {
                "id": "07-06-ex1", "title": "Simulando querySelector",
                "statement": "Simule em Python: dado um dicionário que representa um elemento (`{'tag': 'h1', 'text': 'Título'}`), imprima o valor do campo `text`.",
                "starter_code": "elemento = {'tag': 'h1', 'text': 'Título'}\nprint()",
                "tests": [{"validation": "output_equals", "expected": "Título"}],
                "hint": "print(elemento['text'])",
            },
        },
    ],
    "summary": [
        "DOM é a representação do HTML em memória — o JS pode ler e modificar.",
        "querySelector retorna o 1º match; querySelectorAll retorna todos.",
        "textContent é seguro; innerHTML interpreta HTML (risco de XSS).",
        "classList.add/remove/toggle é o jeito certo de manipular classes.",
        "createElement + appendChild criam; remove() apaga.",
    ],
}


LESSON_07_07 = {
    "id": "07-07", "module_id": "07",
    "title": "Eventos e addEventListener",
    "objectives": [
        "Adicionar listeners a elementos",
        "Conhecer os principais tipos de evento",
        "Usar event.target e preventDefault",
        "Entender event bubbling e delegação",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "Reagindo ao Usuário",
            "content": [
                {"type": "text", "value": "**Eventos** são ações que acontecem na página: clique, digitação, submit, scroll, hover. Sem eles, a página seria estática. Com eles, ela **responde** ao usuário."},
                {"type": "text", "value": "A forma moderna de escutar eventos é com **`addEventListener`**. A forma antiga (usar `onclick=\"...\"` no HTML) é considerada **anti-padrão** — mistura HTML com JS."},
                {
                    "type": "code",
                    "caption": "addEventListener básico",
                    "value": "const botao = document.querySelector('button');\n\nbotao.addEventListener('click', () => {\n    console.log('Clicou!');\n});\n\n// Estrutura: elemento.addEventListener('tipo', função)\n// A função recebe o EVENTO como primeiro argumento (opcional)",
                },
                {"type": "text", "value": "**Por que addEventListener é melhor que `onclick`?** Dois motivos: **separa HTML de JS** (código mais limpo) e **permite múltiplos listeners** no mesmo elemento."},
                {
                    "type": "code",
                    "caption": "onclick vs addEventListener",
                    "value": "// ❌ onclick no HTML\n<button onclick=\"fazerAlgo()\">Clique</button>\n\n// ❌ onclick no JS (só 1 listener por vez)\nbotao.onclick = fazerAlgo;\n\n// ✅ addEventListener (múltiplos listeners)\nbotao.addEventListener('click', fazerAlgo);\nbotao.addEventListener('click', registrarLog);",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Tipos de Evento e event.target",
            "content": [
                {"type": "text", "value": "Existem **dezenas** de eventos, mas você usa uns 8 no dia a dia:"},
                {
                    "type": "code",
                    "caption": "Os eventos mais usados",
                    "value": "click       → clique do mouse/teclado\ninput       → enquanto digita (tempo real)\nchange      → quando o valor muda (blur em inputs, select)\nsubmit      → envio de formulário\nkeydown     → tecla pressionada\nkeyup       → tecla solta\nmouseenter  → mouse entra no elemento\nmouseleave  → mouse sai\nscroll      → rolagem da página\ndomcontentloaded → HTML carregou completamente",
                },
                {"type": "text", "value": "**O objeto `event`** é passado automaticamente para a função handler. Ele contém **informações do evento**: qual tecla foi apertada, onde clicou, qual elemento originou."},
                {
                    "type": "code",
                    "caption": "Explorando o evento",
                    "value": "botao.addEventListener('click', (event) => {\n    console.log(event.target);      // o elemento clicado\n    console.log(event.type);        // 'click'\n    console.log(event.clientX);     // posição X do mouse\n});",
                },
                {"type": "text", "value": "**`event.target`** é muito útil quando o handler cobre vários elementos. Por exemplo, um `<ul>` com vários `<li>` — cada clique no `<li>` tem `event.target` apontando para o li específico."},
                {
                    "type": "code",
                    "caption": "event.target na prática",
                    "value": "document.querySelector('ul').addEventListener('click', (e) => {\n    // Se clicou em um li:\n    if (e.target.tagName === 'LI') {\n        e.target.classList.toggle('feito');\n    }\n});",
                },
                {"type": "text", "value": "**`event.preventDefault()`** impede o comportamento **padrão** do evento. Muito usado para impedir que um formulário recarregue a página."},
                {
                    "type": "code",
                    "caption": "preventDefault",
                    "value": "form.addEventListener('submit', (e) => {\n    e.preventDefault();       // NÃO recarrega a página\n    \n    const nome = e.target.nome.value;\n    console.log('Enviado:', nome);\n});",
                },
                {"type": "text", "value": "**Sem `preventDefault`,** ao submeter o form, o navegador recarrega a página. Isso destrói a ideia de SPA e perde todos os dados não salvos."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Event Bubbling e Delegação",
            "content": [
                {"type": "text", "value": "**Event bubbling** é um conceito fundamental. Quando você clica em um `<li>` dentro de um `<ul>` dentro de uma `<div>`, o evento **\"borbulha\"** — ele dispara em cada ancestral, de dentro para fora."},
                {
                    "type": "code",
                    "caption": "Bubbling visualmente",
                    "value": "Clicou no <button>\n    ↓\nEvento sobe para o <div>\n    ↓\nEvento sobe para o <body>\n    ↓\nEvento chega em <html>\n\n// Se você tem listeners em vários ancestrais, TODOS recebem o evento.",
                },
                {"type": "text", "value": "**Por que isso importa?** Porque permite uma técnica chamada **delegação de eventos**: em vez de colocar um listener em **cada item**, você coloca **um só no pai**."},
                {
                    "type": "code",
                    "caption": "Sem delegação (❌)",
                    "value": "// Cada <li> precisa de seu próprio listener\nconst itens = document.querySelectorAll('li');\n\nitens.forEach(li => {\n    li.addEventListener('click', () => {\n        li.classList.toggle('feito');\n    });\n});\n\n// PROBLEMA: se você adicionar novos <li> depois,\n// eles NÃO terão listener. Bug clássico.",
                },
                {
                    "type": "code",
                    "caption": "Com delegação (✅)",
                    "value": "// Um listener no pai, cobre todos os filhos\nconst lista = document.querySelector('ul');\n\nlista.addEventListener('click', (e) => {\n    if (e.target.tagName === 'LI') {\n        e.target.classList.toggle('feito');\n    }\n});\n\n// VANTAGEM: funciona com <li> adicionados depois também!",
                },
                {"type": "text", "value": "**Delegação é o padrão em apps dinâmicos.** Sempre que você tiver uma lista que pode crescer, use delegação. É mais performático (1 listener vs N) e mais correto."},
                {
                    "type": "code",
                    "caption": "Usando dataset para identificar itens",
                    "value": "// HTML: <li data-id=\"42\">Item</li>\n\nlista.addEventListener('click', (e) => {\n    if (e.target.tagName === 'LI') {\n        const id = e.target.dataset.id;   // '42'\n        console.log('Clicou no item', id);\n    }\n});\n\n// data-* virou e.dataset.*",
                },
                {"type": "text", "value": "**`stopPropagation()`** — se você **quiser** parar o bubbling (raro), chame `e.stopPropagation()` no handler. Mas evite: geralmente você **quer** o bubbling."},
            ],
            "exercise": {
                "id": "07-07-ex1", "title": "preventDefault na prática",
                "statement": "Simule em Python: imprima 'Formulário enviado' depois de impedir o comportamento padrão. Use apenas um `print()`.",
                "starter_code": "# simule o event.preventDefault() seguido do print\n",
                "tests": [{"validation": "output_equals", "expected": "Formulário enviado"}],
                "hint": "print('Formulário enviado')",
            },
        },
    ],
    "summary": [
        "addEventListener é a forma moderna (separa HTML e JS).",
        "event.target identifica o elemento que disparou o evento.",
        "preventDefault evita comportamento padrão (ex: reload do form).",
        "Event bubbling: eventos sobem para os ancestrais.",
        "Delegação: 1 listener no pai cobre todos os filhos (ideal para listas).",
    ],
}


LESSON_07_08 = {
    "id": "07-08", "module_id": "07",
    "title": "Formulários e Validação",
    "objectives": [
        "Capturar dados de formulários",
        "Validar campos obrigatórios e formatos",
        "Mostrar mensagens de erro ao usuário",
        "Combinar validação HTML5 com JS",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "Capturando Dados do Formulário",
            "content": [
                {"type": "text", "value": "Formulários são onde o usuário **envia informação** para sua aplicação. Capturar esses dados corretamente é uma das tarefas mais comuns do JS."},
                {
                    "type": "code",
                    "caption": "Padrão básico de captura",
                    "value": "const form = document.querySelector('form');\n\nform.addEventListener('submit', (e) => {\n    e.preventDefault();      // NÃO recarrega a página\n    \n    // Acesso direto via form.campo.value\n    const dados = {\n        nome: form.nome.value,\n        email: form.email.value,\n        idade: Number(form.idade.value),   // converte para number\n    };\n    \n    console.log(dados);\n});",
                },
                {"type": "text", "value": "**`form.campo.value`** funciona quando o input tem `name=\"campo\"`. Se não tiver `name`, você não consegue acessar assim."},
                {"type": "text", "value": "**Alternativa: `FormData`** — pega todos os campos de uma vez, de forma mais automática:"},
                {
                    "type": "code",
                    "caption": "Usando FormData",
                    "value": "form.addEventListener('submit', (e) => {\n    e.preventDefault();\n    \n    const dados = Object.fromEntries(new FormData(form));\n    console.log(dados);   // { nome: '...', email: '...' }\n});\n\n// FormData coleta TODOS os inputs com name.\n// Object.fromEntries transforma em objeto simples.",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Validação — HTML5 + JS",
            "content": [
                {"type": "text", "value": "**Validação HTML5 nativa** já resolve 60% dos casos **sem uma linha de JS**. Atributos como `required`, `type=\"email\"`, `minlength` fazem o navegador bloquear submits inválidos automaticamente."},
                {
                    "type": "code",
                    "caption": "Validação HTML5 nativa",
                    "value": "<input type=\"email\" required>\n<input type=\"text\" minlength=\"2\" maxlength=\"80\" required>\n<input type=\"number\" min=\"0\" max=\"120\">\n<input type=\"text\" pattern=\"[0-9]{5}\">   <!-- 5 dígitos -->",
                },
                {"type": "text", "value": "**Mas atenção:** a validação HTML5 **não é suficiente**. Um usuário avançado pode usar DevTools para remover os atributos e enviar dados inválidos. Você **sempre precisa validar no backend** também."},
                {"type": "text", "value": "**Validação em JS** — quando você quer **mensagens personalizadas** ou **regras que o HTML5 não cobre** (ex: senha precisa ter número e maiúscula):"},
                {
                    "type": "code",
                    "caption": "Função de validação",
                    "value": "function validar(dados) {\n    const erros = {};\n    \n    if (!dados.nome || dados.nome.trim().length < 2) {\n        erros.nome = 'Nome deve ter pelo menos 2 caracteres';\n    }\n    \n    if (!dados.email.includes('@')) {\n        erros.email = 'Email inválido';\n    }\n    \n    if (dados.senha.length < 8) {\n        erros.senha = 'Senha deve ter pelo menos 8 caracteres';\n    }\n    \n    return erros;\n}",
                },
                {"type": "text", "value": "**O padrão é retornar um objeto de erros.** Se o objeto estiver vazio, tudo ok. Se tiver chaves, mostra os erros ao usuário."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Mostrando Erros ao Usuário",
            "content": [
                {"type": "text", "value": "Validar e não avisar o usuário é inútil. O **feedback visual** dos erros é essencial para UX."},
                {
                    "type": "code",
                    "caption": "Mostrando erros no formulário",
                    "value": "form.addEventListener('submit', (e) => {\n    e.preventDefault();\n    \n    const dados = {\n        nome: form.nome.value,\n        email: form.email.value,\n    };\n    \n    const erros = validar(dados);\n    \n    // Limpa erros antigos\n    document.querySelectorAll('.erro').forEach(el => el.textContent = '');\n    \n    // Se tem erro, mostra e para\n    if (Object.keys(erros).length > 0) {\n        Object.entries(erros).forEach(([campo, msg]) => {\n            const el = document.querySelector(`#erro-${campo}`);\n            if (el) el.textContent = msg;\n        });\n        return;\n    }\n    \n    // Prossegue com o envio\n    console.log('Enviando:', dados);\n});",
                },
                {"type": "text", "value": "**A estrutura HTML esperada:** cada campo tem um `<span id=\"erro-campo\">` ao lado para o erro."},
                {
                    "type": "code",
                    "caption": "HTML com espaço para erros",
                    "value": "<label for=\"email\">Email:</label>\n<input type=\"email\" id=\"email\" name=\"email\">\n<span id=\"erro-email\" class=\"erro\"></span>\n\n<style>\n.erro {\n    color: #ef4444;\n    font-size: 14px;\n    display: block;\n}\n</style>",
                },
                {"type": "text", "value": "**Boas práticas de UX em validação:**"},
                {
                    "type": "code",
                    "caption": "UX em validação",
                    "value": "✅ Valide no blur (quando sai do campo), não a cada tecla\n✅ Mostre o erro PERTO do campo com problema\n✅ Seja específico: 'Senha deve ter 8+ caracteres' > 'Inválido'\n✅ Limpe o erro quando o usuário começar a corrigir\n✅ Foque no primeiro campo com erro após submit\n❌ Não use alert() — é intrusivo e feio",
                },
                {"type": "text", "value": "**Erro comum:** mostrar erro genérico tipo \"Dados inválidos\". O usuário não sabe **o que** está errado. Seja específico. Sempre."},
                {
                    "type": "code",
                    "caption": "Focar no primeiro campo inválido",
                    "value": "// Após validar, se houver erros:\nconst primeiroCampo = Object.keys(erros)[0];\nform[primeiroCampo].focus();\n\n// O cursor vai direto para o campo com problema. Ótima UX.",
                },
            ],
            "exercise": {
                "id": "07-08-ex1", "title": "Validação simples",
                "statement": "Em Python, valide se o email contém `'@'`. Se não contém, imprima `Email inválido`. Se contém, imprima `Email válido`.",
                "starter_code": "email = 'usuario@exemplo.com'\n\n# valide e imprima\n",
                "tests": [{"validation": "output_equals", "expected": "Email válido"}],
                "hint": "if '@' in email: print('Email válido')",
            },
        },
    ],
    "summary": [
        "Capture com form.campo.value ou FormData.",
        "Sempre use e.preventDefault() no submit.",
        "HTML5 valida o básico; JS cobre regras complexas.",
        "Mostre erros perto do campo, específicos, e foque no primeiro.",
        "Sempre valide também no backend — o front pode ser burlado.",
    ],
}


LESSON_07_09 = {
    "id": "07-09", "module_id": "07",
    "title": "ES6+ — Arrow, Destructuring, Spread",
    "objectives": [
        "Usar destructuring em arrays e objetos",
        "Espalhar valores com spread",
        "Combinar objetos e arrays de forma imutável",
        "Conhecer os recursos modernos do JS",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "Recursos que Mudaram o JS",
            "content": [
                {"type": "text", "value": "O **ES6** (2015) foi o maior update da história do JavaScript. Ele trouxe arrow functions, destructuring, spread, template literals, let/const, classes, promises — tudo que hoje é padrão."},
                {"type": "text", "value": "**Por que estudar isso separadamente?** Porque esses recursos aparecem **em todo código moderno** — especialmente React, Vue, Node. Sem entender, você trava em código de terceiros."},
                {
                    "type": "code",
                    "caption": "O antes e depois do ES6",
                    "value": "// ❌ Antes (ES5)\nvar nome = pessoa.nome;\nvar idade = pessoa.idade;\nvar arr2 = arr1.concat([4, 5]);\n\n// ✅ Depois (ES6+)\nconst { nome, idade } = pessoa;\nconst arr2 = [...arr1, 4, 5];",
                },
                {"type": "text", "value": "Vamos focar nos **3 recursos** que você mais vai usar: **destructuring**, **spread** e **rest**."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Destructuring em Profundidade",
            "content": [
                {"type": "text", "value": "**Destructuring** extrai valores de arrays/objetos para variáveis. Existem várias formas de usar, e cada uma é útil em um cenário."},
                {
                    "type": "code",
                    "caption": "Objetos — formas básicas",
                    "value": "const pessoa = { nome: 'Gabrielly', idade: 18, cidade: 'São Carlos' };\n\n// Básico\nconst { nome, idade } = pessoa;\n\n// Renomeando\nconst { nome: nomeCompleto } = pessoa;   // nomeCompleto = 'Gabrielly'\n\n// Valor padrão\nconst { ativo = true } = pessoa;         // ativo = true\n\n// Aninhado\nconst { endereco: { rua } } = pessoa;    // extrai rua de endereco",
                },
                {
                    "type": "code",
                    "caption": "Arrays — formas básicas",
                    "value": "const nums = [10, 20, 30, 40];\n\nconst [a, b] = nums;             // a=10, b=20\nconst [primeiro, ...resto] = nums; // primeiro=10, resto=[20,30,40]\nconst [, segundo] = nums;        // segundo=20 (ignora o 1º)\n\n// Trocar variáveis (sem temp!)\nlet x = 1, y = 2;\n[x, y] = [y, x];   // x=2, y=1",
                },
                {"type": "text", "value": "**Onde isso é mais usado?** Em **parâmetros de função** — é o padrão moderno para receber opções:"},
                {
                    "type": "code",
                    "caption": "Destructuring em parâmetros",
                    "value": "// ❌ Antes (verboso)\nfunction criarUsuario(options) {\n    const nome = options.nome;\n    const idade = options.idade;\n}\n\n// ✅ Com destructuring no parâmetro\nfunction criarUsuario({ nome, idade, ativo = true }) {\n    console.log(nome, idade, ativo);\n}\n\ncriarUsuario({ nome: 'Gabrielly', idade: 18 });",
                },
                {"type": "text", "value": "**Em React**, você vai ver isso **direto**: `function Botao({ texto, onClick, variante = 'primario' })`. É a forma padrão de receber props."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Spread — Copiar sem Mutar",
            "content": [
                {"type": "text", "value": "**Spread (`...`)** espalha os elementos de um array ou objeto. É usado para **copiar**, **combinar** e **substituir valores** — sem mutar o original."},
                {
                    "type": "code",
                    "caption": "Spread em arrays",
                    "value": "const a = [1, 2, 3];\nconst b = [4, 5, 6];\n\n// Combinar\nconst juntos = [...a, ...b];        // [1, 2, 3, 4, 5, 6]\n\n// Copiar (shallow copy)\nconst copia = [...a];                // [1, 2, 3] — nova referência\n\n// Adicionar elemento\nconst comExtra = [...a, 99];        // [1, 2, 3, 99]\nconst comInicio = [0, ...a];        // [0, 1, 2, 3]",
                },
                {
                    "type": "code",
                    "caption": "Spread em objetos",
                    "value": "const base = { nome: 'Gabrielly', idade: 18 };\nconst extra = { cidade: 'São Carlos' };\n\n// Combinar\nconst completo = { ...base, ...extra };\n// { nome: 'Gabrielly', idade: 18, cidade: 'São Carlos' }\n\n// Sobrescrever valor específico\nconst atualizado = { ...base, idade: 19 };\n// { nome: 'Gabrielly', idade: 19 }",
                },
                {"type": "text", "value": "**Por que isso é tão importante?** Porque permite **imutabilidade**. Em vez de mutar o objeto original, você cria um **novo objeto com a mudança aplicada**. É o padrão em React, Redux, e código funcional em geral."},
                {
                    "type": "code",
                    "caption": "Mutação vs Imutabilidade",
                    "value": "// ❌ MUTAÇÃO (evite em React)\nconst user = { nome: 'Gabi', idade: 18 };\nuser.idade = 19;\n// O objeto original foi modificado\n\n// ✅ IMUTABILIDADE (padrão moderno)\nconst user = { nome: 'Gabi', idade: 18 };\nconst novo = { ...user, idade: 19 };\n// 'user' continua igual; 'novo' tem a mudança",
                },
                {"type": "text", "value": "**Spread é shallow (raso).** Ele copia só o **primeiro nível**. Se o objeto tem um campo que é outro objeto, esse campo continua sendo **a mesma referência**."},
                {
                    "type": "code",
                    "caption": "Spread raso (shallow)",
                    "value": "const user = {\n    nome: 'Gabi',\n    endereco: { cidade: 'São Carlos' },\n};\n\nconst copia = { ...user };\ncopia.nome = 'Ana';               // ✅ ok, não afeta o original\ncopia.endereco.cidade = 'SP';     // ❌ MUTA o endereço do original também!\n\n// Para cópia profunda, use structuredClone() (moderno) ou JSON.parse(JSON.stringify(x))",
                },
                {"type": "text", "value": "**Rest (`...` em parâmetros)** é o **oposto** do spread: em vez de espalhar, **coleta** múltiplos valores em um array. Usado em funções que aceitam N argumentos."},
                {
                    "type": "code",
                    "caption": "Rest em parâmetros",
                    "value": "function somarTudo(...numeros) {\n    return numeros.reduce((a, b) => a + b, 0);\n}\n\nsomarTudo(1, 2, 3, 4);   // 10\nsomarTudo();              // 0\n\n// Combina com destructuring:\nconst [primeiro, ...resto] = [1, 2, 3, 4];",
                },
            ],
            "exercise": {
                "id": "07-09-ex1", "title": "Combinando objetos",
                "statement": "Simule em Python: combine dois dicionários `{'nome': 'Gabi'}` e `{'idade': 18}` em um terceiro. Imprima o valor de 'idade'.",
                "starter_code": "a = {'nome': 'Gabi'}\nb = {'idade': 18}\n\n# combine\ncompleto = \nprint(completo['idade'])",
                "tests": [{"validation": "output_equals", "expected": "18"}],
                "hint": "completo = {**a, **b}",
            },
        },
    ],
    "summary": [
        "Destructuring extrai valores de arrays/objetos para variáveis.",
        "Em parâmetros de função, destructuring é padrão (especialmente em React).",
        "Spread (...) copia, combina e sobrescreve — sem mutar.",
        "Spread é raso (shallow); use structuredClone para cópia profunda.",
        "Rest (...) coleta múltiplos argumentos em um array.",
    ],
}


LESSON_07_10 = {
    "id": "07-10", "module_id": "07",
    "title": "map, filter, reduce, find",
    "objectives": [
        "Transformar arrays com map",
        "Filtrar com filter",
        "Reduzir a um valor com reduce",
        "Encontrar elementos com find e findIndex",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "Programação Funcional com Arrays",
            "content": [
                {"type": "text", "value": "Esses métodos **substituem o `for` manual** e deixam o código **declarativo**: você diz **o que** quer, não **como** fazer. É o coração do estilo funcional que domina o JS moderno."},
                {"type": "text", "value": "**A diferença é grande:** com `for`, você escreve o passo a passo. Com `map`/`filter`/`reduce`, você **declara a intenção**. Muito mais legível e menos propenso a bugs."},
                {
                    "type": "code",
                    "caption": "For vs map",
                    "value": "const nums = [1, 2, 3, 4];\n\n// ❌ Com for (imperativo)\nconst dobrados = [];\nfor (let i = 0; i < nums.length; i++) {\n    dobrados.push(nums[i] * 2);\n}\n\n// ✅ Com map (declarativo)\nconst dobrados = nums.map(n => n * 2);",
                },
                {"type": "text", "value": "**Vantagem:** menos linhas, sem variável mutável, fácil de ler. E todos esses métodos podem ser **encadeados** — o resultado de um vira entrada do próximo."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "map e filter",
            "content": [
                {"type": "text", "value": "**`map`** — transforma cada item. Retorna **novo array do mesmo tamanho**, com cada elemento \"mapeado\" para outro valor."},
                {
                    "type": "code",
                    "caption": "map básico",
                    "value": "const nums = [1, 2, 3, 4];\n\nconst dobrados = nums.map(n => n * 2);\nconsole.log(dobrados);   // [2, 4, 6, 8]\n\n// Extrair uma coluna de objetos:\nconst pessoas = [{ nome: 'Gabi' }, { nome: 'Ana' }];\nconst nomes = pessoas.map(p => p.nome);   // ['Gabi', 'Ana']",
                },
                {"type": "text", "value": "**O callback recebe 3 argumentos:** o item, o índice e o array completo. Você geralmente usa só o primeiro."},
                {
                    "type": "code",
                    "caption": "map com índice",
                    "value": "const nums = [10, 20, 30];\n\nconst comIndice = nums.map((n, i) => `${i}: ${n}`);\n// ['0: 10', '1: 20', '2: 30']\n\n// O array original nunca é modificado:\nconsole.log(nums);   // [10, 20, 30]",
                },
                {"type": "text", "value": "**`filter`** — mantém só os itens que passam em uma **condição**. Retorna novo array com tamanho ≤ original."},
                {
                    "type": "code",
                    "caption": "filter básico",
                    "value": "const nums = [1, 2, 3, 4, 5, 6];\n\nconst pares = nums.filter(n => n % 2 === 0);\nconsole.log(pares);   // [2, 4, 6]\n\n// Filtrar objetos:\nconst produtos = [\n    { nome: 'Notebook', preco: 3500 },\n    { nome: 'Mouse', preco: 80 },\n    { nome: 'Teclado', preco: 200 },\n];\n\nconst baratos = produtos.filter(p => p.preco < 1000);\n// [{ nome: 'Mouse', ... }, { nome: 'Teclado', ... }]",
                },
                {"type": "text", "value": "**O callback do `filter` retorna um boolean.** Se for `true`, o item fica. Se for `false`, é descartado."},
                {
                    "type": "code",
                    "caption": "map + filter juntos",
                    "value": "const produtos = [...];\n\n// Nomes dos produtos com preço < 1000\nconst nomesBaratos = produtos\n    .filter(p => p.preco < 1000)\n    .map(p => p.nome);\n\n// Encadeamento: o resultado do filter vira entrada do map.\n// ['Mouse', 'Teclado']",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "reduce, find, findIndex",
            "content": [
                {"type": "text", "value": "**`reduce`** é o mais poderoso e o mais confuso no começo. Ele **reduz** um array a **um único valor** — pode ser número, string, objeto, outro array."},
                {
                    "type": "code",
                    "caption": "reduce — soma de um array",
                    "value": "const nums = [1, 2, 3, 4];\n\nconst soma = nums.reduce((acc, n) => acc + n, 0);\nconsole.log(soma);   // 10\n\n// Parâmetros:\n// acc  → acumulador (valor que vai sendo atualizado)\n// n    → item atual\n// 0    → valor inicial do acumulador",
                },
                {"type": "text", "value": "**Entendendo o fluxo do reduce:** ele percorre o array, e a cada volta o retorno do callback vira o `acc` da próxima volta."},
                {
                    "type": "code",
                    "caption": "reduce passo a passo",
                    "value": "[1, 2, 3, 4].reduce((acc, n) => acc + n, 0)\n\n// volta 1: acc=0, n=1 → retorna 1\n// volta 2: acc=1, n=2 → retorna 3\n// volta 3: acc=3, n=3 → retorna 6\n// volta 4: acc=6, n=4 → retorna 10\n// Resultado final: 10",
                },
                {"type": "text", "value": "**Use `reduce` também para agrupar ou contar:**"},
                {
                    "type": "code",
                    "caption": "reduce para agrupar",
                    "value": "const vendas = [\n    { produto: 'Notebook', valor: 3500 },\n    { produto: 'Mouse', valor: 80 },\n    { produto: 'Notebook', valor: 4000 },\n];\n\n// Total por produto\nconst totalPorProduto = vendas.reduce((acc, v) => {\n    acc[v.produto] = (acc[v.produto] || 0) + v.valor;\n    return acc;\n}, {});\n\n// { Notebook: 7500, Mouse: 80 }",
                },
                {"type": "text", "value": "**`find`** — retorna o **primeiro item** que passa no teste. Ou `undefined` se nenhum passar. Diferente de `filter`, retorna **um único item**, não array."},
                {
                    "type": "code",
                    "caption": "find",
                    "value": "const users = [\n    { id: 1, nome: 'Gabi' },\n    { id: 2, nome: 'Ana' },\n    { id: 3, nome: 'João' },\n];\n\nconst user = users.find(u => u.id === 2);\nconsole.log(user);   // { id: 2, nome: 'Ana' }\n\nconst naoAchou = users.find(u => u.id === 99);\nconsole.log(naoAchou);   // undefined",
                },
                {"type": "text", "value": "**`findIndex`** — igual ao `find`, mas retorna o **índice** em vez do item."},
                {
                    "type": "code",
                    "caption": "findIndex",
                    "value": "const idx = users.findIndex(u => u.id === 2);\nconsole.log(idx);   // 1",
                },
                {"type": "text", "value": "**Resumo do guia de escolha:**"},
                {
                    "type": "code",
                    "caption": "Quando usar cada um",
                    "value": "map      → transformar cada item (mesmo tamanho)\nfilter   → manter apenas os que passam (tamanho ≤)\nreduce   → reduzir a um único valor (soma, objeto, string)\nfind     → primeiro item que passa (ou undefined)\nfindIndex→ índice do primeiro que passa (ou -1)\nsome     → true se ALGUM passa\n every    → true se TODOS passam\nincludes → true se o array contém o valor (primitivos)",
                },
                {"type": "text", "value": "**Você vai usar esses métodos em React o tempo todo.** Renderizar listas, filtrar resultados, calcular totais, buscar itens específicos. Dominar aqui é investimento direto no próximo módulo."},
            ],
            "exercise": {
                "id": "07-10-ex1", "title": "Soma com reduce",
                "statement": "Simule um `reduce` em Python: some todos os números de `[10, 20, 30, 40]` usando um loop e imprima o resultado.",
                "starter_code": "nums = [10, 20, 30, 40]\ntotal = 0\n# some com for\n\nprint(total)",
                "tests": [{"validation": "output_equals", "expected": "100"}],
                "hint": "for n in nums: total += n",
            },
        },
    ],
    "summary": [
        "map transforma cada item (mesmo tamanho).",
        "filter mantém os que passam (tamanho menor ou igual).",
        "reduce reduz a um único valor (com acc e valor inicial).",
        "find retorna o primeiro match; findIndex retorna o índice.",
        "Encadeie métodos: arr.filter(...).map(...).reduce(...)",
    ],
}


LESSON_07_11 = {
    "id": "07-11", "module_id": "07",
    "title": "Promises e async/await",
    "objectives": [
        "Entender o que é assincronismo",
        "Criar e consumir Promises",
        "Usar async/await para código assíncrono limpo",
        "Tratar erros com try/catch e Promise.all",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "t1",
            "title": "O que é Assincronismo",
            "content": [
                {"type": "text", "value": "**JavaScript é single-threaded** — executa **uma coisa por vez**. Isso é diferente de linguagens multi-thread como Java ou C#. Se uma operação demora, ela **trava tudo**... ou travaria, se não existisse assincronismo."},
                {"type": "text", "value": "**O problema:** buscar dados de uma API pode levar 2 segundos. Se o JS esperasse de forma síncrona, a página **congelaria** por 2 segundos. Botões não responderiam. Animações parariam. Experiência péssima."},
                {"type": "text", "value": "**A solução:** operações demoradas (rede, timers, arquivos) são **assíncronas**. O JS dispara a operação, **continua executando o resto do código**, e quando o resultado chega, **volta** para processá-lo."},
                {
                    "type": "code",
                    "caption": "Síncrono vs assíncrono",
                    "value": "// ❌ Bloqueante (hipotético)\nconst dados = buscarAPI();   // trava 2 segundos!\nconsole.log('depois');        // só roda depois\n\n// ✅ Assíncrono (JS real)\nconsole.log('antes');\nbuscarAPI().then(dados => {\n    console.log('dados chegaram');\n});\nconsole.log('depois');\n\n// Saída:\n// 'antes'\n// 'depois'\n// 'dados chegaram'  ← chega depois!",
                },
                {"type": "text", "value": "**Por que isso é bom?** Porque enquanto a API responde, o usuário continua clicando, a página continua rolando, outras operações continuam rodando. É o que torna a web fluida."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Promises — o Antes do async/await",
            "content": [
                {"type": "text", "value": "Uma **Promise** é um **objeto que representa um valor futuro**. Ela tem 3 estados:"},
                {
                    "type": "code",
                    "caption": "Os 3 estados de uma Promise",
                    "value": "pending   → ainda esperando\nfulfilled → deu certo, tem valor\nrejected  → deu erro",
                },
                {"type": "text", "value": "**Criar uma Promise:** você passa uma função com dois callbacks — `resolve` (deu certo) e `reject` (deu erro)."},
                {
                    "type": "code",
                    "caption": "Promise simples",
                    "value": "const esperar = (ms) => {\n    return new Promise((resolve) => {\n        setTimeout(resolve, ms);\n    });\n};\n\nesperar(1000).then(() => {\n    console.log('Passou 1 segundo');\n});",
                },
                {"type": "text", "value": "**Consumir uma Promise:** você usa `.then()` para o sucesso e `.catch()` para o erro. Mas isso gera o famoso **\"callback hell\"** quando você precisa encadear várias operações."},
                {
                    "type": "code",
                    "caption": "Callback hell",
                    "value": "buscarUsuario(id)\n    .then(user => buscarPosts(user.id))\n    .then(posts => buscarComentarios(posts[0].id))\n    .then(comentarios => console.log(comentarios))\n    .catch(erro => console.error(erro));\n\n// Encadeamento de promises funciona, mas fica difícil de ler\n// quando há muitas etapas ou lógica condicional no meio.",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "async/await — o Padrão Moderno",
            "content": [
                {"type": "text", "value": "**`async/await`** é uma forma mais **legível** de trabalhar com Promises. Ele faz código assíncrono parecer **síncrono**, sem bloquear a thread."},
                {"type": "text", "value": "Duas palavras-chave: **`async`** antes da função (habilita `await` dentro) e **`await`** antes da Promise (espera o resultado)."},
                {
                    "type": "code",
                    "caption": "Refatorando callback hell em async/await",
                    "value": "async function carregarTudo() {\n    const user = await buscarUsuario(id);\n    const posts = await buscarPosts(user.id);\n    const comentarios = await buscarComentarios(posts[0].id);\n    console.log(comentarios);\n}",
                },
                {"type": "text", "value": "**Lê-se como código síncrono**, mas por baixo é assíncrono. O `await` **pausa a função** (não a thread) até a Promise resolver. Enquanto isso, o resto do programa continua rodando."},
                {"type": "text", "value": "**Tratando erros:** com `async/await`, use `try/catch` — o mesmo do Python."},
                {
                    "type": "code",
                    "caption": "try/catch com async",
                    "value": "async function buscar() {\n    try {\n        const resposta = await fetch('https://api.exemplo.com');\n        const dados = await resposta.json();\n        return dados;\n    } catch (erro) {\n        console.error('Erro:', erro);\n        return null;\n    }\n}",
                },
                {"type": "text", "value": "**Regra:** sempre que uma função usa `await`, ela precisa ser `async`. E toda chamada de função async retorna uma Promise — que você pode (deve) tratar com `try/catch` ou `.catch()`."},
                {"type": "text", "value": "**Rodar em paralelo:** se as operações **não dependem uma da outra**, você pode rodar **em paralelo** com `Promise.all` — muito mais rápido."},
                {
                    "type": "code",
                    "caption": "Sequencial vs paralelo",
                    "value": "// ❌ Sequencial (2s + 2s = 4s total)\nconst a = await fetchA();   // 2s\nconst b = await fetchB();   // 2s\n\n// ✅ Paralelo (2s total — as duas ao mesmo tempo)\nconst [a, b] = await Promise.all([\n    fetchA(),\n    fetchB(),\n]);",
                },
                {"type": "text", "value": "**`Promise.all`** aceita um array de Promises e retorna **um array com todos os resultados**. Se uma falhar, o `Promise.all` inteiro rejeita. Existe também `Promise.allSettled` que espera **todas**, mesmo as que falharam."},
                {
                    "type": "code",
                    "caption": "Promise.allSettled",
                    "value": "const results = await Promise.allSettled([\n    fetchA(),   // pode falhar\n    fetchB(),   // pode falhar\n]);\n\n// results = [\n//   { status: 'fulfilled', value: ... },\n//   { status: 'rejected', reason: ... },\n// ]\n// Não rejeita — sempre retorna todos os status.",
                },
                {"type": "text", "value": "**A regra prática:** sempre que ver `await`, saiba que aquela linha **pode demorar**. Trate com `try/catch` quando fizer sentido, e use `Promise.all` para paralelizar."},
            ],
            "exercise": {
                "id": "07-11-ex1", "title": "Simulando async",
                "statement": "Em Python, use try/except para simular tratamento de erro. Tente converter 'abc' para inteiro e, no except, imprima 'Erro capturado'.",
                "starter_code": "try:\n    int('abc')\nexcept ValueError:\n    # imprima\n    ",
                "tests": [{"validation": "output_equals", "expected": "Erro capturado"}],
                "hint": "print('Erro capturado')",
            },
        },
    ],
    "summary": [
        "JS é single-threaded, mas operações de rede/timers são assíncronas.",
        "Promises representam valor futuro (pending, fulfilled, rejected).",
        "async/await é a forma moderna e legível de trabalhar com Promises.",
        "Use try/catch para erros; Promise.all para paralelizar.",
    ],
}


LESSON_07_12 = {
    "id": "07-12", "module_id": "07",
    "title": "fetch e Consumo de APIs",
    "objectives": [
        "Fazer requisições HTTP com fetch",
        "Enviar dados com POST",
        "Configurar headers e body",
        "Tratar respostas e erros corretamente",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "fetch — Conversando com APIs",
            "content": [
                {"type": "text", "value": "**`fetch()`** é a forma **nativa** de fazer requisições HTTP no navegador. Retorna uma Promise. Substitui o antigo `XMLHttpRequest`, que era verboso e feio."},
                {"type": "text", "value": "**Onde você usa?** Para consumir APIs — seja sua API FastAPI, a API do GitHub, do Mercado Pago, de qualquer serviço. É a ponte entre seu frontend e o mundo externo."},
                {
                    "type": "code",
                    "caption": "GET básico",
                    "value": "async function buscarUsuarios() {\n    const resposta = await fetch('https://api.exemplo.com/usuarios');\n    const dados = await resposta.json();\n    return dados;\n}\n\n// Duas etapas:\n// 1. fetch retorna a RESPOSTA (headers, status)\n// 2. resposta.json() retorna o BODY (dados)",
                },
                {"type": "text", "value": "**Por que duas etapas?** Porque a resposta HTTP tem **duas partes**: os headers (metadados — status code, content-type) e o body (o conteúdo em si). O `fetch` retorna a resposta completa; você precisa extrair o body com `.json()`, `.text()` ou `.blob()`."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "POST — Enviando Dados",
            "content": [
                {"type": "text", "value": "Para criar ou modificar recursos, você usa **POST** (ou PUT/PATCH/DELETE). O `fetch` recebe um **segundo argumento** com as opções: método, headers, body."},
                {
                    "type": "code",
                    "caption": "POST com body JSON",
                    "value": "async function criarUsuario(usuario) {\n    const resposta = await fetch('https://api.exemplo.com/usuarios', {\n        method: 'POST',\n        headers: {\n            'Content-Type': 'application/json',\n        },\n        body: JSON.stringify(usuario),\n    });\n    \n    return resposta.json();\n}\n\ncriarUsuario({ nome: 'Gabi', email: 'g@x.com' });",
                },
                {"type": "text", "value": "**⚠️ O `Content-Type: application/json` é obrigatório.** Sem ele, o servidor não sabe que está recebendo JSON e pode rejeitar o body. É o erro mais comum de iniciantes."},
                {"type": "text", "value": "**⚠️ `JSON.stringify` no body.** O `fetch` só envia **strings**. Se você passar um objeto direto, o JS converte para `[object Object]` — bug clássico."},
                {
                    "type": "code",
                    "caption": "O que acontece se esquecer stringify",
                    "value": "// ❌ Sem stringify\nbody: { nome: 'Gabi' }\n// Envia: '[object Object]' — o servidor não entende\n\n// ✅ Com stringify\nbody: JSON.stringify({ nome: 'Gabi' })\n// Envia: '{\"nome\":\"Gabi\"}' — correto",
                },
                {"type": "text", "value": "**Enviando token de autenticação:** APIs protegidas esperam o token no header `Authorization`:"},
                {
                    "type": "code",
                    "caption": "Requisição autenticada",
                    "value": "const token = localStorage.getItem('token');\n\nconst resposta = await fetch('/api/perfil', {\n    headers: {\n        'Authorization': `Bearer ${token}`,\n        'Content-Type': 'application/json',\n    },\n});",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Tratando Erros Corretamente",
            "content": [
                {"type": "text", "value": "**Atenção ao detalhe crítico:** o `fetch` **não rejeita** quando recebe um erro HTTP (400, 500). Ele só rejeita quando **falha de rede** (sem internet, DNS errado). Isso pega muita gente."},
                {
                    "type": "code",
                    "caption": "O problema",
                    "value": "const resposta = await fetch('/api/usuarios/999');\n// Se o servidor retorna 404, fetch NÃO lança erro!\n// Você precisa checar manualmente:\n\nif (!resposta.ok) {\n    throw new Error(`Erro ${resposta.status}`);\n}",
                },
                {"type": "text", "value": "**`resposta.ok`** é `true` se o status está entre 200 e 299. Sempre verifique!"},
                {
                    "type": "code",
                    "caption": "Padrão completo de fetch seguro",
                    "value": "async function buscar(url) {\n    try {\n        const resposta = await fetch(url);\n        \n        if (!resposta.ok) {\n            throw new Error(`HTTP ${resposta.status}: ${resposta.statusText}`);\n        }\n        \n        return await resposta.json();\n    } catch (erro) {\n        console.error('Falha na requisição:', erro.message);\n        throw erro;   // relança para quem chamou tratar\n    }\n}",
                },
                {"type": "text", "value": "**O `try/catch` cobre dois tipos de erro:**"},
                {
                    "type": "code",
                    "caption": "Dois tipos de erro",
                    "value": "1. Erro de REDE (sem internet, DNS, CORS)\n   → fetch() lança automaticamente\n\n2. Erro HTTP (400, 404, 500)\n   → fetch NÃO lança, você precisa checar resposta.ok",
                },
                {"type": "text", "value": "**CORS no console do navegador?** Se você vir `CORS policy: No 'Access-Control-Allow-Origin'`, é o **backend** que precisa liberar sua origem. Você configura `CORSMiddleware` no FastAPI (que você já aprendeu no Módulo 05)."},
                {"type": "text", "value": "**Padrão profissional:** crie uma **camada de API** — um arquivo `api.js` com todas as chamadas centralizadas. Assim você não repete headers, tratamento de erro, URL base."},
                {
                    "type": "code",
                    "caption": "Camada de API",
                    "value": "// api.js\nconst API_URL = 'http://localhost:8000';\n\nasync function request(path, options = {}) {\n    const token = localStorage.getItem('token');\n    \n    const resposta = await fetch(`${API_URL}${path}`, {\n        ...options,\n        headers: {\n            'Content-Type': 'application/json',\n            ...(token ? { Authorization: `Bearer ${token}` } : {}),\n            ...options.headers,\n        },\n    });\n    \n    if (!resposta.ok) {\n        throw new Error(`HTTP ${resposta.status}`);\n    }\n    \n    return resposta.json();\n}\n\nexport const api = {\n    listarUsuarios: () => request('/usuarios'),\n    criarUsuario: (u) => request('/usuarios', {\n        method: 'POST',\n        body: JSON.stringify(u),\n    }),\n};",
                },
                {"type": "text", "value": "**Esse padrão é o mesmo que você vai usar no React.** Na verdade, essa camada `api.js` vira módulo importado nos componentes. Faz uma vez, usa em todo lugar."},
            ],
            "exercise": {
                "id": "07-12-ex1", "title": "Simulando JSON",
                "statement": "Converta o dicionário `{'nome': 'Gabi'}` para string JSON (simule JSON.stringify em Python). Imprima o resultado.",
                "starter_code": "import json\ndados = {'nome': 'Gabi'}\nprint()",
                "tests": [{"validation": "output_contains_all", "expected": ["nome", "Gabi"]}],
                "hint": "print(json.dumps(dados, ensure_ascii=False))",
            },
        },
    ],
    "summary": [
        "fetch é nativo e retorna Promise — use com async/await.",
        "GET: só await fetch(url). POST: adicionar method, headers, body.",
        "Content-Type: application/json e JSON.stringify são obrigatórios no POST.",
        "fetch NÃO rejeita em erro HTTP — cheque resposta.ok.",
        "Centralize chamadas em api.js com headers e token automáticos.",
    ],
}


LESSON_07_13 = {
    "id": "07-13", "module_id": "07",
    "title": "LocalStorage e SessionStorage",
    "objectives": [
        "Persistir dados no navegador",
        "Diferenciar localStorage de sessionStorage",
        "Salvar objetos com JSON.stringify/parse",
        "Entender segurança de tokens",
    ],
    "reading_time_minutes": 12,
    "topics": [
        {
            "id": "t1",
            "title": "Guardando Dados no Navegador",
            "content": [
                {"type": "text", "value": "**Web Storage** é o mecanismo do navegador para guardar dados **persistentes** entre visitas — sem precisar de servidor, sem precisar de banco, sem cookies. Tudo do lado do cliente."},
                {"type": "text", "value": "Existem **dois tipos**: `localStorage` e `sessionStorage`. A diferença é só **quando expiram**."},
                {
                    "type": "code",
                    "caption": "localStorage vs sessionStorage",
                    "value": "localStorage    → persiste PARA SEMPRE (até limpar manualmente)\n                  → ~5-10 MB por domínio\n                  → compartilhado entre abas\n\nsessionStorage  → dura só enquanto a ABA está aberta\n                  → ao fechar a aba, some\n                  → NÃO compartilhado entre abas",
                },
                {"type": "text", "value": "**A API é idêntica** para os dois. Só muda o objeto (`localStorage` vs `sessionStorage`)."},
                {
                    "type": "code",
                    "caption": "API básica",
                    "value": "// Salvar\nlocalStorage.setItem('nome', 'Gabrielly');\n\n// Ler\nconst nome = localStorage.getItem('nome');   // 'Gabrielly'\n\n// Remover um item\nlocalStorage.removeItem('nome');\n\n// Limpar tudo\nlocalStorage.clear();",
                },
                {"type": "text", "value": "**⚠️ Web Storage só guarda STRINGS.** Se você tentar salvar um objeto direto, ele vira `[object Object]` — bug clássico."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Salvando Objetos com JSON",
            "content": [
                {"type": "text", "value": "Para salvar objetos ou arrays, você precisa **converter para string JSON** antes de salvar, e **converter de volta** ao ler."},
                {
                    "type": "code",
                    "caption": "Salvando e lendo objetos",
                    "value": "const usuario = { nome: 'Gabrielly', idade: 18 };\n\n// ✅ Salvar convertendo para string\nlocalStorage.setItem('user', JSON.stringify(usuario));\n\n// ✅ Ler convertendo de volta para objeto\nconst lido = JSON.parse(localStorage.getItem('user'));\nconsole.log(lido.nome);   // 'Gabrielly'",
                },
                {"type": "text", "value": "**⚠️ Cuidado com `null`:** se o item não existe, `getItem` retorna `null`. E `JSON.parse(null)` retorna `null`. Se tentar acessar uma propriedade de `null`, dá erro."},
                {
                    "type": "code",
                    "caption": "Padrão seguro com valor padrão",
                    "value": "function carregar(chave, padrao) {\n    const raw = localStorage.getItem(chave);\n    if (!raw) return padrao;\n    try {\n        return JSON.parse(raw);\n    } catch {\n        return padrao;   // JSON inválido\n    }\n}\n\nconst tarefas = carregar('tarefas', []);",
                },
                {"type": "text", "value": "**Sempre forneça um valor padrão** ao ler. Assim você nunca tem `null` quebrando seu código."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Segurança — o que NUNCA guardar",
            "content": [
                {"type": "text", "value": "**⚠️ ATENÇÃO CRÍTICA:** Web Storage é **totalmente acessível por JavaScript** rodando na página. Isso significa que **qualquer** script — inclusive os maliciosos — pode ler tudo que você guardou lá."},
                {
                    "type": "code",
                    "caption": "O que NUNCA colocar no localStorage",
                    "value": "🚫 Senhas\n🚫 Dados de cartão de crédito\n🚫 Chaves de API (secret, private)\n🚫 Informações sensíveis do usuário (CPF, RG)\n🚫 Tokens de sessão de longa duração",
                },
                {"type": "text", "value": "**Por que tokens são um caso delicado?** Muitos devs guardam o JWT no `localStorage` para facilitar. Isso funciona, mas tem um risco: se um atacante conseguir injetar JS na sua página (XSS), ele rouba o token."},
                {"type": "text", "value": "**A alternativa mais segura são cookies `HttpOnly`** — cookies que o **JavaScript NÃO consegue ler**, só o servidor. O navegador envia automaticamente em cada requisição, mas um script malicioso não consegue acessar."},
                {
                    "type": "code",
                    "caption": "Comparação de segurança",
                    "value": "localStorage               Cookie HttpOnly\n─────────────────────      ─────────────────────\nJS consegue ler? ✅        ❌\nEnviado automático? ❌     ✅\nProtegido de XSS? ❌       ✅\nFácil de usar? ✅          ⚠️ requer config backend",
                },
                {"type": "text", "value": "**Recomendação prática:** para projetos didáticos (como este curso), use `localStorage` para guardar o token JWT. Funciona. Mas saiba que em produção real, o ideal é cookie `HttpOnly` + `Secure` + `SameSite`."},
                {"type": "text", "value": "**Quando usar cada um?**"},
                {
                    "type": "code",
                    "caption": "Casos de uso",
                    "value": "localStorage    → tema (dark/light), idioma, preferências, rascunhos, carrinho\nsessionStorage  → dados de formulário em andamento, estado de wizard de múltiplas etapas\n\nNUNCA            → senhas, cartão de crédito, info sensível",
                },
                {"type": "text", "value": "**Como inspecionar:** abra o DevTools (F12) → aba **Application** → **Local Storage**. Você vê tudo que está salvo e pode apagar. Ótimo para debugar."},
            ],
            "exercise": {
                "id": "07-13-ex1", "title": "Simulando localStorage",
                "statement": "Simule em Python: crie um dicionário `storage = {}` e adicione a chave 'nome' com valor 'Gabi'. Imprima `storage['nome']`.",
                "starter_code": "storage = {}\n# adicione 'nome': 'Gabi'\nprint()",
                "tests": [{"validation": "output_equals", "expected": "Gabi"}],
                "hint": "storage['nome'] = 'Gabi' — depois print(storage['nome'])",
            },
        },
    ],
    "summary": [
        "localStorage persiste; sessionStorage dura só a sessão da aba.",
        "Guarde objetos via JSON.stringify/parse — só aceita strings.",
        "Sempre leia com valor padrão para evitar null.",
        "NUNCA guarde senhas ou dados sensíveis no localStorage.",
        "Para produção, prefira cookies HttpOnly para tokens.",
    ],
}


LESSON_07_14 = {
    "id": "07-14", "module_id": "07",
    "title": "Projeto: To-do List",
    "objectives": [
        "Juntar tudo do módulo em um projeto real",
        "Manipular DOM dinamicamente",
        "Persistir estado no localStorage",
        "Aplicar eventos, arrays e manipulação de dados",
    ],
    "reading_time_minutes": 30,
    "topics": [
        {
            "id": "t1",
            "title": "Planejando a To-do List",
            "content": [
                {"type": "text", "value": "Chegou a hora de juntar **tudo** do módulo 07 em uma aplicação real. Vamos construir uma **To-do List** completa: adicionar, listar, marcar como feita, remover e **persistir no navegador**."},
                {"type": "text", "value": "**Por que To-do List?** Porque ela exercita **todos** os conceitos importantes do JS: DOM, eventos, arrays, objetos, localStorage, funções, arrow, destructuring. É o \"hello world\" das SPAs."},
                {"type": "text", "value": "**Funcionalidades da versão final:**"},
                {
                    "type": "code",
                    "caption": "O que vamos construir",
                    "value": "1. Adicionar tarefa via formulário\n2. Listar todas as tarefas\n3. Marcar como feita (toggle)\n4. Remover tarefa\n5. Persistir no localStorage\n6. Renderizar ao carregar a página",
                },
                {"type": "text", "value": "**Estrutura HTML:**"},
                {
                    "type": "code",
                    "caption": "HTML base",
                    "value": "<div class=\"app\">\n    <h1>Minhas Tarefas</h1>\n\n    <form id=\"form\">\n        <input id=\"input\" placeholder=\"Nova tarefa...\" required>\n        <button type=\"submit\">Adicionar</button>\n    </form>\n\n    <ul id=\"lista\"></ul>\n</div>",
                },
                {"type": "text", "value": "**Arquitetura da aplicação** — o conceito mais importante é: **o estado manda, o DOM reflete**."},
                {
                    "type": "code",
                    "caption": "O conceito central",
                    "value": "estado (array de tarefas)\n    ↓\nrenderização (redesenha a UI baseado no estado)\n    ↓\nusuário interage (evento)\n    ↓\nmuda o ESTADO\n    ↓\nre-renderiza\n\n// Você NÃO mexe no DOM diretamente.\n// Você mexe no ESTADO e deixa o render fazer o resto.",
                },
                {"type": "text", "value": "**Esse padrão é o coração do React.** Você está aprendendo a mentalidade certa antes de partir para o framework. A diferença é que no React, o re-render é automático."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Estado e Persistência",
            "content": [
                {"type": "text", "value": "**Primeiro passo:** definir o estado — um array de tarefas. Cada tarefa é um objeto com `texto` e `feita`."},
                {
                    "type": "code",
                    "caption": "Estado inicial",
                    "value": "// Carrega do localStorage ou inicia vazio\nlet tarefas = JSON.parse(localStorage.getItem('tarefas') || '[]');\n\n// Estrutura esperada:\n// [\n//   { texto: 'Estudar JS', feita: false },\n//   { texto: 'Fazer projeto', feita: true },\n// ]",
                },
                {"type": "text", "value": "**Função `salvar()`** — centraliza a gravação no localStorage. Sempre que o estado mudar, você chama essa função."},
                {
                    "type": "code",
                    "caption": "Função de salvar",
                    "value": "function salvar() {\n    localStorage.setItem('tarefas', JSON.stringify(tarefas));\n}",
                },
                {"type": "text", "value": "**Por que sempre chamar `salvar()` depois de cada mudança?** Porque o localStorage não reage automaticamente ao seu array — você precisa **explicitamente** dizer \"agora grava\"."},
                {"type": "text", "value": "**Função `renderizar()`** — desenha o DOM baseado no estado atual. **Toda vez que o estado mudar, chame essa função.**"},
                {
                    "type": "code",
                    "caption": "Função de renderizar",
                    "value": "function renderizar() {\n    const lista = document.getElementById('lista');\n    lista.innerHTML = '';   // limpa tudo\n\n    tarefas.forEach((tarefa, i) => {\n        const li = document.createElement('li');\n        \n        // Estrutura da tarefa:\n        li.innerHTML = `\n            <span class=\"${tarefa.feita ? 'feita' : ''}\">${tarefa.texto}</span>\n            <button data-acao=\"toggle\" data-index=\"${i}\">✓</button>\n            <button data-acao=\"remover\" data-index=\"${i}\">✕</button>\n        `;\n        \n        lista.appendChild(li);\n    });\n}",
                },
                {"type": "text", "value": "**Vamos entender o que essa função faz:**"},
                {
                    "type": "code",
                    "caption": "Passo a passo do render",
                    "value": "1. Pega a <ul>\n2. Limpa ela toda (innerHTML = '') — remove tudo antigo\n3. Para cada tarefa no array:\n   a. Cria um <li>\n   b. Coloca HTML dentro com o texto e 2 botões\n   c. Adiciona o li na <ul>",
                },
                {"type": "text", "value": "**`data-*` attributes** — o `data-index` e `data-acao` são lidos via `dataset` no handler de clique. Isso permite identificar **qual** botão foi clicado dentro de **qual** tarefa."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Adicionando, Marcando e Removendo",
            "content": [
                {"type": "text", "value": "**Adicionar tarefa** — escuta o submit do form e faz push no array."},
                {
                    "type": "code",
                    "caption": "Handler de adicionar",
                    "value": "document.getElementById('form').addEventListener('submit', (e) => {\n    e.preventDefault();\n    \n    const input = document.getElementById('input');\n    const texto = input.value.trim();\n    \n    if (!texto) return;   // ignora vazio\n    \n    tarefas.push({ texto, feita: false });\n    input.value = '';      // limpa o input\n    \n    salvar();\n    renderizar();\n});",
                },
                {"type": "text", "value": "**Repare nos detalhes:**"},
                {
                    "type": "code",
                    "caption": "Boas práticas do handler",
                    "value": "e.preventDefault()      → não recarrega a página\nvalue.trim()            → remove espaços extras\nif (!texto) return      → ignora envios vazios\ninput.value = ''        → limpa após adicionar\nsalvar() + renderizar() → sempre juntos, nessa ordem",
                },
                {"type": "text", "value": "**Marcar/remover — usando delegação de eventos.** Um único listener na `<ul>` cobre **todos** os botões, mesmo os criados depois. Isso é fundamental, porque o render recria os elementos toda vez."},
                {
                    "type": "code",
                    "caption": "Delegação de eventos na lista",
                    "value": "document.getElementById('lista').addEventListener('click', (e) => {\n    const acao = e.target.dataset.acao;\n    const index = Number(e.target.dataset.index);\n    \n    if (!acao) return;   // clicou fora de botão\n    \n    if (acao === 'toggle') {\n        tarefas[index].feita = !tarefas[index].feita;\n    } else if (acao === 'remover') {\n        tarefas.splice(index, 1);\n    }\n    \n    salvar();\n    renderizar();\n});",
                },
                {"type": "text", "value": "**Por que delegação é essencial aqui?** Porque o `renderizar()` **recria** os `<li>` do zero toda vez. Se você tivesse colocado listener em cada botão, os listeners antigos sumiriam. Com delegação no pai, **funciona sempre**."},
                {"type": "text", "value": "**Ponto de entrada da aplicação:** renderizar ao carregar."},
                {
                    "type": "code",
                    "caption": "Bootstrap da app",
                    "value": "// Ao carregar, renderiza o estado atual\nrenderizar();",
                },
                {"type": "text", "value": "**Combinando tudo — o fluxo completo:**"},
                {
                    "type": "code",
                    "caption": "Fluxo de uma ação",
                    "value": "1. Usuário digita 'Estudar JS' e clica em Adicionar\n2. Handler de submit:\n   a. preventDefault\n   b. tarefas.push({ texto: 'Estudar JS', feita: false })\n   c. salvar() → vai pro localStorage\n   d. renderizar() → <li> aparece na tela\n3. Usuário clica no ✓\n4. Delegação captura o clique:\n   a. index = 0, acao = 'toggle'\n   b. tarefas[0].feita = true\n   c. salvar() + renderizar()\n5. Usuário fecha e reabre a página\n6. localStorage.getItem('tarefas') → carrega de volta\n7. Estado restaurado, UI aparece igual",
                },
                {"type": "text", "value": "**Desafios para ir além:**"},
                {
                    "type": "code",
                    "caption": "Melhorias para praticar",
                    "value": "1. Adicionar filtros: todas / ativas / concluídas\n2. Contador de tarefas pendentes\n3. Botão 'limpar concluídas'\n4. Editar uma tarefa (double click → input)\n5. Animação de entrada com CSS transitions\n6. Validação com feedback visual\n7. Ordenar por data de criação",
                },
                {"type": "text", "value": "**Parabéns!** Você acabou de construir uma **aplicação real** com JavaScript puro. Sem framework, sem biblioteca. Tudo que faz aqui, o React faz mais rápido — **mas você entende o porquê** por trás. Isso te coloca à frente de 90% dos devs que pulam direto para framework."},
                {"type": "text", "value": "**Próximo passo:** no módulo de React, você vai reconstruir essa To-do List em **20 linhas**. E vai entender **cada linha**, porque aprendeu o que está por baixo."},
            ],
            "exercise": {
                "id": "07-14-ex1", "title": "Simulando adicionar tarefa",
                "statement": "Em Python, simule adicionar tarefas: crie uma lista `tarefas = []` e adicione 2 dicionários `{'texto': 'Estudar', 'feita': False}` e `{'texto': 'Dormir', 'feita': False}`. Imprima o tamanho da lista.",
                "starter_code": "tarefas = []\n# adicione 2 tarefas\n\nprint(len(tarefas))",
                "tests": [{"validation": "output_equals", "expected": "2"}],
                "hint": "tarefas.append({'texto': 'Estudar', 'feita': False}) e tarefas.append({'texto': 'Dormir', 'feita': False})",
            },
        },
    ],
    "summary": [
        "Estado manda, DOM reflete: mude o array e chame renderizar().",
        "renderizar() recria os <li> do zero, baseado no estado.",
        "Delegação de eventos na <ul> funciona com elementos criados depois.",
        "data-* attributes identificam qual item foi clicado.",
        "salvar() + renderizar() após cada mudança — o par indissociável.",
    ],
}


