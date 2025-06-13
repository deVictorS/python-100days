#CRIPTOGRAFIA DE ARQUIVOS

from cryptography.fernet import Fernet

files = []
arquivo = "txt/day21.txt"

key = Fernet.generate_key()

with open("keys/chave.key", 'wb') as chave:
    chave.write(key)

files.append(arquivo)

for file in files:
    with open(file, 'rb') as arquivos:
        conteudo = arquivos.read()
    conteudo_encrypted = Fernet(key).encrypt(conteudo)

    with open(file, 'wb') as arquivo:
         arquivo.write(conteudo_encrypted)
