from tkinter import *
from interface_para_cmd import *
from functools import partial

class Application:
    def __init__(self, master=None):
        def getOptions():
            buttonVisualizarDados.get()
        self.startMenuOptionsList = ["Adicionar aluno", "Remover aluno", "Analisar relatórios do aluno"]
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
        
        self.buttonVisualizarDados = Button(self.frameTableOptions)
        self.buttonVisualizarDados['text'] = self.startMenuOptionsList[0]
        self.buttonVisualizarDados['command'] = lambda :  telaMostreAlunos(self.studentsList)          
        self.buttonVisualizarDados.grid(row=0, column=0)
        self.buttonVisualizarDados = Button(self.frameTableOptions)
        self.buttonVisualizarDados['text'] = self.startMenuOptionsList[1]
        self.buttonVisualizarDados['command'] = lambda :  telaMostreAlunos(self.studentsList)          
        self.buttonVisualizarDados.grid(row=1, column=0)
        self.buttonVisualizarDados = Button(self.frameTableOptions)
        self.buttonVisualizarDados['text'] = self.startMenuOptionsList[2]
        self.buttonVisualizarDados['command'] = lambda : telaRelatorios(self.studentsList)         
        self.buttonVisualizarDados.grid(row=2, column=0)
    
def telaMostreAlunos(studentsList):
    def mostreAluno():
        studentsList.append(nomeEntry.get())
        print("Nova Lista de Alunos:, ", studentsList)
        print("DADOS DO ALUNO:", nomeEntry.get(), anoEntry.get(), turmaEntry.get())
    
    def mostreAlunos():
        telaAddEstudante.geometry('300x300')
        lista = Label(telaAddEstudante)
        lista["text"] = "Alunos cadastrados\n na plataforma"
        lista['font'] = ('Arial', '11', 'bold')
        lista.grid(row=10, column=0)
        for aluno in studentsList:
            listaDeAlunos = Label(telaAddEstudante)
            listaDeAlunos["text"] = aluno
            listaDeAlunos.grid(row=11+studentsList.index(aluno), column=0)
    
    telaAddEstudante = Toplevel(root)
    telaAddEstudante.title(f'Adicionar alunos')
    telaAddEstudante.geometry('300x200')
        
    frameTableOptions = Frame(root)
    frameTableOptions['pady'] = 50
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
    
    addEstudante = Button(telaAddEstudante, text="Adicionar")
    addEstudante['command'] = mostreAluno
    addEstudante.grid(row=5, column=1)
    fecharGuia = Button(telaAddEstudante, text="Voltar ao menu", command=telaAddEstudante.destroy)
    fecharGuia.grid(row=7, column=1)
    alunosCadastrados = Button(telaAddEstudante, text="Alunos Cadastrados", command=mostreAlunos)
    alunosCadastrados.grid(row=8, column=0)
  
def telaRelatorios(studentsList):            
    telaInicialRelatorios = Toplevel(root)
    telaInicialRelatorios.title(f'Relatórios')
    telaInicialRelatorios.geometry('300x200')
       
    frameTableOptions = Frame(root)
    frameTableOptions['pady'] = 50
    frameTableOptions.pack()
    lista = Label(telaInicialRelatorios)
    lista["text"] = "Alunos cadastrados\n na plataforma"
    lista['font'] = ('Arial', '11', 'bold')
    lista.grid(row=0, column=0)
    for aluno in studentsList:
        listaDeAlunos = Label(telaInicialRelatorios)
        listaDeAlunos["text"] = aluno
        listaDeAlunos.grid(row=1+studentsList.index(aluno), column=0)
        
        buttonVisualizarDados = Button(telaInicialRelatorios)
        buttonVisualizarDados['text'] = "Fazer o RAV"
        buttonVisualizarDados['command'] = lambda student=aluno : telaEstudante(student)           
        buttonVisualizarDados.grid(row=1+studentsList.index(aluno), column=1)
     

def telaEstudante(student):
        ### Nova tela ###
        telaEstudante = Toplevel(root)
        telaEstudante.title(f'Tela de {student}')
        telaEstudante.geometry('300x200')

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