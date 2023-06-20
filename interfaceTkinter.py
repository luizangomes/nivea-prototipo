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
    labelForm['text'] = 'Formulário de avaliação'
    labelForm['font'] = ('Arial', '13', 'bold')
    labelForm.pack()

    ### Frame de checkboxes ###
    frameCheckboxes = Frame(telaResponderForm)
    frameCheckboxes['pady'] = 10
    frameCheckboxes.pack()

    for i in range(10):
        checkbox = Checkbutton(frameCheckboxes)
        checkbox['text'] = i
        checkbox.pack()


root = Tk()
root.title("Interface")
root.geometry("200x200")
Application(root)
root.mainloop()