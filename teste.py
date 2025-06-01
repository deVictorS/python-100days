import requests

class Moeda:
    def __init__(self, valorMoeda: float, origemMoeda: str, destinoMoeda: str):
        self.valorMoeda = valorMoeda
        self.origemMoeda = origemMoeda.upper()
        self.destinoMoeda = destinoMoeda.upper()

class Converter:

    def converterMoeda(self, moeda: Moeda):
        url = f"https://api.exchangerate.host/convert?from={moeda.origemMoeda}&to={moeda.destinoMoeda}&amount={moeda.valorMoeda}"
        resposta = requests.get(url)
        dados = resposta.json()

        if resposta.status_code == 200 and "result" in dados:
            resultado = round(dados["result"], 2)
            print(f"{moeda.valorMoeda:.2f} {moeda.origemMoeda} = {resultado:.2f} {moeda.destinoMoeda}")
            return resultado
        else:
            print("Erro na conversão. Verifique os dados ou sua conexão.")
            return None

converter = Converter()

def menu():
    while True:
        print("\n=== CONVERSOR DE MOEDAS ===")
        try:
            valor = float(input("Digite o valor que deseja converter: "))
        except ValueError:
            print("Valor inválido. Tente novamente.")
            continue

        origem = input("Moeda de origem (BRL, USD, EUR...): ").upper()
        destino = input("Moeda de destino (BRL, USD, EUR...): ").upper()

        moeda = Moeda(valor, origem, destino)
        converter.converterMoeda(moeda)

        continuar = input("\nDeseja converter outro valor? (s/n): ").lower()
        if continuar != 's':
            break

menu()
