from classeItemPergunta import itemPergunta
from classeFormulario import Formulario
from classeAluno import Aluno

listaAlunos = {}

tiposForms = {}

def menu_principal():
    sair = False
    while not(sair):
        print("\n### Escolha uma ação:")
        print("1. Visualisar alunos")
        print("2. Terminar programa")
        match input():
            case "1":
                visualisar_alunos()
            case "2":
                print("Tchau tchau!")
                sair = True
            case _:
                print("Opção inválida.")

def visualisar_alunos():
    sair = False
    while not(sair):
        print("### Você possui os seguintes alunos:\n")
        for i in listaAlunos.keys():
            print(f"NOME: {i}")
            print(f"    ANO: {listaAlunos[i]['ano']} // TURMA: {listaAlunos[i]['turma']}")
            print("")
        print("### Escolha uma ação:")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Analisar relatórios do aluno")
        print("4. Voltar")
        match input():
            case "1":
                adicionar_aluno()
            case "2":
                remover_aluno()
            case "3":
                analisar_aluno()
            case "4":
                sair = True
            case _:
                print("Opção inválida.")

def adicionar_aluno():
    nome = input("NOME DO ALUNO: ")
    if nome in listaAlunos.keys():
        print("Nome inválido, aluno já existe")
    else:
        ano = input("ANO DO ALUNO: ")
        turma = input("TURMA DO ALUNO: ")
        print(f"\nDADOS DO ALUNO:\n    NOME: {nome}\n    ANO: {ano}\n    TURMA: {turma}")
        sair = False
        while not(sair):
            print("### Os dados estão corretos? Escolha uma ação:\n1. Confirmar\n2. Cancelar")
            match input():
                case "1":
                    listaAlunos[nome] = {"ano":ano, "turma":turma, "relatorios":{}}
                    sair = True
                case "2":
                    sair = True
                case _:
                    print("Opção inválida.")

def remover_aluno():
    nome = input("NOME DO ALUNO A SER REMOVIDO: ")
    if nome not in listaAlunos.keys():
        print("Nome inválido, não há um aluno com esse nome")
    else:
        print(f"\nDADOS DO ALUNO:\n    NOME: {nome}\n    ANO: {listaAlunos[nome]['ano']}\n    TURMA: {listaAlunos[nome]['turma']}")
        sair = False
        while not(sair):
            print("### Este aluno deve ser deletado? Escolha uma ação:\n1. Confirmar\n2. Cancelar")
            match input():
                case "1":
                    listaAlunos.pop(nome)
                    sair = True
                case "2":
                    sair = True
                case _:
                    print("Opção inválida.")

def analisar_aluno():
    nome = input("NOME DO ALUNO A SER ANALISADO: ")
    if nome not in listaAlunos.keys():
        print("Nome inválido, não há um aluno com esse nome")
    else:
        sair = False
        while not(sair):
            print(f"\nDADOS DO ALUNO:\n    NOME: {nome}\n    ANO: {listaAlunos[nome]['ano']}\n    TURMA: {listaAlunos[nome]['turma']}\n")
            print(f"{nome} possui esses relatórios:")
            for i in listaAlunos[nome]["relatorios"].keys():
                print("    " + i)
            print("")
            print("### Escolha uma ação:\n1. Ler um relatório\n2. Adicionar um relatório (responder um formulário)\n3. Remover um relatório\n4. Voltar")
            match input():
                case "1":
                    entrada = input("Qual relatório você quer ler? ")
                    if entrada in listaAlunos[nome]["relatorios"].keys():
                        print("\n###")
                        print(listaAlunos[nome]["relatorios"][entrada])
                        print("###\n")
                    else:
                        print("Não há um relatório com esse nome.")
                case "2":
                    print("Esses são os formulários disponíveis para responder:")
                    for i in tiposForms.keys():
                        print("    " + i)
                    entrada = input("Qual formulário você quer responder? ")
                    if entrada in tiposForms.keys():
                        resp_form = tiposForms[entrada].gerarRelatorio()
                        nome_relat = input("Qual é o nome desse relatório? ")
                        listaAlunos[nome]["relatorios"][nome_relat] = resp_form
                    else:
                        print("Não há um formulário com esse nome.")
                case "3":
                    entrada = input("Nome do relatório a ser removido: ")
                    if entrada in listaAlunos[nome]["relatorios"]:
                        print("\n###")
                        print(listaAlunos[nome]["relatorios"][entrada])
                        print("###\n")
                        sair2 = False
                        while not(sair2):
                            print(f"O relatório {entrada} deve ser removido? Escolha uma ação:\n1. Confirmar\n2. Cancelar")
                            match input():
                                case "1":
                                    listaAlunos[nome]["relatorios"].pop(entrada)
                                    sair2 = True
                                case "2":
                                    sair2 = True
                                case _:
                                    print("Opção inválida.")
                    else:
                        print("Não há um relatório com esse nome.")
                case "4":
                    sair = True
                case _:
                    print("Opção inválida.")
