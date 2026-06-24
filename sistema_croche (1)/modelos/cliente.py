class Cliente:
    def __init__(self,id,nome,telefone):
        self.__id = id
        self.__nome = nome
        self.__telefone = telefone

    def realizar_pedido(self):
        print(f"Cliente {self.__nome} realizou um pedido.")

    @property
    def nome(self):
        return self.__nome
    