#GERENCIADOR DE TAREFAS COM STATUS DE PRIVACIDADE E JSON

import json
import os

class Tarefa():
    def __init__(self, nomeTarefa, descTarefa, prioridadeTarefa, horarioTarefa, statusTarefa):
        self.nomeTarefa = nomeTarefa
        self.descTarefa = descTarefa
        self.prioridadeTarefa = prioridadeTarefa
        self.horarioTarefa = horarioTarefa
        self.statusTarefa = statusTarefa

    def to_dict(self):
        return{
        "nomeTarefa": self.nomeTarefa,
        "descTarefa": self.descTarefa,
        "prioridadeTarefa": self.prioridadeTarefa,
        "horarioTarefa": self.horarioTarefa,
        "statusTarefa": self.statusTarefa
    }

class Gerenciador():
    def __init__(self, arquivo = "json/day10.json"):
        self.arquivo = arquivo
        self.tarefa = self.carregarTarefa()

    def carregarTarefa(self):
        if not os.path.exists(self.arquivo):
            return[]
        
        if os.stat(self.arquivo).st_size == 0:
            return[]
        
        with open(self.arquivo, 'r') as file:
            return json.load(file)
        
    def adicionarTarefa(self, tarefa):
        self.tarefa.append(tarefa.to_dict())
        self.salvarTarefa()

    def salvarTarefa(self):
        with open(self.arquivo, 'w') as file:
            json.dump(self.tarefa, file, indent = 4)

    def alterarTarefa(self):
        for tarefa in self.tarefa:
            print(f"{tarefa['nomeTarefa']} - {tarefa['descTarefa']} - {tarefa['prioridadeTarefa']} - {tarefa['horarioTarefa']} - {tarefa['statusTarefa']}")

            novoNome = input("Atualize o nome da tarefa ou pressione enter para manter: ")
            novaDesc = input("Atualize a descrição da tarefa ou pressione enter para manter: ")
            novaPrioridae = input("Atualize a prioridade da tarefa ou pressione enter para manter: ")
            novoHorario = input("Atualize o horário da tarefa ou pressione enter para manter: ")
            novoStatus = input("Atualize o status da tarefa ou pressione enter para manter: ")

            if novoNome:
                tarefa['nomeTarefa'] = novoNome
            if novaDesc:
                tarefa['descTarefa'] = novaDesc
            if novaPrioridae:
                tarefa['prioridadeTarefa'] = novaPrioridae
            if novoHorario:
                tarefa['horarioTarefa'] = novoHorario
            if novoStatus:
                tarefa['statusTarefa'] = novoStatus

            self.salvarTarefa()
            print("Tarefa atualizada com sucesso!")
            return
        
    def listarTarefas(self):
        if not self.tarefa:
            return print("Nenhuma tarefa na lista")

        for tarefa in self.tarefa:
            print(f"{tarefa['nomeTarefa']} - {tarefa['descTarefa']} - {tarefa['prioridadeTarefa']} - {tarefa['horarioTarefa']} - {tarefa['statusTarefa']}")

    def removerTarefa(self):
        remover = input("Digite o nome da tarefa a ser removida: ").lower()
        tarefas_filtradas = [c for c in self.tarefa if c ['nomeTarefa'].lower() != remover]

        if len(tarefas_filtradas) < len(self.tarefa):
            self.tarefa = tarefas_filtradas
            self.salvarTarefa()
            print("Tarefa removida com sucesso!")

        else:
            print("Tarefa não encontrada")
        
gerenciador = Gerenciador()

print("\n=== GERENCIADOR DE TAREFAS ===")

def menu():

    while True:
        print("\n1 - ADICIONAR TAREFAS")
        print("2 - ALTERAR TAREFA")
        print("3 - LISTAR TAREFAS")
        print("4 - EXCLUIR TAREFA")
        print("0 - SAIR")

        opcao = input("Selecione uma opção: ")
        
        if opcao == "1":
            nome = input("\nDigite o nome da tarefa: ")
            desc = input("Digite a descrição da tarefa: ")
            prioridade = input("Prioridade da tarefa (alta, média, baixa): ")
            horario = input("Horário a ser realizada a tarefa: ")
            status = input("Digite o status da tarefa (pendente, em andamento, concluída):" )
            novo = Tarefa(nome, desc, prioridade, horario, status)
            gerenciador.adicionarTarefa(novo)

        if opcao == "2":
            gerenciador.alterarTarefa()

        if opcao == "3":
            gerenciador.listarTarefas()

        if opcao == "4":
            gerenciador.removerTarefa()
        
        if opcao == "0":
            break
menu()