TETO_DESCONTO = 200.00
TIPOS_VALIDOS = ("VIP", "COMUM")


def calcular_desconto(valor_compra, tipo_cliente):
    if isinstance(valor_compra, bool) or not isinstance(valor_compra, (int, float)):
        raise TypeError("valor_compra deve ser numérico")
    if valor_compra < 0:
        raise ValueError("valor_compra não pode ser negativo")

    if not isinstance(tipo_cliente, str):
        raise TypeError("tipo_cliente deve ser texto")
    tipo = tipo_cliente.strip().upper() 
    if tipo not in TIPOS_VALIDOS:
        raise ValueError(f"tipo_cliente inválido: {tipo_cliente!r}")

    if valor_compra >= 500:
        desconto = 0.20
    elif valor_compra >= 100:
        desconto = 0.10
    else:
        desconto = 0.0

    if tipo == "VIP":
        desconto += 0.05

    valor_desconto = valor_compra * desconto

    if valor_desconto > TETO_DESCONTO:
        valor_desconto = TETO_DESCONTO

    return round(valor_desconto, 2)