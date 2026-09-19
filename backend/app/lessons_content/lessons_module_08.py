"""
Lições do Módulo 08 — Git e GitHub (básico para iniciantes absolutos)
======================================================================

Este módulo ensina a guardar o histórico dos seus projetos com Git e a
publicá-los no GitHub, sem assumir NENHUM conhecimento prévio de terminal.

Onde ele entra no currículo?
- Logo depois do FastAPI (05) e ANTES de HTML + CSS (06).
  Assim, o aluno já aprende a salvar e publicar os projetos desde o começo.
- Como a ordem das aulas vem da lista CURRICULUM (app/analytics.py), o id
  "08" pode ficar entre o "05" e o "06" sem renumerar nada.

Sobre os exercícios:
- Como Git não roda no sandbox Python, o aluno escreve o COMANDO (ou o texto)
  dentro de um print(), e a correção confere se as palavras certas aparecem.

Sobre HTML, CSS e GSAP neste módulo:
- O aluno ainda NÃO estudou HTML/CSS/JS aqui. Os trechos de site são
  "copie e veja funcionar" — o foco é o Git. Tudo é explicado de novo, com
  calma, nos módulos de HTML/CSS e JavaScript.

Estrutura:
- LESSON_08_01 ... LESSON_08_10: uma lição por dicionário
- MODULE_08_LESSONS: dicionário agregador, indexado por id ("08-01", ...)
"""

# ============================================================================
# 08-01 — Git e GitHub: o que são e por que usar
# ============================================================================
LESSON_08_01 = {
    "id": "08-01", "module_id": "08",
    "title": "Git e GitHub: o que são e por que usar",
    "objectives": [
        "Entender que problema o Git resolve no dia a dia de quem programa",
        "Saber a diferença entre Git e GitHub",
        "Conhecer as palavras básicas: repositório, commit, branch e remoto",
        "Perceber por que todo desenvolvedor usa essas ferramentas",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "O problema das mil versões",
            "content": [
                {"type": "text", "value": "Antes de aprender qualquer comando, vale entender **por que essa ferramenta existe**. Se você entender o problema, os comandos passam a fazer sentido sozinhos."},
                {"type": "text", "value": "Você já teve uma pasta assim? **trabalho.docx**, **trabalho_v2.docx**, **trabalho_final.docx**, **trabalho_final_agora_vai.docx**, **trabalho_final_agora_vai_2.docx**. Você faz isso para não perder o que já estava bom. Mas, depois de uma semana, nem você sabe qual arquivo é o certo."},
                {"type": "text", "value": "Com código é pior. Um projeto tem **dezenas de arquivos**, e uma mudança em um deles pode quebrar tudo. Se você não tem um jeito de **voltar atrás**, um erro pequeno vira uma tarde inteira perdida."},
                {"type": "text", "value": "Pense em um **videogame**. Antes de enfrentar o chefão, você salva o jogo. Se perder, volta ao ponto salvo em vez de recomeçar do zero. O **Git** é isso para o seu código: uma forma de criar **pontos de salvamento** e voltar a qualquer um deles."},
                {
                    "type": "code",
                    "caption": "Sem Git x com Git",
                    "value": r"""SEM GIT (uma pasta cheia de cópias):
    meu-site/
        site.html
        site_v2.html
        site_final.html
        site_final_agora_vai.html     <- qual é o certo?

COM GIT (uma pasta só, com o histórico guardado):
    meu-site/
        site.html                     <- sempre a versão mais nova

    Histórico (guardado pelo Git, fora da sua vista):
        ponto 1: criei a página
        ponto 2: adicionei o menu
        ponto 3: mudei as cores      <- posso voltar aqui se precisar""",
                },
                {"type": "text", "value": "**Dica profissional:** todas as empresas de software do mundo usam Git. Saber usar bem essa ferramenta não é um diferencial — é o **mínimo esperado** de quem quer trabalhar com programação."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Git e GitHub não são a mesma coisa",
            "content": [
                {"type": "text", "value": "Quase todo iniciante confunde os dois nomes, porque são parecidos e sempre aparecem juntos. Mas eles fazem **trabalhos diferentes**."},
                {"type": "text", "value": "**Git** é um **programa que fica instalado no seu computador**. Ele é quem cria os pontos de salvamento e guarda o histórico. Funciona mesmo sem internet."},
                {"type": "text", "value": "**GitHub** é um **site** (github.com). Ele guarda uma cópia do seu projeto **na internet**, para você acessar de qualquer lugar, mostrar para outras pessoas e trabalhar em equipe."},
                {"type": "text", "value": "Uma analogia: o Git é a **câmera** que tira as fotos do seu projeto. O GitHub é o **álbum online** onde você guarda e compartilha essas fotos. Dá para tirar fotos sem ter o álbum online, mas o álbum não faz nada sem as fotos."},
                {
                    "type": "code",
                    "caption": "Quem faz o quê",
                    "value": r"""GIT (no seu computador)          GITHUB (na internet)
-------------------------------   -------------------------------
Cria os pontos de salvamento      Guarda uma cópia na nuvem
Guarda o histórico                Permite compartilhar o projeto
Volta para versões antigas        Facilita o trabalho em equipe
Funciona sem internet             Serve de portfólio para vagas
Programa (instalado)              Site (você cria uma conta)""",
                },
                {"type": "text", "value": "**Erro comum:** achar que você precisa do GitHub para usar o Git. Não precisa. O Git funciona sozinho. Existem outros sites parecidos com o GitHub, como **GitLab** e **Bitbucket**, e todos funcionam com o mesmo Git. Neste curso vamos usar o GitHub, que é o mais popular."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "O vocabulário que você vai ouvir sempre",
            "content": [
                {"type": "text", "value": "O mundo do Git tem palavras próprias. Elas parecem estranhas no começo, mas cada uma tem uma comparação simples com o dia a dia."},
                {"type": "text", "value": "**Repositório** (ou *repo*): a pasta do seu projeto, com o histórico guardado dentro dela. É uma pasta **com memória**."},
                {"type": "text", "value": "**Commit**: um ponto de salvamento. Cada commit tem uma mensagem dizendo o que mudou, como a etiqueta de uma caixa de mudança."},
                {"type": "text", "value": "**Branch** (ramo): uma linha do tempo paralela, onde você testa ideias sem mexer na versão principal. Vamos ver isso com calma numa lição só dele."},
                {"type": "text", "value": "**Remoto**: a cópia do repositório que fica no GitHub. O repositório que está no seu computador é o **local**."},
                {
                    "type": "code",
                    "caption": "Resumo do vocabulário",
                    "value": r"""repositório  -> a pasta do projeto, com memória
commit       -> um ponto de salvamento, com mensagem
branch       -> uma linha do tempo paralela para testar ideias
local        -> o que está no seu computador
remoto       -> o que está no GitHub (na internet)
clone        -> baixar uma cópia de um repositório do GitHub
push         -> enviar seus commits para o GitHub
pull         -> trazer as novidades do GitHub para o seu computador""",
                },
                {"type": "text", "value": "Não tente decorar tudo agora. Você vai usar cada palavra dessas nas próximas lições, e vai gravar de tanto repetir. Volte aqui se esquecer alguma."},
            ],
            "exercise": {
                "id": "08-01-ex1", "title": "Git ou GitHub?",
                "statement": "Complete as duas variáveis com **Git** ou **GitHub**. A primeira é a ferramenta que guarda o histórico no seu computador. A segunda é o site onde o projeto fica online. Imprima as duas, uma por linha (primeiro a do computador, depois a do site).",
                "starter_code": '''guarda_historico_no_computador = ""   # Git ou GitHub?
fica_online_para_compartilhar = ""    # Git ou GitHub?

print(guarda_historico_no_computador)
print(fica_online_para_compartilhar)''',
                "tests": [
                    {"validation": "output_line_count", "expected": 2},
                    {"validation": "output_contains_all", "expected": ["Git\nGitHub"]},
                ],
                "hint": "Lembre: o Git é o programa instalado no computador (a câmera). O GitHub é o site (o álbum online). Escreva as palavras com G e H maiúsculos.",
            },
        },
    ],
    "summary": [
        "O Git cria pontos de salvamento do seu código e permite voltar a qualquer um deles.",
        "Git é um programa no seu computador; GitHub é um site que guarda o projeto na internet.",
        "Você pode usar Git sem GitHub, mas não o contrário.",
        "Repositório = pasta com memória; commit = ponto de salvamento; branch = linha do tempo paralela.",
    ],
}


# ============================================================================
# 08-02 — Terminal sem medo e configurando o Git
# ============================================================================
LESSON_08_02 = {
    "id": "08-02", "module_id": "08",
    "title": "Terminal sem medo e configurando o Git",
    "objectives": [
        "Entender o que é o terminal e por que o Git é usado por ele",
        "Usar 5 comandos básicos para navegar entre pastas",
        "Instalar o Git e criar sua conta no GitHub",
        "Dizer ao Git quem é você (nome e e-mail)",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "O que é o terminal",
            "content": [
                {"type": "text", "value": "O Git funciona por **comandos escritos**, e não por botões. Por isso você vai precisar do **terminal**. Muita gente sente medo dele, mas ele é mais simples do que parece."},
                {"type": "text", "value": "Pense em um restaurante. Você pode **apontar no cardápio** (é o que você faz com o mouse, clicando em ícones) ou **pedir ao garçom, falando** (é o terminal). O resultado é o mesmo, mas falar é mais rápido quando você sabe o que quer, e permite pedidos que o cardápio não tem."},
                {"type": "text", "value": "O terminal é uma janela onde você **digita uma instrução, aperta Enter, e o computador responde**. Só isso. Ele não faz nada sozinho e não faz nada que você não mandou."},
                {"type": "text", "value": "**Como abrir:** no **Windows**, depois de instalar o Git (próximo tópico), procure por **Git Bash** no menu Iniciar. No **Mac**, aperte Command + Espaço e digite **Terminal**. A opção mais prática é usar o terminal **dentro do VS Code**: aperte Ctrl + ' (a tecla do apóstrofo) ou vá em Terminal > Novo Terminal."},
                {"type": "text", "value": "**Erro comum:** ficar com medo de quebrar o computador. Comandos de Git só mexem na pasta do seu projeto, e quase tudo pode ser desfeito. Errar aqui é parte de aprender."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "5 comandos que já resolvem",
            "content": [
                {"type": "text", "value": "Para usar o Git você só precisa **andar entre pastas**. É como andar por uma casa: primeiro você precisa saber **em que cômodo está**, depois escolher para onde ir."},
                {
                    "type": "code",
                    "caption": "Os 5 comandos de navegação",
                    "value": r"""# Onde estou agora?  (mostra o caminho da pasta atual)
pwd

# O que tem aqui dentro?  (lista os arquivos e pastas)
ls
# No Windows PowerShell, o equivalente é: dir

# Entrar em uma pasta
cd Documentos

# Voltar uma pasta (os dois pontos significam 'a pasta de cima')
cd ..

# Criar uma pasta nova
mkdir meu-site""",
                },
                {"type": "text", "value": "Um exemplo de rotina: você abre o terminal, digita `pwd` para saber onde está, `cd Documentos` para entrar na pasta de documentos, `mkdir meu-site` para criar a pasta do projeto e `cd meu-site` para entrar nela."},
                {"type": "text", "value": "**Erro comum:** digitar `cd meu site` (com espaço). O terminal entende que são **dois nomes**. Prefira nomes sem espaços e sem acentos nas pastas de projeto, usando hífen: `meu-site`."},
                {"type": "text", "value": "**Dica profissional:** o terminal tem dois atalhos que economizam muito tempo. A tecla **Tab** completa o nome de pastas e arquivos (digite `cd Doc` e aperte Tab). A **seta para cima** traz de volta o último comando que você digitou."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Instalando o Git, criando a conta e se apresentando",
            "content": [
                {"type": "text", "value": "Agora vamos deixar tudo pronto. São três passos, e você faz uma **única vez** na vida (ou uma vez por computador)."},
                {"type": "text", "value": "**Passo 1 — Instalar o Git.** Entre em **git-scm.com**, baixe a versão do seu sistema e instale, aceitando as opções padrão. Depois, abra o terminal e teste se deu certo."},
                {
                    "type": "code",
                    "caption": "Testando a instalação",
                    "value": r"""# Pergunta ao computador: qual versão do Git você tem?
git --version

# Se der certo, aparece algo como:
# git version 2.45.0
# Se aparecer 'command not found', feche e abra o terminal de novo.""",
                },
                {"type": "text", "value": "**Passo 2 — Criar a conta no GitHub.** Entre em **github.com**, clique em **Sign up** e preencha e-mail, senha e um **nome de usuário**. Esse nome vai aparecer no endereço dos seus projetos (github.com/seu-usuario), então escolha um nome profissional, que você não vai ter vergonha de colocar no currículo."},
                {"type": "text", "value": "**Passo 3 — Se apresentar ao Git.** Cada ponto de salvamento guarda **quem o fez**. Então o Git precisa saber seu nome e e-mail. Use o **mesmo e-mail da sua conta do GitHub**."},
                {
                    "type": "code",
                    "caption": "Configurando o Git (só uma vez)",
                    "value": r"""# Seu nome (vai aparecer nos commits)
git config --global user.name "Seu Nome"

# O MESMO e-mail da sua conta do GitHub
git config --global user.email "seuemail@exemplo.com"

# Nome padrão da linha do tempo principal: 'main'
git config --global init.defaultBranch main

# Conferir tudo que foi salvo
git config --list""",
                },
                {"type": "text", "value": "**Erro comum:** usar no Git um e-mail diferente do da conta do GitHub. Nesse caso, seus commits ficam sem o seu perfil, e o GitHub não conta a atividade no seu gráfico de contribuições (o quadradinho verde que recrutadores gostam de olhar)."},
                {"type": "text", "value": "O `--global` significa **para todos os projetos deste computador**. Sem ele, a configuração valeria só para um projeto."},
            ],
            "exercise": {
                "id": "08-02-ex1", "title": "Se apresentando ao Git",
                "statement": "Escreva, com `print()`, os dois comandos que dizem ao Git o seu **nome** e o seu **e-mail**, nesta ordem. Use `--global` nos dois. Use qualquer nome e e-mail.",
                "starter_code": '''# Imprima um comando por linha
# 1) o comando que configura o nome (user.name)
# 2) o comando que configura o e-mail (user.email)
''',
                "tests": [
                    {"validation": "output_contains_all", "expected": ["git config --global user.name", "git config --global user.email"]},
                    {"validation": "output_line_count", "expected": 2},
                ],
                "hint": 'print(\'git config --global user.name "Ana Souza"\') e depois o mesmo formato com user.email e um e-mail.',
            },
        },
    ],
    "summary": [
        "O terminal é uma janela onde você digita instruções e o computador responde.",
        "pwd mostra onde você está; ls lista; cd entra; cd .. volta; mkdir cria pasta.",
        "Instale o Git em git-scm.com e confira com git --version.",
        "Configure nome e e-mail uma vez com git config --global, usando o e-mail do GitHub.",
    ],
}


# ============================================================================
# 08-03 — Seu primeiro repositório
# ============================================================================
LESSON_08_03 = {
    "id": "08-03", "module_id": "08",
    "title": "Seu primeiro repositório: init, add, commit, status e log",
    "objectives": [
        "Criar um repositório com git init",
        "Entender o caminho: modificar, add e commit",
        "Usar git status para saber a situação do projeto",
        "Ver o histórico com git log",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "t1",
            "title": "git init: dando memória à pasta",
            "content": [
                {"type": "text", "value": "Uma pasta comum não guarda histórico nenhum. Para que o Git comece a acompanhar seus arquivos, você precisa **avisar**: 'esta pasta agora é um projeto que quero vigiar'. O comando que faz isso é o `git init`."},
                {"type": "text", "value": "Pense em colocar uma **câmera de segurança** em uma sala. Antes de instalar, ninguém registrava nada. Depois, tudo o que mudar lá dentro fica gravado."},
                {
                    "type": "code",
                    "caption": "Criando o primeiro repositório",
                    "value": r"""# 1. Crie uma pasta e entre nela
mkdir meu-primeiro-repo
cd meu-primeiro-repo

# 2. Confirme que você está na pasta certa
pwd

# 3. Ative o Git nesta pasta
git init

# Resposta esperada:
# Initialized empty Git repository in .../meu-primeiro-repo/.git/""",
                },
                {"type": "text", "value": "O `git init` cria uma pasta escondida chamada **.git**. É lá dentro que o Git guarda todo o histórico. **Nunca mexa nela à mão.** Se um dia quiser 'desligar' o Git de um projeto, basta apagar essa pasta."},
                {"type": "text", "value": "**Erro comum:** rodar `git init` na pasta errada, como a área de trabalho inteira ou a pasta do usuário. Aí o Git tenta vigiar centenas de arquivos que não têm nada a ver. **Sempre** rode `pwd` antes para conferir onde você está."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "As 3 etapas: modificar, add e commit",
            "content": [
                {"type": "text", "value": "Aqui está a ideia mais importante do Git. Salvar um ponto **não é automático**: são **duas etapas**, e existe um motivo bom para isso."},
                {"type": "text", "value": "Imagine que você está **se mudando de casa**. Primeiro você **escolhe o que vai em cada caixa** (nem tudo vai na mesma caixa). Depois **fecha a caixa e cola uma etiqueta** dizendo o que tem dentro."},
                {"type": "text", "value": "No Git, **`git add`** é colocar coisas na caixa e **`git commit`** é fechar a caixa com a etiqueta. Assim você escolhe exatamente o que entra em cada ponto de salvamento."},
                {
                    "type": "code",
                    "caption": "O caminho completo de um commit",
                    "value": r"""# Crie um arquivo qualquer (no VS Code ou pelo terminal)
echo "Meu primeiro projeto" > leia-me.txt

# Veja a situação: o Git avisa que tem um arquivo novo, ainda solto
git status

# Coloque o arquivo na caixa
git add leia-me.txt
# Para colocar TUDO que mudou de uma vez, use um ponto:
# git add .

# Feche a caixa e cole a etiqueta (a mensagem entre aspas)
git commit -m "Cria arquivo leia-me"

# Resposta esperada:
# [main (root-commit) a1b2c3d] Cria arquivo leia-me
#  1 file changed, 1 insertion(+)""",
                },
                {"type": "text", "value": "O `git status` é o seu **melhor amigo**. Ele diz o que mudou, o que já está na caixa e o que está solto. Rode-o **o tempo todo**, antes e depois de qualquer comando."},
                {
                    "type": "code",
                    "caption": "Lendo o git status",
                    "value": r"""Untracked files:            <- arquivos novos que o Git ainda não conhece
    leia-me.txt

Changes not staged:          <- arquivos que você mudou, mas não colocou na caixa
    modified: leia-me.txt

Changes to be committed:     <- arquivos na caixa, prontos para o commit
    new file: leia-me.txt

nothing to commit            <- tudo salvo, nada para fazer""",
                },
                {"type": "text", "value": "**Erro comum:** esquecer o `git add` e digitar direto o `git commit`. O Git responde com 'nothing added to commit' porque a caixa está vazia. A regra é sempre a mesma: **primeiro add, depois commit**."},
                {"type": "text", "value": "**Erro comum 2:** esquecer o `-m` e a mensagem. O Git abre um editor de texto estranho no terminal, e muita gente fica presa nele. Se isso acontecer, digite `:q!` e aperte Enter para sair, e refaça o comando com `-m`."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "git log: olhando o histórico",
            "content": [
                {"type": "text", "value": "De que adianta guardar pontos de salvamento se você não puder **ver a lista**? O `git log` mostra todos os commits, do mais novo para o mais antigo, como um **diário do projeto**."},
                {
                    "type": "code",
                    "caption": "Vendo o histórico",
                    "value": r"""# Versão completa (autor, data, mensagem)
git log

# Versão resumida: um commit por linha (a que você vai usar mais)
git log --oneline

# Exemplo de resposta:
# c3d4e5f Adiciona botão de contato
# b2c3d4e Muda a cor do título
# a1b2c3d Cria arquivo leia-me
#
# Cada commit tem um código (c3d4e5f) que funciona como o RG dele.""",
                },
                {"type": "text", "value": "**Erro comum:** o log abre e o terminal 'trava'. Ele não travou: o Git abriu a lista em modo de leitura. Aperte a tecla **q** para sair."},
                {"type": "text", "value": "**Dica profissional:** crie o hábito de rodar `git status` antes de fazer um commit e `git log --oneline` depois. Em poucos segundos você confirma **o que vai entrar** e **o que entrou**."},
            ],
            "exercise": {
                "id": "08-03-ex1", "title": "Seu primeiro commit",
                "statement": "Escreva, com `print()`, os **3 comandos** para criar um repositório e salvar o primeiro ponto, na ordem certa: (1) ativar o Git na pasta, (2) colocar todos os arquivos na caixa, (3) fechar a caixa com a mensagem 'Primeiro commit'. Um comando por linha.",
                "starter_code": '''# 1) ativar o Git na pasta
# 2) colocar tudo na caixa (dica: o ponto significa 'tudo')
# 3) fechar a caixa com a mensagem 'Primeiro commit'
''',
                "tests": [
                    {"validation": "output_line_count", "expected": 3},
                    {"validation": "output_contains_all", "expected": ["git init", "git add", "git commit -m"]},
                ],
                "hint": 'print("git init"), depois print("git add ."), depois print(\'git commit -m "Primeiro commit"\').',
            },
        },
    ],
    "summary": [
        "git init ativa o Git na pasta e cria a pasta escondida .git.",
        "git add coloca arquivos na caixa; git commit fecha a caixa com uma mensagem.",
        "git status mostra a situação do projeto — use o tempo todo.",
        "git log --oneline mostra o histórico; aperte q para sair.",
    ],
}


# ============================================================================
# 08-04 — Conectando ao GitHub
# ============================================================================
LESSON_08_04 = {
    "id": "08-04", "module_id": "08",
    "title": "Conectando ao GitHub: remote, push, pull e clone",
    "objectives": [
        "Criar um repositório vazio no GitHub",
        "Conectar o repositório local ao remoto com git remote add",
        "Enviar seus commits com git push",
        "Trazer novidades com git pull e baixar projetos com git clone",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "t1",
            "title": "Criando o repositório no GitHub",
            "content": [
                {"type": "text", "value": "Até agora seu histórico mora **só no seu computador**. Se o notebook quebrar, você perde tudo. O GitHub resolve isso: ele guarda uma cópia **na nuvem**, como um cofre fora da sua casa."},
                {"type": "text", "value": "Primeiro, crie o cofre. No GitHub, clique no botão **+** no canto superior direito e escolha **New repository**."},
                {
                    "type": "code",
                    "caption": "Preenchendo a tela de novo repositório",
                    "value": r"""Repository name:   meu-primeiro-repo      (sem espaços, use hífen)
Description:       (opcional) Meu primeiro projeto com Git
Visibilidade:      Public  -> qualquer pessoa pode ver
                   Private -> só você (e quem você convidar)

Add a README file:   NÃO MARQUE
Add .gitignore:      None
Choose a license:    None

Clique em: Create repository""",
                },
                {"type": "text", "value": "**Por que deixar o README desmarcado?** Porque você já tem um repositório no computador. Se o GitHub criar um arquivo por lá também, os dois lados ficam **diferentes desde o começo**, e o primeiro envio vai dar problema. Repositório novo e vazio é o caminho mais simples."},
                {"type": "text", "value": "**Dica profissional:** projetos que você quer mostrar no currículo devem ser **públicos**. Projetos com senhas, chaves ou dados de clientes devem ser **privados**."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "remote add e push: enviando para a nuvem",
            "content": [
                {"type": "text", "value": "Agora você precisa **ligar as duas pontas**: o repositório do computador e o do GitHub. O Git não sabe que eles são parentes até você contar."},
                {"type": "text", "value": "Pense em **guardar caixas em um depósito**. Primeiro você anota o **endereço do depósito** (é o `remote add`). Depois você **manda as caixas para lá** (é o `push`)."},
                {
                    "type": "code",
                    "caption": "Conectando e enviando pela primeira vez",
                    "value": r"""# 1. Garanta que a linha do tempo principal se chama 'main'
git branch -M main

# 2. Anote o endereço do depósito.
#    'origin' é só um apelido para esse endereço (padrão de todo mundo).
#    Copie a URL na página do repositório no GitHub.
git remote add origin https://github.com/seu-usuario/meu-primeiro-repo.git

# 3. Envie os commits para o GitHub.
#    O -u grava a ligação para que, nos próximos envios, baste 'git push'.
git push -u origin main""",
                },
                {"type": "text", "value": "Depois desse primeiro envio, atualize a página do repositório no GitHub. Seus arquivos e o histórico de commits estarão lá. **Você acabou de publicar seu código.**"},
                {"type": "text", "value": "Nas próximas vezes, o fluxo do dia a dia é curto: mexeu, `git add .`, `git commit -m \"...\"` e `git push`."},
                {"type": "text", "value": "**Sobre a autenticação:** o GitHub não aceita mais a senha da conta para o push. No Windows, o Git já vem com um assistente que abre uma **janela do navegador** para você entrar na conta, é só autorizar. Se ele pedir uma senha, ela deve ser um **token de acesso** (em GitHub > Settings > Developer settings > Personal access tokens), não a senha da sua conta."},
                {"type": "text", "value": "**Erros comuns:** 'remote origin already exists' quer dizer que você já fez o `remote add`; use `git remote -v` para ver o endereço salvo. 'Authentication failed' quer dizer que o login ou o token está errado. 'Repository not found' quase sempre é erro de digitação na URL."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "pull e clone: trazendo código para o seu computador",
            "content": [
                {"type": "text", "value": "O caminho também funciona no sentido contrário. Você vai precisar **baixar** código do GitHub em duas situações: pegar um projeto que ainda não está no seu computador, ou atualizar um que já está."},
                {"type": "text", "value": "**`git clone`** é para a **primeira vez**: copia o projeto inteiro, com todo o histórico. **`git pull`** é para as **próximas vezes**: traz só as novidades, como abrir o e-mail para ver se chegou algo novo."},
                {
                    "type": "code",
                    "caption": "clone e pull",
                    "value": r"""# CLONE: baixa um projeto inteiro pela primeira vez.
# Ele cria uma pasta nova com o nome do projeto.
git clone https://github.com/seu-usuario/meu-primeiro-repo.git
cd meu-primeiro-repo

# PULL: dentro de um projeto que você já tem,
# traz as novidades que estão no GitHub.
git pull""",
                },
                {"type": "text", "value": "Quando você trabalha em **dois computadores** (casa e trabalho) ou **em equipe**, o GitHub vira o ponto de encontro. Alguém envia com `push`, e os outros trazem com `pull`."},
                {"type": "text", "value": "**Erro comum:** trabalhar sem fazer `git pull` antes. Se o GitHub tem commits que você não tem, o `push` é recusado ('rejected'). A solução é fazer `git pull` primeiro e depois o `git push`."},
                {"type": "text", "value": "**Dica profissional:** todo dia, antes de começar, rode `git pull`. É como olhar o quadro de avisos antes de começar o trabalho."},
            ],
            "exercise": {
                "id": "08-04-ex1", "title": "Conectando ao GitHub",
                "statement": "Escreva, com `print()`, os comandos para (1) ligar o repositório local ao endereço `https://github.com/ana/meu-site.git` usando o apelido `origin`, e (2) enviar o branch `main` gravando a ligação (com `-u`). Um comando por linha.",
                "starter_code": '''# 1) conectar ao endereço remoto com o apelido origin
# 2) enviar o main para o origin, gravando a ligação
''',
                "tests": [
                    {"validation": "output_contains_all", "expected": ["git remote add origin", "https://github.com/ana/meu-site.git", "git push -u origin main"]},
                ],
                "hint": "O primeiro comando começa com git remote add origin e termina com a URL. O segundo é git push -u origin main.",
            },
        },
    ],
    "summary": [
        "Crie o repositório no GitHub vazio, sem README, quando já existe um projeto local.",
        "git remote add origin URL liga o projeto local ao GitHub.",
        "git push -u origin main envia os commits; nas próximas vezes, basta git push.",
        "git clone baixa um projeto pela primeira vez; git pull traz as novidades.",
    ],
}


# ============================================================================
# 08-05 — Branches
# ============================================================================
LESSON_08_05 = {
    "id": "08-05", "module_id": "08",
    "title": "Branches: testando ideias sem medo",
    "objectives": [
        "Entender por que branches existem",
        "Criar uma branch e trocar entre elas",
        "Juntar o trabalho de volta com git merge",
        "Apagar branches que não servem mais",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "t1",
            "title": "Por que existem branches",
            "content": [
                {"type": "text", "value": "Imagine que seu site está funcionando bem e você quer testar um menu novo. Se mexer direto nos arquivos e der errado, o site quebra e você ainda precisa desfazer tudo. Seria bom ter um **espaço de rascunho**."},
                {"type": "text", "value": "É isso que uma **branch** (ramo) faz. Pense em um **filme com universos paralelos**: a história principal continua acontecendo, e você abre uma linha alternativa para testar 'e se eu mudasse isso?'. Se gostar, junta as duas. Se não gostar, descarta o universo paralelo, e a história principal nem percebeu."},
                {"type": "text", "value": "A branch principal se chama **main**. A regra de ouro dos times é: **a main sempre funciona**. Todo trabalho novo acontece em outra branch e só volta para a main quando estiver pronto."},
                {
                    "type": "code",
                    "caption": "Como as branches se parecem",
                    "value": r"""main:      A --- B --- C ----------------- F      <- sempre estável
                    \                   /
teste-menu:          D --- E -----------        <- seu rascunho

A, B, C, D, E, F são commits (pontos de salvamento).
Em F, o trabalho da branch 'teste-menu' foi juntado à main.""",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Criando e trocando de branch",
            "content": [
                {"type": "text", "value": "São só dois comandos para o dia a dia: um para **criar e entrar** em uma branch nova, outro para **trocar** entre branches que já existem."},
                {
                    "type": "code",
                    "caption": "Criar, listar e trocar",
                    "value": r"""# Em qual branch estou? Qual branches existem?
# (a branch atual aparece com um asterisco *)
git branch

# Criar uma branch nova E já entrar nela
git switch -c feature/botao-animado

# Voltar para a main
git switch main

# Entrar de novo na branch que você criou
git switch feature/botao-animado

# Obs.: em tutoriais mais antigos aparece 'git checkout'.
# Ele faz o mesmo, e 'git checkout -b nome' equivale a 'git switch -c nome'.""",
                },
                {"type": "text", "value": "Dentro da branch nova, você trabalha normalmente: edita arquivos, faz `git add` e `git commit`. Esses commits **só existem nessa branch**. Se voltar para a main, seus arquivos voltam a ser como eram, como se o rascunho tivesse sido guardado numa gaveta."},
                {"type": "text", "value": "**Convenção de nomes:** use nomes curtos que dizem o que você vai fazer, com hífen no lugar de espaço. Muitos times usam prefixos: `feature/` para coisas novas e `fix/` para correções."},
                {"type": "text", "value": "**Erro comum:** fazer o trabalho **na branch errada**, geralmente na main, esquecendo de criar a branch antes. Por isso: antes de começar, rode `git status`. A primeira linha diz **em qual branch você está**."},
                {"type": "text", "value": "**Erro comum 2:** tentar trocar de branch com mudanças ainda sem commit. O Git protege você e pode recusar a troca. Faça o commit (ou guarde as mudanças) antes de trocar."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "merge: juntando o trabalho de volta",
            "content": [
                {"type": "text", "value": "Você testou a ideia na sua branch e gostou. Agora precisa **trazer esse trabalho para a main**. Esse encontro das duas linhas do tempo se chama **merge**."},
                {"type": "text", "value": "Vamos a um exemplo prático. Numa branch, você quer que o botão do seu site **cresça um pouquinho quando o mouse passa por cima**. A mudança no arquivo `style.css` é pequena (você vai entender cada linha nos módulos de HTML e CSS, por enquanto o importante é o Git):"},
                {
                    "type": "code",
                    "caption": "A mudança feita na branch: style.css",
                    "value": r"""/* transition: faz a mudança acontecer suavemente em 0.2 segundos,
   em vez de pular de um jeito para o outro de uma vez */
.botao {
    transition: transform 0.2s ease;
}

/* :hover é o momento em que o mouse está em cima do botão.
   scale(1.08) aumenta o tamanho em 8% */
.botao:hover {
    transform: scale(1.08);
}""",
                },
                {
                    "type": "code",
                    "caption": "O caminho completo: da ideia até a main",
                    "value": r"""# 1. Crie a branch e trabalhe nela
git switch -c feature/botao-animado
# ...edite o style.css...
git add .
git commit -m "Adiciona animação ao passar o mouse no botão"

# 2. Volte para a main (quem RECEBE o trabalho)
git switch main

# 3. Traga o trabalho da outra branch para cá
git merge feature/botao-animado

# 4. Apague a branch, que já cumpriu a função
git branch -d feature/botao-animado

# 5. Envie a main atualizada para o GitHub
git push""",
                },
                {"type": "text", "value": "**A regra do merge:** você sempre vai para a branch que vai **receber** o trabalho (a main) e roda `git merge` com o nome da branch que **traz** o trabalho. Fica fácil de memorizar: 'estou na main, quero juntar a feature aqui'."},
                {"type": "text", "value": "**Erro comum:** rodar o merge estando na branch errada e juntar a main dentro da feature. Antes de qualquer merge, confira com `git status` onde você está."},
                {"type": "text", "value": "**Dica profissional:** crie uma branch para **cada tarefa pequena**. Branches pequenas e de vida curta dão poucos problemas ao juntar. Branches que ficam semanas abertas viram dor de cabeça."},
            ],
            "exercise": {
                "id": "08-05-ex1", "title": "Do rascunho para a main",
                "statement": "Escreva, com `print()`, os comandos para: (1) criar e entrar na branch `feature/menu`, (2) voltar para a `main`, (3) juntar a `feature/menu` na main. Um comando por linha, na ordem.",
                "starter_code": '''# 1) criar e entrar na branch feature/menu
# 2) voltar para a main
# 3) juntar a feature/menu na main
''',
                "tests": [
                    {"validation": "output_contains_any", "expected": ["git switch -c feature/menu", "git checkout -b feature/menu"]},
                    {"validation": "output_contains_any", "expected": ["git switch main", "git checkout main"]},
                    {"validation": "output_contains_all", "expected": ["git merge feature/menu"]},
                ],
                "hint": "Comece com git switch -c seguido do nome da branch. Depois git switch main. Por último, git merge com o nome da branch que traz o trabalho.",
            },
        },
    ],
    "summary": [
        "Branch é uma linha do tempo paralela: você testa ideias sem mexer na main.",
        "git switch -c nome cria e entra; git switch nome troca; git branch lista.",
        "Para juntar: vá para a branch que recebe (main) e rode git merge nome-da-branch.",
        "Use uma branch por tarefa pequena e apague depois do merge com git branch -d.",
    ],
}


# ============================================================================
# 08-06 — Pull Requests
# ============================================================================
LESSON_08_06 = {
    "id": "08-06", "module_id": "08",
    "title": "Pull Requests: pedindo para juntar seu trabalho",
    "objectives": [
        "Entender o que é um Pull Request e por que times o usam",
        "Abrir um Pull Request no GitHub, do começo ao fim",
        "Escrever uma boa descrição para o PR",
        "Atualizar seu computador depois do merge",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "O que é um Pull Request e por que existe",
            "content": [
                {"type": "text", "value": "Na lição anterior, você juntou a branch na main **direto pelo terminal**. Isso funciona quando você trabalha sozinho. Mas em uma equipe, ninguém quer que um colega coloque código na main sem ninguém olhar."},
                {"type": "text", "value": "O **Pull Request** (PR) é um **pedido educado**: 'terminei meu trabalho nesta branch; podem dar uma olhada e, se estiver bom, juntar na main?'. O nome vem de 'pedir para **puxar** (pull) o meu código'."},
                {"type": "text", "value": "Pense em uma **redação da escola**. Você não coloca o texto direto no livro da turma: entrega ao professor, ele lê, sugere ajustes e só depois publica. O PR é essa entrega."},
                {"type": "text", "value": "**Mesmo trabalhando sozinho**, PR vale a pena: ele deixa um **registro organizado** de cada mudança (o que foi feito e por quê) e treina o processo que você vai usar no primeiro emprego."},
                {"type": "text", "value": "Um detalhe: o PR **não existe no Git**, ele é um recurso do **GitHub** (lembra da diferença da primeira lição?). Por isso ele é feito no site, não no terminal."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "O passo a passo, do começo ao fim",
            "content": [
                {"type": "text", "value": "O fluxo tem **duas partes**: uma no terminal (preparar e enviar a branch) e outra no site do GitHub (abrir e juntar o PR). Siga na ordem."},
                {
                    "type": "code",
                    "caption": "Parte 1 — no terminal",
                    "value": r"""# 1. Comece sempre com a main atualizada
git switch main
git pull

# 2. Crie a branch da tarefa
git switch -c fix/titulo-do-site

# 3. Trabalhe, salve os pontos
git add .
git commit -m "Corrige o título da página inicial"

# 4. Envie a BRANCH (não a main) para o GitHub
git push -u origin fix/titulo-do-site""",
                },
                {
                    "type": "code",
                    "caption": "Parte 2 — no site do GitHub",
                    "value": r"""1. Abra o repositório no GitHub.
   Aparece uma faixa amarela: 'fix/titulo-do-site had recent pushes'.
2. Clique em 'Compare & pull request'.
3. Escreva um título claro e uma descrição do que você fez.
4. Clique em 'Create pull request'.
5. (Em equipe) espere alguém revisar e aprovar.
6. Clique em 'Merge pull request' e depois em 'Confirm merge'.
7. Clique em 'Delete branch' (ela já cumpriu a função).""",
                },
                {
                    "type": "code",
                    "caption": "Parte 3 — de volta ao terminal",
                    "value": r"""# O merge aconteceu no GitHub. Seu computador ainda não sabe!
# Traga a novidade:
git switch main
git pull

# Apague a branch antiga também do seu computador
git branch -d fix/titulo-do-site""",
                },
                {"type": "text", "value": "**Erro comum:** esquecer a Parte 3. Você faz o merge no site, volta ao computador e sua main continua velha. Se você começar a trabalhar assim, vai criar problemas. **Depois de todo merge no GitHub, faça `git switch main` e `git pull`.**"},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Escrevendo uma boa descrição",
            "content": [
                {"type": "text", "value": "Quem abre seu PR não sabe o que estava na sua cabeça. Uma descrição clara **economiza o tempo** de quem revisa e também ajuda você, daqui a seis meses, a lembrar por que mudou aquilo."},
                {"type": "text", "value": "Uma descrição simples já resolve, com **duas perguntas**: 'o que mudou?' e 'como eu testo?'. Veja um modelo que você pode copiar."},
                {
                    "type": "code",
                    "caption": "Modelo de descrição de PR",
                    "value": r"""## O que mudou
- Corrige o título da página inicial, que estava com erro de digitação
- Aumenta o tamanho da fonte do título no celular

## Como testar
1. Abra o arquivo index.html no navegador
2. Confira se o título aparece como 'Bem-vindo ao meu site'
3. Diminua a janela e veja se o título continua legível""",
                },
                {"type": "text", "value": "**Erro comum:** PRs gigantes, que mexem em dez assuntos diferentes. Ninguém consegue revisar direito. **Um PR, um assunto.**"},
                {"type": "text", "value": "**Dica profissional:** se o seu PR resolve um problema aberto (uma 'issue'), escreva `Closes #12` na descrição (troque 12 pelo número). Ao fazer o merge, o GitHub fecha a issue sozinho."},
            ],
            "exercise": {
                "id": "08-06-ex1", "title": "Descrição de Pull Request",
                "statement": "Imprima uma descrição de PR com **dois títulos**: `## O que mudou` e `## Como testar`, cada um com pelo menos uma linha embaixo. Use `print()`.",
                "starter_code": '''descricao = """
"""
print(descricao)''',
                "tests": [
                    {"validation": "output_contains_all", "expected": ["## O que mudou", "## Como testar"]},
                ],
                "hint": "Dentro das aspas triplas, escreva a linha ## O que mudou, uma linha começando com hífen, depois ## Como testar e outra linha embaixo.",
            },
        },
    ],
    "summary": [
        "Pull Request é um pedido para juntar sua branch na main; ele existe no GitHub, não no Git.",
        "Fluxo: branch, commits, push da branch, abrir PR, revisar, merge.",
        "Depois do merge no site, rode git switch main e git pull no seu computador.",
        "Bom PR: um assunto só, com 'o que mudou' e 'como testar'.",
    ],
}


# ============================================================================
# 08-07 — Resolvendo conflitos
# ============================================================================
LESSON_08_07 = {
    "id": "08-07", "module_id": "08",
    "title": "Resolvendo conflitos sem pânico",
    "objectives": [
        "Entender o que é um conflito e por que ele acontece",
        "Ler os marcadores que o Git coloca no arquivo",
        "Resolver um conflito passo a passo",
        "Saber desistir de um merge com segurança",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "O que é um conflito (e por que não é culpa sua)",
            "content": [
                {"type": "text", "value": "Você vai encontrar conflitos mais cedo ou mais tarde. Eles **assustam** porque aparece uma mensagem vermelha, mas são **normais**, e resolvê-los é simples."},
                {"type": "text", "value": "Imagine que você e uma colega recebem cópias da mesma frase para editar. Você escreve 'Bem-vindo ao site'. Ela, no mesmo lugar, escreve 'Site da Ana'. Quando forem juntar as duas versões, ninguém sabe **qual vale**. O Git também não sabe e **pede ajuda**. Isso é um conflito."},
                {"type": "text", "value": "O conflito só acontece quando **duas branches mudam a mesma parte do mesmo arquivo**. Se você mexe na linha 3 e ela mexe na linha 40, o Git junta tudo sozinho."},
                {"type": "text", "value": "O Git **não escolhe** por você porque não sabe qual versão está certa. Apagar a sua mudança ou a dela sozinho seria pior. Ele para, marca o problema no arquivo e espera você decidir."},
                {"type": "text", "value": "**Erro comum:** achar que o conflito quebrou o projeto. Não quebrou. O Git só pausou o merge e nada foi perdido. Dá para resolver ou desistir a qualquer momento."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Lendo os marcadores",
            "content": [
                {"type": "text", "value": "Quando dá conflito, o Git **escreve dentro do arquivo** as duas versões, separadas por marcadores. Você vai ver algo assim."},
                {
                    "type": "code",
                    "caption": "Um arquivo em conflito",
                    "value": r"""<h1>Meu Site</h1>
<<<<<<< HEAD
<p>Bem-vindo ao site</p>
=======
<p>Site da Ana</p>
>>>>>>> feature/texto-da-ana
<footer>Feito com carinho</footer>""",
                },
                {"type": "text", "value": "**Como ler:**"},
                {"type": "text", "value": "Tudo entre `<<<<<<< HEAD` e `=======` é a **sua versão** (a branch em que você está)."},
                {"type": "text", "value": "Tudo entre `=======` e `>>>>>>>` é a versão da **outra branch** (a que você está juntando). O nome dela aparece no fim do marcador."},
                {"type": "text", "value": "As linhas de fora (o `<h1>` e o `<footer>`) não tiveram problema e ficam como estão."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Resolvendo passo a passo",
            "content": [
                {"type": "text", "value": "Resolver é **editar o arquivo até ele ficar do jeito que deveria ser** e apagar os marcadores. Você escolhe uma das versões, a outra, ou mistura as duas."},
                {
                    "type": "code",
                    "caption": "Do conflito ao commit",
                    "value": r"""# 1. Você tenta o merge e aparece o conflito
git switch main
git merge feature/texto-da-ana
# Auto-merging index.html
# CONFLICT (content): Merge conflict in index.html
# Automatic merge failed; fix conflicts and then commit the result.

# 2. Veja quais arquivos estão em conflito
git status

# 3. Abra o arquivo no VS Code.
#    Ele mostra botões acima do conflito:
#    'Accept Current Change'   -> fica com a sua versão
#    'Accept Incoming Change'  -> fica com a versão da outra branch
#    'Accept Both Changes'     -> fica com as duas
#    Ou edite à mão. O importante: APAGAR as linhas <<<<<<<, ======= e >>>>>>>.

# 4. Avise ao Git que resolveu, e feche o merge
git add index.html
git commit -m "Resolve conflito no texto de boas-vindas"

# Se quiser DESISTIR e voltar como estava antes do merge:
# git merge --abort""",
                },
                {
                    "type": "code",
                    "caption": "Como o arquivo pode ficar depois de resolvido",
                    "value": r"""<h1>Meu Site</h1>
<p>Bem-vindo ao site da Ana</p>
<footer>Feito com carinho</footer>

<!-- Misturamos as duas ideias e não sobrou nenhum marcador. -->""",
                },
                {"type": "text", "value": "**Erro comum grave:** fazer o commit **sem apagar os marcadores**. O arquivo fica com `<<<<<<<` dentro do código e o site quebra. Antes do `git add`, procure por `<<<<<<<` no arquivo (Ctrl + F) para ter certeza de que não sobrou nenhum."},
                {"type": "text", "value": "**Dica profissional:** você evita a maioria dos conflitos fazendo `git pull` com frequência, criando branches pequenas e conversando com o time sobre quem mexe em qual arquivo."},
            ],
            "exercise": {
                "id": "08-07-ex1", "title": "Resolva o conflito",
                "statement": "O texto abaixo está em conflito. Escreva na variável `resolvido` o **texto final**, sem nenhum marcador (`<<<<<<<`, `=======`, `>>>>>>>`). Ele deve conter tanto a palavra **Bem-vindo** quanto o nome **Ana**. Imprima o resultado.",
                "starter_code": '''conflito = """<<<<<<< HEAD
Titulo: Bem-vindo ao site
=======
Titulo: Site da Ana
>>>>>>> feature/texto-da-ana"""

# Escreva aqui o texto final, sem marcadores.
# Ele deve ter 'Bem-vindo' e 'Ana'.
resolvido = ""

print(resolvido)''',
                "tests": [
                    {"validation": "output_not_contains", "value": "<<<<<<<"},
                    {"validation": "output_not_contains", "value": "======="},
                    {"validation": "output_not_contains", "value": ">>>>>>>"},
                    {"validation": "output_contains_all", "expected": ["Bem-vindo", "Ana"]},
                ],
                "hint": 'resolvido = "Titulo: Bem-vindo ao site da Ana"  (uma linha só, misturando as duas versões e sem os marcadores).',
            },
        },
    ],
    "summary": [
        "Conflito acontece quando duas branches mudam a mesma parte do mesmo arquivo.",
        "O Git marca as duas versões com <<<<<<<, ======= e >>>>>>>.",
        "Para resolver: edite o arquivo, apague os marcadores, git add e git commit.",
        "Com git merge --abort você desiste e volta ao estado anterior.",
    ],
}


# ============================================================================
# 08-08 — .gitignore e README
# ============================================================================
LESSON_08_08 = {
    "id": "08-08", "module_id": "08",
    "title": ".gitignore e README: o que esconder e como se apresentar",
    "objectives": [
        "Entender por que alguns arquivos nunca devem ir para o GitHub",
        "Criar e usar um .gitignore",
        "Escrever um README.md claro com Markdown básico",
        "Evitar o erro de publicar senhas e chaves",
    ],
    "reading_time_minutes": 16,
    "topics": [
        {
            "id": "t1",
            "title": "Por que ignorar arquivos",
            "content": [
                {"type": "text", "value": "Quando você faz `git add .`, o Git coloca **tudo** na caixa. Mas nem tudo deve ser guardado. Pense em uma **mala de viagem**: você leva roupas e documentos, mas não leva a caixa do eletrodoméstico nem o lixo do quarto."},
                {"type": "text", "value": "Existem **três tipos** de arquivos que ficam de fora: os **secretos** (senhas e chaves), os **pesados e recriáveis** (como a pasta `node_modules`, que qualquer um baixa de novo) e os **lixos do sistema** (como `.DS_Store` do Mac e a pasta `__pycache__` do Python)."},
                {"type": "text", "value": "O arquivo `.gitignore` é uma **lista de arquivos e pastas que o Git deve fingir que não existem**. Você escreve os nomes, e o Git para de sugerir e de guardar esses itens."},
                {"type": "text", "value": "**Erro grave, e muito comum:** subir o arquivo `.env` (onde ficam senhas de banco de dados, chaves de API e tokens) para um repositório **público**. Robôs varrem o GitHub o tempo todo atrás dessas chaves e as usam em minutos. E **apagar depois não resolve**, porque o histórico guarda tudo. Se acontecer, troque a chave imediatamente."},
                {"type": "text", "value": "É por isso que **o `.gitignore` é o primeiro arquivo que você cria** em um projeto, antes mesmo do primeiro commit."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Criando o seu .gitignore",
            "content": [
                {"type": "text", "value": "Crie um arquivo chamado exatamente `.gitignore` (com o ponto na frente, sem extensão) na **raiz do projeto**, ou seja, na pasta principal. Dentro dele, uma regra por linha."},
                {
                    "type": "code",
                    "caption": ".gitignore para um projeto com Python e JavaScript",
                    "value": r"""# Linhas que começam com # são comentários

# Segredos: NUNCA vão para o GitHub
.env
*.pem

# Python: cache e ambiente virtual
__pycache__/
*.pyc
venv/
.venv/

# JavaScript: bibliotecas baixadas (qualquer um baixa de novo)
node_modules/

# Lixo dos sistemas operacionais e editores
.DS_Store
Thumbs.db
.vscode/

# Arquivos de log
*.log""",
                },
                {"type": "text", "value": "**Como ler as regras:** um nome simples (`.env`) ignora aquele arquivo. Uma barra no fim (`venv/`) ignora a **pasta inteira**. O asterisco (`*.log`) funciona como **coringa**: ignora qualquer arquivo que termine com `.log`."},
                {"type": "text", "value": "**Erro comum:** criar o `.gitignore` **depois** de já ter feito commit de um arquivo. O Git continua acompanhando arquivos que ele já conhece. Para 'esquecer' um deles, use `git rm --cached .env` e faça um novo commit. Mas lembre-se: o histórico antigo ainda guarda o conteúdo."},
                {"type": "text", "value": "**Dica profissional:** ao criar um repositório novo no GitHub, existe a opção **Add .gitignore**, com modelos prontos para Python, Node e outras linguagens. Vale usar. Você também pode ter um arquivo `.env.example` (com nomes de variáveis e valores falsos) para mostrar aos outros o que precisa configurar."},
            ],
            "exercise": {
                "id": "08-08-ex1", "title": "Seu primeiro .gitignore",
                "statement": "Imprima o conteúdo de um `.gitignore` que ignore: o arquivo `.env`, a pasta `node_modules/` e a pasta `__pycache__/`. Use uma regra por linha.",
                "starter_code": '''# Escreva as 3 regras, uma por linha, dentro das aspas triplas
gitignore = """
"""
print(gitignore)''',
                "tests": [
                    {"validation": "output_contains_all", "expected": [".env", "node_modules/", "__pycache__/"]},
                ],
                "hint": "Cada regra é só o nome, em uma linha: .env  depois node_modules/  depois __pycache__/ . As barras no fim indicam pasta.",
            },
        },
        {
            "id": "t3",
            "title": "README: a vitrine do seu projeto",
            "content": [
                {"type": "text", "value": "O **README** é a **primeira coisa** que alguém vê quando abre seu repositório no GitHub. Pense na **vitrine de uma loja**: se estiver vazia ou bagunçada, a pessoa nem entra."},
                {"type": "text", "value": "Ele é um arquivo chamado `README.md`. O `.md` significa **Markdown**, um jeito simples de formatar texto usando símbolos. O GitHub transforma esses símbolos em títulos, listas e código bonitos."},
                {
                    "type": "code",
                    "caption": "Markdown básico",
                    "value": r"""# Título grande (um #)
## Subtítulo (dois ##)

Texto normal. Palavras em **negrito** e em *itálico*.

- Item de lista
- Outro item

1. Passo um
2. Passo dois

`código pequeno no meio do texto`

```
bloco de código
com várias linhas
```

[texto do link](https://github.com)""",
                },
                {"type": "text", "value": "Um bom README responde **cinco perguntas**: o que é o projeto, como ele parece, quais tecnologias usa, como rodar e quem fez. Veja um modelo."},
                {
                    "type": "code",
                    "caption": "Modelo de README",
                    "value": r"""# Meu Site Pessoal

Site de apresentação feito para praticar HTML, CSS e JavaScript.

## Demonstração
https://seu-usuario.github.io/meu-site/

## Tecnologias
- HTML
- CSS
- JavaScript

## Como rodar
1. Baixe o projeto: `git clone https://github.com/seu-usuario/meu-site.git`
2. Abra o arquivo `index.html` no navegador

## Autor
Seu Nome - https://github.com/seu-usuario""",
                },
                {"type": "text", "value": "**Erro comum:** deixar o repositório sem README, ou com aquele texto padrão. Quem avalia seu perfil (como um recrutador) abre o projeto por 10 segundos: se não entender do que se trata, sai."},
                {"type": "text", "value": "**Dica profissional:** adicione um **print da tela** ou um GIF do projeto funcionando no README. Um projeto que se mostra vale mais que mil palavras."},
            ],
            "exercise": None,
        },
    ],
    "summary": [
        "O .gitignore lista o que o Git deve ignorar: segredos, pastas pesadas e lixo do sistema.",
        "Nunca suba .env, chaves ou senhas; apagar depois não resolve, o histórico guarda tudo.",
        "Pasta termina com barra (venv/) e o asterisco é coringa (*.log).",
        "O README.md é a vitrine do projeto: o que é, tecnologias, como rodar e quem fez.",
    ],
}


# ============================================================================
# 08-09 — GitHub Pages
# ============================================================================
LESSON_08_09 = {
    "id": "08-09", "module_id": "08",
    "title": "GitHub Pages: seu site no ar de graça (com animação GSAP)",
    "objectives": [
        "Entender o que o GitHub Pages hospeda e o que não hospeda",
        "Montar um site simples com uma animação de entrada usando GSAP",
        "Publicar o site com o GitHub Pages",
        "Resolver os problemas mais comuns (404, arquivo não carrega)",
    ],
    "reading_time_minutes": 18,
    "topics": [
        {
            "id": "t1",
            "title": "O que é o GitHub Pages",
            "content": [
                {"type": "text", "value": "Até agora seu código está no GitHub, mas ele só **aparece como texto**. Para outras pessoas **abrirem seu site como uma página de verdade**, ele precisa estar hospedado em um servidor. O GitHub oferece isso **de graça**, com o nome de **GitHub Pages**."},
                {"type": "text", "value": "Pense em uma **vitrine na rua**. Sua loja (o repositório) fica guardada no depósito. O GitHub Pages **coloca uma vitrine na calçada**, e qualquer pessoa do mundo pode olhar pelo endereço `https://seu-usuario.github.io/nome-do-repo/`."},
                {"type": "text", "value": "Mas atenção: o Pages hospeda **sites estáticos**, aqueles feitos só de HTML, CSS e JavaScript, que aparecem iguais para todo mundo. Ele **não roda Python**. Um backend em FastAPI, por exemplo, precisa de outro tipo de hospedagem, e isso você vai ver no módulo de Deploy."},
                {"type": "text", "value": "**Aviso:** neste módulo você ainda não estudou HTML, CSS nem JavaScript. Então, nesta lição, você vai **copiar o site pronto** e entender o essencial. **Cada parte dele será explicada com calma nos módulos seguintes.** O objetivo aqui é você ver o seu trabalho **no ar**, do jeito que o Git ensinou."},
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Um site simples com animação (GSAP)",
            "content": [
                {"type": "text", "value": "Vamos criar um site de **3 arquivos**: `index.html` (o conteúdo), `style.css` (a aparência) e `script.js` (o comportamento). Crie uma pasta `meu-site`, rode `git init` dentro dela e crie estes arquivos."},
                {
                    "type": "code",
                    "caption": "index.html",
                    "value": r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Primeiro Site</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main class="pagina">
        <h1 class="titulo">Olá, eu sou a Ana</h1>
        <p class="subtitulo">Estou aprendendo a programar e este site está no ar.</p>
        <a class="botao" href="https://github.com">Ver meu GitHub</a>
    </main>

    <!-- 1) PRIMEIRO a biblioteca GSAP (baixada da internet) -->
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
    <!-- 2) DEPOIS o seu código, que usa o GSAP -->
    <script src="script.js"></script>
</body>
</html>""",
                },
                {
                    "type": "code",
                    "caption": "style.css",
                    "value": r"""/* Deixa tudo centralizado na tela, com fundo escuro */
body {
    margin: 0;
    min-height: 100vh;
    display: grid;
    place-items: center;
    background: #0a0a0b;
    color: #fafafa;
    font-family: system-ui, sans-serif;
    text-align: center;
}

.botao {
    display: inline-block;
    margin-top: 16px;
    padding: 12px 24px;
    background: #f59e0b;
    color: #0a0a0b;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
}""",
                },
                {"type": "text", "value": "Agora a animação. Você pode até animar só com CSS, e isso funciona bem para coisas simples. Mas o **GSAP** é uma biblioteca feita para animar com **mais controle**: dá para encadear vários movimentos, um depois do outro, e ajustar o tempo de cada um. É a biblioteca que muitos sites premium usam."},
                {"type": "text", "value": "A ideia principal é o `gsap.from`. Ele funciona assim: 'anime este elemento **vindo DESTE estado até o estado normal dele**'. Ou seja, você descreve **de onde ele vem**, e o GSAP cuida do caminho."},
                {
                    "type": "code",
                    "caption": "script.js — a animação de entrada",
                    "value": r"""// Uma linha do tempo (timeline) organiza várias animações em sequência.
// 'defaults' vale para todas: cada uma dura 0.7s e desacelera no final.
const linha = gsap.timeline({
    defaults: { duration: 0.7, ease: "power2.out" }
});

linha
    // O título começa invisível (opacity: 0) e 40px mais para baixo (y: 40)
    // e sobe até a posição normal dele.
    .from(".titulo", { opacity: 0, y: 40 })

    // O subtítulo entra logo depois. O "-=0.4" significa
    // 'comece 0.4 segundo ANTES da animação anterior terminar'.
    .from(".subtitulo", { opacity: 0, y: 30 }, "-=0.4")

    // O botão 'cresce' a partir de 80% do tamanho
    .from(".botao", { opacity: 0, scale: 0.8 }, "-=0.3");""",
                },
                {"type": "text", "value": "**Por que uma timeline?** Sem ela, você teria que calcular o atraso de cada animação na mão ('esta espera 0.3s, aquela 0.6s'). Com a timeline, cada animação **espera a anterior**. Se você mudar a duração de uma, o resto se ajusta sozinho."},
                {"type": "text", "value": "**Erro comum:** colocar o `<script src=\"script.js\">` **antes** do script do GSAP. Aí o navegador tenta usar o `gsap` antes de ele existir, e o console mostra **'gsap is not defined'**. A ordem importa: primeiro a biblioteca, depois o seu código."},
                {"type": "text", "value": "**Dica profissional:** algumas pessoas se sentem mal com movimento na tela. Um site bem feito respeita quem configurou o computador para **reduzir animações**. Você aprenderá a checar isso no módulo de JavaScript. Como regra geral, a animação deve **ajudar a entender** a página, não ser só enfeite."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "Publicando no GitHub Pages",
            "content": [
                {"type": "text", "value": "Com os 3 arquivos prontos, o caminho é o que você já conhece: **commit** e **push**. Depois, é só ligar o Pages em uma tela do GitHub."},
                {
                    "type": "code",
                    "caption": "No terminal (dentro da pasta meu-site)",
                    "value": r"""git add .
git commit -m "Cria site inicial com animação GSAP"

git branch -M main
git remote add origin https://github.com/seu-usuario/meu-site.git
git push -u origin main""",
                },
                {
                    "type": "code",
                    "caption": "No site do GitHub",
                    "value": r"""1. Abra o repositório 'meu-site' no GitHub.
2. Clique na aba 'Settings' (Configurações).
3. No menu da esquerda, clique em 'Pages'.
4. Em 'Build and deployment', em 'Source', escolha 'Deploy from a branch'.
5. Em 'Branch', escolha 'main' e a pasta '/ (root)'. Clique em 'Save'.
6. Espere de 1 a 3 minutos e atualize a página.
7. Aparece o endereço do seu site:
   https://seu-usuario.github.io/meu-site/""",
                },
                {"type": "text", "value": "Pronto: **seu site está no ar**, e qualquer pessoa pode abrir esse endereço. A partir de agora, sempre que você fizer `git push`, o site se atualiza sozinho em poucos minutos."},
                {"type": "text", "value": "**Problemas comuns:**"},
                {"type": "text", "value": "**Erro 404:** o arquivo principal precisa se chamar **`index.html`** (tudo minúsculo) e ficar na **raiz** do repositório, não dentro de uma subpasta."},
                {"type": "text", "value": "**Estilo ou animação não aparece:** o GitHub Pages diferencia **maiúsculas de minúsculas**. Se o arquivo se chama `Style.css` e o HTML pede `style.css`, ele não é encontrado. No seu computador pode funcionar, e no ar não."},
                {"type": "text", "value": "**Mudou o código e o site continua igual:** o navegador guardou a versão antiga. Aperte **Ctrl + F5** (ou Command + Shift + R no Mac) para recarregar do zero."},
                {"type": "text", "value": "**Dica profissional:** coloque o endereço do site no **README** e no campo 'About' do repositório (o ícone de engrenagem ao lado). Assim, quem chegar no projeto clica e vê funcionando."},
            ],
            "exercise": {
                "id": "08-09-ex1", "title": "O endereço do seu site",
                "statement": "O GitHub Pages usa o endereço `https://USUARIO.github.io/REPOSITORIO/`. Use f-string para montar e imprimir o endereço a partir das variáveis `usuario` e `repositorio`.",
                "starter_code": '''usuario = "ana"
repositorio = "meu-site"

# Monte o endereço com uma f-string e imprima
url = ""
print(url)''',
                "tests": [
                    {"validation": "output_equals", "expected": "https://ana.github.io/meu-site/"},
                ],
                "hint": 'url = f"https://{usuario}.github.io/{repositorio}/"  — repare na barra final.',
            },
        },
    ],
    "summary": [
        "O GitHub Pages hospeda sites estáticos (HTML, CSS, JS) de graça; ele não roda Python.",
        "GSAP anima com controle: gsap.from descreve de onde o elemento vem; timeline encadeia animações.",
        "O script do GSAP vem ANTES do seu script.js, senão aparece 'gsap is not defined'.",
        "Publicar: push, Settings, Pages, branch main, pasta root. O endereço é usuario.github.io/repositorio.",
    ],
}


# ============================================================================
# 08-10 — Boas práticas de commit
# ============================================================================
LESSON_08_10 = {
    "id": "08-10", "module_id": "08",
    "title": "Boas práticas de commit e a rotina do dia a dia",
    "objectives": [
        "Fazer commits pequenos e com um único assunto",
        "Escrever mensagens claras com prefixos padrão",
        "Seguir uma rotina segura de trabalho com Git",
        "Evitar os erros que mais causam dor de cabeça",
    ],
    "reading_time_minutes": 14,
    "topics": [
        {
            "id": "t1",
            "title": "Um commit conta uma história",
            "content": [
                {"type": "text", "value": "Você já sabe **como** fazer um commit. Agora vem a parte que separa quem só usa Git de quem usa bem: **quando** e **como** fazer."},
                {"type": "text", "value": "O histórico do Git é como o **diário do projeto**. Quando ele é bem escrito, você lê e entende o que aconteceu. Quando é mal escrito ('arrumei', 'mudanças', 'asdf'), ele não serve para nada, nem para você mesmo daqui a dois meses."},
                {"type": "text", "value": "**A regra principal:** cada commit deve ter **um assunto só**. Corrigiu um erro e também mudou a cor do botão? São **dois commits**. Assim, se um dos dois der problema, você desfaz só ele."},
                {
                    "type": "code",
                    "caption": "Diário ruim x diário bom",
                    "value": r"""RUIM (não diz nada, mistura assuntos):
    a1b2c3d arrumei
    b2c3d4e mudanças
    c3d4e5f atualizações do site, botão, texto e login

BOM (cada linha conta uma coisa):
    a1b2c3d Corrige erro de digitação no título
    b2c3d4e Adiciona botão de contato no cabeçalho
    c3d4e5f Muda a cor do fundo para escuro""",
                },
            ],
            "exercise": None,
        },
        {
            "id": "t2",
            "title": "Como escrever a mensagem",
            "content": [
                {"type": "text", "value": "Uma boa mensagem responde: **o que este commit faz?** Ela é curta, específica e começa com um verbo. Um truque é completar a frase: 'Se eu aplicar este commit, ele... **[sua mensagem]**'."},
                {"type": "text", "value": "Muitos times também usam **prefixos** para classificar cada commit. É um padrão simples que ajuda a bater o olho e entender o tipo de mudança."},
                {
                    "type": "code",
                    "caption": "Prefixos mais usados",
                    "value": r"""feat:      uma funcionalidade nova
fix:       a correção de um erro
docs:      mudança só na documentação (README, comentários)
style:     ajuste de formatação, sem mudar o comportamento
refactor:  reorganização do código, sem mudar o resultado
chore:     tarefas de manutenção (configurações, dependências)

# Exemplos completos
git commit -m "feat: adiciona botão de contato"
git commit -m "fix: corrige o título que estava cortado no celular"
git commit -m "docs: explica como rodar o projeto no README"

# Para mensagens que precisam de mais explicação,
# use um segundo -m (vira a descrição do commit)
git commit -m "fix: corrige o cálculo do desconto" -m "O valor era arredondado antes da soma, gerando centavos a mais."
""",
                },
                {"type": "text", "value": "**Regras rápidas:** primeira linha com até uns **50 caracteres**, sem ponto final, começando com **verbo** (adiciona, corrige, remove). Se ficou grande demais, provavelmente o commit está fazendo coisa demais."},
                {"type": "text", "value": "**Erro comum:** mensagens como 'ajustes' e 'update'. Parecem uma economia de tempo, mas você paga com juros quando precisar descobrir **onde** um erro apareceu."},
            ],
            "exercise": None,
        },
        {
            "id": "t3",
            "title": "A rotina do dia a dia",
            "content": [
                {"type": "text", "value": "Para terminar, um roteiro que você pode seguir **em todo projeto**. Com o tempo, ele vira automático, como escovar os dentes."},
                {
                    "type": "code",
                    "caption": "Rotina segura de trabalho",
                    "value": r"""# 1. Comece o dia com a main atualizada
git switch main
git pull

# 2. Crie uma branch para a tarefa
git switch -c feature/nome-da-tarefa

# 3. Trabalhe. A cada pedaço pronto, olhe o que mudou ANTES de salvar
git status          # quais arquivos mudaram?
git diff            # o que mudou dentro deles? (q para sair)

# 4. Salve o ponto
git add .
git commit -m "feat: descreve o que você fez"

# 5. Envie a branch e abra o Pull Request no GitHub
git push -u origin feature/nome-da-tarefa

# 6. Depois do merge: volte para a main e atualize
git switch main
git pull""",
                },
                {"type": "text", "value": "O `git diff` mostra, linha por linha, o que você mudou (as linhas com **+** foram adicionadas e com **-** foram removidas). Passar o olho nele antes de cada commit evita subir por engano um teste, uma senha ou um código pela metade."},
                {"type": "text", "value": "**Erros que mais causam dor de cabeça:**"},
                {"type": "text", "value": "**1. `git add .` sem olhar.** Você pode incluir arquivos que não queria. Rode `git status` antes."},
                {"type": "text", "value": "**2. Commitar código quebrado.** Cada ponto salvo deve funcionar. Teste antes de salvar."},
                {"type": "text", "value": "**3. Usar `git push --force` sem entender.** Ele **sobrescreve** o que está no GitHub e pode apagar o trabalho dos outros. Como iniciante, nunca use."},
                {"type": "text", "value": "**4. Trabalhar direto na main.** Sempre crie uma branch, mesmo em projeto pessoal. É um hábito que o mercado espera."},
                {"type": "text", "value": "**Dica profissional:** faça commits **com frequência**. Um commit pequeno a cada pedaço pronto é melhor que um commit gigante no fim do dia. E lembre: o commit só protege o seu trabalho **de verdade** depois do `git push`, que guarda uma cópia no GitHub."},
            ],
            "exercise": {
                "id": "08-10-ex1", "title": "Uma boa mensagem de commit",
                "statement": "Escreva, com `print()`, um comando de commit com **mensagem clara e com prefixo** (`feat:`, `fix:`, `docs:`, `style:`, `refactor:` ou `chore:`). Exemplo de formato: `git commit -m \"feat: adiciona botão de contato\"`. Use uma mensagem sua.",
                "starter_code": '''# Imprima um comando 'git commit -m' com mensagem que comece
# com um prefixo (feat:, fix:, docs:...) e um verbo.
''',
                "tests": [
                    {"validation": "output_contains_all", "expected": ["git commit -m"]},
                    {"validation": "output_contains_any", "expected": ["feat:", "fix:", "docs:", "style:", "refactor:", "chore:"]},
                ],
                "hint": 'print(\'git commit -m "fix: corrige o título da página"\') — troque a mensagem pela sua, mantendo o prefixo e o verbo.',
            },
        },
    ],
    "summary": [
        "Um commit deve ter um assunto só e contar uma parte da história do projeto.",
        "Mensagem boa: curta, começa com verbo, e usa prefixo (feat:, fix:, docs:...).",
        "Rotina: pull, branch, trabalhar, status e diff, commit, push, Pull Request.",
        "Evite git add . sem olhar, código quebrado no commit, push --force e trabalhar direto na main.",
    ],
}


# ============================================================================
# AGREGADOR — dicionário com todas as lições do módulo 08
# ============================================================================
MODULE_08_LESSONS = {
    "08-01": LESSON_08_01,
    "08-02": LESSON_08_02,
    "08-03": LESSON_08_03,
    "08-04": LESSON_08_04,
    "08-05": LESSON_08_05,
    "08-06": LESSON_08_06,
    "08-07": LESSON_08_07,
    "08-08": LESSON_08_08,
    "08-09": LESSON_08_09,
    "08-10": LESSON_08_10,
}
