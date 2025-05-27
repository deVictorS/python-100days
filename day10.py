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
    def __init__(self, arquivo = "day10.json"):
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

    def alterarPrioridade():
        
        
gerenciador = Gerenciador()

print("\n=== GERENCIADOR DE TAREFAS ===")

def menu():

    while True:
        print("\n1 - ADICIONAR TAREFAS")
        print("2 - ALTERAR PRIORIDADE")
        print("3 - ALTERAR STATUS")
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

        if opcao == "3":

        else:
            print("\nOpção inválida, tente novamente")

menu()