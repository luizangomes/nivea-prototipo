class Formulario:
    def __init__(self, *itens):
        self.itens = list(itens)
    
    def gerarRelatorio(self):
        relatorioFinal = ""
        for i in self.itens:
            print(i.enunciado)
            for j in i.respostas.keys():
                print(f"{j}. {i.respostas[j]}")
            sair = False
            while not(sair):
                entrada = input()
                if entrada in i.respostas.keys():
                    relatorioFinal += i.respostas[entrada]
                    sair = True
                else:
                    print("Resposta inválida. Tente novamente.")
        return relatorioFinal
    
    def retornarRespostas(self):
        respostaFinal = []
        for i in self.itens:
            print(i.enunciado)
            for j in i.respostas.keys():
                print(f"{j}. {i.respostas[j]}")
            sair = False
            while not(sair):
                entrada = input()
                if entrada in i.respostas.keys():
                    respostaFinal.append(int(entrada))
                    sair = True
                else:
                    print("Resposta inválida. Tente novamente.")
        return respostaFinal
            

""" ip1 = itemPergunta("Quantos anos você tem?", **{"1":"Tenho um ano. ", "2":"Tenho dois anos. ", "3":"Minha idade não importa. "})
ip2 = itemPergunta("Que curso você faz?", **{"1":"Faço Engenharia da Computação. ", "2":"Faço Ciência da Computação. ", "3":"Faço Licenciatura em Computação. ", "4":"Faço Engenharia Mecatrônica. ", "5":"Sou de humanas >:]"})

form1 = Formulario(ip1, ip2)
print(form1.gerarRelatorio()) """