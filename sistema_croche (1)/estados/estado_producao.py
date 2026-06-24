from abc import ABC, abstractmethod
##utilizei aqui a classe abstrata para criar os estados de producao e poder utilizar o polimorfismo para alterar o estado do pedido ##
class EstadoProducao(ABC):

    @abstractmethod
    def proximo_estado(self, pedido):
        pass

    @abstractmethod
    def nome(self):
        pass