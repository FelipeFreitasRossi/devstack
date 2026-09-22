from datetime import datetime, timedelta
from app.database import (
    progress_collection,
    achievements_collection,
    daily_activity_collection,
)

# ============================================================================
# MODO DA PLATAFORMA
# ============================================================================
# True  → todos os módulos ficam desbloqueados (útil para desenvolver/testar)
# False → modo trilha: só desbloqueia o próximo módulo quando TODAS as lições
#         do módulo anterior forem concluídas (exercício resolvido)
# ============================================================================
FREE_MODE = False

CURRICULUM = [
    {
        "id": "01",
        "title": "Lógica de Programação",
        "description": "O básico antes de programar: pensar como um dev",
        "duration_hours": 8,
        "lessons": [
            {"id": "01-01", "title": "Fundamentos da Programação", "reading_time_minutes": 34, "has_exercise": True},
            {"id": "01-03", "title": "Variáveis e Constantes", "reading_time_minutes": 18, "has_exercise": True},
            {"id": "01-04", "title": "Tipos de Dados", "reading_time_minutes": 16, "has_exercise": True},
            {"id": "01-05", "title": "Operadores Aritméticos", "reading_time_minutes": 14, "has_exercise": True},
            {"id": "01-06", "title": "Operadores Lógicos e Relacionais", "reading_time_minutes": 14, "has_exercise": True},
            {"id": "01-07", "title": "Estruturas Condicionais (if/else)", "reading_time_minutes": 16, "has_exercise": True},
            {"id": "01-08", "title": "Estruturas de Repetição (for/while)", "reading_time_minutes": 18, "has_exercise": True},
            {"id": "01-09", "title": "Listas", "reading_time_minutes": 16, "has_exercise": True},
            {"id": "01-10", "title": "Dicionários", "reading_time_minutes": 16, "has_exercise": True},
            {"id": "01-11", "title": "Funções", "reading_time_minutes": 18, "has_exercise": True},
            {"id": "01-12", "title": "Projeto: Calculadora", "reading_time_minutes": 20, "has_exercise": True},
        ],
    },
    {
        "id": "02",
        "title": "Python Fundamentos",
        "description": "Sintaxe, entrada/saída e estruturas básicas",
        "duration_hours": 10,
        "lessons": [
            {"id": "02-01", "title": "Instalando Python e o VS Code", "reading_time_minutes": 14, "has_exercise": True},
            {"id": "02-02", "title": "Primeiro programa: print()", "reading_time_minutes": 12, "has_exercise": True},
            {"id": "02-03", "title": "Variáveis e Tipos em Python", "reading_time_minutes": 12, "has_exercise": True},
            {"id": "02-04", "title": "Entrada de dados: input()", "reading_time_minutes": 10, "has_exercise": True},
            {"id": "02-05", "title": "Conversão de Tipos", "reading_time_minutes": 12, "has_exercise": True},
            {"id": "02-06", "title": "Strings: Métodos Principais", "reading_time_minutes": 14, "has_exercise": True},
            {"id": "02-07", "title": "Listas, Tuplas e Sets", "reading_time_minutes": 16, "has_exercise": True},
            {"id": "02-08", "title": "Dicionários em Python", "reading_time_minutes": 12, "has_exercise": True},
            {"id": "02-09", "title": "Condicionais em Python", "reading_time_minutes": 14, "has_exercise": True},
            {"id": "02-10", "title": "Loops em Python", "reading_time_minutes": 14, "has_exercise": True},
            {"id": "02-11", "title": "Projeto: Sistema de Cadastro", "reading_time_minutes": 25, "has_exercise": True},
        ],
    },
    {
        "id": "03",
        "title": "Python Intermediário",
        "description": "Funções avançadas, POO, módulos e arquivos",
        "duration_hours": 12,
        "lessons": [
            {"id": "03-01", "title": "Funções com Parâmetros e Retorno", "reading_time_minutes": 14, "has_exercise": True},
            {"id": "03-02", "title": "Argumentos Opcionais e Nomeados", "reading_time_minutes": 12, "has_exercise": True},
            {"id": "03-03", "title": "*args e **kwargs", "reading_time_minutes": 12, "has_exercise": True},
            {"id": "03-04", "title": "Funções Lambda", "reading_time_minutes": 10, "has_exercise": True},
            {"id": "03-05", "title": "List Comprehensions", "reading_time_minutes": 14, "has_exercise": True},
            {"id": "03-06", "title": "Tratamento de Erros (try/except)", "reading_time_minutes": 15, "has_exercise": True},
            {"id": "03-07", "title": "Módulos, Pacotes e pip", "reading_time_minutes": 12, "has_exercise": True},
            {"id": "03-08", "title": "Ambientes Virtuais (venv)", "reading_time_minutes": 10, "has_exercise": False},
            {"id": "03-09", "title": "Manipulação de Arquivos e JSON", "reading_time_minutes": 15, "has_exercise": True},
            {"id": "03-10", "title": "Programação Orientada a Objetos (POO)", "reading_time_minutes": 18, "has_exercise": True},
        ],
    },
    {
        "id": "04",
        "title": "Python para Desenvolvimento",
        "description": "HTTP, APIs, autenticação e banco de dados",
        "duration_hours": 8,
        "lessons": [
            {"id": "04-01", "title": "HTTP e APIs REST", "reading_time_minutes": 12, "has_exercise": False},
            {"id": "04-02", "title": "Biblioteca requests", "reading_time_minutes": 14, "has_exercise": True},
            {"id": "04-03", "title": "Trabalhando com JSON", "reading_time_minutes": 12, "has_exercise": True},
            {"id": "04-04", "title": "Autenticação básica", "reading_time_minutes": 12, "has_exercise": True},
            {"id": "04-05", "title": "Variáveis de ambiente", "reading_time_minutes": 10, "has_exercise": False},
            {"id": "04-06", "title": "Introdução a banco de dados", "reading_time_minutes": 14, "has_exercise": False},
            {"id": "04-07", "title": "CRUD — Create, Read, Update, Delete", "reading_time_minutes": 16, "has_exercise": True},
        ],
    },
    {
        "id": "05",
        "title": "FastAPI",
        "description": "Criando APIs profissionais com Python",
        "duration_hours": 10,
        "lessons": [
            {"id": "05-01", "title": "Introdução ao FastAPI", "reading_time_minutes": 12, "has_exercise": False},
            {"id": "05-02", "title": "Rotas GET e POST", "reading_time_minutes": 14, "has_exercise": True},
            {"id": "05-03", "title": "Rotas PUT e DELETE", "reading_time_minutes": 12, "has_exercise": True},
            {"id": "05-04", "title": "Validação com Pydantic", "reading_time_minutes": 14, "has_exercise": True},
            {"id": "05-05", "title": "Middleware e CORS", "reading_time_minutes": 12, "has_exercise": False},
            {"id": "05-06", "title": "Autenticação com JWT", "reading_time_minutes": 18, "has_exercise": True},
            {"id": "05-07", "title": "Integração com banco de dados", "reading_time_minutes": 16, "has_exercise": True},
            {"id": "05-08", "title": "Documentação automática (Swagger)", "reading_time_minutes": 10, "has_exercise": False},
        ],
    },
    {
        "id": "08",
        "title": "Git e GitHub",
        "description": "Salve, versione e publique seus projetos",
        "duration_hours": 3,
        "lessons": [
            {"id": "08-01", "title": "Git e GitHub: o que são e por que usar", "reading_time_minutes": 14, "has_exercise": True},
            {"id": "08-02", "title": "Terminal sem medo e configurando o Git", "reading_time_minutes": 16, "has_exercise": True},
            {"id": "08-03", "title": "Seu primeiro repositório", "reading_time_minutes": 18, "has_exercise": True},
            {"id": "08-04", "title": "Conectando ao GitHub", "reading_time_minutes": 18, "has_exercise": True},
            {"id": "08-05", "title": "Branches", "reading_time_minutes": 18, "has_exercise": True},
            {"id": "08-06", "title": "Pull Requests", "reading_time_minutes": 16, "has_exercise": True},
            {"id": "08-07", "title": "Resolvendo conflitos", "reading_time_minutes": 16, "has_exercise": True},
            {"id": "08-08", "title": ".gitignore e README", "reading_time_minutes": 16, "has_exercise": True},
            {"id": "08-09", "title": "GitHub Pages", "reading_time_minutes": 18, "has_exercise": True},
            {"id": "08-10", "title": "Boas práticas de commit", "reading_time_minutes": 14, "has_exercise": True},
        ],
    },
    # ======================================================================
    # CONTEÚDO ESTACIONADO (fora do curso ativo)
    # ----------------------------------------------------------------------
    # Os módulos 06 (HTML + CSS), 07 (JavaScript) e 12 (Deploy) abaixo estão
    # COMENTADOS de propósito. Nada foi apagado: os arquivos
    # lessons_module_06.py e lessons_module_07.py continuam na pasta
    # lessons_content/, só não estão sendo usados.
    #
    # Como REATIVAR um módulo:
    #   1. Aqui no analytics.py: selecione TODAS as linhas do bloco do módulo
    #      (de '# {' até '# },') e aperte Ctrl + / (VS Code) para tirar os #.
    #   2. No lessons_content/__init__.py: faça o mesmo com o import do módulo
    #      e com as linhas dele no dicionário LESSONS.
    #   3. Reinicie o servidor.
    #
    # A ORDEM dos blocos nesta lista é a ordem que o aluno vê. Se reativar o
    # 06 e o 07, eles aparecem logo depois do 08 (Git e GitHub).
    # ======================================================================
    # --- [ESTACIONADO] Módulo 06 — HTML + CSS -----------------------------
    # {
    #     "id": "06",
    #     "title": "HTML + CSS",
    #     "description": "Estrutura e estilo das páginas web",
    #     "duration_hours": 14,
    #     "lessons": [
    #         {"id": "06-01", "title": "Estrutura HTML", "reading_time_minutes": 12, "has_exercise": True},
    #         {"id": "06-02", "title": "Tags principais e textos", "reading_time_minutes": 12, "has_exercise": True},
    #         {"id": "06-03", "title": "Links, imagens e listas", "reading_time_minutes": 12, "has_exercise": True},
    #         {"id": "06-04", "title": "Tabelas e formulários", "reading_time_minutes": 14, "has_exercise": True},
    #         {"id": "06-05", "title": "HTML semântico", "reading_time_minutes": 12, "has_exercise": True},
    #         {"id": "06-06", "title": "Acessibilidade", "reading_time_minutes": 10, "has_exercise": False},
    #         {"id": "06-07", "title": "CSS: seletores e box model", "reading_time_minutes": 14, "has_exercise": True},
    #         {"id": "06-08", "title": "Flexbox", "reading_time_minutes": 16, "has_exercise": True},
    #         {"id": "06-09", "title": "Grid", "reading_time_minutes": 16, "has_exercise": True},
    #         {"id": "06-10", "title": "Cores, tipografia e sombras", "reading_time_minutes": 12, "has_exercise": True},
    #         {"id": "06-11", "title": "Gradientes e transições", "reading_time_minutes": 12, "has_exercise": True},
    #         {"id": "06-12", "title": "Animações CSS", "reading_time_minutes": 14, "has_exercise": True},
    #         {"id": "06-13", "title": "Responsividade e media queries", "reading_time_minutes": 16, "has_exercise": True},
    #         {"id": "06-14", "title": "Projeto: Landing Page", "reading_time_minutes": 30, "has_exercise": True},
    #     ],
    # },
    # --- [ESTACIONADO] Módulo 07 — JavaScript -----------------------------
    # {
    #     "id": "07",
    #     "title": "JavaScript",
    #     "description": "A linguagem da web, do básico ao assíncrono",
    #     "duration_hours": 16,
    #     "lessons": [
    #         {"id": "07-01", "title": "Variáveis e tipos", "reading_time_minutes": 12, "has_exercise": True},
    #         {"id": "07-02", "title": "Operadores e condicionais", "reading_time_minutes": 12, "has_exercise": True},
    #         {"id": "07-03", "title": "Loops", "reading_time_minutes": 12, "has_exercise": True},
    #         {"id": "07-04", "title": "Funções", "reading_time_minutes": 14, "has_exercise": True},
    #         {"id": "07-05", "title": "Arrays e objetos", "reading_time_minutes": 14, "has_exercise": True},
    #         {"id": "07-06", "title": "DOM — manipulando elementos", "reading_time_minutes": 16, "has_exercise": True},
    #         {"id": "07-07", "title": "Eventos e addEventListener", "reading_time_minutes": 14, "has_exercise": True},
    #         {"id": "07-08", "title": "Formulários e validação", "reading_time_minutes": 14, "has_exercise": True},
    #         {"id": "07-09", "title": "ES6+ — Arrow functions, destructuring, spread", "reading_time_minutes": 16, "has_exercise": True},
    #         {"id": "07-10", "title": "map, filter, reduce, find", "reading_time_minutes": 16, "has_exercise": True},
    #         {"id": "07-11", "title": "Promises e async/await", "reading_time_minutes": 18, "has_exercise": True},
    #         {"id": "07-12", "title": "fetch e consumo de APIs", "reading_time_minutes": 16, "has_exercise": True},
    #         {"id": "07-13", "title": "LocalStorage e SessionStorage", "reading_time_minutes": 12, "has_exercise": True},
    #         {"id": "07-14", "title": "Projeto: To-do List", "reading_time_minutes": 30, "has_exercise": True},
    #     ],
    # },
    # --- [ESTACIONADO] Módulo 12 — Deploy ---------------------------------
    # Este módulo ainda não tem conteúdo escrito (falta criar o arquivo
    # lessons_module_12.py). Só reative depois que ele existir, senão as
    # lições vão aparecer na trilha, mas não vão abrir.
    # {
    #     "id": "12",
    #     "title": "Deploy",
    #     "description": "Colocando o projeto no ar gratuitamente",
    #     "duration_hours": 4,
    #     "lessons": [
    #         {"id": "12-01", "title": "Deploy do frontend (Vercel)", "reading_time_minutes": 12, "has_exercise": False},
    #         {"id": "12-02", "title": "Deploy do backend (Railway)", "reading_time_minutes": 12, "has_exercise": False},
    #         {"id": "12-03", "title": "Projeto final: landing page animada no ar", "reading_time_minutes": 30, "has_exercise": True},
    #     ],
    # },
]

ACHIEVEMENTS_CATALOG = [
    {"id": "first_lesson", "title": "Primeiro passo", "description": "Complete a primeira aula", "accent": "brand"},
    {"id": "streak_3", "title": "Streak de 3 dias", "description": "Estude 3 dias seguidos", "accent": "brand"},
    {"id": "streak_7", "title": "Semana completa", "description": "Estude 7 dias seguidos", "accent": "accent"},
    {"id": "module_complete", "title": "Módulo completo", "description": "Conclua um módulo inteiro", "accent": "accent"},
    {"id": "10_hours", "title": "Dev dedicado", "description": "Estude 10h no total", "accent": "brand"},
    {"id": "all_modules", "title": "Devstack master", "description": "Conclua todos os módulos", "accent": "accent"},
]


def calculate_streak(user_id: str) -> dict:
    activities = list(
        daily_activity_collection.find({"user_id": user_id}).sort("date", -1)
    )
    if not activities:
        return {"current_days": 0, "longest_days": 0, "last_study_date": None}

    dates = sorted({a["date"] for a in activities}, reverse=True)
    today = datetime.utcnow().date()
    yesterday = today - timedelta(days=1)

    current_streak = 0
    last_date = datetime.strptime(dates[0], "%Y-%m-%d").date()

    if last_date in (today, yesterday):
        current_streak = 1
        check_date = last_date
        for d in dates[1:]:
            parsed = datetime.strptime(d, "%Y-%m-%d").date()
            if (check_date - parsed).days == 1:
                current_streak += 1
                check_date = parsed
            else:
                break

    longest = 0
    temp = 0
    prev = None
    for d in sorted(dates):
        parsed = datetime.strptime(d, "%Y-%m-%d").date()
        if prev and (parsed - prev).days == 1:
            temp += 1
        else:
            temp = 1
        longest = max(longest, temp)
        prev = parsed

    return {
        "current_days": current_streak,
        "longest_days": longest,
        "last_study_date": dates[0],
    }


def calculate_total_hours(user_id: str) -> float:
    pipeline = [
        {"$match": {"user_id": user_id}},
        {"$group": {"_id": None, "total": {"$sum": "$minutes_studied"}}},
    ]
    result = list(daily_activity_collection.aggregate(pipeline))
    if not result:
        return 0.0
    return round(result[0]["total"] / 60, 1)


def is_lesson_accessible(user_id: str, lesson_id: str) -> bool:
    """
    Confere se o aluno pode abrir/enviar exercício desta lição agora.
    Usada pelas rotas de lições para não depender só do frontend escondendo
    o link: sem isso, dava para acessar uma lição trancada digitando a URL.
    """
    module_id = lesson_id.split("-")[0]
    for index, module in enumerate(CURRICULUM):
        if module["id"] == module_id:
            return _is_module_unlocked(user_id, index)
    return False  # lição de um módulo que nem existe no currículo


def _is_module_unlocked(user_id: str, module_index: int) -> bool:
    """
    Verifica se um módulo está desbloqueado.
    
    - MODO LIVRE (FREE_MODE=True): todos os módulos ficam desbloqueados.
    - MODO TRILHA (FREE_MODE=False): desbloqueio sequencial (só desbloqueia
      quando TODOS os módulos anteriores estiverem concluídos).
    """
    # 🚧 Modo livre — todos os módulos liberados
    if FREE_MODE:
        return True

    # Modo trilha — desbloqueio sequencial
    if module_index == 0:
        return True

    for i in range(module_index):
        previous_module = CURRICULUM[i]
        prev_total = len(previous_module["lessons"])
        prev_completed = progress_collection.count_documents({
            "user_id": user_id,
            "module_id": previous_module["id"],
            "completed": True,
        })
        if prev_completed < prev_total:
            return False

    return True


def calculate_module_progress(
    user_id: str, module: dict, module_index: int = 0
) -> dict:
    """Calcula progresso do aluno em um módulo."""
    module_id = module["id"]
    total = len(module["lessons"])

    completed = progress_collection.count_documents({
        "user_id": user_id,
        "module_id": module_id,
        "completed": True,
    })

    percent = round((completed / total) * 100) if total > 0 else 0

    unlocked = _is_module_unlocked(user_id, module_index)

    if not unlocked:
        status = "locked"
    elif completed == total:
        status = "completed"
    else:
        status = "in_progress"

    return {
        "id": module_id,
        "title": module["title"],
        "description": module["description"],
        "lessons_count": total,
        "completed_lessons": completed,
        "status": status,
        "duration_hours": module["duration_hours"],
        "progress_percent": percent,
        "unlocked": unlocked,
    }


def get_next_lesson(user_id: str) -> dict | None:
    for module_index, module in enumerate(CURRICULUM):
        if not _is_module_unlocked(user_id, module_index):
            break

        for lesson in module["lessons"]:
            done = progress_collection.find_one({
                "user_id": user_id,
                "lesson_id": lesson["id"],
                "completed": True,
            })
            if not done:
                module_progress = calculate_module_progress(
                    user_id, module, module_index
                )
                return {
                    "module_id": module["id"],
                    "module_title": module["title"],
                    "lesson_id": lesson["id"],
                    "lesson_title": lesson["title"],
                    "reading_time_minutes": lesson["reading_time_minutes"],
                    "has_exercise": lesson["has_exercise"],
                    "progress_percent": module_progress["progress_percent"],
                }
    return None


def get_weekly_goal_progress(user_id: str, goal: int = 5) -> str:
    today = datetime.utcnow().date()
    week_start = today - timedelta(days=today.weekday())

    count = progress_collection.count_documents({
        "user_id": user_id,
        "completed": True,
        "completed_at": {"$gte": datetime.combine(week_start, datetime.min.time())},
    })

    return f"{min(count, goal)}/{goal}"


def check_achievements(user_id: str) -> list[str]:
    unlocked_ids = {
        a["achievement_id"]
        for a in achievements_collection.find({"user_id": user_id})
    }

    new_unlocked = []
    total_done = progress_collection.count_documents({
        "user_id": user_id,
        "completed": True,
    })
    streak = calculate_streak(user_id)
    hours = calculate_total_hours(user_id)

    modules_complete = 0
    for index, module in enumerate(CURRICULUM):
        prog = calculate_module_progress(user_id, module, index)
        if prog["status"] == "completed":
            modules_complete += 1

    candidates = {
        "first_lesson": total_done >= 1,
        "streak_3": streak["current_days"] >= 3,
        "streak_7": streak["current_days"] >= 7,
        "module_complete": modules_complete >= 1,
        "10_hours": hours >= 10,
        "all_modules": modules_complete == len(CURRICULUM),
    }

    for achievement_id, condition in candidates.items():
        if condition and achievement_id not in unlocked_ids:
            achievements_collection.insert_one({
                "user_id": user_id,
                "achievement_id": achievement_id,
                "unlocked_at": datetime.utcnow(),
            })
            new_unlocked.append(achievement_id)

    return new_unlocked


def get_all_achievements(user_id: str) -> list[dict]:
    unlocked_ids = {
        a["achievement_id"]
        for a in achievements_collection.find({"user_id": user_id})
    }

    result = []
    for ach in ACHIEVEMENTS_CATALOG:
        result.append({
            "id": ach["id"],
            "title": ach["title"],
            "description": ach["description"],
            "accent": ach["accent"],
            "unlocked": ach["id"] in unlocked_ids,
        })
    return result


def get_all_modules_with_progress(user_id: str) -> list[dict]:
    result = []
    for index, module in enumerate(CURRICULUM):
        result.append(calculate_module_progress(user_id, module, index))
    return result


def get_weekly_activity(user_id: str) -> list[dict]:
    today = datetime.utcnow().date()
    result = []

    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        date_str = day.strftime("%Y-%m-%d")

        activity = daily_activity_collection.find_one({
            "user_id": user_id,
            "date": date_str,
        })

        result.append({
            "date": date_str,
            "weekday": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"][
                day.weekday()
            ],
            "minutes": activity["minutes_studied"] if activity else 0,
        })

    return result


def get_time_distribution(user_id: str) -> list[dict]:
    pipeline = [
        {"$match": {"user_id": user_id}},
        {
            "$group": {
                "_id": "$module_id",
                "minutes": {"$sum": "$time_spent_minutes"},
            }
        },
    ]
    result = list(progress_collection.aggregate(pipeline))
    minutes_by_module = {r["_id"]: r["minutes"] for r in result}

    distribution = []
    for module in CURRICULUM:
        minutes = minutes_by_module.get(module["id"], 0)
        if minutes > 0:
            distribution.append({
                "module_id": module["id"],
                "module_title": module["title"],
                "minutes": minutes,
            })

    distribution.sort(key=lambda x: x["minutes"], reverse=True)
    return distribution


def get_timeline(user_id: str, limit: int = 10) -> list[dict]:
    entries = list(
        progress_collection.find({
            "user_id": user_id,
            "completed": True,
        })
        .sort("completed_at", -1)
        .limit(limit)
    )

    lesson_lookup = {}
    for module in CURRICULUM:
        for lesson in module["lessons"]:
            lesson_lookup[lesson["id"]] = {
                "lesson_title": lesson["title"],
                "module_title": module["title"],
            }

    result = []
    for entry in entries:
        lesson_id = entry["lesson_id"]
        info = lesson_lookup.get(lesson_id, {})
        completed_at = entry.get("completed_at")

        result.append({
            "id": str(entry["_id"]),
            "lesson_id": lesson_id,
            "lesson_title": info.get("lesson_title", "Lição"),
            "module_title": info.get("module_title", ""),
            "date": (
                completed_at.isoformat()
                if completed_at
                else datetime.utcnow().isoformat()
            ),
        })

    return result


def get_lesson_sidebar(user_id: str, current_lesson_id: str) -> list[dict]:
    completed_lesson_ids = {
        p["lesson_id"]
        for p in progress_collection.find({"user_id": user_id, "completed": True})
    }

    sidebar = []
    for index, module in enumerate(CURRICULUM):
        module_unlocked = _is_module_unlocked(user_id, index)
        lessons_out = []

        for lesson in module["lessons"]:
            if lesson["id"] == current_lesson_id:
                status = "current"
            elif lesson["id"] in completed_lesson_ids:
                status = "completed"
            elif not module_unlocked:
                status = "locked"
            else:
                status = "pending"

            lessons_out.append({
                "id": lesson["id"],
                "title": lesson["title"],
                "reading_time_minutes": lesson["reading_time_minutes"],
                "has_exercise": lesson["has_exercise"],
                "status": status,
            })

        sidebar.append({
            "id": module["id"],
            "title": module["title"],
            "unlocked": module_unlocked,
            "lessons": lessons_out,
        })

    return sidebar