print("\n---SISTEMA DE ESTOQUE---")

produtos = []

while True:
    print("\n1 - ADICIONAR PRODUTO")
    print("2 - LISTAR TODOS OS PRODUTOS")
    print("3 - CONSULTAR PRODUTOS")
    print("0 - SAIR")

    opcao = input("\nESCOLHA UMA OPÇÃO: ")

    if opcao == "1":
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        qntd = int(input("Quantidade em estoque: "))

        #Criação do dicionário
        produto = {"nome": nome, "preco": preco, "qntd": qntd}

        #Inserção dentro da lista
        produtos.append(produto)

        print("\n---PRODUTO CADASTRADO---")

    elif opcao == "2":
        print("\n---LISTA DOS PRODUTOS---")
        for i, p in enumerate(produtos, 1):
            print(f"{i}. {p['nome']} - R$ {p['preco']:.2f} - Estoque: {p['qntd']}")


    elif opcao == "3":
        busca = input("Digite o nome do produto: ").lower()
        encontrados = [p for p in produtos if p['nome'].lower() == busca]
                
        if encontrados:
            for p in encontrados:
                print(f"\nProduto encontrado: {p['nome']} - R$ {p['preco']:.2f} - Estoque: {p['qntd']}")
        
        else:
            print("Produto não encontrado")

    elif opcao == "0":
        print("\n---SAINDO DO SISTEMA---")
        break        
