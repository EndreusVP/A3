def adicionar_item(carrinho, produto, quantidade):
    """
    Adiciona um item ao carrinho.
    Se já existir, soma a quantidade.
    """

    for item in carrinho:

        if item["id"] == produto["id"]:

            item["quantidade"] += quantidade
            return

    carrinho.append({
        "id": produto["id"],
        "nome": produto["nome"],
        "preco": produto["preco"],
        "quantidade": quantidade
    })


def remover_item(carrinho, produto_id):
    """
    Remove um item pelo ID.
    """

    for item in carrinho:

        if item["id"] == produto_id:

            carrinho.remove(item)
            return True

    return False


def mostrar_carrinho(carrinho):

    if not carrinho:
        print("\nCarrinho vazio.")
        return

    print("\n=== CARRINHO ===\n")

    for item in carrinho:

        subtotal = (
            item["preco"] *
            item["quantidade"]
        )

        print(
            f'{item["nome"]} '
            f'| Qtd: {item["quantidade"]} '
            f'| R$ {subtotal:.2f}'
        )


def limpar_carrinho(carrinho):

    carrinho.clear()