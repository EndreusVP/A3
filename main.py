import tkinter as tk

janela =tk.Tk()

janela.title("FoodRank")
janela.geometry("500x400")

def login():
    titulo.pack_forget()
    btn_login.pack_forget()
    btn_cadastro.pack_forget()

    lbl_email.pack(pady=10)
    entrada_email.pack(pady=5)

    lbl_senha.pack(pady=10) 
    entrada_senha.pack(pady=5)

    btn_entrar.pack(pady=20) 
    btn_voltar.pack(pady=10)

def voltar():
    lbl_email.pack_forget()
    entrada_email.pack_forget()

    lbl_senha.pack_forget()
    entrada_senha.pack_forget()

    btn_entrar.pack_forget()
    btn_voltar.pack_forget()


    lbl_criar_email.pack_forget()
    entrada_criar_email.pack_forget()

    lbl_criar_senha.pack_forget()
    entrada_criar_senha.pack_forget()

    btn_cadastrar_usuario.pack_forget()

    titulo.pack(pady=20)
    btn_login.pack(pady=10)
    btn_cadastro.pack(pady=10)

def voltar_restaurantes():
    lbl_restaurantes.pack_forget()
    btn_voltar_restaurantes.pack_forget()

    lbl_ranking.pack_forget()
    btn_voltar_ranking.pack_forget()

    lbl_filtro.pack_forget()
    btn_hamburgueria.pack_forget()
    btn_pizzaria.pack_forget()
    btn_sushi.pack_forget()
    btn_churrascaria.pack_forget()
    btn_voltar_filtro.pack_forget()

    lbl_bem_vindo.pack(pady=20)
    btn_todos_restaurantes.pack(pady=10)
    btn_ranking.pack(pady=10)
    btn_filtrar.pack(pady=10)


def cadastrar():
    titulo.pack_forget()
    btn_login.pack_forget()
    btn_cadastro.pack_forget()

    lbl_criar_email.pack(pady=10)
    entrada_criar_email.pack(pady=5)

    lbl_criar_senha.pack(pady=10)
    entrada_criar_senha.pack(pady=5)

    btn_cadastrar_usuario.pack(pady=20)
    btn_voltar.pack(pady=10)

def entrar():
    entrada_email.pack_forget()
    lbl_email.pack_forget()
    entrada_senha.pack_forget()
    lbl_senha.pack_forget()
    btn_entrar.pack_forget()
    btn_voltar.pack_forget()

    lbl_bem_vindo.pack(pady=20)
    btn_todos_restaurantes.pack(pady=10)
    btn_ranking.pack(pady=10)
    btn_filtrar.pack(pady=10)

def todos_restaurantes():
    lbl_bem_vindo.pack_forget()
    btn_todos_restaurantes.pack_forget()
    btn_ranking.pack_forget()
    btn_filtrar.pack_forget()

    lbl_restaurantes.pack(pady=20)
    btn_voltar_restaurantes.pack(pady=10)

def ranking():
    lbl_bem_vindo.pack_forget()
    btn_todos_restaurantes.pack_forget()
    btn_ranking.pack_forget()
    btn_filtrar.pack_forget()

    lbl_ranking.pack(pady=20)
    btn_voltar_ranking.pack(pady=10)

def filtrar():
    lbl_bem_vindo.pack_forget()
    btn_todos_restaurantes.pack_forget()
    btn_ranking.pack_forget()
    btn_filtrar.pack_forget()

    lbl_filtro.pack(pady=20)
    btn_hamburgueria.pack(pady=5)
    btn_pizzaria.pack(pady=5)
    btn_sushi.pack(pady=5)
    btn_churrascaria.pack(pady=5)
    btn_voltar_filtro.pack(pady=10)

#menu login
titulo =tk.Label(janela, text="FoodRank", font=("Arial", 20))
titulo.pack(pady=20)

btn_login = tk.Button(janela, text="login", command=login)
btn_login.pack(pady=10)

btn_cadastro = tk.Button(janela, text="cadastrar", command=cadastrar)
btn_cadastro.pack(pady=10)

#login
lbl_email = tk.Label(janela, text="Email:")
entrada_email =tk.Entry(janela)

lbl_senha = tk.Label(janela, text="Senha:")
entrada_senha = tk.Entry(janela, show="*")

btn_entrar = tk.Button(janela, text="Entrar", command=entrar)
btn_voltar = tk.Button(janela, text="Voltar", command=voltar)

#cadastro
lbl_criar_email = tk.Label(janela, text="Email:")
entrada_criar_email = tk.Entry(janela)

lbl_criar_senha = tk.Label(janela, text="Senha:")
entrada_criar_senha = tk.Entry(janela, show="*")

btn_cadastrar_usuario = tk.Button(janela, text="Cadastrar", command=voltar)
btn_voltar= tk.Button(janela, text="Voltar", command=voltar)

#menu principal
lbl_bem_vindo = tk.Label(janela, text="Bem-vindo ao FoodRank!")

btn_todos_restaurantes = tk.Button(janela, text="Todos os Restaurantes", command=todos_restaurantes)

btn_ranking = tk.Button(janela, text="Ranking dos Restaurantes", command=ranking)

btn_filtrar = tk.Button(janela, text="Filtrar por Categoria", command=filtrar)

#menu de restaurantes
lbl_restaurantes = tk.Label(janela, text="Lista de Restaurantes") 

btn_voltar_restaurantes = tk.Button(janela, text="Voltar", command=voltar_restaurantes)

#menu de ranking
lbl_ranking = tk.Label(janela, text="Ranking dos Restaurantes")

btn_voltar_ranking = tk.Button(janela, text="Voltar", command=voltar_restaurantes)

#menu filtro
lbl_filtro = tk.Label(janela, text="Filtrar por Categoria")

btn_hamburgueria = tk.Button(janela, text="Hamburgueria")

btn_pizzaria = tk.Button(janela, text="Pizzaria")   

btn_sushi = tk.Button(janela, text="Sushi") 

btn_churrascaria = tk.Button(janela, text="Churrascaria")

btn_voltar_filtro = tk.Button(janela, text="Voltar", command=voltar_restaurantes)

janela.mainloop()

