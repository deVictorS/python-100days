nomes = []
sobrenomes = []
dominios = []
numeros = []
caracteres = []

with open("txt/wordlists/password.txt", 'w') as file:
    for nome in nomes:
        for sobrenome in sobrenomes:
            for dominio in dominios:
                for numero in numeros:
                    for simbolo in caracteres:
                        combinacoes = [
                            f"{nome}{numero}",
                            f"{nome.capitalize()}{numero}",
                            f"{nome}{sobrenome}{numero}",
                            f"{sobrenome}{nome}{numero}",
                            f"{nome}{dominio}{numero}{simbolo}",
                            f"{nome}_{sobrenome}{numero}{simbolo}",
                            f"{nome.capitalize()}{sobrenome.capitalize()}{numero}{simbolo}",
                            f"{sobrenome.capitalize()}{nome}{simbolo}",
                            f"{nome}@{dominio}.com",
                            f"{nome}{sobrenome}{simbolo}{numero}",
                        ]

                        for senha in combinacoes:
                            file.write(senha + "\n")

print("\nArquivo gerado\n")