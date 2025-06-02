#VARREDURA DE PORTAS

import socket
from datetime import datetime
import json
import os
from dataclasses import dataclass, asdict
from tqdm import tqdm
import sys

@dataclass
class IP():
    host: str
    portaInicial: str
    portaFinal: str
    horaInicio: str
    horaFim: str

    def to_dict(self):
        return asdict(self)

def caminhoJson(nomeArquivo):
    if getattr(sys, 'frozen', False):
        caminhoBase = sys._MEIPASS
    else:
        caminhoBase = os.path.abspath(".")
    return os.path.join(caminhoBase, nomeArquivo)

class Scan():
    def __init__(self):
        self.arquivo = caminhoJson("json/day14.json")
        self.portas = self.carregarJson()

    def carregarJson(self):
        if not os.path.exists(self.arquivo):
            return []
        if os.stat(self.arquivo).st_size == 0:
            return []
        with open(self.arquivo, 'r') as file:
            print("\nAbrindo arquivo. . .")
            return json.load(file)

    def salvarScan(self):
        with open(self.arquivo, 'w') as file:
            json.dump(self.portas, file, indent=4)

    def listarScan(self):
        for i, item in enumerate(self.portas, start=1):
            print(f"\nRegistro {i}: {item.get('host')} {item.get('portaInicial')} - {item.get('portaFinal')} | {item.get('horaInicio')} → {item.get('horaFim')}")

    def scanner(self, host, portaInicial, portaFinal):
        inicio = datetime.now()
        print(f"\nIniciando scanner em {host} de {portaInicial} até {portaFinal}")
        print(f"Hora de início: {inicio}\n")

        try:
            for porta in tqdm(range(portaInicial, portaFinal + 1)):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                resultado = sock.connect_ex((host, porta))

                if resultado == 0:
                    print(f" Porta {porta}: ABERTA")
                sock.close()

        except KeyboardInterrupt:
            print("\nScanner interrompido pelo usuário.")
        except socket.gaierror:
            print("\nErro: nome de host inválido.")
        except socket.error:
            print("\nErro ao conectar ao servidor.")

        fim = datetime.now()
        print(f"\nHora do término: {fim}")

        registro = IP(
            host=host,
            portaInicial=str(portaInicial),
            portaFinal=str(portaFinal),
            horaInicio=str(inicio),
            horaFim=str(fim)
        )

        self.portas.append(registro.to_dict())
        self.salvarScan()

# Instância do scanner
scan = Scan()

def menu():

    while (True):
        print("=== SCANNER DE PORTAS ===")
        print("--- 1 SCANNEAR HOST ---")
        print("--- 2 LISTAR TODAS OS HOSTS/PORTAS SCANNEADAS ---")
        print("--- 0 PARA SAIR ---")
        opcao = input("ESCOLHA A OPÇÃO: ")


        match opcao: 
            case "1":
                alvo = input("Digite o IP ou hostname para escanear: ")
                scanner1 = int(input("Digite a porta inicial: "))
                scanner2 = int(input("Digite a porta final: "))
                scan.scanner(alvo, scanner1, scanner2)

            case "2":
                scan.listarScan()

            case "0":
                break


if __name__ == "__main__":
    menu()
    input("\nPressione Enter para sair. . . ")
