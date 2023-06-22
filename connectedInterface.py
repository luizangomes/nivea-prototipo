from tkinter import *
from interface_para_cmd import *

class Application:
    def __init__(self, master=None):
        self.startMenuOptionsList = ["Adicionar aluno", "Remover aluno", "Analisar relatórios do aluno", "Voltar"]
        self.studentsList = []

        ### Título ###
        self.frameTitle = Frame(master)
        self.frameTitle['pady'] = 13
        self.frameTitle['padx'] = 0
        self.frameTitle.pack()
        
        self.title = Label(self.frameTitle)
        self.title["text"] = "Crie um RAV"
        self.title['font'] = ('Arial', '13', 'bold')
        self.title.pack()
        
        # ### Tabela de Opções ###
        self.frameTableOptions = Frame(master)
        self.frameTableOptions['pady'] = 20
        self.frameTableOptions.pack()

        for option in self.startMenuOptionsList:
            self.buttonVisualizarDados = Button(self.frameTableOptions)
            self.buttonVisualizarDados['text'] = option
            self.buttonVisualizarDados['command'] = lambda option=option : telaMostreAlunos(self.studentsList)          
            self.buttonVisualizarDados.grid(row=self.startMenuOptionsList.index(option), column=0)
     
    
def telaMostreAlunos(studentsList):
  telaAddEstudante = Toplevel(root)
  telaAddEstudante.title(f'Adicionar alunos')
  telaAddEstudante.geometry('350x350')
  
        
  frameTableOptions = Frame(root)
  frameTableOptions['pady'] = 25
  frameTableOptions.pack()
  
  title = Label(telaAddEstudante)
  title["text"] = "Adicionar Aluno"
  title['font'] = ('Arial', '13', 'bold')
  title.grid(row=0, column=0)
  
  nomeLabel = Label(telaAddEstudante, text="Nome Completo")
  nomeLabel.grid(row=1, column=0)
  nomeEntry = Entry(telaAddEstudante)
  nomeEntry.grid(row=1, column=1)
  
  anoLabel = Label(telaAddEstudante, text="Ano Escolar")
  anoLabel.grid(row=2, column=0)
  anoEntry = Entry(telaAddEstudante)
  anoEntry.grid(row=2, column=1)
  
  turmaLabel = Label(telaAddEstudante, text="Turma")
  turmaLabel.grid(row=3, column=0)
  turmaEntry = Entry(telaAddEstudante)
  turmaEntry.grid(row=3, column=1)
  
  addEstudante = Button(telaAddEstudante, text="Adicionar", command=telaAddEstudante.destroy)
  addEstudante['command'] = studentsList.append(str(nomeEntry.focus_get()))
  addEstudante.grid(row=5, column=1)
  print(studentsList, str(nomeEntry.get()))
  
def telaEstudante(student):
        ### Nova tela ###
        telaEstudante = Toplevel(root)
        telaEstudante.title(f'Tela de {student}')
        telaEstudante.geometry('300x300')

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
root.geometry("300x300")
Application(root)
root.mainloop()