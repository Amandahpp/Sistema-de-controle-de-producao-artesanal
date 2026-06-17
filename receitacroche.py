class ReceitaCroche:
    """
    Relaciona um material a um produto e
    informa quanto daquele material é necessário.
    """

    def __init__(self, id, material, quantidade_necessaria):
        self.id = id
        self.material = material
        self.quantidade_necessaria = quantidade_necessaria

    def custo_material(self):
        """
        Calcula o custo do material utilizado.
        """
        return (
            self.quantidade_necessaria *
            self.material.custo_unitario
        )