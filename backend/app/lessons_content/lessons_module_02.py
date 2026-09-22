"""Lições do Módulo 02 — extraídas automaticamente de lessons_content.py."""

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
                {"type": "text", "value": "**Passo 1 — Baixe o Python.** Acesse [python.org/downloads](https://www.python.org/downloads/) e clique no botão amarelo de download; o site já identifica seu sistema (Windows, Mac ou Linux) sozinho. No instalador do **Windows**, marque a caixinha **\"Add python.exe to PATH\"** logo na primeira tela, antes de clicar em Install Now. Sem isso, o Python não funciona no terminal. No **Mac**, essa etapa já é feita automaticamente pelo instalador."},
                {"type": "text", "value": "**Passo 2 — Baixe o VS Code.** Acesse [code.visualstudio.com](https://code.visualstudio.com/) e clique no botão azul de download. Abra o instalador, aceite os termos e siga com as opções padrão até instalar. No Windows, marque também a opção **\"Adicionar ao PATH\"**, se ela aparecer."},
                {"type": "text", "value": "**Passo 3 — Instale a extensão do Python.** Abra o VS Code, clique no ícone de quadrados (**Extensions**) na barra lateral esquerda, digite \"Python\" e instale a extensão oficial da **Microsoft** — é a primeira da lista, com o ícone azul e amarelo. Ela adiciona autocomplete, execução e detecção de erros."},
                {"type": "text", "value": "**Passo 4 — Confira se o Python está instalado.** Abra o terminal integrado do VS Code (atalho `` Ctrl + ` ``, ou `View → Terminal`) e digite:"},
                {
                    "type": "code",
                    "caption": "Verificando a instalação",
                    "value": "python --version\n# ou, se não funcionar:\npy --version\n\n# Saída esperada:\n# Python 3.12.x (ou similar)",
                },
                {"type": "text", "value": "**Passo 5 — Crie sua pasta de projetos.** Crie uma pasta no seu computador para guardar seus códigos — por exemplo, `python-curso` na Área de Trabalho. No VS Code, vá em `File → Open Folder` e selecione essa pasta."},
                {"type": "text", "value": "**Passo 6 — Crie o arquivo e dê um nome a ele.** Na barra lateral esquerda, passe o mouse sobre o nome da pasta e clique no ícone de página com um **\"+\"** que aparece. Digite o nome do arquivo **seguido da extensão `.py`** — por exemplo, `main.py` — e aperte Enter."},
                {"type": "text", "value": "É a extensão `.py` no final do nome que avisa o VS Code (e o Python) que esse arquivo é código Python. Sem ela, o botão de rodar não aparece e a extensão não reconhece o arquivo. Evite espaços e acentos no nome — prefira `meu_arquivo.py` a `meu arquivo.py`."},
                {
                    "type": "code",
                    "caption": "Primeiro programa",
                    "value": "print(\"Olá, mundo!\")",
                },
                {"type": "text", "value": "Escreva o código acima no arquivo, salve com `Ctrl + S` (ou `Cmd + S` no Mac) e rode clicando no **▶** no canto superior direito, ou no terminal com `python main.py`. Se aparecer **\"Olá, mundo!\"**, parabéns — seu ambiente está pronto! 🎉"},
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
        "Todo arquivo Python termina com a extensão .py — sem ela, o VS Code não roda o código.",
    ],
}


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


