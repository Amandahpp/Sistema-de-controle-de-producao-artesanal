class ReceitaCroche:
   
    ##aqui eu fiz o relacionamento de um material a um produto ##
    ##e tambem a quantidade necessaria do material para fazer a atualizacao no estoque quanod for necessario ##

    def __init__(self, id, material, qntd_necessaria):
        self.id = id
        self.material = material
        self.qntd_necessaria = qntd_necessaria

    def custo_material(self):
       ##calcula o custo dos materiais utilizados ##
        return (self.qntd_necessaria * self.material.custo_uni)