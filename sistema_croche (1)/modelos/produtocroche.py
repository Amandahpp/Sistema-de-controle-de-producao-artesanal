class Produto:

##meu factory se encixa aqui ele guarda as infos dos dados la aqui calcula os valores de cada produto e retorna o valor final do produto com base no custo dos materiais e da mão de obra.##
    def __init__(self, id, nome, descricao, preco_venda, tempo_producao):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco_venda = preco_venda
        self.tempo_producao = tempo_producao

        # composição -> ReceitaCroche
        self.receitas = []

    def adicionar_material(self, receita):
        
        self.receitas.append(receita)

    def _custo_materiais(self):
        #soma o custo de todos os materiais utilizados na produção do produto
        return sum(receita.custo_material() for receita in self.receitas)

    def valor_hora(self):
      #coloquei valores reais para produção de peças de crochê, mas podem ser ajustados conforme a necessidade do usuário.
        return 13.50

    def calcular_custo(self):
        custo_mao_obra = self.tempo_producao * self.valor_hora()
        return self._custo_materiais() + custo_mao_obra

    def __str__(self):
        return self.nome

# aqui tambem nos temos polimorfismo e herança, pois cada subclasse recebe um valor diferente, e herda os dados do produto #
class ProdutoAmigurumi(Produto):
    ##coloquei valores reais por mais que nao seja meu nicho ##
    def valor_hora(self):
        return 16.00


class ProdutoVestuario(Produto):
    ##coloquei os valores reais  para producao de roupas e pecas  ##
    def valor_hora(self):
        return 13.50


class ProdutoAcessorio(Produto):
    ##coloquei valores reais para producao de bolsas e outros acessórios ##
    def valor_hora(self):
        return 11.00
