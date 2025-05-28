#VALIDAÇÃO DE DADOS POR MEIO DE CPF
import json
import os

class User():
    def __init__(self, nomeUser, cpfUser, idadeUser):
        self.nomeUser = nomeUser
        self.cpfUser = cpfUser
        self.idadeUser = idadeUser

    def to_dict(self):
        return{
            "nomeUser": self.nomeUser,
            "cpfUser": self.cpfUser,
            "idadeUser": self.idadeUser
        }
    
class Cadastro():
    def __init__(self, arquivo = "day11.json"):
        self.arquivo = arquivo
        self.user = self.carregarArquivo() or []

    def carregarArquivo(self):
        if not os.path.exists(self.arquivo):
            print("\nArquivo não existente. Criando um. . . ")
            return[]
        if os.stat(self.arquivo).st_size == 0:
            return[]
        with open(self.arquivo, 'r') as file:
            return json.load(file)
        
    def adicionarUser(self, user, cpf):
        for u in self.user:
            if u['cpfUser'] == cpf:
                print("\nCPF já cadastrado")
                return False
        
        self.user.append(user.to_dict())
        self.salvarUser()
        print("Usuário cadastrado com sucesso")
        return True

    def salvarUser(self):
        with open(self.arquivo, 'w') as file:
            json.dump(self.user, file, indent = 4)

    def consultaUser(self, cpf):
        for u in self.user:
            if u['cpfUser'] == cpf:
                print(f"\nUsuário encontrado: {u['nomeUser']} - {u['cpfUser']} - {u['idadeUser']}")
                return
            
        print("\nUsuário não encontrado")

    def listarUser(self):
        for u in self.user:
            print(f"{u['nomeUser']} - {u['cpfUser']} - {u['idadeUser']}")
        
cadastro = Cadastro()

print("\n=== VALIDAÇÃO DE DADOS POR CPF ===")

def menu():
    while True:
        print("\n1 - CADASTRAR USUÁRIO")
        print("2 - CONSULTAR USUÁRIO")
        print("3 - LISTAR USUÁRIOS")
        print("0 - SAIR")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            nome = input("\nDigite o nome do usuário: ")
            cpf = input("Digite o cpf do usuário: ")
            idade = input("Digite a idade do usuário: ")
            novo = User(nome, cpf, idade)
            cadastro.adicionarUser(novo, cpf)

        elif opcao == "2":       
            cpf = input("\nDigite o CPF do usuário: ")  
            cadastro.consultaUser(cpf)

        elif opcao == "3":
            cadastro.listarUser()

        elif opcao == "0":
            print("\nFINALIZANDO PROGRAMA. . .")

        else:
            print("\n*OPÇÃO INVÁLIDA, TENTE NOVAMENTE*")

menu()