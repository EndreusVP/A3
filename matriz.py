import json

def carregar_restaurantes():
    with open("data/restaurantes.json", "r", encoding="utf-8") as f:
        return json.load(f)

def ranking_restaurantes(restaurante):
    restaurante = sorted(restaurante, key=lambda r: r ["nota"], reverse=True)
    return restaurante

def ranking_categoria(restaurante, categoria):
    restaurante = sorted(restaurante, key=lambda r: r["nota"], reverse=True)
    categoria_res = []
    for r in restaurante:
        if r["tipo"] == categoria:
            categoria_res.append(r)
    return categoria_res

def filtrar_restaurantes(restaurante, categoria):
    filtro =[]

    for r in restaurante:
        if r ["tipo"] == categoria:
            filtro.append(r)
    return filtro