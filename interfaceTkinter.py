from tkinter import *

class Application:
    def __init__(self, master=None):
        self.studentsList = ["Pedro", "Cássio", "Pejão"]


        ### Título ###
        self.frameTitle = Frame(master)
        self.frameTitle['pady'] = 10
        self.frameTitle['padx'] = 0
        self.frameTitle.pack()

        self.title = Label(self.frameTitle)
        self.title["text"] = "Alunos:"
        self.title['font'] = ('Arial', '13', 'bold')
        self.title.pack()
        
        ### Tabela de alunos ###
        self.frameTableStudents = Frame(master)
        self.frameTableStudents['pady'] = 20
        self.frameTableStudents.pack()


        for student in self.studentsList:
            self.labelName = Label(self.frameTableStudents)
            self.labelName['text'] = student
            self.labelName['font'] = ('Arial', '10')
            self.labelName.grid(row=self.studentsList.index(student), column=0)

            self.buttonVisualizarDados = Button(self.frameTableStudents)
            self.buttonVisualizarDados['text'] = "Visualizar dados"
            self.buttonVisualizarDados['command'] = lambda student=student : telaEstudante(student)           
            self.buttonVisualizarDados.grid(row=self.studentsList.index(student), column=1)
     
    
def telaEstudante(student):
        
        ### Nova tela ###
        telaEstudante = Toplevel(root)
        telaEstudante.title(f'Tela de {student}')
        telaEstudante.geometry('200x200')

        ### Título = nome do estudante ###
        studentName = Label(telaEstudante)
        studentName['text'] = student
        studentName['pady'] = 10
        studentName['font'] = ('Arial', '13', 'bold')
        studentName.pack()

        ### Frame de dados ###
        frameDados = Frame(telaEstudante)
        frameDados['pady'] = 10
        frameDados.pack()
        
        labelDados = Label(frameDados)
        labelDados['text'] = "Dados"
        labelDados.pack()

        buttonRelatorio = Button(frameDados)
        buttonRelatorio['text'] = "Ler relatório"
        buttonRelatorio['command'] = lambda: telaRelatorio(student, telaEstudante)
        buttonRelatorio.pack()

        ### Fame do form ###
        frameForm = Frame(telaEstudante)
        frameForm['pady'] = 10
        frameForm.pack()

        buttonForm = Button(frameForm)
        buttonForm['text'] = "Responder formulário"
        buttonForm['command'] = lambda: telaResponderForm(student, telaEstudante)
        buttonForm.pack()

        
def telaRelatorio(student, telaEstudante):
    ### Nova tela ###
    telaRelatorio = Toplevel(telaEstudante)
    telaRelatorio.title(f'Relatório de {student}')

    ### Título relatório ###
    labelRelatorio = Label(telaRelatorio)
    labelRelatorio['text'] = f'Relatório de {student}'
    labelRelatorio['font'] = ('Arial', '13', 'bold')
    labelRelatorio['pady'] = 10
    labelRelatorio.pack()

    ### Frame relatório ###
    frameRelatorio = Frame(telaRelatorio)
    frameRelatorio['pady'] = 10
    frameRelatorio.pack()

    textoRelatorio = Label(frameRelatorio)
    textoRelatorio['text'] = f'Segundo o teste da psicogênese de {student}, foi possível constatar que a criança iniciou este bimestre no nível da escrita\
                                pré-silábico; utilizava-se de letras muitas vezes do próprio nome ou misturava números e letras para representar a escrita. No entanto,\
                                no encerramento do bimestre, apresentou estar no mesmo nível da escrita. Com isto, evidenciou que quanto ao nível da escrita ela merece atenção\
                                em relação à sua compreensão do processo de escrita.'
    textoRelatorio['font'] = ('Arial', '10')
    textoRelatorio['wraplength'] = 300
    textoRelatorio.pack()


def telaResponderForm(student, telaEstudante):
    
    ### Nova tela ###
    telaResponderForm = Toplevel(telaEstudante)
    telaResponderForm.title(f'Formulário de avaliação de {student}')
    
    ### Label formulário ###
    labelForm = Label(telaResponderForm)
    labelForm['text'] = '"Segundo o teste da psicogênese de Emília Ferreiro, foi possível constatar que a criança iniciou este bimestre no nível da escrita "'
    labelForm['font'] = ('Arial', '13', 'bold')
    labelForm.pack()

    ### Frame de checkboxes ###
    frameCheckboxes = Frame(telaResponderForm)
    frameCheckboxes['pady'] = 10
    frameCheckboxes.pack()

    respDict = {"1":"pré-silábico; ainda não fazer a correspondência entre letras e os sons. Inventa desenhos garatujas e rabiscos para representas a escrita ", "2":"pré-silábico com uso de letras muitas vezes do próprio nome ou misturam números e letras para representar a escrita", "3":"pré-silábico; utiliza muitas letras para escrever o nome de coisas grandes e que coisas pequenas têm nomes pequenos", "4": "pré-silábico; escreve uma palavra utilizando uma variedade de letras, acredita que para escrever tem que variar as letras", "5": "silábico sem valor sonoro; acredita que existe relação entre o que se fala e o que se escreve. Faz correspondência entre quantidade de sílabas e uma letra para cada sílaba sem valor sonoro, não se preocupa com a correspondência do som e letra", "6": "silábico com valor sonoro; utiliza uma letra para representar cada sílaba com valor sonoro. Às vezes só usa vogais, ou só consoantes, ou consoantes e vogais", "7": "silábico alfabético; escreve combinando consoante e vogais formando sílabas, mas as vezes não forma a sílaba completa usando só vogais ou só consoantes", "8": "alfabético; registra os sons através das letras fazendo uso de sílabas simples.", "9": "da escrita ortográfico; faz reconhecimento visual direto das palavras, pela estratégia lexical (reconhecimento visual diretamente da forma ortográfica das letras) e não está mais na decodificação (estratégia fonológica)."}

    for i in respDict:
        checkbox = Checkbutton(frameCheckboxes)
        checkbox['text'] = respDict[i]
        checkbox.pack()


root = Tk()
root.title("Interface")
root.geometry("200x200")
Application(root)
root.mainloop()