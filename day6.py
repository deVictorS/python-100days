print("\n=== CADASTRO DE PESSOAS ===")

for i in range(3):
    nome = input(f"\nDigite o nome da {i + 1}º pessoa: ")
    with open("day6.txt", 'a', encoding='utf-8') as arquivo:
        arquivo.write(nome + "\n")

print("\nLista cadastrada com sucesso!") 

with open("day6.txt", 'r', encoding='utf-8') as arquivo:
    print("\nLista de pessoas cadastradas: ")
    print(arquivo.read())
