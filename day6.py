#CADASTRAR PESSOAS E INSERIR NUMA LISTA .TXT

#PRINT DO OBJETIVO DO CÓDIGO
print("\n=== CADASTRO DE PESSOAS ===")

#SOLICITA A INSERÇÃO DE ATÉ 3 NOMES
for i in range(3):
    nome = input(f"\nDigite o nome da {i + 1}º pessoa: ")
    with open("day6.txt", 'a', encoding='utf-8') as arquivo: #ABRE O ARQUIVO day6.txt, PERMITE A INSERÇÃO DE DADOS E ESCRITA, LINGUAGEM PT-BR
        arquivo.write(nome + "\n")                           #NOMEIA O ARQUIVO COMO arquivo E ESCREVE OS NOMES LINHA A LINHA NO MESMO

print("\nLista cadastrada com sucesso!") 

with open("day6.txt", 'r', encoding='utf-8') as arquivo: #ABRE O ARQUIVO COM PERMISSÃO DE LEITURA E EXIBE AS PESSOAS CADASTRADAS
    print("\nLista de pessoas cadastradas: ")
    print(arquivo.read())
