class ItemPedido:
    """
    Item pertencente a um pedido.
    """

    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.subtotal = self.calcular_subtotal()

    def calcular_subtotal(self):
        """
        Quantidade x preço do produto.
        """
        return self.quantidade * self.produto.preco_venda

    def __str__(self):
        return (
            f"{self.produto.nome} - "
            f"Qtd: {self.quantidade} - "
            f"Subtotal: R$ {self.subtotal:.2f}"
        )