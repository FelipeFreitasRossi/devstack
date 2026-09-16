"""Lições do Módulo 04 — extraídas automaticamente de lessons_content.py."""

LESSON_04_01 = {
    "id": "04-01",
    "module_id": "04",
    "title": "HTTP e APIs REST",
    "objectives": [
        "Entender o que é HTTP e como a web funciona",
        "Conhecer os principais métodos HTTP (GET, POST, PUT, DELETE)",
        "Entender o que é uma API REST",
        "Saber o que são status codes e como interpretá-los",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "topico-1",
            "title": "Como a Web Conversa",
            "content": [
                {"type": "text", "value": "Sempre que você abre um site, seu navegador **pede** uma página para um servidor, e o servidor **responde**. Essa conversa acontece através do **HTTP** (HyperText Transfer Protocol)."},
                {"type": "text", "value": "Pense em HTTP como um **idioma** que todo cliente (navegador, app, script) e todo servidor falam. Toda conversa tem **requisição** (o que o cliente quer) e **resposta** (o que o servidor devolve)."},
                {
                    "type": "code",
                    "caption": "Anatomia de uma requisição HTTP",
                    "value": "GET /api/usuarios HTTP/1.1\nHost: meusite.com\nAuthorization: Bearer abc123\n\n# Método | Caminho | Versão\n# Host: onde está o servidor\n# Authorization: quem está pedindo",
                },
                {"type": "text", "value": "A resposta também tem estrutura: **status code**, **headers** (metadados) e **body** (conteúdo). O status code diz se deu certo ou não."},
                {
                    "type": "code",
                    "caption": "Anatomia de uma resposta HTTP",
                    "value": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\"id\": 1, \"nome\": \"Gabrielly\"}\n\n# 200 = sucesso\n# Content-Type = formato do body\n# body = dados em si",
                },
            ],
            "exercise": None,
        },
        {
            "id": "topico-2",
            "title": "Métodos HTTP e APIs REST",
            "content": [
                {"type": "text", "value": "Os **métodos HTTP** dizem **o que o cliente quer fazer**. Os quatro principais são a base de qualquer API:"},
                {
                    "type": "code",
                    "caption": "Os 4 métodos principais",
                    "value": "GET    → buscar/ler dados      (não muda nada)\nPOST   → criar novo recurso     (envia dados)\nPUT    → atualizar recurso      (substitui)\nDELETE → apagar recurso",
                },
                {"type": "text", "value": "Uma **API REST** é uma forma padronizada de organizar esses métodos. A ideia é: cada **recurso** (usuário, produto, pedido) tem uma **URL** própria, e você usa os métodos HTTP para manipulá-los."},
                {
                    "type": "code",
                    "caption": "API REST de usuários",
                    "value": "GET    /usuarios        → lista todos os usuários\nGET    /usuarios/1      → busca o usuário 1\nPOST   /usuarios        → cria um novo usuário\nPUT    /usuarios/1      → atualiza o usuário 1\nDELETE /usuarios/1      → apaga o usuário 1",
                },
                {"type": "text", "value": "**Status codes** são números que o servidor devolve para dizer como foi. Você já viu alguns por aí — o famoso **404** (não encontrado) é um deles."},
                {
                    "type": "code",
                    "caption": "Status codes mais comuns",
                    "value": "2xx → sucesso\n  200 OK              → deu tudo certo\n  201 Created         → recurso criado\n\n4xx → erro do cliente\n  400 Bad Request     → dados inválidos\n  401 Unauthorized    → não está logado\n  403 Forbidden       → sem permissão\n  404 Not Found       → não existe\n\n5xx → erro do servidor\n  500 Internal Error  → deu ruim no servidor",
                },
                {"type": "text", "value": "**Por que isso importa?** Toda aplicação moderna consome API — seu frontend React vai falar com o backend FastAPI, e ambos falam HTTP. Saber interpretar status code é metade do trabalho de debugar."},
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "HTTP é o idioma da web: requisição + resposta.",
        "GET, POST, PUT, DELETE são os 4 métodos principais.",
        "API REST organiza recursos em URLs padronizadas.",
        "Status codes 2xx = sucesso, 4xx = erro do cliente, 5xx = erro do servidor.",
    ],
}


LESSON_04_02 = {
    "id": "04-02",
    "module_id": "04",
    "title": "Biblioteca requests",
    "objectives": [
        "Instalar e importar a biblioteca requests",
        "Fazer requisições GET e POST",
        "Passar parâmetros e headers",
        "Tratar erros de rede e status codes",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "topico-1",
            "title": "Fazendo Requisições",
            "content": [
                {"type": "text", "value": "A biblioteca **`requests`** é a forma mais simples de fazer requisições HTTP em Python. Ela esconde toda a complexidade e deixa o código limpo."},
                {"type": "text", "value": "Primeiro, instale no terminal:"},
                {
                    "type": "code",
                    "caption": "Instalando requests",
                    "value": "pip install requests",
                },
                {"type": "text", "value": "Depois, importe e faça uma requisição GET. O método `.get()` faz uma requisição para a URL informada:"},
                {
                    "type": "code",
                    "caption": "Primeira requisição GET",
                    "value": "import requests\n\nresposta = requests.get(\"https://api.github.com\")\n\nprint(resposta.status_code)   # 200\nprint(resposta.text[:100])     # primeiros 100 caracteres",
                },
                {"type": "text", "value": "Se a API devolver **JSON**, você pode usar `.json()` para transformar direto em um dicionário Python:"},
                {
                    "type": "code",
                    "caption": "Convertendo resposta em dicionário",
                    "value": "import requests\n\nresposta = requests.get(\"https://api.github.com/users/octocat\")\ndados = resposta.json()\n\nprint(dados[\"name\"])       # The Octocat\nprint(dados[\"public_repos\"])",
                },
                {"type": "text", "value": "Para **POST** (criar recurso), use `.post()` e passe o body com `json=`:"},
                {
                    "type": "code",
                    "caption": "Requisição POST",
                    "value": "import requests\n\nnovo_usuario = {\n    \"nome\": \"Gabrielly\",\n    \"email\": \"g@email.com\"\n}\n\nresposta = requests.post(\n    \"https://api.exemplo.com/usuarios\",\n    json=novo_usuario\n)\n\nprint(resposta.status_code)   # 201",
                },
            ],
            "exercise": {
                "id": "04-02-ex1",
                "title": "Simulando uma requisição",
                "statement": "Como o sandbox não tem acesso à internet, vamos **simular** uma resposta. Crie um dicionário `resposta` com `status_code = 200` e `dados = {'nome': 'Gabrielly'}`. Depois, imprima o valor de `resposta['dados']['nome']`.",
                "starter_code": "resposta = {\n    'status_code': 200,\n    'dados': {'nome': 'Gabrielly'}\n}\n\n# Imprima o nome\nprint()",
                "tests": [
                    {"validation": "output_equals", "expected": "Gabrielly"},
                ],
                "hint": "print(resposta['dados']['nome'])",
            },
        },
        {
            "id": "topico-2",
            "title": "Parâmetros, Headers e Erros",
            "content": [
                {"type": "text", "value": "Quando você precisa filtrar dados, use **`params`**. Ele converte um dicionário em query string automaticamente."},
                {
                    "type": "code",
                    "caption": "Enviando parâmetros (query string)",
                    "value": "import requests\n\nparametros = {\"q\": \"python\", \"page\": 1}\n\nresposta = requests.get(\n    \"https://api.exemplo.com/busca\",\n    params=parametros\n)\n\n# A URL vira:\n# https://api.exemplo.com/busca?q=python&page=1",
                },
                {"type": "text", "value": "**Headers** enviam metadados como autenticação, tipo de conteúdo, idioma:"},
                {
                    "type": "code",
                    "caption": "Enviando headers",
                    "value": "import requests\n\nheaders = {\n    \"Authorization\": \"Bearer meu-token-aqui\",\n    \"Accept\": \"application/json\"\n}\n\nresposta = requests.get(\n    \"https://api.exemplo.com/perfil\",\n    headers=headers\n)",
                },
                {"type": "text", "value": "Toda requisição pode falhar: sem internet, timeout, servidor fora do ar. Use **`try/except`** com `requests.exceptions` para tratar."},
                {
                    "type": "code",
                    "caption": "Tratando erros de rede",
                    "value": "import requests\n\ntry:\n    resposta = requests.get(\"https://api.exemplo.com\", timeout=5)\n    resposta.raise_for_status()   # lança exceção se status >= 400\nexcept requests.exceptions.Timeout:\n    print(\"O servidor demorou demais para responder\")\nexcept requests.exceptions.ConnectionError:\n    print(\"Falha na conexão — verifique sua internet\")\nexcept requests.exceptions.HTTPError as e:\n    print(f\"Erro na API: {e}\")",
                },
                {"type": "text", "value": "**`raise_for_status()`** é sua amiga: ela **lança uma exceção** se o status code for 4xx ou 5xx. Assim você não precisa verificar `if resposta.status_code == 200` em todo lugar."},
            ],
            "exercise": {
                "id": "04-02-ex2",
                "title": "Montando uma URL com parâmetros",
                "statement": "Simule a construção de uma URL com parâmetros. Crie uma variável `url` com o valor `'https://api.exemplo.com/busca?q=python&page=1'`. Depois, imprima a URL.",
                "starter_code": "url = \nprint(url)",
                "tests": [
                    {"validation": "output_contains_all", "expected": ["q=python", "page=1"]},
                ],
                "hint": "url = 'https://api.exemplo.com/busca?q=python&page=1'",
            },
        },
    ],
    "summary": [
        "requests.get() e requests.post() são os mais usados.",
        "Use .json() para converter respostas em dicionários.",
        "params monta query string; headers envia metadados.",
        "Trate erros com try/except e raise_for_status().",
    ],
}


LESSON_04_03 = {
    "id": "04-03",
    "module_id": "04",
    "title": "Trabalhando com JSON",
    "objectives": [
        "Entender o formato JSON",
        "Converter entre Python e JSON",
        "Acessar dados aninhados em JSON",
        "Salvar e ler arquivos JSON",
    ],
    "reading_time_minutes": 12,
    "topics": [
        {
            "id": "topico-1",
            "title": "O Formato Universal de Dados",
            "content": [
                {"type": "text", "value": "**JSON** (JavaScript Object Notation) é o formato **universal** de troca de dados. APIs, bancos NoSQL, arquivos de configuração — tudo usa JSON. Ele é basicamente um dicionário Python com regras próprias."},
                {
                    "type": "code",
                    "caption": "Estrutura básica de JSON",
                    "value": "{\n    \"nome\": \"Gabrielly\",\n    \"idade\": 18,\n    \"ativo\": true,\n    \"cursos\": [\"Python\", \"React\"],\n    \"endereco\": {\n        \"cidade\": \"São Carlos\",\n        \"estado\": \"SP\"\n    }\n}",
                },
                {"type": "text", "value": "As **regras** do JSON: chaves sempre entre aspas duplas, valores podem ser string, número, boolean, null, lista ou outro objeto. Sem vírgula no último item."},
                {"type": "text", "value": "Para **converter um dicionário Python em string JSON**, use `json.dumps()` (a letra **s** significa \"string\"):"},
                {
                    "type": "code",
                    "caption": "Python → JSON (dumps)",
                    "value": "import json\n\nusuario = {\"nome\": \"Gabrielly\", \"idade\": 18}\n\n# dumps = dict to string\njson_str = json.dumps(usuario, ensure_ascii=False)\nprint(json_str)\n# {\"nome\": \"Gabrielly\", \"idade\": 18}\nprint(type(json_str))   # <class 'str'>",
                },
                {"type": "text", "value": "Para o caminho contrário — **string JSON em dicionário Python** — use `json.loads()`:"},
                {
                    "type": "code",
                    "caption": "JSON → Python (loads)",
                    "value": "import json\n\ntexto = '{\"nome\": \"Gabrielly\", \"idade\": 18}'\n\n# loads = string to dict\nusuario = json.loads(texto)\nprint(usuario[\"nome\"])   # Gabrielly\nprint(type(usuario))     # <class 'dict'>",
                },
            ],
            "exercise": {
                "id": "04-03-ex1",
                "title": "Dicionário para JSON",
                "statement": "Importe `json`. Converta o dicionário `{'produto': 'Notebook', 'preco': 3500}` em uma string JSON usando `json.dumps()` com `ensure_ascii=False`. Imprima o resultado.",
                "starter_code": "import json\n\ndados = {'produto': 'Notebook', 'preco': 3500}\n\n# Converta para string JSON\nresultado = \nprint(resultado)",
                "tests": [
                    {"validation": "output_contains_all", "expected": ["Notebook", "3500"]},
                ],
                "hint": "resultado = json.dumps(dados, ensure_ascii=False)",
            },
        },
        {
            "id": "topico-2",
            "title": "Dados Aninhados e Arquivos",
            "content": [
                {"type": "text", "value": "JSONs reais têm **vários níveis**. Você acessa assim como faria com dicionários e listas aninhados."},
                {
                    "type": "code",
                    "caption": "Acessando dados aninhados",
                    "value": "import json\n\ndados = json.loads('''\n{\n    \"empresa\": \"Devstack\",\n    \"funcionarios\": [\n        {\"nome\": \"Gabrielly\", \"cargo\": \"Dev\"},\n        {\"nome\": \"Ana\", \"cargo\": \"Designer\"}\n    ]\n}\n''')\n\nprint(dados[\"empresa\"])                    # Devstack\nprint(dados[\"funcionarios\"][0][\"nome\"])   # Gabrielly\nprint(dados[\"funcionarios\"][1][\"cargo\"])  # Designer",
                },
                {"type": "text", "value": "Para **gravar** JSON em um arquivo, use `json.dump()` (sem o **s**). Note que é uma função diferente — ela escreve no arquivo em vez de retornar string."},
                {
                    "type": "code",
                    "caption": "Gravando JSON em arquivo",
                    "value": "import json\n\nconfig = {\n    \"tema\": \"dark\",\n    \"idioma\": \"pt-BR\",\n    \"notificacoes\": True\n}\n\nwith open(\"config.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(config, f, ensure_ascii=False, indent=2)",
                },
                {"type": "text", "value": "E para **ler** de um arquivo, use `json.load()` (sem o **s**):"},
                {
                    "type": "code",
                    "caption": "Lendo JSON de arquivo",
                    "value": "import json\n\nwith open(\"config.json\", \"r\", encoding=\"utf-8\") as f:\n    config = json.load(f)\n\nprint(config[\"tema\"])   # dark",
                },
                {"type": "text", "value": "**Diferença que confunde muita gente:**"},
                {
                    "type": "code",
                    "caption": "dumps/loads vs dump/load",
                    "value": "dumps() → objeto → string    (s = string)\nloads() → string → objeto    (s = string)\n\ndump()  → objeto → arquivo   (sem s = sem string)\nload()  → arquivo → objeto   (sem s = sem string)",
                },
            ],
            "exercise": {
                "id": "04-03-ex2",
                "title": "Lendo dados aninhados",
                "statement": "Dada a variável `dados` (um dicionário já pronto), acesse o nome do segundo funcionário da lista `funcionarios` e imprima. Estrutura: `{'funcionarios': [{'nome': 'Gabrielly'}, {'nome': 'Ana'}]}`.",
                "starter_code": "dados = {'funcionarios': [{'nome': 'Gabrielly'}, {'nome': 'Ana'}]}\n\n# Imprima o nome do segundo funcionário\nprint()",
                "tests": [
                    {"validation": "output_equals", "expected": "Ana"},
                ],
                "hint": "print(dados['funcionarios'][1]['nome'])",
            },
        },
    ],
    "summary": [
        "JSON é o formato universal de dados na web.",
        "dumps/loads convertem entre Python e string JSON.",
        "dump/load leem e gravam arquivos JSON.",
        "Use ensure_ascii=False para preservar acentos.",
    ],
}


LESSON_04_04 = {
    "id": "04-04",
    "module_id": "04",
    "title": "Autenticação Básica",
    "objectives": [
        "Entender por que APIs precisam de autenticação",
        "Conhecer os tipos principais (Basic, API Key, Bearer/JWT)",
        "Enviar credenciais em requisições",
        "Guardar tokens com segurança (variáveis de ambiente)",
    ],
    "reading_time_minutes": 12,
    "topics": [
        {
            "id": "topico-1",
            "title": "Formas de Autenticação",
            "content": [
                {"type": "text", "value": "A maioria das APIs **não deixa qualquer um acessar**. Elas precisam saber **quem está pedindo** e se essa pessoa tem permissão. Isso é autenticação."},
                {"type": "text", "value": "Existem 3 formas principais que você vai encontrar:"},
                {
                    "type": "code",
                    "caption": "Os 3 tipos mais comuns",
                    "value": "1. Basic Auth    → usuário e senha em Base64 (simples, mas inseguro sem HTTPS)\n2. API Key       → chave única em header ou query string\n3. Bearer / JWT  → token gerado após login (padrão moderno)",
                },
                {"type": "text", "value": "O **Bearer Token** (usado com JWT) é o padrão atual. O fluxo é: o cliente faz login enviando email/senha, o servidor devolve um **token**, e o cliente envia esse token em **todas as requisições futuras**."},
                {
                    "type": "code",
                    "caption": "Fluxo de autenticação com token",
                    "value": "1. Cliente → POST /login {email, senha}\n2. Servidor → 200 {token: \"eyJhbGc...\"}\n3. Cliente salva o token\n4. Cliente → GET /perfil com header Authorization: Bearer eyJhbGc...\n5. Servidor valida o token e responde",
                },
                {"type": "text", "value": "Em Python com `requests`, o token vai no **header** `Authorization`:"},
                {
                    "type": "code",
                    "caption": "Enviando Bearer Token",
                    "value": "import requests\n\ntoken = \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...\"\n\nheaders = {\n    \"Authorization\": f\"Bearer {token}\",\n    \"Content-Type\": \"application/json\"\n}\n\nresposta = requests.get(\n    \"https://api.exemplo.com/perfil\",\n    headers=headers\n)",
                },
            ],
            "exercise": {
                "id": "04-04-ex1",
                "title": "Montando o header",
                "statement": "Crie uma variável `token` com o valor `'abc123'`. Depois, crie um dicionário `headers` com a chave `'Authorization'` e valor `'Bearer abc123'` (use f-string). Imprima o valor de `headers['Authorization']`.",
                "starter_code": "token = 'abc123'\n\n# Monte o header\nheaders = {\n    'Authorization': \n}\n\nprint(headers['Authorization'])",
                "tests": [
                    {"validation": "output_equals", "expected": "Bearer abc123"},
                ],
                "hint": "'Authorization': f\"Bearer {token}\"",
            },
        },
        {
            "id": "topico-2",
            "title": "Segurança de Tokens",
            "content": [
                {"type": "text", "value": "**Nunca** coloque tokens, senhas ou chaves de API direto no código. Se você fizer isso e subir pro GitHub, qualquer pessoa no mundo pode usar suas credenciais — e você pode perder dinheiro."},
                {
                    "type": "code",
                    "caption": "❌ Como NÃO fazer",
                    "value": "API_KEY = \"sk-1234567890abcdef\"   # 🚨 EXPOSTO NO GITHUB!\n\ntoken = \"eyJhbGciOiJIUzI1NiJ9...\"  # 🚨 VAZOU!",
                },
                {"type": "text", "value": "A forma correta é usar **variáveis de ambiente**. Elas ficam num arquivo `.env` que **NUNCA é commitado** (sempre no `.gitignore`)."},
                {
                    "type": "code",
                    "caption": "✅ Como fazer direito",
                    "value": "# Arquivo .env\nAPI_KEY=sk-1234567890abcdef\nDATABASE_URL=mongodb://...",
                },
                {
                    "type": "code",
                    "caption": "Lendo do .env no código",
                    "value": "import os\nfrom dotenv import load_dotenv\n\nload_dotenv()   # carrega o .env\n\nAPI_KEY = os.getenv(\"API_KEY\")\n\n# Agora API_KEY tem o valor, sem estar no código\nheaders = {\"Authorization\": f\"Bearer {API_KEY}\"}\n\n# Instale com: pip install python-dotenv",
                },
                {"type": "text", "value": "**JWT (JSON Web Token)** é o formato de token mais usado. Ele tem 3 partes separadas por ponto: **header.payload.signature**. O payload carrega informações (id do usuário, expiração) e a signature garante que ninguém adulterou."},
                {
                    "type": "code",
                    "caption": "Anatomia de um JWT",
                    "value": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyMTIzIn0.abc123xyz\n\n|     header      |      payload      |   signature   |\n\nO payload decodificado seria:\n{\"sub\": \"user123\", \"exp\": 1735689600}",
                },
                {"type": "text", "value": "**Boa prática:** tokens **nunca** devem ser guardados no `localStorage` de sites públicos. Use cookies `HttpOnly` quando possível. Mas isso é papo de frontend — no Python, o importante é só usar variáveis de ambiente."},
            ],
            "exercise": {
                "id": "04-04-ex2",
                "title": "Simulando leitura de .env",
                "statement": "Simule a leitura de uma variável de ambiente. Crie um dicionário `env` com `{'API_KEY': 'minha-chave-secreta'}`. Depois, imprima o valor de `env['API_KEY']`.",
                "starter_code": "env = {'API_KEY': 'minha-chave-secreta'}\n\n# Imprima o valor\nprint()",
                "tests": [
                    {"validation": "output_equals", "expected": "minha-chave-secreta"},
                ],
                "hint": "print(env['API_KEY'])",
            },
        },
    ],
    "summary": [
        "Bearer Token (JWT) é o padrão moderno de autenticação.",
        "Tokens vão no header Authorization: Bearer <token>.",
        "NUNCA coloque credenciais no código — use .env.",
        "Sempre coloque .env no .gitignore.",
    ],
}


LESSON_04_05 = {
    "id": "04-05",
    "module_id": "04",
    "title": "Variáveis de Ambiente",
    "objectives": [
        "Entender o que são variáveis de ambiente",
        "Criar e usar arquivo .env",
        "Carregar variáveis com python-dotenv",
        "Organizar configurações por ambiente (dev/prod)",
    ],
    "reading_time_minutes": 10,
    "topics": [
        {
            "id": "topico-1",
            "title": "Configurações Fora do Código",
            "content": [
                {"type": "text", "value": "**Variável de ambiente** é um valor que fica **fora do código** e é lido em tempo de execução. É a forma profissional de guardar configurações que **mudam entre ambientes** (desenvolvimento, teste, produção)."},
                {"type": "text", "value": "Pense assim: o código é o mesmo em todos os lugares, mas a **URL do banco de dados**, **chave de API**, **senha de email** mudam entre sua máquina e o servidor. Esses valores ficam nas variáveis de ambiente."},
                {
                    "type": "code",
                    "caption": "Exemplos de variáveis de ambiente",
                    "value": "DATABASE_URL   → string de conexão com o banco\nAPI_KEY        → chave de API externa\nJWT_SECRET     → chave secreta para gerar tokens\nDEBUG          → True em dev, False em produção\nPORT           → porta do servidor",
                },
                {"type": "text", "value": "Você **não precisa de biblioteca** para ler variáveis de ambiente que já existem no sistema — o módulo `os` resolve:"},
                {
                    "type": "code",
                    "caption": "Lendo com os.getenv()",
                    "value": "import os\n\n# Lê a variável PATH (que todo sistema tem)\npath = os.getenv(\"PATH\")\n\n# Se não existir, retorna None\nvalor = os.getenv(\"NAO_EXISTE\")            # None\n\n# Ou você pode passar um valor padrão\nvalor = os.getenv(\"NAO_EXISTE\", \"padrao\")  # \"padrao\"",
                },
                {"type": "text", "value": "Mas **definir** variáveis de ambiente no sistema para cada projeto é chato. Por isso usamos o arquivo **`.env`** com a biblioteca `python-dotenv`."},
            ],
            "exercise": None,
        },
        {
            "id": "topico-2",
            "title": "Arquivo .env na Prática",
            "content": [
                {"type": "text", "value": "O arquivo `.env` fica na raiz do projeto, com **uma variável por linha**, no formato `CHAVE=valor`. Sem espaços em volta do `=`."},
                {
                    "type": "code",
                    "caption": "Exemplo de .env",
                    "value": "# Configurações do projeto\nDATABASE_URL=mongodb://localhost:27017/meuapp\nAPI_KEY=sk-abc123xyz\nJWT_SECRET=minha-chave-super-secreta\nDEBUG=True\nPORT=8000",
                },
                {"type": "text", "value": "No código, você instala e usa `python-dotenv` para carregar essas variáveis automaticamente:"},
                {
                    "type": "code",
                    "caption": "Carregando o .env",
                    "value": "# No terminal\npip install python-dotenv\n\n# No código\nimport os\nfrom dotenv import load_dotenv\n\nload_dotenv()   # lê o .env e popula o ambiente\n\ndatabase_url = os.getenv(\"DATABASE_URL\")\njwt_secret = os.getenv(\"JWT_SECRET\")\ndebug = os.getenv(\"DEBUG\") == \"True\"\n\nprint(database_url)",
                },
                {"type": "text", "value": "**Regra de ouro:** o `.env` **NUNCA** vai pro GitHub. Adicione no `.gitignore` **antes** do primeiro commit. Se vazar, qualquer um acessa seu banco."},
                {
                    "type": "code",
                    "caption": ".gitignore correto",
                    "value": "# .gitignore\n.env\n.env.local\n.env.production\nvenv/\n__pycache__/",
                },
                {"type": "text", "value": "**Boa prática profissional:** crie um arquivo **`.env.example`** com as chaves mas **sem valores**. Ele vai pro Git e serve de guia para outros devs."},
                {
                    "type": "code",
                    "caption": ".env.example (vai pro Git)",
                    "value": "# Copie para .env e preencha os valores\nDATABASE_URL=\nAPI_KEY=\nJWT_SECRET=\nDEBUG=False\nPORT=8000",
                },
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "Variáveis de ambiente guardam configurações fora do código.",
        "os.getenv() lê; load_dotenv() carrega o .env.",
        "NUNCA commite o .env — coloque no .gitignore.",
        "Crie .env.example como template para o time.",
    ],
}


LESSON_04_06 = {
    "id": "04-06",
    "module_id": "04",
    "title": "Introdução a Banco de Dados",
    "objectives": [
        "Entender o que é um banco de dados e por que usar",
        "Diferenciar bancos relacionais (SQL) de não-relacionais (NoSQL)",
        "Conhecer os principais bancos do mercado",
        "Entender o conceito de tabela, documento, coleção",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "topico-1",
            "title": "Por que Usar um Banco de Dados",
            "content": [
                {"type": "text", "value": "Você já guardou dados em **arquivos JSON** — funcionou bem para pouca coisa. Mas quando sua aplicação cresce, arquivos ficam lentos, difíceis de consultar e perigosos de corromper."},
                {"type": "text", "value": "**Banco de dados** é um sistema especializado em **armazenar, buscar e organizar** dados com segurança, performance e concorrência (vários usuários ao mesmo tempo)."},
                {
                    "type": "code",
                    "caption": "Arquivo JSON vs Banco de dados",
                    "value": "Arquivo JSON                  → Banco de dados\n─────────────────────────────────────────────────\n1 usuário por vez              → milhares simultâneos\nBusca lenta em arquivo grande  → Busca otimizada (índices)\nSem validação                  → Schema validado\nSem backup                     → Backup automático\nSem segurança                  → Autenticação + permissões",
                },
                {"type": "text", "value": "Existem **dois grandes tipos** de banco de dados, e cada um brilha em cenários diferentes:"},
                {
                    "type": "code",
                    "caption": "SQL vs NoSQL",
                    "value": "SQL (relacional)              NoSQL (não-relacional)\n──────────────────────────────────────────────────\nTabelas com colunas fixas     → Documentos/coleções flexíveis\nRelações entre tabelas        → Dados aninhados\nSchema rígido                 → Schema flexível\nEx: PostgreSQL, MySQL         → Ex: MongoDB, Redis\nIdeal para: dados estruturados → Ideal para: dados variados",
                },
                {"type": "text", "value": "**Banco relacional (SQL)** organiza dados em **tabelas** com linhas e colunas. Imagine uma planilha do Excel — cada aba é uma tabela, cada linha é um registro, cada coluna é um campo."},
                {
                    "type": "code",
                    "caption": "Exemplo de tabela SQL — usuários",
                    "value": "id  | nome        | email           | idade\n────┼─────────────┼─────────────────┼──────\n1   | Gabrielly   | g@email.com     | 18\n2   | Ana         | ana@email.com   | 25\n3   | João        | joao@email.com  | 20",
                },
                {"type": "text", "value": "**Banco NoSQL** (como MongoDB) organiza dados em **documentos** dentro de **coleções**. Um documento parece um dicionário Python, e uma coleção é como uma lista de documentos."},
                {
                    "type": "code",
                    "caption": "Exemplo de documento no MongoDB",
                    "value": "// Coleção: usuarios\n{\n    \"_id\": \"abc123\",\n    \"nome\": \"Gabrielly\",\n    \"email\": \"g@email.com\",\n    \"idade\": 18,\n    \"cursos\": [\"Python\", \"React\"]\n}",
                },
            ],
            "exercise": None,
        },
        {
            "id": "topico-2",
            "title": "Qual Banco Escolher?",
            "content": [
                {"type": "text", "value": "Não existe \"melhor banco\" universal — existe o banco **adequado ao problema**. Vamos ver quando cada um faz sentido:"},
                {
                    "type": "code",
                    "caption": "Quando usar SQL",
                    "value": "✅ Dados muito estruturados (financeiro, ERP, e-commerce)\n✅ Relações complexas (usuário → pedido → produto)\n✅ Transações críticas (não pode perder dinheiro)\n✅ Relatórios complexos com JOINs",
                },
                {
                    "type": "code",
                    "caption": "Quando usar NoSQL",
                    "value": "✅ Dados com schema variável (posts, comentários)\n✅ Prototipagem rápida (schema flexível)\n✅ Escala horizontal massiva (milhões de usuários)\n✅ Dados aninhados naturalmente (perfil com endereço, telefone)",
                },
                {"type": "text", "value": "**Neste curso**, vamos usar **MongoDB** porque:"},
                {
                    "type": "code",
                    "caption": "Por que MongoDB neste curso",
                    "value": "1. Documentos são parecidos com dicionários Python (curva menor)\n2. Não precisa aprender SQL separadamente\n3. MongoDB Atlas tem camada gratuita excelente\n4. É o padrão em stacks modernas (MERN, MEAN, e Python moderno)\n5. Schema flexível ajuda no início de projetos",
                },
                {"type": "text", "value": "**Conceitos que você vai usar no MongoDB** — decora essa relação:"},
                {
                    "type": "code",
                    "caption": "SQL → MongoDB",
                    "value": "SQL              MongoDB\n──────────────────────────\nDatabase    →    Database\nTabela      →    Coleção (collection)\nLinha       →    Documento (document)\nColuna      →    Campo (field)\nSELECT      →    find()\nINSERT      →    insert_one()\nUPDATE      →    update_one()\nDELETE      →    delete_one()",
                },
                {"type": "text", "value": "**Dica prática:** se você souber os dois, sabe escolher. Empresas grandes raramente usam só um — muitas usam PostgreSQL **e** MongoDB, cada um para o que faz melhor."},
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "Banco de dados é essencial para qualquer app real.",
        "SQL = tabelas relacionadas; NoSQL = documentos flexíveis.",
        "MongoDB: Database → Coleção → Documento → Campo.",
        "Escolha o banco pelo problema, não pela moda.",
    ],
}


LESSON_04_07 = {
    "id": "04-07",
    "module_id": "04",
    "title": "CRUD — Create, Read, Update, Delete",
    "objectives": [
        "Entender o que é CRUD e por que é a base de todo sistema",
        "Implementar as 4 operações com dicionários Python",
        "Simular um banco de dados em memória",
        "Preparar o terreno para usar MongoDB",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "topico-1",
            "title": "As 4 Operações Universais",
            "content": [
                {"type": "text", "value": "**CRUD** é a sigla para as **4 operações básicas** de qualquer sistema que guarda dados. Instagram, iFood, Nubank — tudo é CRUD por baixo."},
                {
                    "type": "code",
                    "caption": "As 4 operações",
                    "value": "Create  → criar novo registro    (INSERT / POST)\nRead    → buscar/ler registros   (SELECT / GET)\nUpdate  → atualizar registro     (UPDATE / PUT)\nDelete  → apagar registro        (DELETE / DELETE)",
                },
                {"type": "text", "value": "Antes de partir para MongoDB, vamos **simular um banco de dados** com uma lista de dicionários Python. É uma forma ótima de entender a lógica sem depender de instalação."},
                {
                    "type": "code",
                    "caption": "Simulando um banco em memória",
                    "value": "# Nossa \"tabela\" é uma lista de dicionários\nusuarios = []\n\n# Cada usuário terá este formato:\n# {\"id\": 1, \"nome\": \"Gabrielly\", \"email\": \"g@email.com\"}",
                },
                {"type": "text", "value": "**CREATE** — Adicionar um novo registro. Precisamos gerar um **id único** para cada um."},
                {
                    "type": "code",
                    "caption": "CREATE — criar usuário",
                    "value": "def criar_usuario(nome, email):\n    novo_id = len(usuarios) + 1\n    usuario = {\"id\": novo_id, \"nome\": nome, \"email\": email}\n    usuarios.append(usuario)\n    return usuario\n\ncriar_usuario(\"Gabrielly\", \"g@email.com\")\ncriar_usuario(\"Ana\", \"ana@email.com\")\n\nprint(usuarios)\n# [{\"id\": 1, \"nome\": \"Gabrielly\", ...}, {\"id\": 2, \"nome\": \"Ana\", ...}]",
                },
            ],
            "exercise": {
                "id": "04-07-ex1",
                "title": "Criar um registro",
                "statement": "Você tem uma lista vazia `usuarios = []`. Crie um dicionário `novo` com `{'id': 1, 'nome': 'Gabrielly'}` e adicione na lista com `append()`. Imprima o tamanho da lista usando `len()`.",
                "starter_code": "usuarios = []\n\nnovo = {'id': 1, 'nome': 'Gabrielly'}\n\n# Adicione na lista\n\n\nprint(len(usuarios))",
                "tests": [
                    {"validation": "output_equals", "expected": "1"},
                ],
                "hint": "usuarios.append(novo)",
            },
        },
        {
            "id": "topico-2",
            "title": "Read, Update e Delete",
            "content": [
                {"type": "text", "value": "**READ** — Buscar registros. Você pode listar todos ou filtrar por algum critério (id, nome, etc)."},
                {
                    "type": "code",
                    "caption": "READ — listar e buscar",
                    "value": "def listar_usuarios():\n    return usuarios\n\ndef buscar_por_id(id_usuario):\n    for u in usuarios:\n        if u[\"id\"] == id_usuario:\n            return u\n    return None\n\nprint(buscar_por_id(1))\n# {\"id\": 1, \"nome\": \"Gabrielly\", \"email\": \"g@email.com\"}",
                },
                {"type": "text", "value": "**UPDATE** — Modificar um registro existente. Você encontra pelo id e altera os campos que quiser."},
                {
                    "type": "code",
                    "caption": "UPDATE — atualizar registro",
                    "value": "def atualizar_email(id_usuario, novo_email):\n    for u in usuarios:\n        if u[\"id\"] == id_usuario:\n            u[\"email\"] = novo_email\n            return True\n    return False\n\natualizar_email(1, \"gabrielly@novo.com\")\nprint(usuarios[0][\"email\"])   # gabrielly@novo.com",
                },
                {"type": "text", "value": "**DELETE** — Remover um registro. Você filtra pelo id e retira da lista."},
                {
                    "type": "code",
                    "caption": "DELETE — remover registro",
                    "value": "def deletar_usuario(id_usuario):\n    global usuarios\n    usuarios = [u for u in usuarios if u[\"id\"] != id_usuario]\n\ndeletar_usuario(1)\nprint(len(usuarios))   # 1 (só sobrou o segundo)",
                },
                {"type": "text", "value": "**Pronto!** Você acabou de implementar CRUD completo com dicionários. Quando aprendermos MongoDB no Módulo 10, essas mesmas 4 funções vão virar `insert_one()`, `find()`, `update_one()` e `delete_one()` — a **lógica é a mesma**."},
                {"type": "text", "value": "**Por que essa lição é importante?** Todo sistema é CRUD + regras de negócio. Instagram: criar post (C), ver feed (R), editar bio (U), apagar post (D). iFood: criar pedido (C), ver histórico (R), alterar endereço (U), cancelar (D). Entender CRUD é entender 80% dos backends."},
            ],
            "exercise": {
                "id": "04-07-ex2",
                "title": "Atualizar um registro",
                "statement": "Você tem uma lista `usuarios = [{'id': 1, 'nome': 'Gabrielly', 'idade': 18}]`. Atualize a `idade` do usuário com id 1 para `19`. Depois, imprima `usuarios[0]['idade']`.",
                "starter_code": "usuarios = [{'id': 1, 'nome': 'Gabrielly', 'idade': 18}]\n\n# Atualize a idade\n\n\nprint(usuarios[0]['idade'])",
                "tests": [
                    {"validation": "output_equals", "expected": "19"},
                ],
                "hint": "usuarios[0]['idade'] = 19",
            },
        },
    ],
    "summary": [
        "CRUD: Create, Read, Update, Delete.",
        "Toda aplicação real é CRUD + regras de negócio.",
        "Em Python puro: lista + dicionários + for + if.",
        "Em MongoDB: insert_one, find, update_one, delete_one.",
    ],
}


