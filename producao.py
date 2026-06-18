from pendente import Pendente

class Producao:

    def __init__(
        self,
        id,
        produto,
        quantidade_produzida
    ):

        self.id = id
        self.produto = produto
        self.quantidade_produzida = quantidade_produzida

        self.estado = Pendente()

    def alterar_estado(self):
        self.estado.proximo_estado(self)

    def mostrar_estado(self):
        return self.estado.nome()

    def __str__(self):

        return (
            f"Produção {self.id} - "
            f"{self.produto.nome} - "
            f"Estado: {self.mostrar_estado()}"
        )
