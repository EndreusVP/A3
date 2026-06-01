import tkinter as tk
from tkinter import messagebox
import login as login_module

janela = tk.Tk()
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
    # Limpa os campos
    entrada_email.delete(0, tk.END)
    entrada_senha.delete(0, tk.END)
    entrada_criar_email.delete(0, tk.END)
    entrada_criar_senha.delete(0, tk.END)
    entrada_criar_cpf.delete(0, tk.END)

    # Esconde login
    lbl_email.pack_forget()
    entrada_email.pack_forget()
    lbl_senha.pack_forget()
    entrada_senha.pack_forget()
    btn_entrar.pack_forget()
    btn_voltar.pack_forget()

    # Esconde cadastro
    lbl_criar_email.pack_forget()
    entrada_criar_email.pack_forget()
    lbl_criar_senha.pack_forget()
    entrada_criar_senha.pack_forget()
    lbl_criar_cpf.pack_forget()
    entrada_criar_cpf.pack_forget()
    btn_cadastrar_usuario.pack_forget()

    # Mostra inicial
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

    lbl_filtro_resultados.pack_forget()
    btn_voltar_resultados.pack_forget()

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

    lbl_criar_cpf.pack(pady=10)
    entrada_criar_cpf.pack(pady=5)

    btn_cadastrar_usuario.pack(pady=20)
    btn_voltar.pack(pady=10)

def cadastrar_usuario():
    usuario = entrada_criar_email.get()
    senha = entrada_criar_senha.get()
    cpf = entrada_criar_cpf.get()

    if not usuario.strip() or not senha.strip() or not cpf.strip():
        messagebox.showerror("Erro de Cadastro", "Todos os campos (usuário, senha e CPF) são obrigatórios!")
        return

    cpf_limpo = "".join(filter(str.isdigit, cpf))
    if not login_module.validar_cpf(cpf_limpo):
        messagebox.showerror("Erro de Cadastro", "CPF inválido! Por favor, digite um CPF correto de 11 dígitos.")
        return

    cadastro = login_module.Cadastro(usuario, senha, cpf_limpo)
    sucesso, mensagem = cadastro.cadastrar()

    if sucesso:
        messagebox.showinfo("Sucesso", mensagem)
        voltar()
    else:
        messagebox.showerror("Erro de Cadastro", mensagem)

def entrar():
    usuario = entrada_email.get()
    senha = entrada_senha.get()

    if not usuario.strip() or not senha.strip():
        messagebox.showerror("Erro de Login", "Por favor, preencha todos os campos!")
        return

    log = login_module.Login(usuario, senha)
    sucesso, mensagem = log.logar()

    if sucesso:
        messagebox.showinfo("Login com Sucesso", mensagem)
        
        # Oculta tela de login
        entrada_email.pack_forget()
        lbl_email.pack_forget()
        entrada_senha.pack_forget()
        lbl_senha.pack_forget()
        btn_entrar.pack_forget()
        btn_voltar.pack_forget()

        # Configura mensagem de boas vindas
        lbl_bem_vindo.config(text=f"Bem-vindo ao FoodRank, {usuario}!")

        # Exibe menu principal
        lbl_bem_vindo.pack(pady=20)
        btn_todos_restaurantes.pack(pady=10)
        btn_ranking.pack(pady=10)
        btn_filtrar.pack(pady=10)
    else:
        messagebox.showerror("Erro de Login", mensagem)

def todos_restaurantes():
    lbl_bem_vindo.pack_forget()
    btn_todos_restaurantes.pack_forget()
    btn_ranking.pack_forget()
    btn_filtrar.pack_forget()

    try:
        import matriz
        restaurantes = matriz.carregar_restaurantes()
        texto = "Lista de Restaurantes:\n\n"
        for r in restaurantes:
            texto += f"• {r['nome']} ({r['tipo']}) - Nota: {r['nota']}\n"
    except Exception as e:
        texto = f"Erro ao carregar restaurantes: {e}"

    lbl_restaurantes.config(text=texto)
    lbl_restaurantes.pack(pady=20)
    btn_voltar_restaurantes.pack(pady=10)

def ranking():
    lbl_bem_vindo.pack_forget()
    btn_todos_restaurantes.pack_forget()
    btn_ranking.pack_forget()
    btn_filtrar.pack_forget()

    try:
        import matriz
        restaurantes = matriz.carregar_restaurantes()
        ordenados = matriz.ranking_restaurantes(restaurantes)
        texto = "Ranking dos Restaurantes:\n\n"
        for i, r in enumerate(ordenados, 1):
            texto += f"{i}º - {r['nome']} - Nota: {r['nota']} ({r['tipo']})\n"
    except Exception as e:
        texto = f"Erro ao carregar ranking: {e}"

    lbl_ranking.config(text=texto)
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

def exibir_categoria(categoria):
    lbl_filtro.pack_forget()
    btn_hamburgueria.pack_forget()
    btn_pizzaria.pack_forget()
    btn_sushi.pack_forget()
    btn_churrascaria.pack_forget()
    btn_voltar_filtro.pack_forget()

    try:
        import matriz
        restaurantes = matriz.carregar_restaurantes()
        categoria_busca = "sushi" if categoria.lower() == "sushi" else categoria
        filtrados = matriz.filtrar_restaurantes(restaurantes, categoria_busca)
        
        texto = f"Restaurantes - {categoria}:\n\n"
        if not filtrados:
            texto += "Nenhum restaurante encontrado."
        else:
            for r in filtrados:
                texto += f"• {r['nome']} - Nota: {r['nota']}\n"
    except Exception as e:
        texto = f"Erro ao filtrar restaurantes: {e}"

    lbl_filtro_resultados.config(text=texto)
    lbl_filtro_resultados.pack(pady=20)
    btn_voltar_resultados.pack(pady=10)

def ranking_categoria(categoria):
    lbl_filtro.pack_forget()
    btn_hamburgueria.pack_forget()
    btn_pizzaria.pack_forget()
    btn_sushi.pack_forget()
    btn_churrascaria.pack_forget()
    btn_voltar_filtro.pack_forget()

    try:
        import matriz
        restaurantes = matriz.carregar_restaurantes()
        categoria_busca = "sushi" if categoria.lower() == "sushi" else categoria
        ordenados = matriz.ranking_categoria(restaurantes, categoria_busca)
        
        texto = f"Ranking - {categoria}:\n\n"
        if not ordenados:
            texto += "Nenhum restaurante encontrado."
        else:
            for i, r in enumerate(ordenados, 1):
                texto += f"{i}º - {r['nome']} - Nota: {r['nota']}\n"
    except Exception as e:
        texto = f"Erro ao carregar ranking: {e}"

    lbl_filtro_resultados.config(text=texto)
    lbl_filtro_resultados.pack(pady=20)
    btn_voltar_resultados.pack(pady=10)

def voltar_resultados():
    lbl_filtro_resultados.pack_forget()
    btn_voltar_resultados.pack_forget()
    filtrar()

# --- Configuração da Interface (Widgets) ---

# Menu Inicial
titulo = tk.Label(janela, text="FoodRank", font=("Arial", 20))
titulo.pack(pady=20)

btn_login = tk.Button(janela, text="login", command=login)
btn_login.pack(pady=10)

btn_cadastro = tk.Button(janela, text="cadastrar", command=cadastrar)
btn_cadastro.pack(pady=10)

# Tela de Login
lbl_email = tk.Label(janela, text="Email:")
entrada_email = tk.Entry(janela)

lbl_senha = tk.Label(janela, text="Senha:")
entrada_senha = tk.Entry(janela, show="*")

btn_entrar = tk.Button(janela, text="Entrar", command=entrar)
btn_voltar = tk.Button(janela, text="Voltar", command=voltar)

# Tela de Cadastro
lbl_criar_email = tk.Label(janela, text="Email:")
entrada_criar_email = tk.Entry(janela)

lbl_criar_senha = tk.Label(janela, text="Senha:")
entrada_criar_senha = tk.Entry(janela, show="*")

lbl_criar_cpf = tk.Label(janela, text="CPF:")
entrada_criar_cpf = tk.Entry(janela)

btn_cadastrar_usuario = tk.Button(janela, text="Cadastrar", command=cadastrar_usuario)

# Menu Principal (Pós-login)
lbl_bem_vindo = tk.Label(janela, text="Bem-vindo ao FoodRank!")
btn_todos_restaurantes = tk.Button(janela, text="Todos os Restaurantes", command=todos_restaurantes)
btn_ranking = tk.Button(janela, text="Ranking dos Restaurantes", command=ranking)
btn_filtrar = tk.Button(janela, text="Filtrar por Categoria", command=filtrar)

# Menu de Restaurantes (Lista)
lbl_restaurantes = tk.Label(janela, text="Lista de Restaurantes") 
btn_voltar_restaurantes = tk.Button(janela, text="Voltar", command=voltar_restaurantes)

# Menu de Ranking
lbl_ranking = tk.Label(janela, text="Ranking dos Restaurantes")
btn_voltar_ranking = tk.Button(janela, text="Voltar", command=voltar_restaurantes)

# Menu Filtro
lbl_filtro = tk.Label(janela, text="Filtrar por Categoria")
btn_hamburgueria = tk.Button(janela, text="Hamburgueria", command=lambda: ranking_categoria("Hamburgueria"))
btn_pizzaria = tk.Button(janela, text="Pizzaria", command=lambda: ranking_categoria("Pizzaria"))   
btn_sushi = tk.Button(janela, text="Sushi", command=lambda: ranking_categoria("Sushi")) 
btn_churrascaria = tk.Button(janela, text="Churrascaria", command=lambda: ranking_categoria("Churrascaria"))
btn_voltar_filtro = tk.Button(janela, text="Voltar", command=voltar_restaurantes)

# Tela de Resultados do Filtro
lbl_filtro_resultados = tk.Label(janela, text="")
btn_voltar_resultados = tk.Button(janela, text="Voltar", command=voltar_resultados)

janela.mainloop()