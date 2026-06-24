from estados.pendente import Pendente


class Pedido:
    """
    Pedido realizado por um cliente.
    """

    def __init__(self, id, cliente=None):
        self.id = id
        self.cliente = cliente
        self.estado = Pendente()
        self.valor_total = 0.0
        self.itens = []

    def adicionar_item(self, item):
        """
        Adiciona item ao pedido e recalcula o total.
        """
        self.itens.append(item)
        self.valor_total = self.calcular_total()

    def calcular_total(self):
        """
        Soma os subtotais dos itens.
        """
        total = 0

        for item in self.itens:
            total += item.calcular_subtotal()

        return total

    def alterar_estado(self):
        self.estado.proximo_estado(self)

    def mostrar_estado(self):
        return self.estado.nome()

    def __str__(self):
        return (
            f"Pedido {self.id} - "
            f"Total: R$ {self.valor_total:.2f} - "
            f"Estado: {self.mostrar_estado()}"
        )
