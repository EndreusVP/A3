import hashlib 
import json
import base64

# Chave simétrica usada para a criptografia (ideal para fins acadêmicos)
CHAVE_CRIPTOGRAFIA = "chave_secreta_a3"

def criptografar(dados, chave=CHAVE_CRIPTOGRAFIA):
    
    if not dados:
        return ""
    resultado = []
    for i, char in enumerate(dados):
        char_chave = chave[i % len(chave)]
        char_criptografado = chr(ord(char) ^ ord(char_chave))
        resultado.append(char_criptografado)
    dados_criptografados = "".join(resultado)
    return base64.b64encode(dados_criptografados.encode('utf-8')).decode('utf-8')

def descriptografar(dados_criptografados, chave=CHAVE_CRIPTOGRAFIA):
    if not dados_criptografados:
        return ""
    dados_decodificados = base64.b64decode(dados_criptografados.encode('utf-8')).decode('utf-8')
    resultado = []
    for i, char in enumerate(dados_decodificados):
        char_chave = chave[i % len(chave)]
        char_descriptografado = chr(ord(char) ^ ord(char_chave))
        resultado.append(char_descriptografado)
    return "".join(resultado)

def validar_cpf(cpf):
    """
    Validação oficial do CPF brasileiro utilizando algoritmo dos dígitos verificadores.
    """
    # Remove qualquer caractere que não seja número
    cpf = "".join(filter(str.isdigit, cpf))
    
    # CPF precisa ter 11 dígitos
    if len(cpf) != 11:
        return False
        
    # CPFs com todos os números iguais são inválidos
    if cpf == cpf[0] * 11:
        return False
        
    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito_1 = 0 if resto < 2 else 11 - resto
    
    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito_2 = 0 if resto < 2 else 11 - resto
    
    # Compara os dígitos calculados com os informados
    return int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2

def formatar_cpf(cpf):
    """
    Mascara o CPF no formato padrão XXX.XXX.XXX-XX
    """
    cpf = "".join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return cpf
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


class Cadastro():
    def __init__(self, usuario, senha, cpf):
        self.usuario = usuario
        self.senha = senha
        self.cpf = cpf

    def cadastrar(self):
        # Valida se foi inserido usuário, senha ou CPF
        if not self.usuario.strip() or not self.senha.strip() or not self.cpf.strip():
            return False, "Erro: Usuário, senha ou CPF vazios"
            
        # Validação do CPF
        cpf_limpo = "".join(filter(str.isdigit, self.cpf))
        if not validar_cpf(cpf_limpo):
            return False, "Erro: CPF inválido! Digite um CPF correto com 11 dígitos."
            
        # Ler todos os usuários da db
        try:
            with open("data/usuarios.json", "r") as f:
                usuarios = json.load(f)
        except FileNotFoundError:
            # Se o arquivo não existir inicia uma lista vazia
            usuarios = []
        except Exception as e:
            return False, f"Erro ao carregar banco de dados: {e}"

        for user in usuarios:
            if user.get("usuario") == self.usuario:
                return False, "Erro: Usuário já cadastrado"

        try:
            senha_hash = hashlib.sha256(self.senha.encode('utf-8')).hexdigest()
            # Salva o CPF limpo criptografado no JSON
            cpf_criptografado = criptografar(cpf_limpo)

            novo_usuario = {
                "usuario": self.usuario,
                "senha": senha_hash,
                "cpf": cpf_criptografado
            }
            usuarios.append(novo_usuario)
            with open("data/usuarios.json", "w") as f:
                json.dump(usuarios, f, indent=4)
            return True, "Usuário cadastrado com sucesso"
        except Exception as e:
            return False, f"Erro ao salvar usuário: {e}"


class Login():
    def __init__ (self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def logar(self):
        if not self.usuario.strip() or not self.senha.strip():
            return False, "Erro: Usuário ou senha vazios"
            
        # Ler usuários da db
        try:
            with open("data/usuarios.json", "r") as f:
                usuarios = json.load(f)
        except FileNotFoundError:
            return False, "Erro: Nenhum usuário cadastrado no sistema"
        except Exception as e:
            return False, f"Erro ao carregar banco de dados: {e}"

        # Gera o hash da senha informada para comparar
        try:
            senha_hash = hashlib.sha256(self.senha.encode('utf-8')).hexdigest()
        except Exception as e:
            return False, f"Erro ao processar senha: {e}"

        for user in usuarios:
            if user.get("usuario") == self.usuario:
                if user.get("senha") == senha_hash:
                    # Descriptografa e formata o CPF para exibir na tela pós-login
                    cpf_criptografado = user.get("cpf", "")
                    cpf_descriptografado = descriptografar(cpf_criptografado)
                    cpf_formatado = formatar_cpf(cpf_descriptografado)
                    
                    msg = (
                        f"Login realizado com sucesso!\n"
                        f"Bem-vindo, {self.usuario}!\n"
                        f"Seu CPF (descriptografado da base de dados) é: {cpf_formatado}"
                    )
                    return True, msg
                else:
                    return False, "Erro: Senha incorreta"

        return False, "Erro: Usuário não encontrado"
        