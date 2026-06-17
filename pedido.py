from datetime import date


class Pedido:
    """
    Pedido realizado por um cliente.
    """

    def __init__(self, id):
        self.id = id
        self.data_pedido = date.today()
        self.status = "Aberto"
        self.valor_total = 0.0
        self.itens = []

    def adicionar_item(self, item):
        """
        Adiciona item ao pedido.
        """
        self.itens.append(item)#veer isso 
        self.valor_total = self.calcular_total()

    def calcular_total(self):
        """
        Soma os subtotais dos itens.
        """
        total = 0

        for item in self.itens:
            total += item.subtotal

        return total

    def __str__(self):
        return (
            f"Pedido {self.id} - "
            f"Total: R$ {self.valor_total:.2f}"
        )
