from no import No

class Pilha:
  #Construtor
  def __init__(self, topo = None):
    self.__topo = topo



  #Metodo para adicionar um elemento na pilha
  def add(self, nome, matricula, curso):
    p = No(nome, matricula, curso)

    if self.__topo == None:
      self.__topo = p

    else:
      p.set_proximo(self.__topo)
      self.__topo = p



  #Metodo para remover um elemento da pilha
  def remove(self):
    if self.__topo == None:
      return None
      
    else:
      removido = self.__topo
      self.__topo = self.__topo.get_proximo()
      return removido
  


  #Metodo para retornar para checar se a pilha está vazia
  def isEmpty(self):
    if self.__topo == None:
      return True
    else:
      return False



  #Metodo para retornar o tamanho da pilha
  def size(self):
    if self.__topo == None:
      return 0
    else:
      cont = 0
      p = self.__topo
      while p != None:
        p = p.get_proximo()
        cont += 1
      return cont
  

  
  #Metodo para retornar o topo da pilha
  def show(self):
    if self.__topo == None:
      return None
    else:
      return self.__topo