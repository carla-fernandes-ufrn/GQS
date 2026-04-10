def medico_com_mais_horas(dados):
    if not dados:
        return []

    # Descobre o maior número de horas
    max_horas = max(medico["horas"] for medico in dados)

    # Retorna todos os médicos com essa quantidade de horas
    return [
        medico for medico in dados
        if medico["horas"] == max_horas
    ]

from decimal import Decimal, ROUND_HALF_UP

def percentual_renda_por_hospital(dados):
    if not dados:
        return []

    total = sum(item["valor"] for item in dados)

    # Se total for zero, todos percentuais são zero
    if total == 0:
        return [
            {"hospital": item["hospital"], "percentual": 0.00}
            for item in dados
        ]

    resultado = []

    for item in dados:
        percentual = (item["valor"] / total) * 100

        # Arredondamento financeiro (half-up) com 2 casas decimais
        percentual_arredondado = float(
            Decimal(str(percentual)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        )

        resultado.append({
            "hospital": item["hospital"],
            "percentual": percentual_arredondado
        })

    return resultado

def percentual_medio_por_hospital(dados):
    if not dados:
        return []

    # Agrupa os valores por hospital
    acumulado_por_hospital = {}

    for item in dados:
        hospital = item["hospital"]
        valor = item["valor"]

        if hospital not in acumulado_por_hospital:
            acumulado_por_hospital[hospital] = 0

        acumulado_por_hospital[hospital] += valor

    # Converte para o formato esperado pela função já existente
    dados_agregados = [
        {"hospital": hospital, "valor": valor}
        for hospital, valor in acumulado_por_hospital.items()
    ]

    # Reutiliza a função existente
    return percentual_renda_por_hospital(dados_agregados)