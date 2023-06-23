class itemPergunta:
    def __init__(self, enunciado, **respostas):
        self.enunciado = enunciado
        self.respostas = respostas
    
    def retEnunciado(self):
        return self.enunciado
    
    def alterarEnun(self, enun):
        self.enunciado = enun
    
    def retRespostas(self):
        return self.respostas.values()
    
    def alterarResp(self, resp):
        self.respostas = resp

""" ip1 = itemPergunta("Quantos anos você tem?", **{"1":"Um ano", "2":"Dois anos", "3":"Não te interessa"})
print(ip1.retRespostas())
print(ip1.retEnunciado())
ip1.alterarEnun("Faz quantos anos que você entrou na UnB?")
print(ip1.retEnunciado()) """

# 1) Icônica	
# 2) Grafismo primitivo	
# 3) Pré silabica	Escrita sem controle de qualidade
# 4) Pré silabica	Escrita Unigráfica
# 5) Pré silabica	Escrita Fixa
# 6) Pré silabica	Quantidade variável Repertório Fixo / Parcial
# 7) Pré silabica	Quantidade constante Repertório Variável
# 8) Pré silabica	Quantidade variável Repertório Variável
# 9) Pré silabica	Quantidade e repertório variaveis. Presença valor silabico inicio e fim
# 10) Silábica Sem Valor  	
# 11) Silábica com Valor  	
# 12) Silábica Alfabética	
# 13) Alfabética