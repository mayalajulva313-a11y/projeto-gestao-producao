from math import isfinite


def validar_registro(registro):
    if not registro["setor"].strip():
        return "O setor não pode ficar vazio."
    if not isinstance(registro["produzidas"], int) or registro["produzidas"] < 0:
        return "A quantidade produzida deve ser um inteiro não negativo."
    if (
        not isinstance(registro["pecas_rejeitadas"], int)
        or registro["pecas_rejeitadas"] < 0
    ):
        return "A quantidade rejeitada deve ser um inteiro não negativo."

    custo = registro["custo_unitario"]
    if not isinstance(custo, (int, float)) or not isfinite(custo) or custo < 0:
        return "O custo unitário deve ser um número não negativo."
    return None


def buscar_por_id(registros, identificador):
    return next(
        (registro for registro in registros if registro["id"] == identificador),
        None,
    )


def gerar_proximo_id(registros):
    return max((registro["id"] for registro in registros), default=0) + 1


def calcular_indicadores(registros):
    produzidas = sum(registro["produzidas"] for registro in registros)
    rejeitadas = sum(registro["pecas_rejeitadas"] for registro in registros)
    total_inspecionado = produzidas + rejeitadas
    custo_medio = (
        sum(registro["custo_unitario"] for registro in registros) / len(registros)
        if registros
        else 0
    )

    return {
        "total_registros": len(registros),
        "produzidas": produzidas,
        "rejeitadas": rejeitadas,
        "percentual_rejeitadas": (
            rejeitadas / total_inspecionado * 100 if total_inspecionado else 0
        ),
        "custo_unitario_medio": custo_medio,
    }