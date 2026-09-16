"""Lições do Módulo 05 — extraídas automaticamente de lessons_content.py."""

LESSON_05_01 = {
    "id": "05-01", "module_id": "05",
    "title": "Introdução ao FastAPI",
    "objectives": [
        "Entender o que é FastAPI e por que ele domina o mercado Python",
        "Saber quando usar FastAPI, Flask ou Django",
        "Instalar FastAPI e Uvicorn corretamente",
        "Criar e rodar o primeiro servidor",
        "Conhecer a documentação interativa automática",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "t1",
            "title": "O Framework Moderno",
            "content": [
                {"type": "text", "value": "Antes de escrever qualquer rota, você precisa entender **o que é o FastAPI** e por que ele virou o framework favorito de quem faz backend Python moderno. Não é hype — é consequência direta de três problemas que ele resolveu de uma vez."},
                {"type": "text", "value": "Imagine que você precisa criar uma API que vai receber dados de um app React, validar tudo, autenticar usuários e devolver respostas rápidas. Com Flask, você escreveria **tudo na mão**: validação, documentação, tipos, tratamento de erro. Com FastAPI, **quase tudo isso é automático**."},
                {"type": "text", "value": "**FastAPI é um framework Python moderno para construir APIs.** Ele usa **type hints** (aquela sintaxe `nome: str` que você viu no TypeScript) para gerar **validação automática**, **documentação interativa** e **serialização de dados** — de graça."},
                {"type": "text", "value": "Ele foi criado por Sebastián Ramírez em 2018 e hoje é usado por Microsoft, Netflix, Uber e milhares de startups. Em performance, ele compete de igual pra igual com Node.js e Go — algo raro em Python."},
                {
                    "type": "code",
                    "caption": "O que você ganha 'de graça' com FastAPI",
                    "value": "✅ Validação automática de dados (via Pydantic)\n✅ Documentação interativa em /docs (Swagger UI)\n✅ Documentação alternativa em /redoc (ReDoc)\n✅ Type hints como contrato (menos bugs)\n✅ Suporte nativo a async/await\n✅ Performance comparável a Node.js/Go"
                },
                {"type": "text", "value": "**Por que isso importa na prática?** Quando você define uma rota com `def criar(usuario: Usuario)`, o FastAPI já sabe:\n\n1. Que `usuario` precisa ter os campos definidos na classe `Usuario`\n2. Que se faltar um campo, deve retornar `422`\n3. Que isso deve aparecer no `/docs` como um exemplo clicável\n4. Que a resposta precisa ser serializada em JSON\n\n**Você escreve uma linha. O FastAPI faz quatro coisas.**"},
                {
                    "type": "code",
                    "caption": "Exemplo mínimo — repare na mágica",
                    "value": "from fastapi import FastAPI\nfrom pydantic import BaseModel\n\napp = FastAPI()\n\nclass Usuario(BaseModel):\n    nome: str\n    email: str\n\n@app.post(\"/usuarios\")\ndef criar(usuario: Usuario):\n    return {\"criado\": usuario.nome}\n\n# Se o cliente enviar { \"nome\": \"Gabrielly\" } sem email,\n# o FastAPI já responde 422 automaticamente. Você não escreveu nada."
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Instalando e Rodando o Primeiro Servidor",
            "content": [
                {"type": "text", "value": "Agora que você entendeu **o que é** e **por que usar**, vamos colocar a mão na massa. O FastAPI precisa de duas coisas para funcionar:"},
                {"type": "text", "value": "**1. O framework em si** (`fastapi`) — é o que você importa no código.\n**2. Um servidor ASGI** (`uvicorn`) — é quem vai rodar sua aplicação de verdade."},
                {"type": "text", "value": "Pense assim: o **FastAPI** é o **motor do carro**, e o **Uvicorn** é o **chassi que faz ele andar na estrada**. Sem um dos dois, não funciona."},
                {
                    "type": "code",
                    "caption": "Instalando com pip",
                    "value": "pip install fastapi uvicorn[standard]\n\n# O [standard] instala dependências extras:\n# - httptools (parsing HTTP mais rápido)\n# - uvloop (event loop mais rápido)\n# - watchfiles (hot reload confiável)"
                },
                {"type": "text", "value": "**Crie um arquivo `main.py`** na sua pasta do projeto e escreva o código abaixo. Esse é o **servidor mínimo funcional** do FastAPI:"},
                {
                    "type": "code",
                    "caption": "main.py — o servidor mais simples possível",
                    "value": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get(\"/\")\ndef home():\n    return {\"mensagem\": \"Olá, mundo!\"}\n\n# Rode com: uvicorn main:app --reload\n# main   → nome do arquivo (main.py)\n# app    → nome da variável FastAPI() no código\n# --reload → reinicia sozinho quando você salva"
                },
                {"type": "text", "value": "**Entendendo o comando `uvicorn main:app --reload`:**\n\n- `main` = nome do arquivo **sem** `.py`\n- `app` = nome da variável `FastAPI()` dentro do arquivo\n- `--reload` = em desenvolvimento, reinicia automaticamente quando você altera o código\n\nSe seu arquivo se chamasse `server.py` e a variável `api`, o comando seria `uvicorn server:api --reload`."},
                {"type": "text", "value": "**Atenção:** o `--reload` é **exclusivo para desenvolvimento**. Em produção (no servidor real), você roda **sem** ele, porque reiniciar sozinho em produção derruba usuários conectados."},
                {
                    "type": "code",
                    "caption": "Saída do Uvicorn ao iniciar",
                    "value": "INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)\nINFO:     Started reloader process\nINFO:     Application startup complete.\n\n# Acesse no navegador:\n# http://localhost:8000        → sua API\n# http://localhost:8000/docs   → Swagger UI (documentação)"
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Documentação Interativa Automática",
            "content": [
                {"type": "text", "value": "Esse é o recurso que **mais impressiona** quem vem de outros frameworks. Sem escrever **uma linha sequer** de documentação, o FastAPI gera **duas interfaces completas** para você testar a API."},
                {"type": "text", "value": "Acesse **`http://localhost:8000/docs`** e você vai ver o **Swagger UI** — uma tela com **todos os seus endpoints**, seus parâmetros, seus schemas, e um botão **\"Try it out\"** que executa a requisição de verdade."},
                {
                    "type": "code",
                    "caption": "O que você vê em /docs",
                    "value": "┌─────────────────────────────────────────┐\n│  FastAPI          [Authorize]            │\n├─────────────────────────────────────────┤\n│  ▼ default                               │\n│  ┌────────────────────────────────────┐ │\n│  │ GET  /              Home            │ │\n│  │ [Try it out]                       │ │\n│  └────────────────────────────────────┘ │\n└─────────────────────────────────────────┘"
                },
                {"type": "text", "value": "**Por que isso muda tudo?** Lembra que o Postman era obrigatório para testar APIs? Com FastAPI, você **testa direto no navegador**. Clica em \"Try it out\", preenche os campos, clica em \"Execute\" e vê a resposta real do servidor — com status code, headers e body."},
                {"type": "text", "value": "Existe também o **ReDoc** em **`/redoc`** — uma documentação mais limpa, focada em leitura. Mesma informação, formato diferente. Ideal para compartilhar com o time de frontend."},
                {"type": "text", "value": "**O que gera tudo isso?** Os **type hints** e o **Pydantic**. Cada vez que você anota `nome: str` ou `idade: int`, o FastAPI registra isso no schema OpenAPI (o padrão de mercado para descrever APIs REST)."},
                {
                    "type": "code",
                    "caption": "OpenAPI JSON — o arquivo gerado",
                    "value": "# Acesse http://localhost:8000/openapi.json\n# É um JSON gigante descrevendo sua API inteira.\n\n# Ferramentas que consomem esse JSON:\n# - Swagger UI (/docs)\n# - ReDoc (/redoc)\n# - Postman (importa automaticamente)\n# - Geração de SDKs em outras linguagens"
                },
                {
                    "type": "code",
                    "caption": "Personalizando a documentação",
                    "value": "app = FastAPI(\n    title=\"API do Meu SaaS\",\n    description=\"Backend do curso Devstack — autenticação, cursos e pagamentos.\",\n    version=\"1.0.0\",\n    contact={\"name\": \"Felipe\", \"email\": \"felipe@devstack.com\"},\n)\n\n# Agora /docs mostra esse cabeçalho bonito em cima."
                },
            ],
            "exercise": None,
        },
        {
            "id": "t4",
            "title": "FastAPI vs Flask vs Django",
            "content": [
                {"type": "text", "value": "Uma pergunta que **todo iniciante** faz: *\"Se existe Flask e Django, por que aprender FastAPI?\"* A resposta curta: **cada um resolve um problema diferente**. Vamos ver quando usar cada um."},
                {
                    "type": "code",
                    "caption": "Comparação direta",
                    "value": "FastAPI  → APIs modernas, async, validação automática, docs\nFlask    → micro-framework, mais livre, menos estrutura\nDjango   → full-stack, admin pronto, mais pesado"
                },
                {"type": "text", "value": "**Flask** foi lançado em 2010 e virou o padrão do Python por muito tempo. É um **micro-framework**: te dá o básico (rotas, templates) e você monta o resto. Ótimo para projetos pequenos ou quando você quer controle total. **Mas:** validação, serialização, documentação e async — tudo na mão."},
                {"type": "text", "value": "**Django** é o **canhão**: vem com ORM, admin automático, sistema de autenticação, templates, migrations e mais. É usado por Instagram, Pinterest e Mozilla. **Mas:** é pesado, opinativo e o admin pronto vira overhead quando você só quer uma API JSON."},
                {"type": "text", "value": "**FastAPI** nasceu justamente para preencher o **meio do caminho**: leve como Flask, mas com validação, docs e async nativos. É a escolha padrão para **APIs modernas que vão servir um frontend React/Vue/mobile**."},
                {
                    "type": "code",
                    "caption": "Qual escolher?",
                    "value": "Precisa servir API JSON para um frontend?       → FastAPI\nVai construir sistema administrativo com         → Django\n  CRUD pronto e admin gerado?\nPrecisa de algo minúsculo e simples?             → Flask\nQuer async (chat, tempo real, concorrência)?     → FastAPI\nEstá começando em backend moderno em 2025?       → FastAPI"
                },
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "FastAPI é o framework Python moderno para APIs: rápido, com validação automática e docs interativas.",
        "Uvicorn é o servidor ASGI que roda a aplicação. Sem ele, o FastAPI não sobe.",
        "/docs (Swagger UI) e /redoc (ReDoc) são gerados automaticamente a partir dos type hints.",
        "FastAPI = leve como Flask + recursos modernos (async, validação, docs).",
        "Escolha: FastAPI para APIs modernas, Django para sistemas full-stack, Flask para casos mínimos.",
    ],
}


LESSON_05_02 = {
    "id": "05-02", "module_id": "05",
    "title": "Rotas GET e POST",
    "objectives": [
        "Entender quando usar GET e quando usar POST",
        "Criar rotas com path parameters e query parameters",
        "Receber dados no body com Pydantic",
        "Entender o erro 422 e como o FastAPI valida automaticamente",
        "Testar rotas direto no Swagger",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "t1",
            "title": "GET e POST — Duas Filosofias",
            "content": [
                {"type": "text", "value": "Antes de escrever `@app.get` ou `@app.post`, você precisa entender **o que cada método significa** na web. Não é escolha estética — é um **contrato** com o cliente."},
                {"type": "text", "value": "**GET** significa **\"me dê algo\"**. Ele busca dados e **nunca modifica nada** no servidor. É o método usado quando você abre o Instagram e quer ver o feed — só está lendo."},
                {"type": "text", "value": "**POST** significa **\"crie algo novo\"**. Ele **muda o estado** do servidor. É o método usado quando você posta uma foto, envia um comentário ou faz login."},
                {
                    "type": "code",
                    "caption": "A diferença fundamental",
                    "value": "GET  → buscar dados          (não muda nada)\nPOST → criar recurso novo    (envia dados no body)"
                },
                {"type": "text", "value": "**Por que essa distinção importa?** Porque o navegador, os proxies e os caches **tratam GET e POST de formas diferentes**:\n\n- GET pode ser **cacheado** (o navegador salva a resposta)\n- GET pode ser **repetido** sem problema (é *idempotente*)\n- POST **nunca** é cacheado nem repetido automaticamente\n\nSe você criar uma rota `GET /deletar-usuario/1`, um bot do Google pode passar por ali e **apagar seu usuário sem querer**. Por isso existem regras."},
                {"type": "text", "value": "**Regra de ouro:** se a rota **muda algo** no servidor, ela **não pode** ser GET. Use POST, PUT ou DELETE."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Path Parameters — Dados na URL",
            "content": [
                {"type": "text", "value": "**Path parameters** são valores que fazem parte da **própria URL** e identificam um recurso específico. Eles vêm entre `{}` no decorator."},
                {
                    "type": "code",
                    "caption": "Rota GET com path parameter",
                    "value": "@app.get(\"/usuarios/{user_id}\")\ndef buscar_usuario(user_id: int):\n    return {\"id\": user_id, \"nome\": \"Gabrielly\"}\n\n# GET /usuarios/1  → {\"id\": 1, \"nome\": \"Gabrielly\"}\n# GET /usuarios/42 → {\"id\": 42, \"nome\": \"Gabrielly\"}"
                },
                {"type": "text", "value": "**Repare em detalhes importantes:**"},
                {"type": "text", "value": "**1. O nome do parâmetro na função precisa bater com o nome entre chaves.** Se a URL é `{user_id}`, a função precisa ter `user_id`."},
                {"type": "text", "value": "**2. O type hint (`int`) faz validação automática.** Se alguém chamar `/usuarios/abc`, o FastAPI retorna **422 Unprocessable Entity** — o parâmetro precisa ser número, e `abc` não é."},
                {"type": "text", "value": "**3. Não precisa converter manualmente.** Sem type hints, você teria que fazer `int(user_id)` na mão e tratar erro. FastAPI faz isso em zero linhas suas."},
                {
                    "type": "code",
                    "caption": "Sem FastAPI você escreveria isso na mão",
                    "value": "@app.get(\"/usuarios/{user_id}\")\ndef buscar_usuario(user_id):\n    try:\n        user_id = int(user_id)\n    except ValueError:\n        return {\"erro\": \"ID inválido\"}, 400\n    # ... resto da lógica\n\n# Com FastAPI, tudo isso é automático pelo type hint."
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Query Parameters — Dados Após o ?",
            "content": [
                {"type": "text", "value": "**Query parameters** são os valores que vêm **depois do `?`** na URL. Eles servem para **filtros, buscas, paginação** — coisas que não identificam um recurso único, mas ajustam a resposta."},
                {
                    "type": "code",
                    "caption": "Rota GET com query parameter",
                    "value": "@app.get(\"/buscar\")\ndef buscar(q: str = \"\", limite: int = 10):\n    return {\"termo\": q, \"limite\": limite}\n\n# GET /buscar?q=python&limite=5\n# → {\"termo\": \"python\", \"limite\": 5}"
                },
                {"type": "text", "value": "**Path vs Query — como decidir?**"},
                {
                    "type": "code",
                    "caption": "Path vs Query — a regra",
                    "value": "PATH  → identifica um recurso\n        /usuarios/42        (o usuário 42)\n        /produtos/notebook  (o produto notebook)\n\nQUERY → filtra, ordena, ajusta\n        /usuarios?ativo=true\n        /produtos?categoria=eletronicos&ordem=preco"
                },
                {"type": "text", "value": "**Dica importante:** parâmetros de função com **valor padrão** (`q: str = \"\"`) automaticamente viram **query parameters opcionais**. Se não têm padrão, são **obrigatórios** — a chamada sem eles retorna 422."},
                {
                    "type": "code",
                    "caption": "Opcional vs obrigatório",
                    "value": "@app.get(\"/produtos\")\ndef listar(categoria: str, pagina: int = 1):\n    # categoria é OBRIGATÓRIA (sem padrão)\n    # pagina é OPCIONAL (tem padrão = 1)\n    return {\"categoria\": categoria, \"pagina\": pagina}\n\n# GET /produtos?categoria=livros        → ✅ funciona\n# GET /produtos                          → ❌ 422 (falta categoria)"
                },
            ],
            "exercise": None,
        },
        {
            "id": "t4",
            "title": "POST com Pydantic — Body Estruturado",
            "content": [
                {"type": "text", "value": "Quando você cria algo com POST, os dados vão no **corpo da requisição** (body), não na URL. E o FastAPI usa o **Pydantic** para validar esses dados automaticamente."},
                {"type": "text", "value": "**O que é Pydantic?** É uma biblioteca de validação que usa **type hints** para checar se os dados estão no formato certo. Você define uma classe com os campos e tipos, e o Pydantic faz o resto."},
                {
                    "type": "code",
                    "caption": "Rota POST com body",
                    "value": "from pydantic import BaseModel\n\nclass Usuario(BaseModel):\n    nome: str\n    email: str\n\n@app.post(\"/usuarios\")\ndef criar_usuario(usuario: Usuario):\n    return {\"mensagem\": \"Criado\", \"usuario\": usuario}\n\n# POST /usuarios\n# Body: {\"nome\": \"Gabrielly\", \"email\": \"g@x.com\"}"
                },
                {"type": "text", "value": "**O que o FastAPI faz por você nesse exemplo:**\n\n1. **Lê o JSON** do body da requisição\n2. **Valida** que `nome` e `email` existem e são strings\n3. **Cria um objeto `Usuario`** tipado\n4. **Injeta na função** como parâmetro\n5. Se algo estiver errado, retorna **422** com detalhes do erro"},
                {"type": "text", "value": "**Teste você mesmo:** envie um POST sem o campo `email`. Você recebe algo assim automaticamente:"},
                {
                    "type": "code",
                    "caption": "Erro 422 automático do FastAPI",
                    "value": "{\n    \"detail\": [\n        {\n            \"type\": \"missing\",\n            \"loc\": [\"body\", \"email\"],\n            \"msg\": \"Field required\",\n            \"input\": {\"nome\": \"Gabrielly\"}\n        }\n    ]\n}"
                },
                {"type": "text", "value": "**Você não escreveu nenhuma validação.** O Pydantic + FastAPI fizeram isso. Compare com Flask, onde você teria que checar `if \"email\" not in data: return 400` na mão — em toda rota."},
                {"type": "text", "value": "**Dica profissional:** sempre defina uma classe Pydantic para o body. **Nunca** aceite `dict` cru. O type hint é o contrato com quem consome a API — e vira documentação interativa em `/docs` automaticamente."},
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "GET busca (não muda nada); POST cria (muda o estado).",
        "Path params ficam na URL (`/usuarios/42`); query params vêm após `?` (`?ativo=true`).",
        "Pydantic valida o body automaticamente com base nos type hints.",
        "Erros de validação retornam 422 com detalhes — sem código extra seu.",
    ],
}


LESSON_05_03 = {
    "id": "05-03", "module_id": "05",
    "title": "Rotas PUT e DELETE",
    "objectives": [
        "Entender quando usar PUT e DELETE",
        "Saber a diferença entre PUT e PATCH",
        "Retornar os status codes corretos (200, 201, 204)",
        "Usar as constantes de status do FastAPI",
        "Construir um CRUD completo com os 4 verbos HTTP",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "PUT e DELETE — Completando o CRUD",
            "content": [
                {"type": "text", "value": "Se GET lê e POST cria, faltam duas operações para completar o CRUD: **atualizar** e **apagar**. É aí que entram PUT e DELETE."},
                {
                    "type": "code",
                    "caption": "Os 4 verbos HTTP",
                    "value": "GET    → buscar     (Read)\nPOST   → criar      (Create)\nPUT    → atualizar  (Update)\nDELETE → apagar     (Delete)"
                },
                {"type": "text", "value": "**PUT** atualiza um recurso **existente**. Em geral, o cliente manda **o recurso inteiro** com os dados novos — o servidor substitui o antigo."},
                {
                    "type": "code",
                    "caption": "PUT — atualizar um usuário",
                    "value": "@app.put(\"/usuarios/{user_id}\")\ndef atualizar(user_id: int, usuario: Usuario):\n    return {\"id\": user_id, \"atualizado\": usuario}\n\n# PUT /usuarios/1\n# Body: {\"nome\": \"Gabrielly\", \"email\": \"novo@x.com\"}"
                },
                {"type": "text", "value": "**PUT vs PATCH — a diferença que muita gente confunde:**"},
                {
                    "type": "code",
                    "caption": "PUT vs PATCH",
                    "value": "PUT   → substitui o recurso INTEIRO\n        Se você manda só nome, os outros campos se perdem.\n\nPATCH → atualiza SÓ os campos enviados\n        Se você manda só nome, os outros ficam como estão."
                },
                {"type": "text", "value": "**Na prática:** a maioria das APIs modernas prefere **PATCH** para editar parcialmente. Mas muitas ainda usam PUT com body contendo todos os campos — é mais fácil de implementar e validar. FastAPI suporta os dois: `@app.put(...)` e `@app.patch(...)`."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "DELETE e o Status 204",
            "content": [
                {"type": "text", "value": "**DELETE** apaga um recurso. A rota geralmente recebe o **id** do recurso a remover via path parameter."},
                {
                    "type": "code",
                    "caption": "DELETE — apagar usuário",
                    "value": "@app.delete(\"/usuarios/{user_id}\")\ndef deletar(user_id: int):\n    return {\"mensagem\": f\"Usuário {user_id} apagado\"}"
                },
                {"type": "text", "value": "**Pergunta importante:** o que devolver depois de apagar? Duas opções comuns:"},
                {"type": "text", "value": "**Opção 1: 200 com mensagem.** Você confirma que apagou e retorna um JSON qualquer."},
                {"type": "text", "value": "**Opção 2: 204 No Content.** Você não retorna **nada**. É o mais correto quando a operação deu certo e não há conteúdo para devolver."},
                {
                    "type": "code",
                    "caption": "DELETE com status 204",
                    "value": "@app.delete(\"/usuarios/{user_id}\", status_code=204)\ndef deletar(user_id: int):\n    return None\n\n# O cliente recebe 204 (No Content) e nenhum body."
                },
                {"type": "text", "value": "**Por que 204 é considerado mais correto?** Porque comunica exatamente o que aconteceu: \"operação bem-sucedida, e não há nada para você ler\". É sinal de API bem desenhada."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Status Codes Corretos",
            "content": [
                {"type": "text", "value": "Cada operação tem um status code **esperado** pela comunidade. Usar o certo é sinal de profissionalismo — e os clientes (frontend, mobile) dependem disso para tratar respostas corretamente."},
                {
                    "type": "code",
                    "caption": "Status codes padrão por operação",
                    "value": "GET    → 200 OK              (busca bem-sucedida)\nPOST   → 201 Created         (recurso criado)\nPUT    → 200 OK              (atualizado)\nDELETE → 204 No Content      (apagado)\n\nErros comuns:\n400 → dados inválidos\n401 → não autenticado\n403 → sem permissão\n404 → não encontrado\n422 → falha de validação (FastAPI usa isso)"
                },
                {"type": "text", "value": "**Repare:** o padrão do FastAPI é **200** em todas as rotas. Se você quer **201** ao criar ou **204** ao apagar, precisa dizer explicitamente no decorator."},
                {
                    "type": "code",
                    "caption": "Personalizando status code",
                    "value": "from fastapi import status\n\n@app.post(\"/usuarios\", status_code=status.HTTP_201_CREATED)\ndef criar(usuario: Usuario):\n    return usuario\n\n# 201 = Created"
                },
                {"type": "text", "value": "**Por que usar `status.HTTP_201_CREATED` em vez de só `201`?** Legibilidade. O nome diz **o que** o código significa, não só o número. Se você revisa o código 6 meses depois, `HTTP_201_CREATED` é infinitamente mais claro."},
                {
                    "type": "code",
                    "caption": "Os status mais usados do FastAPI",
                    "value": "status.HTTP_200_OK            → 200\nstatus.HTTP_201_CREATED       → 201\nstatus.HTTP_204_NO_CONTENT    → 204\nstatus.HTTP_400_BAD_REQUEST   → 400\nstatus.HTTP_401_UNAUTHORIZED  → 401\nstatus.HTTP_403_FORBIDDEN     → 403\nstatus.HTTP_404_NOT_FOUND     → 404"
                },
                {"type": "text", "value": "**Dica profissional:** retornar os status codes corretos desde o começo custa nada e mostra domínio. É o tipo de detalhe que distingue um dev júnior de um pleno em revisão de código."},
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "PUT atualiza; PATCH atualiza parcialmente; DELETE remove.",
        "DELETE bem feito retorna 204 (sem body).",
        "POST bem feito retorna 201 (Created).",
        "Use as constantes `status.HTTP_*` — código autoexplicativo.",
    ],
}


LESSON_05_04 = {
    "id": "05-04", "module_id": "05",
    "title": "Validação com Pydantic",
    "objectives": [
        "Entender o que é Pydantic e por que ele é essencial",
        "Validar tipos, tamanhos e formatos com Field",
        "Criar validações customizadas com @field_validator",
        "Entender a estrutura dos erros de validação",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "t1",
            "title": "Pydantic — O Guarda-Costas da Sua API",
            "content": [
                {"type": "text", "value": "Imagine que você tem uma API pública. Um usuário mal-intencionado envia `idade: \"abc\"` no cadastro. Sem validação, você salva uma string no banco e quebra todo o sistema depois. **Pydantic impede isso antes de chegar na sua lógica.**"},
                {"type": "text", "value": "**Pydantic é a biblioteca de validação que o FastAPI usa por baixo.** Você define a **forma esperada** dos dados (um *schema*), e ele garante que **tudo que chega** bate com essa forma."},
                {"type": "text", "value": "Se a validação falhar, o FastAPI retorna **422** com detalhes do erro — você **não precisa escrever** `if campo is None: return 400` em nenhuma rota."},
                {
                    "type": "code",
                    "caption": "Schema básico com Pydantic",
                    "value": "from pydantic import BaseModel\n\nclass Usuario(BaseModel):\n    nome: str\n    email: str\n    idade: int\n\n# Se o body não tiver 'nome', 'email' ou 'idade',\n# OU se 'idade' não for número, o FastAPI retorna 422."
                },
                {"type": "text", "value": "**Por que isso é uma revolução?** Em frameworks mais antigos (Flask, Express), você escrevia validação manual **em toda rota**. Com Pydantic, o schema fica **separado** da lógica, é **reutilizável** e aparece **automaticamente na documentação**."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Field() — Regras Avançadas",
            "content": [
                {"type": "text", "value": "O type hint (`idade: int`) já valida o **tipo**. Mas às vezes você precisa ir além: `idade` não pode ser 200, `nome` precisa ter pelo menos 2 caracteres, `email` precisa ter formato de email. Para isso existe **`Field()`**."},
                {
                    "type": "code",
                    "caption": "Validação com Field",
                    "value": "from pydantic import BaseModel, Field, EmailStr\n\nclass Usuario(BaseModel):\n    nome: str = Field(..., min_length=2, max_length=80)\n    email: EmailStr\n    idade: int = Field(..., ge=0, le=120)  # 0 <= idade <= 120\n    ativo: bool = True"
                },
                {"type": "text", "value": "**Vamos destrinchar cada regra:**"},
                {
                    "type": "code",
                    "caption": "As regras do Field",
                    "value": "min_length → tamanho mínimo (str)\nmax_length → tamanho máximo (str)\nge         → greater or equal (>=)\nle         → less or equal (<=)\ngt         → greater than (>)\nlt         → less than (<)\nregex      → expressão regular (padrão)\n...        → obrigatório (sem valor padrão)"
                },
                {"type": "text", "value": "**O `...` (Ellipsis):** quando usado em `Field(...)`, significa que o campo é **obrigatório**. É o equivalente Pydantic de dizer \"esse campo não tem default\"."},
                {"type": "text", "value": "**`EmailStr`:** valida formato de email (precisa de `pip install pydantic[email]`). Se alguém mandar `\"nao-e-email\"`, retorna 422."},
                {"type": "text", "value": "**Valores padrão:** `ativo: bool = True` significa que se o cliente não mandar `ativo`, ele assume `True`. Isso é ótimo para flags opcionais."},
                {
                    "type": "code",
                    "caption": "O que acontece quando a validação falha",
                    "value": "# Requisição:\nPOST /usuarios\n{\"nome\": \"A\", \"email\": \"nao-email\", \"idade\": 200}\n\n# Resposta (422):\n{\n  \"detail\": [\n    {\"loc\": [\"body\", \"nome\"], \"msg\": \"String should have at least 2 characters\"},\n    {\"loc\": [\"body\", \"email\"], \"msg\": \"value is not a valid email address\"},\n    {\"loc\": [\"body\", \"idade\"], \"msg\": \"Input should be less than or equal to 120\"}\n  ]\n}"
                },
                {"type": "text", "value": "**Repare:** o FastAPI lista **todos os erros** de uma vez, não só o primeiro. Isso economiza idas e voltas do frontend e melhora a UX."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Validação Customizada",
            "content": [
                {"type": "text", "value": "Às vezes, as regras do `Field()` não bastam. Exemplo: você quer validar que **a senha tem pelo menos um número**. Nenhuma regra pronta resolve isso. É aí que entra **`@field_validator`**."},
                {
                    "type": "code",
                    "caption": "Validação customizada com field_validator",
                    "value": "from pydantic import BaseModel, field_validator\n\nclass Senha(BaseModel):\n    valor: str\n\n    @field_validator(\"valor\")\n    def senha_forte(cls, v):\n        if len(v) < 8:\n            raise ValueError(\"Senha deve ter no mínimo 8 caracteres\")\n        if not any(c.isdigit() for c in v):\n            raise ValueError(\"Senha precisa ter pelo menos um número\")\n        return v"
                },
                {"type": "text", "value": "**Entendendo a estrutura:**"},
                {
                    "type": "code",
                    "caption": "Anatomia do field_validator",
                    "value": "@field_validator(\"valor\")   → diz QUAL campo está sendo validado\n\ndef senha_forte(cls, v):     → 'cls' é a classe, 'v' é o valor recebido\n\n    if len(v) < 8:           → regra que você inventa\n        raise ValueError(...)  → lança erro → FastAPI devolve 422\n\n    return v                 → SEMPRE retorne o valor no final"
                },
                {"type": "text", "value": "**Erro comum:** esquecer o `return v`. Se você não retornar, o campo vira `None` silenciosamente."},
                {"type": "text", "value": "**Validações que valem a pena:** força de senha, formato de CPF, consistência entre campos (`data_fim > data_inicio`), normalização de string (`nome.strip().title()`)."},
                {
                    "type": "code",
                    "caption": "Validando consistência entre campos",
                    "value": "from pydantic import BaseModel, model_validator\nfrom datetime import date\n\nclass Reserva(BaseModel):\n    data_inicio: date\n    data_fim: date\n\n    @model_validator(mode=\"after\")\n    def validar_datas(self):\n        if self.data_fim < self.data_inicio:\n            raise ValueError(\"data_fim precisa ser depois de data_inicio\")\n        return self"
                },
                {"type": "text", "value": "**`field_validator`** valida **um campo**. **`model_validator`** valida **o modelo inteiro** — útil quando dois campos dependem um do outro."},
            ],
            "exercise": {
                "id": "05-04-ex1", "title": "Criar um schema", 
                "statement": "Crie uma classe `Produto` (herdando de BaseModel) com dois campos: `nome` (str) e `preco` (float). Depois, crie uma instância com `nome='Mouse'` e `preco=80.0`, e imprima o valor de `.nome`.",
                "starter_code": "from pydantic import BaseModel\n\nclass Produto(BaseModel):\n    # defina os campos\n    \n\np = Produto(nome='Mouse', preco=80.0)\nprint(p.nome)",
                "tests": [{"validation": "output_equals", "expected": "Mouse"}],
                "hint": "nome: str, preco: float",
            },
        },
    ],
    "summary": [
        "Pydantic valida os dados antes de chegar na sua função.",
        "Field() aplica regras avançadas: tamanho, intervalo, formato.",
        "@field_validator cria validações customizadas para 1 campo.",
        "@model_validator valida o modelo inteiro (ex: duas datas).",
        "Sempre retorne o valor no final do validator.",
    ],
}


LESSON_05_05 = {
    "id": "05-05", "module_id": "05",
    "title": "Middleware e CORS",
    "objectives": [
        "Entender o que é middleware e quando usar",
        "Configurar CORS corretamente para o frontend",
        "Diferenciar CORS de CSRF",
        "Criar middlewares customizados (logs, tempo de resposta)",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "O que é Middleware",
            "content": [
                {"type": "text", "value": "**Middleware** é um código que roda **antes e depois** de cada requisição, independente da rota. Pense como uma **esteira de aeroporto**: toda bagagem passa por ela."},
                {
                    "type": "code",
                    "caption": "Fluxo de um middleware",
                    "value": "Cliente → [Middleware] → Rota → [Middleware] → Cliente\n              ↑                            ↑\n              Antes do handler            Depois do handler"
                },
                {"type": "text", "value": "**Por que isso é útil?** Porque existem coisas que **toda** requisição precisa: verificar autenticação, adicionar cabeçalhos, logar o tempo de resposta, aplicar CORS, comprimir a resposta. Sem middleware, você repetiria esse código **em cada rota**."},
                {"type": "text", "value": "**Exemplos de middleware no mundo real:**"},
                {
                    "type": "code",
                    "caption": "Casos de uso de middleware",
                    "value": "CORS            → libera acesso do frontend\nAutenticação    → valida token antes da rota\nLogs            → registra toda requisição\nRate limiting   → limita N requisições por minuto\nCompressão      → gzip nas respostas\nMedir tempo     → quanto tempo cada rota demorou"
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "CORS — Cross-Origin Resource Sharing",
            "content": [
                {"type": "text", "value": "Este é **o middleware que você vai configurar em todo projeto**. Se você já viu um erro tipo **`CORS policy: No 'Access-Control-Allow-Origin' header`** no console do navegador, esse é o problema."},
                {"type": "text", "value": "**Por que CORS existe?** Por segurança. Imagine que você está logado no seu banco em `banco.com`. Você abre outra aba em `site-malicioso.com`. Esse site **não deveria** poder fazer requisições autenticadas para `banco.com` usando seus cookies. CORS impede isso."},
                {"type": "text", "value": "O navegador aplica a regra: **se a origem da requisição é diferente da origem do servidor**, ela precisa ser **explicitamente autorizada** pelo servidor via headers CORS."},
                {
                    "type": "code",
                    "caption": "O problema clássico",
                    "value": "Frontend React rodando em:  http://localhost:5173\nBackend FastAPI rodando em:  http://localhost:8000\n\n→ São ORIGENS DIFERENTES (porta diferente)\n→ Navegador bloqueia a requisição SEM CORS"
                },
                {"type": "text", "value": "**Solução: configurar CORSMiddleware no FastAPI.**"},
                {
                    "type": "code",
                    "caption": "Configurando CORS",
                    "value": "from fastapi.middleware.cors import CORSMiddleware\n\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=[\"http://localhost:5173\"],\n    allow_credentials=True,\n    allow_methods=[\"*\"],\n    allow_headers=[\"*\"],\n)"
                },
                {"type": "text", "value": "**Entendendo cada opção:**"},
                {
                    "type": "code",
                    "caption": "Cada parâmetro do CORS",
                    "value": "allow_origins     → quais domínios podem chamar a API\nallow_credentials → permite envio de cookies/Authorization\nallow_methods     → quais verbos HTTP (GET, POST, ...)\nallow_headers     → quais headers são aceitos\n\n[\"*\"]  → libera tudo (útil em dev, PERIGOSO em prod)"
                },
                {"type": "text", "value": "**⚠️ Erro crítico em produção:** usar `allow_origins=[\"*\"]` com `allow_credentials=True`. **É proibido pela spec CORS** — o navegador rejeita. Em produção, liste **origens específicas**."},
                {
                    "type": "code",
                    "caption": "Configuração correta para produção",
                    "value": "import os\n\norigens = [\n    \"http://localhost:5173\",\n    \"https://meu-app.vercel.app\",\n    \"https://meusite.com.br\",\n]\n\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=origens,\n    allow_credentials=True,\n    allow_methods=[\"*\"],\n    allow_headers=[\"*\"],\n)"
                },
                {"type": "text", "value": "**⚠️ Ordem importa!** `app.add_middleware()` precisa vir **antes** de `include_router` e das rotas serem definidas. Se você colocar depois, não funciona."},
                {"type": "text", "value": "**CORS vs CSRF — não confunda:**\n\n- **CORS** é política **do navegador** que controla **quem pode chamar sua API**. Você configura no **backend**.\n- **CSRF** é um **ataque** onde um site malicioso faz requisição autenticada em nome do usuário. Você previne com **tokens CSRF** e cookies `SameSite`."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Middleware Customizado — Logs e Tempo",
            "content": [
                {"type": "text", "value": "Além do CORS, você pode criar **middlewares próprios** com `@app.middleware(\"http\")`. Um caso muito útil: **medir o tempo de cada requisição** e logar."},
                {
                    "type": "code",
                    "caption": "Middleware de log customizado",
                    "value": "import time\nfrom fastapi import Request\n\n@app.middleware(\"http\")\nasync def log_tempo(request: Request, call_next):\n    inicio = time.time()\n    response = await call_next(request)\n    duracao = time.time() - inicio\n    print(f\"{request.method} {request.url.path} → {duracao:.3f}s\")\n    return response"
                },
                {"type": "text", "value": "**Passo a passo do que acontece:**"},
                {
                    "type": "code",
                    "caption": "Fluxo do middleware customizado",
                    "value": "1. Requisição chega\n2. Você captura o tempo de início\n3. 'await call_next(request)' → chama a rota\n4. Rota processa e devolve response\n5. Você calcula o tempo total\n6. Imprime o log\n7. Devolve a response para o cliente"
                },
                {"type": "text", "value": "**Por que `async`?** Porque o FastAPI permite requisições concorrentes. Enquanto uma aguarda resposta do banco, a outra roda. Se você bloquear o middleware (síncrono), você mata a concorrência."},
                {"type": "text", "value": "**Outros middlewares úteis:**"},
                {
                    "type": "code",
                    "caption": "Exemplo — adicionar header customizado",
                    "value": "@app.middleware(\"http\")\nasync def add_header(request: Request, call_next):\n    response = await call_next(request)\n    response.headers[\"X-App-Version\"] = \"1.0.0\"\n    return response\n\n# Agora toda resposta tem esse header, sem escrever em cada rota."
                },
                {"type": "text", "value": "**Dica profissional:** middlewares são poderosos mas **invisíveis**. Se você tem 5 middlewares empilhados e algo quebra, debugar fica difícil. Use com moderação e deixe cada um com uma responsabilidade clara."},
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "Middleware roda antes e depois de cada requisição.",
        "CORS libera requisições entre origens diferentes — sempre configure em dev.",
        "Em produção, liste origens específicas — nunca `[\"*\"]` com credenciais.",
        "Middlewares customizados servem para logs, tempo, headers extras.",
    ],
}


LESSON_05_06 = {
    "id": "05-06", "module_id": "05",
    "title": "Autenticação com JWT",
    "objectives": [
        "Entender o que é JWT e por que ele é o padrão",
        "Fazer hash de senhas com bcrypt",
        "Gerar e validar tokens",
        "Proteger rotas com Depends()",
    ],
    "reading_time_minutes": 22,
    "topics": [
        {
            "id": "t1",
            "title": "O que é JWT e por que usar",
            "content": [
                {"type": "text", "value": "Toda API séria precisa saber **quem está fazendo a requisição**. Se você tem uma rota `/perfil`, precisa responder: \"o perfil de **quem**?\". É aí que entra autenticação."},
                {"type": "text", "value": "**JWT** (JSON Web Token) é o padrão moderno. O fluxo é simples:\n\n1. Cliente faz login (email + senha)\n2. Servidor valida e devolve um **token assinado**\n3. Cliente guarda o token\n4. Em **toda** requisição, o cliente envia o token no header `Authorization`\n5. Servidor valida o token e sabe quem é o usuário"},
                {
                    "type": "code",
                    "caption": "Fluxo de autenticação JWT",
                    "value": "1. POST /login {email, senha}  →  200 {token}\n2. Cliente salva o token\n3. GET /perfil\n   Headers: Authorization: Bearer eyJhbGc...\n4. Servidor valida o token → responde com dados"
                },
                {"type": "text", "value": "**Por que não usar sessões com cookies?** Porque JWT é **stateless**: o token carrega a informação necessária (quem é o usuário, quando expira), sem o servidor precisar guardar estado. Isso escala muito melhor — funciona com múltiplos servidores sem compartilhar sessão."},
                {
                    "type": "code",
                    "caption": "Anatomia de um JWT",
                    "value": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJnQHguY29tIiwiZXhwIjoxNzM1fQ.abc123\n\n|     header      |       payload         | signature |\n\nHeader:    { \"alg\": \"HS256\", \"typ\": \"JWT\" }\nPayload:   { \"sub\": \"g@x.com\", \"exp\": 1735689600 }\nSignature: hash do header+payload com sua SECRET_KEY"
                },
                {"type": "text", "value": "**A signature é o segredo.** Se alguém tentar alterar o payload (ex: mudar `sub` para outro email), a signature deixa de bater. É assim que o servidor sabe que o token é autêntico — **não foi adulterado**."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Hash de Senhas com bcrypt",
            "content": [
                {"type": "text", "value": "**Primeira regra inegociável:** NUNCA guarde senhas em texto puro no banco. Se o banco vazar (e vaza com frequência), todas as senhas dos usuários ficam expostas. É por isso que usamos **hash**."},
                {"type": "text", "value": "**O que é hash?** É uma função que transforma uma string em outra, **de forma irreversível**. Você não consegue voltar de `$2b$12$...` para `minhasenha123` — só consegue verificar se uma senha **bate** com o hash."},
                {"type": "text", "value": "**Por que bcrypt e não MD5/SHA1?** Porque bcrypt é **lento de propósito**. Ele faz milhares de iterações internas, o que atrasa ataques de força bruta. Um atacante que testa 1 bilhão de senhas por segundo em MD5, testa 100 por segundo em bcrypt."},
                {
                    "type": "code",
                    "caption": "Hash e verificação com bcrypt",
                    "value": "import bcrypt\n\ndef hash_senha(senha: str) -> str:\n    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()\n\ndef verificar_senha(senha: str, hash: str) -> bool:\n    return bcrypt.checkpw(senha.encode(), hash.encode())"
                },
                {"type": "text", "value": "**Entendendo o que acontece:**"},
                {
                    "type": "code",
                    "caption": "Passo a passo do bcrypt",
                    "value": "1. senha.encode()          → texto vira bytes\n2. bcrypt.gensalt()        → gera um 'salt' aleatório\n3. hashpw(...)             → aplica o algoritmo\n4. .decode()               → bytes viram string para salvar no banco\n\nNo login:\n1. Pega a senha digitada\n2. Compara com o hash do banco via checkpw()\n3. Retorna True ou False"
                },
                {"type": "text", "value": "**O que é 'salt'?** É um valor aleatório adicionado à senha antes do hash. Sem salt, duas pessoas com a mesma senha teriam o mesmo hash. Com salt, cada hash é **único** mesmo para senhas iguais — impedindo ataques de tabela pré-computada (*rainbow tables*)."},
                {"type": "text", "value": "**Você nunca 'descriptografa' o hash.** Você aplica a mesma função na senha digitada e compara os resultados. É por isso que bcrypt é seguro: não tem volta."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Gerando Tokens com python-jose",
            "content": [
                {"type": "text", "value": "Para **gerar e validar JWT** em Python, usamos a biblioteca **`python-jose`**. Ela faz encode e decode de tokens assinados com HMAC-SHA256 (HS256)."},
                {
                    "type": "code",
                    "caption": "Instalação",
                    "value": "pip install \"python-jose[cryptography]\""
                },
                {
                    "type": "code",
                    "caption": "Gerando um token",
                    "value": "from jose import jwt\nfrom datetime import datetime, timedelta\n\nSECRET = \"sua-chave-secreta-super-longa-e-aleatoria\"\nALGORITHM = \"HS256\"\n\ndef criar_token(email: str) -> str:\n    payload = {\n        \"sub\": email,\n        \"exp\": datetime.utcnow() + timedelta(hours=24),\n    }\n    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)"
                },
                {"type": "text", "value": "**O que cada campo do payload significa:**"},
                {
                    "type": "code",
                    "caption": "Campos padrão do JWT",
                    "value": "sub → 'subject' — quem é o usuário (email, id, username)\nexp → 'expiration' — timestamp Unix de expiração\niat → 'issued at' — quando foi emitido (opcional)\n\nNomes são padronizados pela RFC 7519 — use-os."
                },
                {"type": "text", "value": "**⚠️ `SECRET` é crítica.** Se alguém descobrir sua SECRET, pode forjar tokens válidos como se fosse qualquer usuário. Use uma string **longa, aleatória** e guarde **em variável de ambiente** (nunca no código)."},
                {
                    "type": "code",
                    "caption": "Gerando uma SECRET segura",
                    "value": "# No terminal:\npython -c \"import secrets; print(secrets.token_urlsafe(64))\"\n\n# Cole o resultado no .env:\n# JWT_SECRET=abc123xyz..."
                },
                {"type": "text", "value": "**Sobre a expiração (`exp`):** 24 horas é um valor comum, mas depende do app. Bancos usam expiração curta (15 min) + refresh token. Redes sociais usam tokens longos (30 dias). Para um MVP de SaaS, 24 horas é o padrão."},
            ],
            "exercise": None,
        },
        {
            "id": "t4",
            "title": "Protegendo Rotas com Depends()",
            "content": [
                {"type": "text", "value": "Agora a parte mais poderosa: **como exigir o token em rotas protegidas**. O FastAPI tem um sistema de **injeção de dependências** que faz isso de forma elegante com **`Depends()`**."},
                {"type": "text", "value": "A ideia é: você define uma função que **lê o token do header**, valida, e devolve o usuário. Depois, qualquer rota que precise de autenticação inclui essa dependência."},
                {
                    "type": "code",
                    "caption": "Dependência de autenticação",
                    "value": "from fastapi import Depends, HTTPException\nfrom fastapi.security import HTTPBearer, HTTPAuthorizationCredentials\nfrom jose import jwt\n\nsecurity = HTTPBearer()\n\ndef usuario_atual(creds: HTTPAuthorizationCredentials = Depends(security)):\n    try:\n        payload = jwt.decode(creds.credentials, SECRET, algorithms=[ALGORITHM])\n        return payload[\"sub\"]\n    except Exception:\n        raise HTTPException(status_code=401, detail=\"Token inválido\")"
                },
                {"type": "text", "value": "**Como usar em uma rota protegida:**"},
                {
                    "type": "code",
                    "caption": "Protegendo a rota /perfil",
                    "value": "@app.get(\"/perfil\")\ndef perfil(email = Depends(usuario_atual)):\n    return {\"email\": email}\n\n# Se o cliente NÃO manda token → 401\n# Se manda token expirado → 401\n# Se manda token válido → função roda com o email do usuário"
                },
                {"type": "text", "value": "**Por que isso é elegante?** Porque a rota `perfil` **não precisa se preocupar** com autenticação. Ela só declara: *\"eu preciso de um usuário logado\"*. O FastAPI resolve o resto antes de chamar a função."},
                {"type": "text", "value": "**O que o FastAPI faz automaticamente ao ver `Depends`:**"},
                {
                    "type": "code",
                    "caption": "Fluxo do Depends",
                    "value": "1. Vê que a rota precisa da dependência 'usuario_atual'\n2. Chama 'usuario_atual' antes da rota\n3. Passa o resultado como argumento\n4. Se a dependência lançar HTTPException → corta a requisição\n5. Só se tudo passar, chama a função da rota"
                },
                {"type": "text", "value": "**Também dá pra usar `Depends` para outras coisas:** conexão com banco, validação de permissões (admin), configuração de paginação. Qualquer coisa que precise rodar **antes** da rota."},
                {
                    "type": "code",
                    "caption": "Depends para admin",
                    "value": "def somente_admin(email = Depends(usuario_atual)):\n    user = db.usuarios.find_one({\"email\": email})\n    if not user or user.get(\"role\") != \"admin\":\n        raise HTTPException(403, \"Acesso negado\")\n    return user\n\n@app.get(\"/admin/dashboard\")\ndef dashboard(admin = Depends(somente_admin)):\n    return {\"ok\": True}"
                },
                {"type": "text", "value": "**Dica profissional:** cadeias de `Depends` são poderosas. Uma dependência pode depender de outra — o FastAPI resolve a árvore inteira automaticamente. Isso mantém cada peça pequena e reutilizável."},
            ],
            "exercise": {
                "id": "05-06-ex1", "title": "Validando hash",
                "statement": "Simule o hash de senha. Crie uma string `senha_hash` com o valor `'hash_da_senha'`. Crie uma variável `senha_digitada` com `'hash_da_senha'`. Se forem iguais, imprima `Senha correta`.",
                "starter_code": "senha_hash = 'hash_da_senha'\nsenha_digitada = 'hash_da_senha'\n\nif senha_hash == senha_digitada:\n    # imprima 'Senha correta'\n    ",
                "tests": [{"validation": "output_equals", "expected": "Senha correta"}],
                "hint": "print('Senha correta')",
            },
        },
    ],
    "summary": [
        "JWT assina tokens com SECRET — quem altera o payload invalida a assinatura.",
        "bcrypt faz hash de senhas (nunca salve texto puro).",
        "python-jose gera e valida tokens.",
        "Depends() injeta o usuário autenticado nas rotas de forma limpa.",
        "SECRET sempre em variável de ambiente.",
    ],
}


LESSON_05_07 = {
    "id": "05-07", "module_id": "05",
    "title": "Integração com Banco de Dados",
    "objectives": [
        "Separar responsabilidades em módulos (database, models, routes)",
        "Conectar FastAPI ao MongoDB com PyMongo",
        "Criar operações CRUD através de rotas",
        "Organizar projetos com APIRouter",
    ],
    "reading_time_minutes": 20,
    "topics": [
        {
            "id": "t1",
            "title": "Arquitetura — Por que separar em módulos",
            "content": [
                {"type": "text", "value": "Nos primeiros projetos, você colocou tudo em um `main.py`. **Isso não escala.** Quando o projeto passa de 200 linhas, você perde tempo rolando o arquivo tentando achar a rota, e qualquer mudança vira caça ao tesouro."},
                {"type": "text", "value": "A solução é **separar responsabilidades**. Cada arquivo faz uma coisa só. É o mesmo princípio SRP que vimos em POO, aplicado a arquivos."},
                {
                    "type": "code",
                    "caption": "Estrutura recomendada",
                    "value": "app/\n├── main.py            ← cria o FastAPI, inclui routers\n├── database.py        ← conexão com MongoDB\n├── models.py          ← schemas Pydantic\n├── routes/\n│   ├── __init__.py\n│   ├── users.py       ← rotas de usuários\n│   └── produtos.py    ← rotas de produtos\n└── .env"
                },
                {"type": "text", "value": "**Vantagem prática:** quando você mexe em usuários, abre `routes/users.py`. Quando mexe em banco, abre `database.py`. Cada arquivo tem 50–150 linhas, não 2.000. Isso é o que separa projeto pessoal de projeto profissional."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "database.py — Conexão com MongoDB",
            "content": [
                {"type": "text", "value": "**MongoDB Atlas** é a versão na nuvem do MongoDB. Plano gratuito M0 dá 512 MB — mais que suficiente para milhares de usuários de um curso."},
                {"type": "text", "value": "Instale o driver oficial:"},
                {
                    "type": "code",
                    "caption": "Instalando",
                    "value": "pip install pymongo[srv] python-dotenv"
                },
                {"type": "text", "value": "Agora crie o arquivo `app/database.py`:"},
                {
                    "type": "code",
                    "caption": "database.py",
                    "value": "import os\nfrom pymongo import MongoClient\nfrom dotenv import load_dotenv\n\nload_dotenv()\n\nclient = MongoClient(os.getenv(\"MONGODB_URI\"))\ndb = client[os.getenv(\"DB_NAME\", \"curso\")]\n\nusuarios = db[\"usuarios\"]\ncursos = db[\"cursos\"]"
                },
                {"type": "text", "value": "**Detalhes importantes:**"},
                {"type": "text", "value": "**1. `MongoClient` cria o pool de conexões.** Não precisa ficar abrindo/fechando. O driver gerencia por baixo."},
                {"type": "text", "value": "**2. `db[\"usuarios\"]` cria uma referência à coleção.** Se ela não existir, o MongoDB **cria automaticamente** no primeiro insert."},
                {"type": "text", "value": "**3. Nunca coloque a URI no código.** Ela tem usuário e senha — vai no `.env`."},
                {
                    "type": "code",
                    "caption": ".env",
                    "value": "MONGODB_URI=mongodb+srv://usuario:senha@cluster.mongodb.net/curso?retryWrites=true&w=majority\nDB_NAME=curso_saas"
                },
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "APIRouter — Rotas Organizadas",
            "content": [
                {"type": "text", "value": "O **APIRouter** permite criar rotas em arquivos separados e depois **plugar no app principal**. É assim que se organiza um projeto profissional."},
                {
                    "type": "code",
                    "caption": "routes/users.py",
                    "value": "from fastapi import APIRouter, HTTPException\nfrom bson import ObjectId\nfrom app.database import usuarios\nfrom app.models import Usuario\n\nrouter = APIRouter(prefix=\"/usuarios\", tags=[\"Usuários\"])\n\n@router.get(\"\")\ndef listar():\n    resultado = []\n    for u in usuarios.find():\n        u[\"_id\"] = str(u[\"_id\"])\n        resultado.append(u)\n    return resultado\n\n@router.post(\"\", status_code=201)\ndef criar(usuario: Usuario):\n    resultado = usuarios.insert_one(usuario.dict())\n    return {\"id\": str(resultado.inserted_id)}\n\n@router.get(\"/{user_id}\")\ndef buscar(user_id: str):\n    u = usuarios.find_one({\"_id\": ObjectId(user_id)})\n    if not u:\n        raise HTTPException(404, \"Usuário não encontrado\")\n    u[\"_id\"] = str(u[\"_id\"])\n    return u"
                },
                {"type": "text", "value": "**O que ganhamos com APIRouter:**\n\n- `prefix=\"/usuarios\"` → todas as rotas ganham o prefixo automaticamente\n- `tags=[\"Usuários\"]` → agrupa no Swagger em vez de listar tudo junto\n- Cada arquivo cuida de um recurso"},
                {"type": "text", "value": "**⚠️ ObjectId — o detalhe que confunde todo mundo:** o MongoDB gera IDs no formato `ObjectId` (não é string comum). Ao devolver para o cliente, **converta com `str()`**. Ao receber na URL, **converta com `ObjectId(...)`**."},
                {
                    "type": "code",
                    "caption": "main.py — juntando tudo",
                    "value": "from fastapi import FastAPI\nfrom app.routes import users, cursos\n\napp = FastAPI(title=\"Meu SaaS\")\n\napp.include_router(users.router)\napp.include_router(cursos.router)\n\n# Agora as rotas vivem em:\n# /usuarios, /usuarios/{id}, /cursos, etc."
                },
                {"type": "text", "value": "**Dica profissional:** crie um `APIRouter` por recurso (users, cursos, pagamentos, etc). No `main.py`, só inclua os routers. Cada arquivo fica com responsabilidade única, e o `main.py` fica com 20 linhas, não 500."},
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "Separe database.py, models.py e routes/ — cada um faz uma coisa só.",
        "APIRouter com prefix e tags organiza rotas e agrupa no Swagger.",
        "MongoDB gera ObjectId — converta para str() ao devolver.",
        "MongoClient gerencia conexões por baixo — não abra/fecha a cada request.",
    ],
}


LESSON_05_08 = {
    "id": "05-08", "module_id": "05",
    "title": "Documentação Automática (Swagger)",
    "objectives": [
        "Entender o que é OpenAPI e por que ele é o padrão",
        "Conhecer Swagger UI e ReDoc",
        "Personalizar metadados e agrupar endpoints",
        "Documentar campos com Field e exemplos",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "OpenAPI — o padrão por trás",
            "content": [
                {"type": "text", "value": "O FastAPI não inventou a documentação automática. Ele **implementa o padrão OpenAPI** — uma especificação aberta que descreve APIs REST de forma legível por máquinas."},
                {"type": "text", "value": "**O que isso significa na prática?** O FastAPI gera um arquivo JSON (`/openapi.json`) que descreve **todos os endpoints, parâmetros, schemas e respostas** da sua API. Ferramentas leem esse JSON e geram interfaces visuais."},
                {
                    "type": "code",
                    "caption": "Ferramentas que consomem OpenAPI",
                    "value": "/docs      → Swagger UI (interativo, com 'Try it out')\n/redoc     → ReDoc (documentação limpa, focada em leitura)\n/openapi.json → JSON cru, para integrações\n\nExternas:\n- Postman (importa .json automaticamente)\n- Insomnia\n- Geradores de SDK (Python, TypeScript, Go)"
                },
                {"type": "text", "value": "**Por que isso é uma vantagem competitiva?** Porque você **não escreve documentação** — ela é derivada do código. Se o código muda, a doc muda. Nunca fica desatualizada. Isso resolve o problema histórico de APIs com docs desatualizadas."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Personalizando a API",
            "content": [
                {"type": "text", "value": "A doc padrão é funcional, mas genérica. Personalizar os metadados deixa sua API com **cara de produto**, não de protótipo."},
                {
                    "type": "code",
                    "caption": "Metadados da API",
                    "value": "app = FastAPI(\n    title=\"API do Devstack\",\n    description=\"Backend do curso Devstack — autenticação, cursos e pagamentos.\",\n    version=\"1.0.0\",\n    contact={\"name\": \"Felipe\", \"email\": \"felipe@devstack.com\"},\n)"
                },
                {"type": "text", "value": "**Agrupando endpoints com tags** — as tags viram seções no Swagger:"},
                {
                    "type": "code",
                    "caption": "Tags organizam o Swagger",
                    "value": "@app.get(\"/usuarios\", tags=[\"Usuários\"])\ndef listar(): ...\n\n@app.post(\"/cursos\", tags=[\"Cursos\"])\ndef criar_curso(): ...\n\n# No /docs, aparece como:\n# ▼ Usuários\n# ▼ Cursos"
                },
                {"type": "text", "value": "**Documentando cada rota com `summary` e `description`:**"},
                {
                    "type": "code",
                    "caption": "Documentando a rota",
                    "value": "@app.post(\n    \"/usuarios\",\n    summary=\"Criar usuário\",\n    description=\"Cria um novo usuário no banco. Email deve ser único.\",\n    response_description=\"Usuário criado com sucesso\",\n    tags=[\"Usuários\"],\n    status_code=201,\n)\ndef criar(usuario: Usuario):\n    return usuario"
                },
                {"type": "text", "value": "**`summary`** aparece ao lado do endpoint na listagem. **`description`** aparece ao expandir. **`response_description`** aparece junto da resposta 200/201. Esses três campos fazem sua doc parecer feita por uma equipe de produto."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Documentando Campos com Field",
            "content": [
                {"type": "text", "value": "Além de validar, o `Field()` também **documenta**. Você pode passar `description` e `example` que aparecem direto no Swagger."},
                {
                    "type": "code",
                    "caption": "Field com descrição e exemplo",
                    "value": "from pydantic import BaseModel, Field\n\nclass Usuario(BaseModel):\n    nome: str = Field(\n        ..., \n        description=\"Nome completo do usuário\",\n        example=\"Gabrielly Milhor\"\n    )\n    email: str = Field(\n        ...,\n        description=\"Email válido e único no sistema\",\n        example=\"gabrielly@devstack.com\"\n    )"
                },
                {"type": "text", "value": "**O que acontece no `/docs`:** cada campo aparece com a descrição ao lado e com o exemplo clicável. Quem consome a API sabe **exatamente** o que enviar — sem precisar perguntar no Slack."},
                {
                    "type": "code",
                    "caption": "Como aparece no Swagger",
                    "value": "┌──────────────────────────────────────────┐\n│ nome  *string                            │\n│ Nome completo do usuário                 │\n│ Ex: \"Gabrielly Milhor\"                   │\n│                                          │\n│ email  *string                           │\n│ Email válido e único no sistema          │\n│ Ex: \"gabrielly@devstack.com\"             │\n└──────────────────────────────────────────┘"
                },
                {"type": "text", "value": "**Dica profissional:** todo campo de schema merece `description` e `example`. Custa 10 segundos por campo e economiza horas de suporte. É o tipo de detalhe que diferencia uma API amadora de uma API profissional."},
                {"type": "text", "value": "**Try it out — o recurso que substitui o Postman:** no `/docs`, cada endpoint tem um botão **\"Try it out\"**. Você preenche os campos, clica em **Execute**, e vê a requisição e resposta reais. Perfeito para testar rápido durante o desenvolvimento."},
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "FastAPI implementa OpenAPI — docs geradas do código.",
        "/docs (Swagger) e /redoc (ReDoc) são geradas automaticamente.",
        "tags agrupam endpoints no Swagger.",
        "Field com description e example documenta os campos.",
        "Try it out substitui o Postman no dia a dia.",
    ],
}


