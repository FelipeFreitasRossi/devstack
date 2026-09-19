"""
Pacote lessons_content
=======================
Este pacote substitui o antigo arquivo único `lessons_content.py`.

Cada módulo do curso vive no seu próprio arquivo:
    lessons_module_01.py, lessons_module_02.py, ...

O dicionário LESSONS (abaixo) só inclui os módulos que realmente têm
conteúdo. Assim, o erro `NameError: name 'LESSON_08_01' is not defined`
não acontece mais, porque não citamos lições que não existem.

Como adicionar um módulo novo:
-------------------------------
1. Crie o arquivo `lessons_module_XX.py` nesta mesma pasta.
2. Escreva as lições nele (LESSON_XX_01 = {...}, LESSON_XX_02 = {...}).
3. Neste arquivo (__init__.py), importe as lições e registre no dicionário
   LESSONS (procure os comentários marcando onde adicionar).
"""

from app.analytics import CURRICULUM

# ----------------------------------------------------------------------
# Módulo 01 — Lógica de Programação
# ----------------------------------------------------------------------
from .lessons_module_01 import (
    LESSON_01_01, LESSON_01_03, LESSON_01_04, LESSON_01_05, LESSON_01_06,
    LESSON_01_07, LESSON_01_08, LESSON_01_09, LESSON_01_10, LESSON_01_11,
    LESSON_01_12,
)

# ----------------------------------------------------------------------
# Módulo 02 — Python Fundamentos
# ----------------------------------------------------------------------
from .lessons_module_02 import (
    LESSON_02_01, LESSON_02_02, LESSON_02_03, LESSON_02_04, LESSON_02_05,
    LESSON_02_06, LESSON_02_07, LESSON_02_08, LESSON_02_09, LESSON_02_10,
    LESSON_02_11,
)

# ----------------------------------------------------------------------
# Módulo 03 — Python Intermediário
# ----------------------------------------------------------------------
from .lessons_module_03 import (
    LESSON_03_01, LESSON_03_02, LESSON_03_03, LESSON_03_04, LESSON_03_05,
    LESSON_03_06, LESSON_03_07, LESSON_03_08, LESSON_03_09, LESSON_03_10,
)

# ----------------------------------------------------------------------
# Módulo 04 — Python para Desenvolvimento
# ----------------------------------------------------------------------
from .lessons_module_04 import (
    LESSON_04_01, LESSON_04_02, LESSON_04_03, LESSON_04_04, LESSON_04_05,
    LESSON_04_06, LESSON_04_07,
)

# ----------------------------------------------------------------------
# Módulo 05 — FastAPI
# ----------------------------------------------------------------------
from .lessons_module_05 import (
    LESSON_05_01, LESSON_05_02, LESSON_05_03, LESSON_05_04, LESSON_05_05,
    LESSON_05_06, LESSON_05_07, LESSON_05_08,
)

# ----------------------------------------------------------------------
# Módulo 06 — HTML + CSS
# ----------------------------------------------------------------------
from .lessons_module_06 import (
    LESSON_06_01, LESSON_06_02, LESSON_06_03, LESSON_06_04, LESSON_06_05,
    LESSON_06_06, LESSON_06_07, LESSON_06_08, LESSON_06_09, LESSON_06_10,
    LESSON_06_11, LESSON_06_12, LESSON_06_13, LESSON_06_14,
)

# ----------------------------------------------------------------------
# Módulo 07 — JavaScript
# ----------------------------------------------------------------------
from .lessons_module_07 import (
    LESSON_07_01, LESSON_07_02, LESSON_07_03, LESSON_07_04, LESSON_07_05,
    LESSON_07_06, LESSON_07_07, LESSON_07_08, LESSON_07_09, LESSON_07_10,
    LESSON_07_11, LESSON_07_12, LESSON_07_13, LESSON_07_14,
)

# ----------------------------------------------------------------------
# Módulo 08 — Git e GitHub
# ----------------------------------------------------------------------
from .lessons_module_08 import (
    LESSON_08_01, LESSON_08_02, LESSON_08_03, LESSON_08_04, LESSON_08_05,
    LESSON_08_06, LESSON_08_07, LESSON_08_08, LESSON_08_09, LESSON_08_10,
)


# ============================================================================
# LESSONS — dicionário com TODAS as lições, indexado por id ("01-01", ...)
# ============================================================================
LESSONS: dict[str, dict] = {
    # Módulo 01
    "01-01": LESSON_01_01, "01-03": LESSON_01_03, "01-04": LESSON_01_04,
    "01-05": LESSON_01_05, "01-06": LESSON_01_06, "01-07": LESSON_01_07,
    "01-08": LESSON_01_08, "01-09": LESSON_01_09, "01-10": LESSON_01_10,
    "01-11": LESSON_01_11, "01-12": LESSON_01_12,
    # Módulo 02
    "02-01": LESSON_02_01, "02-02": LESSON_02_02, "02-03": LESSON_02_03,
    "02-04": LESSON_02_04, "02-05": LESSON_02_05, "02-06": LESSON_02_06,
    "02-07": LESSON_02_07, "02-08": LESSON_02_08, "02-09": LESSON_02_09,
    "02-10": LESSON_02_10, "02-11": LESSON_02_11,
    # Módulo 03
    "03-01": LESSON_03_01, "03-02": LESSON_03_02, "03-03": LESSON_03_03,
    "03-04": LESSON_03_04, "03-05": LESSON_03_05, "03-06": LESSON_03_06,
    "03-07": LESSON_03_07, "03-08": LESSON_03_08, "03-09": LESSON_03_09,
    "03-10": LESSON_03_10,
    # Módulo 04
    "04-01": LESSON_04_01, "04-02": LESSON_04_02, "04-03": LESSON_04_03,
    "04-04": LESSON_04_04, "04-05": LESSON_04_05, "04-06": LESSON_04_06,
    "04-07": LESSON_04_07,
    # Módulo 05
    "05-01": LESSON_05_01, "05-02": LESSON_05_02, "05-03": LESSON_05_03,
    "05-04": LESSON_05_04, "05-05": LESSON_05_05, "05-06": LESSON_05_06,
    "05-07": LESSON_05_07, "05-08": LESSON_05_08,
    # Módulo 06
    "06-01": LESSON_06_01, "06-02": LESSON_06_02, "06-03": LESSON_06_03,
    "06-04": LESSON_06_04, "06-05": LESSON_06_05, "06-06": LESSON_06_06,
    "06-07": LESSON_06_07, "06-08": LESSON_06_08, "06-09": LESSON_06_09,
    "06-10": LESSON_06_10, "06-11": LESSON_06_11, "06-12": LESSON_06_12,
    "06-13": LESSON_06_13, "06-14": LESSON_06_14,
    # Módulo 07
    "07-01": LESSON_07_01, "07-02": LESSON_07_02, "07-03": LESSON_07_03,
    "07-04": LESSON_07_04, "07-05": LESSON_07_05, "07-06": LESSON_07_06,
    "07-07": LESSON_07_07, "07-08": LESSON_07_08, "07-09": LESSON_07_09,
    "07-10": LESSON_07_10, "07-11": LESSON_07_11, "07-12": LESSON_07_12,
    "07-13": LESSON_07_13, "07-14": LESSON_07_14,
    # Módulo 08 — Git e GitHub
    "08-01": LESSON_08_01, "08-02": LESSON_08_02, "08-03": LESSON_08_03,
    "08-04": LESSON_08_04, "08-05": LESSON_08_05, "08-06": LESSON_08_06,
    "08-07": LESSON_08_07, "08-08": LESSON_08_08, "08-09": LESSON_08_09,
    "08-10": LESSON_08_10,
}


# ============================================================================
# FUNÇÕES AUXILIARES  ⚠️ NÃO REMOVA ESTE BLOCO
# ============================================================================
# As rotas em `app/routes/lessons.py` importam estas 3 funções:
#     get_lesson, get_adjacent_lesson_ids, validate_submission
# Se qualquer uma delas faltar, o servidor sobe com ImportError.
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