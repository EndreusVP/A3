import json

def carregar_restaurantes():
    with open("restaurantes.json") as f:
        return json.load(f)

def ranking_restaurantes(restaurante):
    restaurante = sorted(restaurante, key=lambda r: r ["nota"], reverse=True)
    return restaurante

def filtrar_restaurantes(restaurante, categoria):
    filtro =[]

    for r in restaurante:
        if r ["categoria"] == categoria:
            filtro.append(r)
    return filtro
