#DIA 3: CRIAÇÃO DE UMA AGENDA DIÁRIA USANDO LISTA

print("\n---AGENDA DIÁRIA---") #PRINT DO OBJETIVO DO PROGRAMA

tarefas = [] #CRIAÇÃO DA LISTA

#CRIAÇÃO DE UM MENU USANDO WHILE
while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Sair")

    opcao = input("\nEscolha uma opção:") #CRIA A VARIÁVEL OPCAO PARA RECEBER A ESCOLHA DO USUÁRIO

    #SE O USUÁRIO ESCOLHE 1: SOLICITA NOVA TAREFA QUE É ARMAZENADA NA LISTA POR MEIO DO .append
    if opcao == "1":
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa) 
        print("Tarefa adicionada!")

    #SE O USUÁRIO ESCOLHE 2: EXIBE TODAS AS TEREFAS JÁ INSERIDAS PELO USUÁRIO
    elif opcao == "2":
        if tarefas:
            print("\n---TAREFAS DO DIA---")
            for i, tarefa in enumerate(tarefas, start=1): #ENUMERA TODAS AS TEREFAS DA LISTA COMEÇANDO PELA PRIMEIRA
                print(f"{i}. {tarefa}") #PRINTA AS TAREFAS DA LISTA POR MEIO DO FOR (I = O ÍNDICE NA LISTA; TAREFA = TODA A LISTA) MAIÚSCULO
        else:
            print("Nenhuma tarefa adicionada ainda") #SE NÃO HÁ TAREFAS

    #SE O USUÁRIO ESCOLHE 2: PAUSA O PROGRAMA
    elif opcao == "3":
        print("\nSaindo da agenda. Bom dia!")
        break #Pausa o while    

    #SE O USUÁRIO DIGITA QUALQUER COISA ALÉM DE 1, 2 OU 3
    else:
        print("\nOpção inválida. Tente novamente.")              

