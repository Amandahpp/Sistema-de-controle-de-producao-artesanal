class Material:
    def __init__(self,id,nome,qntd_estoque, uni_medida,custo_uni):
        self.id= id
        self.nome = nome
        self.qntd_estoque = qntd_estoque
        self.uni_media = uni_medida
        self.custo_uni = custo_uni

    def atualizar_estoque(self,qntd):
        self.qntd_estoque += qntd
    #ver pra que serve isso 
    def __str__(self):
        return f"{self.nome} ({self.quantidade_estoque} {self.unidade_medida})"