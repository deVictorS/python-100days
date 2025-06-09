# MONITORAMENTO DE PORTAS

import psutil
import time
from datetime import datetime
import os
from dataclasses import dataclass, asdict
import json
import socket

JSON_FILE = "json/day20.json"
JSON_SAIDA = "json/day20_saida.json"

@dataclass
class Porta:
    portas: str
    processo: str
    caminho: str
    hora_inicial: str
    hora_final: str

    def to_dict(self):
        return asdict(self)

class Scan:

    def __init__(self):
        self.arquivo = JSON_FILE
        self.portas = self.carregar_json()

    def carregar_json(self):
        if not os.path.exists(self.arquivo):
            return []
        if os.stat(self.arquivo).st_size == 0:
            return []
        with open(self.arquivo, 'r') as file:
            print("\nAbrindo arquivo. . .")
            return json.load(file)

    def salvar_scan(self):
        with open(self.arquivo, 'w') as file:
            json.dump(self.portas, file, indent=4)

    def listar_scan(self):
        for i, item in enumerate(self.portas, start=1):
            print(f"\nRegistro {i}: Porta {item.get('portas')}")
            print(f"Processo: {item.get('processo')}")
            print(f"Caminho: {item.get('caminho')}")
            print(f"Início: {item.get('hora_inicial')} | Fim: {item.get('hora_final')}")

    def monitorar(self, lista_portas):
        print(f"\nMONITORANDO PORTAS {lista_portas}... PRESSIONE Ctrl+C PARA PARAR.")
        estado_anterior = {}

        try:
            while True:
                for porta in lista_portas:
                    porta_em_uso = False
                    processo = "Não em uso"
                    caminho = "---"

                    conexoes = psutil.net_connections(kind='inet')

                    for conn in conexoes:
                        if conn.laddr.port == porta:
                            porta_em_uso = True
                            try:
                                proc = psutil.Process(conn.pid)
                                processo = proc.name()
                                caminho = proc.exe()
                            except:
                                processo = "Desconhecido"
                                caminho = "Acesso negado"
                            break

                    chave = f"{porta}-{processo}-{caminho}"
                    if estado_anterior.get(porta) != chave:
                        estado_anterior[porta] = chave
                        hora_atual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                        log = Porta(
                            portas=str(porta),
                            processo=processo,
                            caminho=caminho,
                            hora_inicial=hora_atual,
                            hora_final=hora_atual
                        )
                        self.portas.append(log.to_dict())
                        status = "USO" if porta_em_uso else "LIVRE"
                        print(f"[{status}] Porta {porta} | {processo} | {caminho} | {hora_atual}")

                self.salvar_scan()
                time.sleep(5)

        except KeyboardInterrupt:
            print("\n=== MONITORAMENTO INTERROMPIDO ===")

    def monitorar_conexoes_ativas(self):
        print("\n🌐 MONITORANDO CONEXÕES TCP/UDP ATIVAS... Ctrl+C para parar.")
        estado_anterior = []

        try:
            while True:
                conexoes = psutil.net_connections(kind='inet')
                registros = []

                for conn in conexoes:
                    # TCP
                    if conn.type == socket.SOCK_STREAM:
                        if conn.status != 'ESTABLISHED' or not conn.raddr:
                            continue
                    # UDP
                    elif conn.type == socket.SOCK_DGRAM:
                        if not conn.laddr:
                            continue

                    try:
                        proc = psutil.Process(conn.pid)
                        nome_proc = proc.name()
                        caminho = proc.exe()
                    except:
                        nome_proc = "Desconhecido"
                        caminho = "---"

                    registro = {
                        "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                        "protocolo": "TCP" if conn.type == socket.SOCK_STREAM else "UDP",
                        "ip_local": conn.laddr.ip if conn.laddr else "",
                        "porta_local": conn.laddr.port if conn.laddr else "",
                        "ip_remoto": conn.raddr.ip if conn.raddr else "",
                        "porta_remota": conn.raddr.port if conn.raddr else "",
                        "pid": conn.pid,
                        "processo": nome_proc,
                        "caminho": caminho
                    }

                    if registro not in estado_anterior:
                        estado_anterior.append(registro)
                        registros.append(registro)

                        print(f"[{registro['protocolo']}] {registro['ip_local']}:{registro['porta_local']}"
                              f" → {registro['ip_remoto']}:{registro['porta_remota']}")
                        print(f"PID: {registro['pid']} | {nome_proc} | {caminho}\n")

                if registros:
                    self.salvar_saida_json(registros)

                time.sleep(5)

        except KeyboardInterrupt:
            print("\n⛔ Monitoramento encerrado pelo usuário.")

    def salvar_saida_json(self, registros):
        if not os.path.exists(JSON_SAIDA):
            with open(JSON_SAIDA, 'w') as f:
                json.dump([], f)

        with open(JSON_SAIDA, 'r') as f:
            try:
                dados_existentes = json.load(f)
            except json.JSONDecodeError:
                dados_existentes = []

        dados_existentes.extend(registros)

        with open(JSON_SAIDA, 'w') as f:
            json.dump(dados_existentes, f, indent=4)

scan = Scan()

def menu():
    lista_portas = []

    while True:
        print("\n=== MONITORAMENTO DE PORTAS ===")
        print("1 - ESCOLHER AS PORTAS")
        print("2 - MOSTRAR REGISTROS")
        print("3 - MONITORAR CONEXÕES ATIVAS TCP/UDP")
        print("0 - SAIR")
        opcao = input("Escolha a opção: ")

        match opcao:
            case "1":
                print("\nDigite as portas uma a uma. Digite '1' para iniciar o monitoramento ou '0' para cancelar.")
                while True:
                    entrada = input("Porta: ")
                    if entrada == "0":
                        lista_portas = []
                        print("Cancelado.")
                        break
                    elif entrada == "1":
                        if lista_portas:
                            scan.monitorar(lista_portas)
                            lista_portas = []  # limpa após execução
                        else:
                            print("Nenhuma porta digitada.")
                        break
                    elif entrada.isdigit():
                        lista_portas.append(int(entrada))
                        print(f"Porta {entrada} adicionada.")
                    else:
                        print("Entrada inválida.")
            case "2":
                scan.listar_scan()
            case "3":
                scan.monitorar_conexoes_ativas()
            case "0":
                break
            case _:
                print("Opção inválida.")

menu()
