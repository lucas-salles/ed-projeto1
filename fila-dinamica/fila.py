from no import No

class Fila: 
  #Construtor
  def __init__(self, topo=None):
    self.__topo = topo



  #Metodo para inserir um elemento na fila
  def insere(self, nome, matricula, curso):
    p = No(nome, matricula, curso)
    
    if self.__topo == None:
      self.__topo = p

    else:
      aux = self.__topo

      while aux.get_proximo() != None:
        aux = aux.get_proximo()

      aux.set_proximo(p)



  #Metodo para remover um elemento da fila
  def remove(self):
    if self.__topo == None:
      return None
      
    else:
      removido = self.__topo
      self.__topo = self.__topo.get_proximo()
      return removido



  #Metodo para checar se a fila está vazia
  def isEmpty(self):
    if self.__topo == None:
      return True
    else:
      return False



  #Metodo para retornar o tamanho da fila
  def size(self):
    if self.__topo == None:
      return 0

    else:
      p = self.__topo
      cont = 0

      while p != None:
        p = p.get_proximo()
        cont += 1

      return cont



  #Metodo para retornar o topo da fila
  def show(self):
    if self.__topo == None:
      return None

    else:
      return self.__topo