#DIA 3: CRIAÇÃO DE UMA AGENDA DIÁRIA USANDO LISTA

print("\n---AGENDA DIÁRIA---")

tarefas = []

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Sair")

    opcao = input("\nEscolha uma opção:") 

    if opcao == "1":
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa) 
        print("Tarefa adicionada!")

    elif opcao == "2":
        if tarefas:
            print("\n---TAREFAS DO DIA---")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}") 
        else:
            print("Nenhuma tarefa adicionada ainda")

    elif opcao == "3":
        print("\nSaindo da agenda. Bom dia!")
        break   

    else:
        print("\nOpção inválida. Tente novamente.")              

