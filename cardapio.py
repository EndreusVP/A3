import json
import os


def carregar_itens():

    caminho = os.path.join(
        os.path.dirname(__file__),
        "data",
        "cardapio.json"
    )

    with open(
        caminho,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)


def buscar_itens_por_restaurante(restaurante_id):

    itens = carregar_itens()

    return [
        item
        for item in itens
        if item["restaurante_id"] == restaurante_id
    ]


def mostrar_cardapio(restaurante_id):

    itens = buscar_itens_por_restaurante(
        restaurante_id
    )

    print("\n=== CARDÁPIO ===\n")

    for item in itens:

        print(
            f'{item["id"]} - '
            f'{item["nome"]} '
            f'- R$ {item["preco"]:.2f}'
        )


def buscar_item_por_id(item_id):

    itens = carregar_itens()

    for item in itens:

        if item["id"] == item_id:
            return item

    return None