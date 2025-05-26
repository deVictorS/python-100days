#CADASTRO DE CONTATO USANDO JSON E CLASSE

import json
import os

print("\n=== CADASTRO DE CONTATO ===")

#CADASTRAR CONTATO
class Contato():
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
    
    #CRIAÇÃO DO DICIONÁRIO
    def to_dict(self):
        return{
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email
        }

#MANIPULAR O ARQUIVOS
class Agenda():
    def __init__(self, arquivo = 'day9.json'):
        self.arquivo = arquivo
        self.contatos = self.carregarContatos()

    def carregarContatos(self):
        if not os.path.exists(self.arquivo):
            return[]
        
        if os.stat(self.arquivo).st_size == 0:
            return[]
        
        with open(self.arquivo, 'r') as file:
            return json.load(file)
        
    def salvarContato(self):
        with open(self.arquivo, 'w') as file:
            json.dump(self.contatos, file, indent = 4)
        
    def cadastrarContato(self, contato):
        self.contatos.append(contato.to_dict())
        self.salvarContato()

    def buscarContato(self, nome):
        for contato in self.contatos:
            if contato['nome'].lower() == nome.lower():
                print(f"Contato encontrado: {contato['nome']} - {contato['telefone']} - {contato['email']}")
                return
        print("Contato não encontrado")    

    def removerContato(self):
        remover = input("Digite o nome do contato a ser removido: ").lower()
        contatos_filtrados = [c for c in self.contatos if c['nome'].lower() != remover]

        if len(contatos_filtrados) < len(self.contatos):
            self.contatos = contatos_filtrados
            self.salvarContato()
            print("Contato removido com sucesso.")
        else:
            print("Contato não encontrado.")

    def listarContatos(self):
        for contato in self.contatos:
            print(f"{contato['nome']} - {contato['email']} - {contato['telefone']}")

    def atualizarContato(self):
        atualizar = input("Digite o nome do contato a ser atualizado: " ).lower()

        for contato in self.contatos:
            if contato ['nome'].lower() ==  atualizar:
                print(f"\nContato encontrado: {contato['nome']} - {contato['telefone']} - {contato['email']}")

                novoNome = input("Atualize pelo novo nove ou pressione enter para manter: ")
                novoTelefone = input("Atualize o novo telefone ou pressione enter para manter:") 
                novoEmail = input("Atualize o novo email ou pressione enter para manter: ") 

            if novoNome:
                contato["nome"] = novoNome
            if novoTelefone:
                contato["telefone"] = novoTelefone
            if novoEmail:
                contato["email"] = novoEmail

            self.salvarContato()
            print("Contato atualizado com suscesso")
            return
        
agenda = Agenda()

#MENU
def menu():
    while True:
        print("\n1 - CADASTRAR CONTATO")
        print("2 - REMOVER CONTATO")
        print("3 - PROCURAR POR CONTATO")
        print("4 - LISTAR TODOS OS CONTATOS")
        print("5 - ATUALIZAR CONTATO")
        print("0 - SAIR")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            novo = Contato(nome, telefone, email)
            agenda.cadastrarContato(novo)

        if opcao == "2":
            agenda.removerContato()

        if opcao == "3":
            nome = input("Nome do contato: ")
            agenda.buscarContato(nome)

        if opcao == "4":
            agenda.listarContatos()

        if opcao == "5":
            agenda.atualizarContato()

        if opcao == "0":
            print("ENCERRANDO PROGRAMA. . .")
            break

menu()       