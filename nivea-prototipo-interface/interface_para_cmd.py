from classeItemPergunta import itemPergunta
from classeFormulario import Formulario
from classeAluno import Aluno
import os

listaAlunos = {}

tiposForms = {}

def menu_principal():
    os.system('cls||clear')
    sair = False
    while not(sair):
        print("\n### Escolha uma ação:")
        print("1. Visualizar alunos")
        print("2. Terminar programa")
        match input():
            case "1":
                os.system('cls||clear')
                visualisar_alunos()
            case "2":
                os.system('cls||clear')
                print("Tchau tchau!")
                sair = True
            case _:
                os.system('cls||clear')
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
                os.system('cls||clear')
                adicionar_aluno()
            case "2":
                os.system('cls||clear')
                remover_aluno()
            case "3":
                os.system('cls||clear')
                analisar_aluno()
            case "4":
                os.system('cls||clear')
                sair = True
            case _:
                os.system('cls||clear')
                print("Opção inválida.")

def adicionar_aluno():
    nome = input("NOME DO ALUNO: ")
    if nome in listaAlunos.keys():
        os.system('cls||clear')
        print("Nome inválido, aluno já existe")
    else:
        ano = input("ANO DO ALUNO: ")
        turma = input("TURMA DO ALUNO: ")
        os.system('cls||clear')
        print(f"DADOS DO ALUNO:\n    NOME: {nome}\n    ANO: {ano}\n    TURMA: {turma}\n")
        sair = False
        while not(sair):
            print("### Os dados estão corretos? Escolha uma ação:\n1. Confirmar\n2. Cancelar")
            match input():
                case "1":
                    os.system('cls||clear')
                    listaAlunos[nome] = {"ano":ano, "turma":turma, "relatorios":{}}
                    sair = True
                case "2":
                    os.system('cls||clear')
                    sair = True
                case _:
                    os.system('cls||clear')
                    print("Opção inválida.")

def remover_aluno():
    nome = input("NOME DO ALUNO A SER REMOVIDO: ")
    if nome not in listaAlunos.keys():
        os.system('cls||clear')
        print("Nome inválido, não há um aluno com esse nome")
    else:
        os.system('cls||clear')
        print(f"DADOS DO ALUNO:\n    NOME: {nome}\n    ANO: {listaAlunos[nome]['ano']}\n    TURMA: {listaAlunos[nome]['turma']}")
        sair = False
        while not(sair):
            print("### Este aluno deve ser deletado? Escolha uma ação:\n1. Confirmar\n2. Cancelar")
            match input():
                case "1":
                    os.system('cls||clear')
                    listaAlunos.pop(nome)
                    sair = True
                case "2":
                    os.system('cls||clear')
                    sair = True
                case _:
                    os.system('cls||clear')
                    print("Opção inválida.")

def analisar_aluno():
    nome = input("NOME DO ALUNO A SER ANALISADO: ")
    if nome not in listaAlunos.keys():
        os.system('cls||clear')
        print("Nome inválido, não há um aluno com esse nome")
    else:
        os.system('cls||clear')
        sair = False
        while not(sair):
            print(f"DADOS DO ALUNO:\n    NOME: {nome}\n    ANO: {listaAlunos[nome]['ano']}\n    TURMA: {listaAlunos[nome]['turma']}\n")
            print(f"{nome} possui esses relatórios:")
            for i in listaAlunos[nome]["relatorios"].keys():
                print("    " + i)
            print("")
            print("### Escolha uma ação:\n1. Ler um relatório\n2. Adicionar um relatório (responder um formulário)\n3. Remover um relatório\n4. Voltar")
            match input():
                case "1":
                    os.system('cls||clear')
                    entrada = input("Qual relatório você quer ler? ")
                    if entrada in listaAlunos[nome]["relatorios"].keys():
                        print("\n###")
                        print(listaAlunos[nome]["relatorios"][entrada])
                        print("###\n")
                    else:
                        print("Não há um relatório com esse nome.")
                case "2":
                    os.system('cls||clear')
                    resp_form = gerarRelatorio(tiposForms["Primeiro parágrafo"].retornarRespostas())
                    nome_relat = "Relatorio" + str(len(listaAlunos[nome]["relatorios"].keys()))
                    listaAlunos[nome]["relatorios"][nome_relat] = resp_form
                case "3":
                    os.system('cls||clear')
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
                    os.system('cls||clear')
                    sair = True
                case _:
                    os.system('cls||clear')
                    print("Opção inválida.")

def gerarRelatorio(listaResp):
    intro = "Segundo o teste da psicogênese de Emília Ferreiro, foi possível constatar que a criança iniciou este bimestre no nível da escrita "
    conjun = ". No entanto, no encerramento do bimestre, apresentou estar no nível "

    objetivo_do_bimestre = 6
    if listaResp[1] >= objetivo_do_bimestre:
        concl = ". Com isto, evidenciou-se que quanto ao nível da escrita ela conseguiu alcançar o objetivo projetado para o bimestre."
    elif listaResp[1] - objetivo_do_bimestre <= 2:
        concl = ". Com isto, evidenciou-se que quanto ao nível da escrita ela vem avançando em relação ao objetivo projetado para o bimestre."
    else:
        concl = ". Com isto, evidenciou-se que quanto ao nível da escrita ela merece atenção em relação à sua compreensão do processo de escrita."

    def textoResposta(indice):
        match indice:
            case 1:
                return("pré-silábico; ainda não fazer a correspondência entre letras e os sons. Inventa desenhos garatujas e rabiscos para representas a escrita")
            case 2:
                return("pré-silábico com uso de letras muitas vezes do próprio nome ou misturam números e letras para representar a escrita")
            case 3:
                return("pré-silábico; utiliza muitas letras para escrever o nome de coisas grandes e que coisas pequenas têm nomes pequenos")
            case 4:
                return("pré-silábico; escreve uma palavra utilizando uma variedade de letras, acredita que para escrever tem que variar as letras")
            case 5:
                return("silábico sem valor sonoro; acredita que existe relação entre o que se fala e o que se escreve. Faz correspondência entre quantidade de sílabas e uma letra para cada sílaba sem valor sonoro, não se preocupa com a correspondência do som e letra")
            case 6:
                return("silábico com valor sonoro; utiliza uma letra para representar cada sílaba com valor sonoro. Às vezes só usa vogais, ou só consoantes, ou consoantes e vogais")
            case 7:
                return("silábico alfabético; escreve combinando consoante e vogais formando sílabas, mas as vezes não forma a sílaba completa usando só vogais ou só consoantes")
            case 8:
                return("alfabético; registra os sons através das letras fazendo uso de sílabas simples.")
            case 9:
                return("da escrita ortográfico; faz reconhecimento visual direto das palavras, pela estratégia lexical (reconhecimento visual diretamente da forma ortográfica das letras) e não está mais na decodificação (estratégia fonológica).")
    
    resp1 = textoResposta(listaResp[0])
    resp2 = textoResposta(listaResp[1])
    
    paragrafo = intro + resp1 + conjun + resp2 + concl

    return paragrafo


