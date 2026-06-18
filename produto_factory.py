from produtocroche import Produto

class ProdutoFactory:
    @staticmethod
    def criar_produto(id,nome,descricao, preco_venda,tempo_producao):
          return Produto(id,nome,descricao,preco_venda,tempo_producao)