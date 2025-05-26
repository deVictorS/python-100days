#CRUD COM CADASTRO DE USUÁRIOS

users = [] 

#CRIAÇÃO DA FUNÇÃO PARA CADASTAR USUÁRIO E INSERIR OS DADOS NA LISTA
def cadastrarUser():
    nome = input("\nDigite o nome do usuário: ").strip().upper()
    cpf = input("Digite o CPF do usuário: ").strip().upper()
    idade = input("Digite a idade do usuário: ").strip().upper()

    user = {'nome': nome, 'cpf': cpf, 'idade': idade}
    users.append(user)

    print("\n=== USUÁRIO CADASTRADO COM SUCESSO ===")
    print(f"\n{user['nome']} - {user['cpf']} - {user['idade']}")

#CRIAÇÃO DA FUNÇÃO PARA LISTAR USUÁRIOS PRESENTES NA LISTA
def listarUser():
    for i, user in enumerate(users, 1):
        print(f"{i} - {user['nome']} - {user['cpf']} - {user['idade']}")

    if not users:
        print("Nenhum usuário cadastrado")

#CRIAÇÃO DA FUNÇÃO PARA BUSCAR USUÁRIO PELO CPF
def buscarUser():
    busca = input("\nDigite o CPF do usuário: ").strip().upper()
    encontrado = [user for user in users if user['cpf'].upper() == busca]

    if encontrado:
        for user in encontrado:
            print(f"Usuário encontrado: {user['nome']} - {user['cpf']} - {user['idade']}")

    else:
        print("Usuário não encontrado")    

#CRIAÇÃO DA FUNÇÃO QUE REMOVE O USUÁRIO DA LISTA
def removerUser():
    remover = input("Digite o CPF do usuário a ser removido da lista: ").strip().upper()
    removido = [user for user in users if user['cpf'].upper() == remover]

    if removido:
        for user in removido:
            users.remove(user)
            print("\nUsuário removido com sucesso")

    else:
        print("Usuário não encontrado")        


print("\n=== CADASTRO DE USUÁRIOS ===")

#CRIAÇÃO DA FUNÇÃO MENU
def menu():
    while True:

        print("\n1 - CADASTRAR USUÁRIO")
        print("2 - LISTAR USUÁRIOS")
        print("3 - BUSCAR USUÁRIO PELO CPF")
        print("4 - REMOVER USUÁRIO")
        print("0 - SAIR")

        opcao = input("Escolha uma opção: ")

        #USUÁRIO ESCOLHE UMA OPÇÃO QUE DIRECIONA PARA A DEVIDA FUNÇÃO A SER EXECUTADA
        if opcao == "1":
            cadastrarUser()
            

        elif opcao == "2":
            listarUser()
            

        elif opcao == "3":
            buscarUser()
            

        elif opcao == "4":
            removerUser()
            
        elif opcao == "0":
            print("\n=== SAINDO DO PROGRAMA ===")
            break   

        else:
            print("Opção inválida, tente novamente")         

menu()


