class ReceitaCroche:
    """
    Relaciona um material a um produto e
    informa quanto daquele material é necessário.
    """

    def __init__(self, id, material, qntd_necessaria):
        self.id = id
        self.material = material
        self.qntd_necessaria = qntd_necessaria

    def custo_material(self):
        """
        Calcula o custo do material utilizado.
        """
        return (self.qntd_necessaria * self.material.custo_uni)