from fila import Fila
from tkinter import *

f1 = Fila()
  
class Application:
    #Construtor
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
  
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
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
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()


        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()


        
  
        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()
  
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

        self.bntExcluir = Button(self.container8, text="Topo", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.buscarUsuario
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()





    #Método para inserir aluno
    def inserirUsuario(self):
        nome = self.txtnome.get()
        matricula = self.txtmatricula.get()
        curso = self.txtcurso.get()

        if (nome != '') and (matricula != '') and (curso != ''):
            f1.insere(nome, matricula, curso)
    
            self.lblmsg["text"] = "Inserção feita com sucesso!"
    
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

        if f1.isEmpty() == True:
            self.lblmsg["text"] = "Fila vazia!"

            
            self.txtnome.delete(0, END)
            self.txtmatricula.delete(0, END)
            self.txtcurso.delete(0, END)
        
        else:
            divisao = f1.show()
  
            self.lblmsg["text"] = "Remoção feita com sucesso!"
    
            
            self.txtnome.delete(0, END)
            self.txtmatricula.delete(0, END)
            self.txtcurso.delete(0, END)

            self.txtnome.insert(INSERT, divisao.get_nome())
            self.txtmatricula.insert(INSERT, divisao.get_matricula())
            self.txtcurso.insert(INSERT, divisao.get_curso())

            f1.remove()
  





    #Método para buscar por aluno
    def buscarUsuario(self):

        if f1.isEmpty() == True:
            self.lblmsg["text"] = "Fila vazia!"

            
            self.txtnome.delete(0, END)
            self.txtmatricula.delete(0, END)
            self.txtcurso.delete(0, END)
        
        else:
            divisao = f1.show()
    
            self.lblmsg["text"] = "Busca feita com sucesso!"
    

            self.txtnome.delete(0, END)
            self.txtnome.insert(INSERT, divisao.get_nome())
    
            self.txtmatricula.delete(0, END)
            self.txtmatricula.insert(INSERT, divisao.get_matricula())
    
            self.txtcurso.delete(0, END)
            self.txtcurso.insert(INSERT, divisao.get_curso())




    #Método para checar se a lista de alunos está vazia
    def emptyList(self):
        self.lblmsg["text"] = 'Fila vazia? \n{}'.format(str(f1.isEmpty()))
    




    #Método para checar o tamanho da lista de alunos
    def sizeList(self):
        self.lblmsg["text"] = 'Tamanho da fila: \n{}'.format(str(f1.size()))
  
  




  
root = Tk()
root.title('Fila')
Application(root)
root.mainloop()
