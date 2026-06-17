class Produto:
    """
    Produto vendido pela empresa.
    """

    def __init__(self, id, nome, descricao,
                 preco_venda, tempo_producao):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco_venda = preco_venda
        self.tempo_producao = tempo_producao

        # composição -> ReceitaCroche
        self.receitas = []

    def adicionar_material(self, receita):
        """
        Adiciona um item da receita.
        """
        self.receitas.append(receita)

    def calcular_custo(self):
        """
        Soma o custo de todos os materiais.
        """
        total = 0

        for receita in self.receitas:
            total += receita.custo_material()

        return total

    def __str__(self):
        return self.nome