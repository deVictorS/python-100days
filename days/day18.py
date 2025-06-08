import requests
from datetime import datetime
import json

def obterDados():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

    try:
        resposta = requests.get(url)
        dados = resposta.json()

        cotacao = {
        
            "Dolar": float(dados['USDBRL']['bid']),
            "Euro": float(dados['EURBRL']['bid']),
            "Bitcoin": float(dados['USDBRL']['bid']),
            "Data" :datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return cotacao
    except Exception as e:
        print("Erro ao obter dados", e)
        return None
    
def salvarCotacao(cotacao):
    caminho = "json/day18.json"
    with open(caminho, 'w') as arquivo:
        json.dump(cotacao, arquivo, indent = 4)
    print(f"\nArquivo salvo em {caminho}")



    
def mostrarDados():
    cotacao = obterDados()
    hoje = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    if cotacao:
        print(f"\n=== COTAÇÃO DIA {hoje} ===")
        for moeda, valor in cotacao.items():
            if moeda != "Data":
                print(f"{moeda}: R$ {valor:.2f}")
        salvarCotacao(cotacao)

mostrarDados()