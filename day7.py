#CADASTRO DE LIVRO COM AUTOR E ANO USANDO DICIONÁRIO

print("=== CADASTRO DE LIVROS ===")

livros = []

while True:
    print("\n1 - Cadastrar livro: ")
    print("2 - Buscar por nome do livro: ")
    print("3 - Buscar por gênero do livro")
    print("4 - Listar todos os livros")
    print("0 - Sair")

    opcao = input("\nDigite uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o autor do livro: ")
        genero = input("Digite o gênero do livro: ")
        ano = input("Digite o ano de lançamento do livro: ")

        livro = {"nome": nome, "autor": autor, "genero": genero,"ano": ano}
        livros.append(livro)

        print("\n=== LIVRO CADASTRADO COM SUCESSO ===")
        print(f"\n{livro['nome']} -  {livro['autor']} - {livro['genero']} - {livro['ano']}")

    elif opcao == "2":
        busca = input("Digite o nome do livro: ").lower()
        encontrado = [livro for livro in livros if livro['nome'].lower() == busca]

        if encontrado:
            for livro in encontrado:
                print(f"Livro encontrado: {livro['nome']} - {livro['autor']} - {livro['ano']}")

        else:
            print("Livro não encontrado")   


    elif opcao == "3":
        buscar = input("Digite o gênero do livro: ").lower()
        filtrado = [livro for livro in livros if livro['genero'].lower() == buscar]

        if filtrado:
            for livro in filtrado:
                print(f"Livros encontrados com esse genero: {livro['nome']} - {livro['autor']} - {livro['genero']} - {livro['ano']}")

        else:
            print("Não foi encontrado nenhum livro com esse gênero")

    elif opcao == "4":
        for i, livro in enumerate(livros, 1):
            print(f"{i} - {livro['nome']} - {livro['autor']} - {livro['genero']} - {livro['ano']}")

        if not livros:
            print("Nenhum livro cadastrado")

    elif opcao == "0":
        print("\n=== DESLIGANDO ===")
        break            