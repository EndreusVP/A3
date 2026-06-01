from restaurantes import (
    listar_restaurantes,
    buscar_restaurante_por_id
)

from cardapio import (
    mostrar_cardapio,
    buscar_item_por_id
)

from carrinho import (
    adicionar_item,
    mostrar_carrinho
)

from recorrencia import calcular_total


def main():

    carrinho = []

    # Lista restaurantes
    listar_restaurantes()

    # Escolha do restaurante
    id_restaurante = int(
        input("\nEscolha um restaurante: ")
    )

    restaurante = buscar_restaurante_por_id(
        id_restaurante
    )

    if restaurante is None:

        print("\nRestaurante não encontrado.")
        return

    print(
        f'\nVocê escolheu: '
        f'{restaurante["nome"]}'
    )

    # Mostra cardápio
    mostrar_cardapio(
        restaurante["id"]
    )

    # Adiciona itens ao carrinho
    while True:

        item_id = int(
            input(
                "\nDigite o ID do produto (0 para finalizar): "
            )
        )

        if item_id == 0:
            break

        produto = buscar_item_por_id(
          item_id
        )

        if (
            produto is None
            or produto["restaurante_id"] != id_restaurante
        ):

            print(
                "\nEsse produto não pertence ao restaurante escolhido."
            )
            continue

        quantidade = int(
            input("Quantidade: ")
        )

        adicionar_item(
            carrinho,
            produto,
            quantidade
        )

        print(
            "\nProduto adicionado ao carrinho!"
        )

    # Mostra carrinho
    mostrar_carrinho(carrinho)
    total = calcular_total(carrinho)

    print(f"\nTOTAL DO PEDIDO: R$ {total:.2f}")

if __name__ == "__main__":
    main()