from matriz import carregar_restaurantes

def criacao_grafo():
    restaurantes = carregar_restaurantes()
    grafo = {}

    for r in restaurantes:
        nome = r["nome"]
        tipo = r["tipo"]

        relacionados = []

        for outro in restaurantes:
            if outro["nome"] != nome and outro["tipo"] == tipo:
                relacionados.append(outro["nome"])

        grafo[nome] = relacionados

    return grafo


def recomendacao(restaurante):
    grafo = criacao_grafo()

    if restaurante in grafo:
        
        return f"Já que você gostou de {restaurante}, você também pode gostar de {', '.join(grafo[restaurante])}."

    return "Restaurante não encontrado."


# # Teste

# if __name__ == "__main__":
    
#     print(recomendacao("Pizza Vip"))
#     print(recomendacao("Sushi House"))
#     print(recomendacao("McDonald's"))
#     print(recomendacao("Burguer King"))
#     print(recomendacao("Churrascaria do Zé"))
#     print(recomendacao("Churrascaria Boi Gordo"))
