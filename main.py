import tkinter as tk
from tkinter import messagebox
import login as login_module
import cardapio as cardapio_module
import carrinho as carrinho_module
import recorrencia
import grafos

carrinho_atual = []
restaurante_selecionado_id = None
historico_pedidos = [] 

janela = tk.Tk()
janela.title("FoodRank")
janela.geometry("550x580") 


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
    # Esconde a lista e campos de seleção
    lbl_restaurantes.pack_forget()
    lbl_escolher_rest.pack_forget()
    entrada_rest_id.pack_forget()
    btn_ver_cardapio.pack_forget()
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

    # Retorna ao Menu Principal
    lbl_bem_vindo.pack(pady=20)
    btn_todos_restaurantes.pack(pady=10)
    btn_ranking.pack(pady=10)
    btn_filtrar.pack(pady=10)
    btn_ver_carrinho.pack(pady=10)
    btn_recomendacoes.pack(pady=10)

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
        btn_ver_carrinho.pack(pady=10)
        btn_recomendacoes.pack(pady=10)
    else:
        messagebox.showerror("Erro de Login", mensagem)

def todos_restaurantes():
    lbl_bem_vindo.pack_forget()
    btn_todos_restaurantes.pack_forget()
    btn_ranking.pack_forget()
    btn_filtrar.pack_forget()
    btn_ver_carrinho.pack_forget()
    btn_recomendacoes.pack_forget()

    try:
        import matriz
        restaurantes = matriz.carregar_restaurantes()
        texto = "Lista de Restaurantes:\n\n"
        for r in restaurantes:
            texto += f"[{r['id']}] {r['nome']} ({r['tipo']}) - Nota: {r['nota']}\n"
    except Exception as e:
        texto = f"Erro ao carregar restaurantes: {e}"

    lbl_restaurantes.config(text=texto)
    lbl_restaurantes.pack(pady=10)
    
    
    lbl_escolher_rest.pack(pady=5)
    entrada_rest_id.pack(pady=5)
    btn_ver_cardapio.pack(pady=5)
    btn_voltar_restaurantes.pack(pady=10)

def ranking():
    lbl_bem_vindo.pack_forget()
    btn_todos_restaurantes.pack_forget()
    btn_ranking.pack_forget()
    btn_filtrar.pack_forget()
    btn_ver_carrinho.pack_forget()
    btn_recomendacoes.pack_forget()

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
    btn_ver_carrinho.pack_forget()
    btn_recomendacoes.pack_forget()

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


def abrir_cardapio():
    global restaurante_selecionado_id
    try:
        rest_id = int(entrada_rest_id.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um ID numérico válido!")
        return

    import matriz
    restaurantes = matriz.carregar_restaurantes()
    restaurante = next((r for r in restaurantes if r["id"] == rest_id), None)
    
    if not restaurante:
        messagebox.showerror("Erro", "Restaurante não encontrado!")
        return
        
    restaurante_selecionado_id = rest_id
    
    # Esconde a lista de restaurantes
    lbl_restaurantes.pack_forget()
    lbl_escolher_rest.pack_forget()
    entrada_rest_id.pack_forget()
    btn_ver_cardapio.pack_forget()
    btn_voltar_restaurantes.pack_forget()
    
    # Busca e formata o cardápio
    itens = cardapio_module.buscar_itens_por_restaurante(rest_id)
    texto = f"=== Cardápio do {restaurante['nome']} ===\n\n"
    
    if not itens:
        texto += "Nenhum item cadastrado."
    else:
        for item in itens:
            texto += f"[{item['id']}] {item['nome']} - R$ {item['preco']:.2f}\n"
            
    lbl_cardapio_itens.config(text=texto)
    
    # Mostra a tela do cardápio
    lbl_cardapio_titulo.pack(pady=5)
    lbl_cardapio_itens.pack(pady=10)
    
    lbl_item_id.pack()
    entrada_item_id.pack(pady=2)
    lbl_item_qtd.pack()
    entrada_item_qtd.pack(pady=2)
    
    btn_adicionar_carrinho.pack(pady=10)
    btn_voltar_cardapio.pack(pady=5)

def adicionar_ao_carrinho():
    try:
        item_id = int(entrada_item_id.get())
        qtd = int(entrada_item_qtd.get())
    except ValueError:
        messagebox.showerror("Erro", "ID e Quantidade devem ser numéricos!")
        return

    if qtd <= 0:
        messagebox.showerror("Erro", "A quantidade deve ser maior que 0.")
        return

    produto = cardapio_module.buscar_item_por_id(item_id)
    if produto is None or produto["restaurante_id"] != restaurante_selecionado_id:
        messagebox.showerror("Erro", "Item não encontrado ou não pertence a este restaurante!")
        return
        
    carrinho_module.adicionar_item(carrinho_atual, produto, qtd)
    messagebox.showinfo("Sucesso", f"{qtd}x '{produto['nome']}' adicionado ao carrinho!")
    
    # Limpa as entradas
    entrada_item_id.delete(0, tk.END)
    entrada_item_qtd.delete(0, tk.END)

def voltar_para_restaurantes_do_cardapio():
    lbl_cardapio_titulo.pack_forget()
    lbl_cardapio_itens.pack_forget()
    lbl_item_id.pack_forget()
    entrada_item_id.pack_forget()
    lbl_item_qtd.pack_forget()
    entrada_item_qtd.pack_forget()
    btn_adicionar_carrinho.pack_forget()
    btn_voltar_cardapio.pack_forget()
    
    # Recarrega a tela de restaurantes
    todos_restaurantes()

def abrir_carrinho():
    # Esconde menu principal
    lbl_bem_vindo.pack_forget()
    btn_todos_restaurantes.pack_forget()
    btn_ranking.pack_forget()
    btn_filtrar.pack_forget()
    btn_ver_carrinho.pack_forget()
    btn_recomendacoes.pack_forget()
    
    if not carrinho_atual:
        texto = "O seu carrinho está vazio."
    else:
        texto = ""
        for item in carrinho_atual:
            subtotal = item["preco"] * item["quantidade"]
            texto += f"{item['nome']} | Qtd: {item['quantidade']} | R$ {subtotal:.2f}\n"
            
        total = recorrencia.calcular_total(carrinho_atual)
        texto += f"\n--------------------------\nTOTAL: R$ {total:.2f}"
        
    lbl_carrinho_itens.config(text=texto)
    
    lbl_carrinho_titulo.pack(pady=10)
    lbl_carrinho_itens.pack(pady=10)
    btn_limpar_carrinho.pack(pady=5)
    btn_finalizar_pedido.pack(pady=5)
    btn_voltar_carrinho.pack(pady=10)

def limpar_carrinho_ui():
    carrinho_module.limpar_carrinho(carrinho_atual)
    voltar_do_carrinho()
    abrir_carrinho()
    messagebox.showinfo("Aviso", "Carrinho esvaziado!")

def finalizar_pedido():
    global carrinho_atual, restaurante_selecionado_id, historico_pedidos
    
    if not carrinho_atual:
        messagebox.showwarning("Aviso", "Seu carrinho está vazio!")
        return
        
    total = recorrencia.calcular_total(carrinho_atual)
    
    # 1. Descobre o nome do restaurante atual
    import matriz
    restaurantes = matriz.carregar_restaurantes()
    nome_restaurante_pedido = ""
    for r in restaurantes:
        if r["id"] == restaurante_selecionado_id:
            nome_restaurante_pedido = r["nome"]
            break
            
    # 2. Salva no histórico
    if nome_restaurante_pedido:
        historico_pedidos.append(nome_restaurante_pedido)

    # 3. Limpa carrinho e avisa sucesso
    carrinho_module.limpar_carrinho(carrinho_atual)
    voltar_do_carrinho()
    messagebox.showinfo("Sucesso", f"Pedido realizado com sucesso!\nValor pago: R$ {total:.2f}")
    
    # 4. Exibe recomendação usando Grafos
    if nome_restaurante_pedido:
        recomendacao_texto = grafos.recomendacao(nome_restaurante_pedido)
        if recomendacao_texto != "Restaurante não encontrado.":
            messagebox.showinfo("Recomendação Especial", recomendacao_texto)

def voltar_do_carrinho():
    lbl_carrinho_titulo.pack_forget()
    lbl_carrinho_itens.pack_forget()
    btn_limpar_carrinho.pack_forget()
    btn_finalizar_pedido.pack_forget()
    btn_voltar_carrinho.pack_forget()
    
    # Mostra o menu principal
    lbl_bem_vindo.pack(pady=20)
    btn_todos_restaurantes.pack(pady=10)
    btn_ranking.pack(pady=10)
    btn_filtrar.pack(pady=10)
    btn_ver_carrinho.pack(pady=10)
    btn_recomendacoes.pack(pady=10)

def ver_recomendacoes():
    if not historico_pedidos:
        messagebox.showinfo("Recomendações", "Você ainda não fez nenhum pedido.\nFaça um pedido para recebermos suas preferências!")
        return
        
    ultimo_pedido = historico_pedidos[-1]
    recomendacao_texto = grafos.recomendacao(ultimo_pedido)
    messagebox.showinfo("Baseado no seu último pedido", recomendacao_texto)

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
btn_ver_carrinho = tk.Button(janela, text="Meu Carrinho", command=abrir_carrinho)
btn_recomendacoes = tk.Button(janela, text="Ver Recomendações", command=ver_recomendacoes)

# Menu de Restaurantes (Lista)
lbl_restaurantes = tk.Label(janela, text="Lista de Restaurantes") 
lbl_escolher_rest = tk.Label(janela, text="Digite o ID do Restaurante para ver o cardápio:")
entrada_rest_id = tk.Entry(janela)
btn_ver_cardapio = tk.Button(janela, text="Ver Cardápio", command=abrir_cardapio)
btn_voltar_restaurantes = tk.Button(janela, text="Voltar", command=voltar_restaurantes)

# Menu de Ranking e Filtros
lbl_ranking = tk.Label(janela, text="Ranking dos Restaurantes")
btn_voltar_ranking = tk.Button(janela, text="Voltar", command=voltar_restaurantes)

lbl_filtro = tk.Label(janela, text="Filtrar por Categoria")
btn_hamburgueria = tk.Button(janela, text="Hamburgueria", command=lambda: ranking_categoria("Hamburgueria"))
btn_pizzaria = tk.Button(janela, text="Pizzaria", command=lambda: ranking_categoria("Pizzaria"))   
btn_sushi = tk.Button(janela, text="Sushi", command=lambda: ranking_categoria("Sushi")) 
btn_churrascaria = tk.Button(janela, text="Churrascaria", command=lambda: ranking_categoria("Churrascaria"))
btn_voltar_filtro = tk.Button(janela, text="Voltar", command=voltar_restaurantes)

lbl_filtro_resultados = tk.Label(janela, text="")
btn_voltar_resultados = tk.Button(janela, text="Voltar", command=voltar_resultados)

# Widgets da Tela de Cardápio
lbl_cardapio_titulo = tk.Label(janela, text="Cardápio", font=("Arial", 16))
lbl_cardapio_itens = tk.Label(janela, text="")
lbl_item_id = tk.Label(janela, text="ID do Produto:")
entrada_item_id = tk.Entry(janela)
lbl_item_qtd = tk.Label(janela, text="Quantidade:")
entrada_item_qtd = tk.Entry(janela)
btn_adicionar_carrinho = tk.Button(janela, text="Adicionar ao Carrinho", bg="lightblue", command=adicionar_ao_carrinho)
btn_voltar_cardapio = tk.Button(janela, text="Voltar", command=voltar_para_restaurantes_do_cardapio)

# Widgets da Tela de Carrinho
lbl_carrinho_titulo = tk.Label(janela, text="Meu Carrinho", font=("Arial", 16))
lbl_carrinho_itens = tk.Label(janela, text="", justify="left")
btn_limpar_carrinho = tk.Button(janela, text="Limpar Carrinho", command=limpar_carrinho_ui)
btn_finalizar_pedido = tk.Button(janela, text="Finalizar Pedido", bg="lightgreen", command=finalizar_pedido)
btn_voltar_carrinho = tk.Button(janela, text="Voltar", command=voltar_do_carrinho)

janela.mainloop()