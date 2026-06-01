import json


def carregar_restaurantes():
    """
    Carrega os restaurantes do arquivo JSON.
    """

    with open(
        "data/restaurantes2.json",
        "r",
        encoding="utf-8"
    ) as arquivo:

        return json.load(arquivo)


def listar_restaurantes():
    """
    Exibe os restaurantes cadastrados.
    """

    restaurantes = carregar_restaurantes()

    print("\n=== RESTAURANTES ===\n")

    for restaurante in restaurantes:

        print(
            f'{restaurante["id"]} - '
            f'{restaurante["nome"]} '
            f'({restaurante["tipo"]}) '
            f'{restaurante["nota"]}'
        )


def buscar_restaurante_por_id(id_restaurante):
    """
    Retorna um restaurante pelo ID.
    """

    restaurantes = carregar_restaurantes()

    for restaurante in restaurantes:

        if restaurante["id"] == id_restaurante:
            return restaurante

    return None