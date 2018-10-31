class No:
    #Construtor
    def __init__(self, nome=None, matricula=None, curso=None, proximo=None):
        self.__nome = nome
        self.__matricula = matricula
        self.__curso = curso
        self.__proximo = proximo



    #Métodos Acessadores    
    def get_nome(self):
        return self.__nome
    
    def get_matricula(self):
        return self.__matricula
    
    def get_curso(self):
        return self.__curso
    
    def get_proximo(self):
        return self.__proximo
    


    #Métodos Alteradores
    def set_nome(self, novoNome):
        self.__nome = novoNome
    
    def set_matricula(self, novaMatricula):
        self.__matricula = novaMatricula
    
    def set_curso(self, novoCurso):
        self.__curso = novoCurso

    def set_proximo(self, outro):
        self.__proximo = outro
    




    def __str__(self):
        return 'Nome: {}\nMatrícula: {}\nCurso: {}'.format(self.__nome, self.__matricula, self.__curso)