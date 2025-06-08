import os
import json
import hashlib
from dataclasses import dataclass, asdict

@dataclass
class User():
    emailUser: str
    nomeUser: str
    senhaUser: str
       
    def to_dict(self):
        return asdict(self)
    
class Gerenciador():
    def __init__(self, arquivo = "json/day19.json"):
        self.arquivo = arquivo
        self.usuarios = self.carregarArquivo()

    def carregarArquivo(self):
        if not os.path.exists(self.arquivo):
            print("\nArquivo inexistente, criando arquivo JSON. . .")
            return[]
        
        if os.stat(self.arquivo).st_size == 0:
            return[]
            
        with open(self.arquivo, 'r') as file:
            return json.load(file)
        
    def adicionarUser(self, user: User):

        for u in self.usuarios:
            if u['emailUser'] == user.emailUser:
                print("\nEmail já cadastrado")
                return

        self.usuarios.append(user.to_dict())
        self.salvarUser()
        print("\nUsuário cadastrado com sucesso!")

    def salvarUser(self):
        with open(self.arquivo, 'w') as file:
            json.dump(self.usuarios, file, indent = 4)

    @staticmethod
    def hashSenha(senhaUser):
        return hashlib.sha256(senhaUser.encode()).hexdigest()
    
    def autenticar(self, email, senha):
        senhaHash = self.hashSenha(senha)
        for u in self.usuarios:
            if u['emailUser'] == email and u['senhaUser'] ==senhaHash:
                return u['nomeUser']
        return None


gerenciador = Gerenciador()

def menu():
    while True:
        print("\n=== AUTENTICAÇÃO ===")
        print("1 - LOGIN")
        print("2 - CADASTRO")
        print("0 - SAIR")
        opcao = input("Escolha uma opção: ")

        match opcao:

            case "1":
                print("\n--- LOGIN DE USUÁRIO ---")
                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")

                nome = gerenciador.autenticar(email, senha)

                if nome:
                    print(f"\nBem vindo(a), {nome}!")

                else:
                    print("\nEmail ou senha inválidos")
            
            case "2":
                print("\n--- CADASTRO DE USUÁRIO ---")
                email = input("Digite o email: ")
                nome = input("Digite o nome: ")

                while True:
                    senha = input("Digite a senha: ")
                    confirmacao = input("Confirme a senha: ")

                    if senha == confirmacao:
                        break
                    
                    print("\nSenhas não coincidem, tente novamente:")

                
                senhaHash = gerenciador.hashSenha(senha)
                novoCadastro = User(email, nome, senhaHash)
                gerenciador.adicionarUser(novoCadastro)

            case "3":
                break


menu()