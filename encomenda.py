from estoque import EstadoEncomenda

class Encomenda:
    def __init__(self,nome:str, descricao:str, recompensa:int):
        self.__cliente = ""       
        self.__encomenda = ""
        self.__produtocroche= 0
        self.__roupacroche= 0
        self.__bolsacroche= 0

        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa
        self.__estado = EstadoEncomenda(self)

    @property
    def cliente(self):
        return self.__cliente
    @property
    def encomenda(self):
        return self.__encomenda
    @property
    def produtocroche(self):
        return self.__produtocroche
    
    @property
    def roupacroche(self):
        return self.__roupacroche
    @property
    def bolsacroche(self):
        return self.__bolsacroche
    
    @property
    def estado(self):
        return self.__estado
     
    @estado.setter
    def estado(self, novo_estado):
        self.__estado = novo_estado