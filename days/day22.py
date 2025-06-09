#DESCRIPTOGRAFIA DE ARQUIVOS

from cryptography.fernet import Fernet

files = []

arquivo = "txt/day21.txt"

with open("keys/chave.key", 'rb') as chave:
    key = chave.read()

files.append(arquivo)

for file in files:
    with open(file, 'rb') as arquivos:
        conteudo = arquivos.read()
    conteudo_descryptded = Fernet(key).decrypt(conteudo)

    with open(file, 'wb') as arquivo:
         arquivo.write(conteudo_descryptded)