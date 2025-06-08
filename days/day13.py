#CÁLCULO DE IP

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

    def __init__(self, arquivo="json/day13.json"):
        self.arquivo = arquivo
        self.lista_ip = self.carregarJson()
        self.ip = None

    def carregarJson(self):
        if not os.path.exists(self.arquivo):
            return []
        if os.stat(self.arquivo).st_size == 0:
            print("\nArquivo vazio")
            return []
        with open(self.arquivo, 'r') as file:
            print("\nAbrindo arquivo. . .")
            return json.load(file)

    def salvarJson(self, obj):
        self.lista_ip.append(obj.to_dict())
        with open(self.arquivo, 'w') as file:
            json.dump(self.lista_ip, file, indent=4)

    def calculoIp(self, ip_str):
        try:
            self.ip = ipaddress.ip_network(ip_str, strict=False)
            primeiro_ip = next(self.ip.hosts(), 'N/A')
            ultimo_ip = list(self.ip.hosts())[-1] if self.ip.num_addresses > 2 else primeiro_ip

            novo_ip = IP(
                ip=ip_str,
                rede=str(self.ip.network_address),
                broadcast=str(self.ip.broadcast_address),
                mascara=str(self.ip.netmask),
                prefixo=str(self.ip.prefixlen),
                totalHosts=str(self.ip.num_addresses - 2 if self.ip.num_addresses > 2 else 0),
                primeiroIp=str(primeiro_ip),
                ultimoIp=str(ultimo_ip)
            )

            self.salvarJson(novo_ip)
            self.mostrarDetalhes(novo_ip)

        except ValueError:
            print("\nIP INVÁLIDO")
            self.ip = None

    def mostrarDetalhes(self, ip_obj):
        print("\nIP VÁLIDO:")
        print(f"IP: {ip_obj.ip}")
        print(f"Rede: {ip_obj.rede}")
        print(f"Broadcast: {ip_obj.broadcast}")
        print(f"Máscara: {ip_obj.mascara}")
        print(f"Prefixo: /{ip_obj.prefixo}")
        print(f"Total de hosts: {ip_obj.totalHosts}")
        print(f"Primeiro IP útil: {ip_obj.primeiroIp}")
        print(f"Último IP útil: {ip_obj.ultimoIp}")

    def mostrarTodosIps(self):
        if not self.lista_ip:
            print("\nNenhum IP salvo")
            return
        print("\n=== IPs SALVOS ===")
        for i, ip in enumerate(self.lista_ip, start=1):
            print(f"\n--- Registro {i} ---")
            print(f"IP: {ip['ip']}")
            print(f"Rede: {ip['rede']}")
            print(f"Broadcast: {ip['broadcast']}")
            print(f"Máscara: {ip['mascara']}")
            print(f"Prefixo: /{ip['prefixo']}")
            print(f"Total de hosts: {ip['totalHosts']}")
            print(f"Primeiro IP útil: {ip['primeiroIp']}")
            print(f"Último IP útil: {ip['ultimoIp']}")

def menu():
    calculo = Calculo()

    while True:
        print("\n=== CÁLCULO DE IPv4 ===")
        print("Pressione '0' para sair")
        print("Pressione 1 para listar todos os IPs salvos")
        ipNovo = input("Digite o IPv4 com prefixo (ex: 192.168.0.0/24): ")
        
        if ipNovo == "1":
            calculo.mostrarTodosIps()

        if ipNovo == "0":
            break

        calculo.calculoIp(ipNovo)

menu()
