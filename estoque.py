class Estoque:
    def __init__(self, id, material, qntd_atual, estoque_min):
        self.id = id
        self.material = material
        self.qntd_atual = qntd_atual
        self.estoque_min = estoque_min

    def entrada(self, quantidade):
        self. qntd_atual += quantidade

    def saida(self, quantidade):
        if quantidade > self.qntd_atual:
            raise ValueError("Estoque insuficiente")

        self.qntd_atual -= quantidade

    def verificar_estoque(self):
        return self.qntd_atual <= self.estoque_min