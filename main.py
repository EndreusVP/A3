import login
import sys
import getpass

# Tenta importar msvcrt para o Windows para capturar teclas sem exibir no terminal
try:
    import msvcrt
    WINDOWS_CONSOLE = True
except ImportError:
    WINDOWS_CONSOLE = False

def obter_senha_mascarada(prompt="Digite sua senha: "):
    """
    Função para receber a senha do usuário exibindo asteriscos (*) em vez dos caracteres reais.
    Compatível com o terminal do Windows, com fallback para getpass caso não esteja no terminal interativo.
    """
    if not WINDOWS_CONSOLE:
        # Fallback caso não seja Windows ou não seja terminal interativo
        return getpass.getpass(prompt)

    print(prompt, end="", flush=True)
    senha = ""
    while True:
        # Captura uma tecla pressionada
        ch = msvcrt.getch()
        
        # Enter (finaliza a digitação)
        if ch in (b'\r', b'\n'):
            print()
            break
        # Backspace (apaga o caractere anterior)
        elif ch == b'\x08':
            if len(senha) > 0:
                senha = senha[:-1]
                sys.stdout.write('\b \b') # Move o cursor de volta, escreve espaço em branco, move o cursor de volta
                sys.stdout.flush()
        # Ctrl+C (cancela a execução)
        elif ch == b'\x03':
            raise KeyboardInterrupt
        else:
            try:
                char_str = ch.decode('utf-8')
                # Apenas caracteres normais legíveis (ASCII >= 32)
                if ord(char_str) >= 32:
                    senha += char_str
                    sys.stdout.write('*')
                    sys.stdout.flush()
            except UnicodeDecodeError:
                pass
    return senha


while True:
    print('\nBem-vindo ao sistema de login!')
    print('1 - Cadastrar')
    print('2 - Login')
    print('3 - Sair')

    opcao = input('Digite sua opção: ')

    if opcao == '1':
        usuario = input('Digite seu usuário: ')
        senha = obter_senha_mascarada('Digite sua senha: ')
        while True:
            cpf = input('Digite seu CPF (Dado Criptografado) ou 0 para voltar: ')
            if cpf.strip() == '0':
                print('Cadastro cancelado.')
                break
            
            cpf_limpo = "".join(filter(str.isdigit, cpf))
            if login.validar_cpf(cpf_limpo):
                cadastro = login.Cadastro(usuario, senha, cpf_limpo)
                sucesso, mensagem = cadastro.cadastrar()
                print(mensagem)
                break
            else:
                print('Erro: CPF inválido! Por favor, digite um CPF correto de 11 dígitos.')
    elif opcao == '2':
        tentativas = 3
        logado = False
        while tentativas > 0:
            print(f'\n--- Tentativa {4 - tentativas} de 3 ---')
            usuario = input('Digite seu usuário: ')
            senha = obter_senha_mascarada('Digite sua senha: ')
            log = login.Login(usuario, senha)
            
            sucesso, mensagem = log.logar()
            if sucesso:
                print("\n=========================================")
                print(mensagem)
                print("=========================================")
                logado = True
                exit()
            else:
                print(mensagem)
            
            tentativas -= 1
            if tentativas > 0:
                print(f'Você ainda tem {tentativas} tentativa(s).')
        
        if not logado:
            print('\nNúmero máximo de tentativas excedido. Encerrando o sistema...')
            exit()
            
    elif opcao == '3':
        print('Saindo do sistema.')
        exit()
    else:
        print('Opção inválida')