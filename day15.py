import requests

class Moeda:
    valorMoeda: float
    origemMoeda: str
    destinoMoeda: str

class Converter():

    def converterMoeda(self, valorMoeda, origemMoeda, destinoMoeda):
        url = f"https://api.exchangerate.host/convert?from={origemMoeda}&to={destinoMoeda}&amount={valorMoeda}"
        resposta = requests.get(url)
        dados = resposta.json()


        if resposta.status_code == 200 and "result" in dados:
            resultado = round(dados["result"], 2)
            print(f"{valorMoeda:.2f} {origemMoeda} = {resultado:.2f} {destinoMoeda}")
            return resultado
        else:
            return None

converter = Converter()

def menu():
    print("\n=== CONVERSOR DE MEODAS ===")
    valor = float(input("Digite o valor que deseja converter: "))
    origem = input("Moeda de origem (BRL, USD, EUR...): ").upper()
    destino = input("Moeda de destino (BRL, USD, EUR...): ").upper()

    converter.converterMoeda(valor, origem, destino)

menu()