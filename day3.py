#DIA 3: CRIAÇÃO DE UMA AGENDA DIÁRIA USANDO LISTA

print("\n---AGENDA DIÁRIA---")

#CRIAÇÃO DA LISTA
tarefas = []

#CRIAÇÃO DE UM MENU USANDO WHILE
while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Sair")

    #CRIA A VARIÁVEL OPCAO PARA RECEBER A ESCOLHA DO USUÁRIO
    opcao = input("\nEscolha uma opção:") 

    #SE O USUÁRIO ESCOLHE 1: SOLICITA NOVA TAREFA QUE É ARMAZENADA NA LISTA POR MEIO DO .append
    if opcao == "1":
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa) 
        print("Tarefa adicionada!")

    #SE O USUÁRIO ESCOLHE 2: EXIBE TODAS AS TEREFAS JÁ INSERIDAS PELO USUÁRIO
    elif opcao == "2":
        if tarefas:
            print("\n---TAREFAS DO DIA---")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}") 
        else:
            print("Nenhuma tarefa adicionada ainda") #SE NÃO HÁ TAREFAS

    #SE O USUÁRIO ESCOLHE 2: PAUSA O PROGRAMA
    elif opcao == "3":
        print("\nSaindo da agenda. Bom dia!")
        break #Pausa o while    

    #SE O USUÁRIO DIGITA QUALQUER COISA ALÉM DE 1, 2 OU 3
    else:
        print("\nOpção inválida. Tente novamente.")              

