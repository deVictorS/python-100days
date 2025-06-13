#GERAÇÃO DE POSSÍVEIS USUÁRIOS

nomes = []
sobrenomes = []
caracteres = []
dominio = ""

with open("txt/wordlists/username.txt", 'w') as file:
    for nome in nomes:
        for sobrenome in sobrenomes:
            combinacoes = [
            (f"{nome}@{dominio}"),
            (f"{sobrenome}@{dominio}"),
            (f"{sobrenome}.{nome}@{dominio}"),
            (f"{nome}.{sobrenome}@{dominio}")
            ]
            
            for usuario in combinacoes:
                file.write(usuario + "\n")

print("\nArquivo gerado\n")
