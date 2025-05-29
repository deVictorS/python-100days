#DICIONÁRIO E TUPLAS PARA CADASTRO DE DISPOSITIVOS DE REDE SEM ALTERAÇÃO DE DADOS
import os
import json

class Equipamento():
    def __init__(self, nomeEquip, serialEquip, ipEquip, localEquip):
        self.nomeEquip = nomeEquip
        self.serialEquip = serialEquip
        self.ipEquip = ipEquip
        self.localEquip = localEquip

    def to_dict_tup(self):
        return{
            'equipamento': (self.nomeEquip, self.serialEquip, self.ipEquip, self.localEquip)
        }
    
class Documento():

    def __init__(self, arquivo = 'day12.json'):
        self.arquivo = arquivo
        self.equipamento = self.carregarArquivo()

    def carregarArquivo(self):
        if not os.path.exists(self.arquivo):
            print("\nArquivo não encontrado, criando um. . .")
            return []
        
        if os.stat(self.arquivo).st_size == 0:
            print("Arquivo vazio")
            return[]
        
        with open(self.arquivo, 'r') as file:
            return json.load(file)
        
    def adicionarEquipamento(self, equipamento):
        self.equipamento.append(equipamento.to_dict_tup())
        self.salvarEquipamento()
        print("\nEquipamento adicionado com sucesso!")

    def salvarEquipamento(self):
        with open(self.arquivo, 'w') as file:
            json.dump(self.equipamento, file, indent = 4)

    def listarEquipamento(self):
        print("\n=== LISTA DE EQUIPAMENTOS ===")
        for id, e in enumerate(self.equipamento, start = 1):
            nome, serie, ip, local = e['equipamento']
            print(f"{id}: {nome} - {serie} - {ip} - {local}")

    def buscarEquipamento(self, serial):
            for id, e in enumerate(self.equipamento, start=1):
                nome, serial_equip, ip, local = e['equipamento']
                if serial_equip == serial:
                    print(f"\nEquipamento encontrado: {id}: {nome} - {serial_equip} - {ip} - {local}")
                    return



documento = Documento()

def menu():

    while True:
        print("\n=== EQUIPAMENTOS DE REDE ===")
        print("\n1 - CADASTRAR EQUIPAMENTO")
        print("2 - LISTAR EQUIPAMENTOS")
        print("3 - BUSCA POR EQUIPAMENTOS")
        print("0 - SAIR")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            print("\n=== CADASTRO DE EQUIPAMENTO ===")
            nome = input("\nDigite o nome do equipamento: ")
            serial = input("Digite o número de série do equipamento: ")
            ip = input("Digite o IP do equipamento: ")
            local = input("Digite a localização do equipamento: ")
            novo = Equipamento(nome, serial, ip, local)
            documento.adicionarEquipamento(novo)

        elif opcao == "2":
            documento.listarEquipamento()

        elif opcao == "3":
            serial = input("Digite o número de série do equipamento: ")
            documento.buscarEquipamento(serial)

        elif opcao == "0":
            print("ENCERRANDO PROGRAMA. . .")
            break

        else:
            print("\nOpção inválida, tente novamente")

menu()