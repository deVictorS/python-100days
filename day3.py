print("\n---AGENDA DIÁRIA---")

tarefas = [] #Criação de lista:

#Criação de um menu usando while:
while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Sair")

#Adicionar nova tarefa

    opcao = input("\nEscolha uma opção:")

    if opcao == "1":
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa) #Adiciona nova tarefa na lista por meio do append
        print("Tarefa adicionada!")

#Exibição de tarefas
    elif opcao == "2":
        if tarefas:
            print("\n---TAREFAS DO DIA---")
            for i, tarefa in enumerate(tarefas, start=1): #Enumera toda a lista começando pelo primeiro elemento
                print(f"{i}. {tarefa}") #Printa as tarefas da lista por meio do for (i = o índice na lista; tarefa = toda a lista)
        else:
            print("Nenhuma tarefa adicionada ainda")

#Sair do menu/pausar código
    elif opcao == "3":
        print("\nSaindo da agenda. Bom dia!")
        break #Pausa o while    

#Boas práticas de inserção de dados
    else:
        print("\nOpção inválida. Tente novamente.")              

