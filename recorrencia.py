def calcular_total(carrinho, indice=0):

    # Caso base: chegou ao fim da lista
    if indice >= len(carrinho):
        return 0

    item = carrinho[indice]

    subtotal = (
        item["preco"] *
        item["quantidade"]
    )

    # Chamada recursiva
    return subtotal + calcular_total(
        carrinho,
        indice + 1
    )