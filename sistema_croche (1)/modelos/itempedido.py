class ItemPedido:
    #essa classe representa um item de um pedido, contendo informações sobre o produto e a quantidade solicitada. Ela também possui um método para calcular o subtotal do item com base no preço de venda do produto e na quantidade.#
    #facilita a organização e o cálculo do valor total de um pedido, permitindo que cada item seja tratado individualmente.#
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_subtotal(self):
        return self.produto.preco_venda * self.quantidade