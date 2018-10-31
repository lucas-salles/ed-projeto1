from no import No

class Lista:
    #Construtor
    def __init__(self, head = None):
        self.__head = head



    #Metodo para adicionar um valor na lista
    def add(self, posicao, nome, matricula, curso):
        p = No(nome, matricula, curso)

        if self.__head == None:
            self.__head = p

        elif posicao == 0:
            p.set_proximo(self.__head)
            self.__head = p

        elif posicao > self.size():
            aux = self.__head

            while aux.get_proximo() != None:
                aux = aux.get_proximo()

            aux.set_proximo(p)

        else:
            q = self.__head
            r = self.__head

            for i in range(posicao):
                q = r
                r = r.get_proximo()
            p.set_proximo(r)
            q.set_proximo(p)



    #Metodo para remover um valor da lista
    def remove(self, posicao):
        if self.__head == None:
            return None

        elif posicao == 0 or self.size() == 1:
            removido = self.__head
            self.__head = self.__head.get_proximo()
            return removido

        elif posicao >= self.size():
            p = self.__head
            q = self.__head

            while p.get_proximo() != None:
                q = p
                p = p.get_proximo()

            removido = p
            q.set_proximo(None)
            return removido

        else:
            p = self.__head
            q = self.__head

            for i in range(posicao):
                p = q
                q = q.get_proximo()

            removido = q
            p.set_proximo(q.get_proximo())
            return removido



    #Metodo para checar se a lista está vazia      
    def isEmpty(self):
        if self.__head == None:
            return True
        else:
            return False



    #Metodo para retornar o tamanho da lista
    def size(self):
        if self.__head == None:
            return 0

        else:
            p = self.__head
            cont = 0

            while p != None:
                p = p.get_proximo()
                cont += 1

            return cont
    


    #Metodo para retornar um elemento da lista
    def show(self, posicao):
        if self.__head == None:
            return None

        elif posicao == 0:
            return self.__head

        elif posicao >= self.size():
            p = self.__head

            while p.get_proximo() != None:
                p = p.get_proximo()

            return p

        else:
            p = self.__head

            for i in range(posicao):
                p = p.get_proximo()

            return p