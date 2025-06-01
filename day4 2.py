#CADASTRO DE NOMES

print("---CADASTRO DE NOMES---")

nomes = []

while True:
    print("\n1 - Inserir nomes")
    print("2 - Mostrar nomes da lista")
    print("0 - Sair")


    opcao = input("\nEscolha uma opção: ")

    #INSERE 5 NOMES NA LISTA
    if opcao == "1":
        for i in range(5):
            nome = input(f"Digite o {i + 1}º nome: ")
            nomes.append(nome)
            
        
        print("Nomes adicionados:", ", ".join(nomes))

    #MOSTRA QUAIS NOMES COMEÇAM OU NÃO COM VOGAL/QUANTIDADE DE LETRAS E QUANTIDADE DE VOGAIS
    elif opcao == "2":
        for i, nome in enumerate(nomes, start = 1):
            vogal = nome[0].lower() in 'aeiou'
            statusVogal = "começa com vogal" if vogal else "não começa com vogal"
            print(f"{i}º nome:", nome, "tem", len(nome), "letras", "e", statusVogal)

    elif opcao == "0":
        print("---SAINDO DO PROGRAMA---")
        break        



    