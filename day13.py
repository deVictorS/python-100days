#CÁLCULO E VALIDAÇÃO DE IP

import json
import os
from dataclasses import dataclass, asdict
import ipaddress

@dataclass
class IP():
    ip: str
    rede: str
    broadcast: str
    mascara: str
    prefixo: str
    totalHosts: str
    primeiroIp: str
    ultimoIp: str

    def to_dict(self):
        return asdict(self)
    
class Calculo():

    def __init__(self, arquivo = "day13.json"):
        self.arquivo = arquivo
        self.ip = self.carregarJson()

    def carregarJson(self):
        if not os.path.exists(self.arquivo):
            return[]
        
        if os.stat(self.arquivo).st_size == 0:
            print("\nArquivo vazio")
            return[]
        
        with open(self.arquivo, 'r') as file:
            print("\nAbrindo arquivo. . .")
            return json.load(file)
        
    def calculoIp(self, ip):
        try:
            self.ip = ipaddress.ip_network(ip, strict = False)
        
        except ValueError:
            self.ip = None

    def validar(self):
        return self.ip is not None
    
    def mostrarDetalhes(self):
        if not self.validar():
            print("\nIP INVÁLIDO")
            return
        
        print("\nIP VÁLIDO: ")
        print(f"Rede: {self.ip.network_address}")
        print(f"Broadcast: {self.ip.broadcast_address}")
        print(f"Máscara: {self.ip.netmask}")
        print(f"Prefixo: /{self.ip.prefixlen}")
        print(f"Total de hosts: {self.ip.num_addresses}")
        print(f"Primeiro IP útil: {list(self.ip.hosts()[0])}")
        print(f"Último IP útil: {list(self.ip.hosts()[-1])}")
        
calculo = Calculo()

def menu():
    
    while True:

        print("\n=== CÁLCULO DE IPv4 ===")
        print("Pressione '0' para sair")
        ipNovo = input("Digite o IPv4 com prefixo: ")
        novo = IP(ipNovo)
        calculo.calculoIp(novo)


        if ipNovo == "0":
            break

menu()


