from lista import Lista
from tkinter import *

l1 = Lista()
  
class Application:
    #Construtor
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
  
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 10
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 10
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["pady"] = 15
        self.container8.pack()


        
  
        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()
  
        self.lblposicao = Label(self.container2, text="Posição:", font=self.fonte, width=10)
        self.lblposicao.pack(side=LEFT)
  
        self.txtposicao = Entry(self.container2)
        self.txtposicao["width"] = 10
        self.txtposicao["font"] = self.fonte
        self.txtposicao.pack(side=LEFT)
  
        self.btnBuscar = Button(self.container2, text="Show", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)
  
        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
  
        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)
  
        self.lblmatricula = Label(self.container4, text="Matrícula:", font=self.fonte, width=10)
        self.lblmatricula.pack(side=LEFT)
  
        self.txtmatricula = Entry(self.container4)
        self.txtmatricula["width"] = 25
        self.txtmatricula["font"] = self.fonte
        self.txtmatricula.pack(side=LEFT)
  
        self.lblcurso= Label(self.container5, text="Curso:", font=self.fonte, width=10)
        self.lblcurso.pack(side=LEFT)
  
        self.txtcurso = Entry(self.container5)
        self.txtcurso["width"] = 25
        self.txtcurso["font"] = self.fonte
        self.txtcurso.pack(side=LEFT)
  
       

        self.bntInsert = Button(self.container6, text="Add", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack(side=LEFT)
  
  
        self.bntExcluir = Button(self.container6, text="Remove", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)


        self.bntEmpty = Button(self.container7, text="isEmpty?", font=self.fonte, width=12)
        self.bntEmpty["command"] = self.emptyList
        self.bntEmpty.pack(side=LEFT)


        self.bntSize = Button(self.container7, text="Size", font=self.fonte, width=12)
        self.bntSize["command"] = self.sizeList
        self.bntSize.pack(side=LEFT)


        self.lblmsg = Label(self.container8, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()





    #Método para inserir aluno
    def inserirUsuario(self):
        nome = self.txtnome.get()
        matricula = self.txtmatricula.get()
        curso = self.txtcurso.get()
        try:
            posicao = int(self.txtposicao.get())
        except ValueError:
            posicao = ''
        if (nome != '') and (matricula != '') and (curso != '') and (posicao != ''):
            l1.add(posicao, nome, matricula, curso)
    
            self.lblmsg["text"] = "Inserção feita com sucesso!"
    
            self.txtposicao.delete(0, END)
            self.txtnome.delete(0, END)
            self.txtmatricula.delete(0, END)
            self.txtcurso.delete(0, END)

        else:
            self.lblmsg["text"] = "Ocorreu um erro na inserção do aluno!"

            self.txtnome.delete(0, END)
            self.txtmatricula.delete(0, END)
            self.txtcurso.delete(0, END)

  
  
  
  
    #Método para remover aluno
    def excluirUsuario(self):
        try:
            posicao = int(self.txtposicao.get())
        except ValueError:
            posicao = ''

        if (l1.isEmpty() == True) or (posicao == ''):
            self.lblmsg["text"] = "Ocorreu um erro na remoção!"

            self.txtposicao.delete(0, END)
            self.txtnome.delete(0, END)
            self.txtmatricula.delete(0, END)
            self.txtcurso.delete(0, END)
            
        
        else:
            divisao = l1.show(posicao)
  
            self.lblmsg["text"] = "Remoção feita com sucesso!"
    
            self.txtposicao.delete(0, END)
            self.txtnome.delete(0, END)
            self.txtmatricula.delete(0, END)
            self.txtcurso.delete(0, END)

            self.txtnome.insert(INSERT, divisao.get_nome())
            self.txtmatricula.insert(INSERT, divisao.get_matricula())
            self.txtcurso.insert(INSERT, divisao.get_curso())

            l1.remove(posicao)
  





    #Método para buscar por aluno
    def buscarUsuario(self):
        try:
            posicao = int(self.txtposicao.get())
        except ValueError:
            posicao = ''

        if (l1.isEmpty() == True) or (posicao == ''):
            self.lblmsg["text"] = "Ocorreu um erro na busca!"

            self.txtposicao.delete(0, END)
            self.txtnome.delete(0, END)
            self.txtmatricula.delete(0, END)
            self.txtcurso.delete(0, END)
            
        
        else:
            divisao = l1.show(posicao)
    
            self.lblmsg["text"] = "Busca feita com sucesso!"
    
            self.txtposicao.delete(0, END)
    
            self.txtnome.delete(0, END)
            self.txtnome.insert(INSERT, divisao.get_nome())
    
            self.txtmatricula.delete(0, END)
            self.txtmatricula.insert(INSERT, divisao.get_matricula())
    
            self.txtcurso.delete(0, END)
            self.txtcurso.insert(INSERT, divisao.get_curso())




    #Método para checar se a lista de alunos está vazia
    def emptyList(self):
        self.lblmsg["text"] = 'Lista vazia? \n{}'.format(str(l1.isEmpty()))
    




    #Método para checar o tamanho da lista de alunos
    def sizeList(self):
        self.lblmsg["text"] = 'Tamanho da lista: \n{}'.format(str(l1.size()))
  
  
  
  
root = Tk()
root.title('Lista Encadeada')
Application(root)
root.mainloop()
