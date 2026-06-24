class Material:
    def __init__(self, id, nome, qntd_estoque, uni_medida, custo_uni, estoque_min=0):
        self.id = id
        self.nome = nome
        self.qntd_estoque = qntd_estoque
        self.uni_medida = uni_medida
        self.custo_uni = custo_uni

    def atualizar_estoque(self, quantidade):
       #aqui eu criei a função atualizar_estoque para poder atualizar o estoque do material#
        if self.qntd_estoque + quantidade < 0:
            raise ValueError(
                "Material insuficiente."
            )

        self.qntd_estoque += quantidade
       
