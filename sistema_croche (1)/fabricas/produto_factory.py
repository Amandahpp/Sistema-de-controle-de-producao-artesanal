from modelos.produtocroche import (
    Produto,
    ProdutoAmigurumi,
    ProdutoVestuario,
    ProdutoAcessorio,
)
##minha classe factory foi criada para centralizar a criação de objetos Produto, decidindo qual subclasse instanciar de acordo com a categoria informada. Isso permite que o código que cria produtos não precise conhecer os detalhes de cada subclasse, tornando-o mais limpo e fácil de manter.##
class ProdutoFactory:
   
    _TIPOS = {"amigurumi": ProdutoAmigurumi,"vestuario": ProdutoVestuario,"acessorio": ProdutoAcessorio,}

    @staticmethod
    def tipos_disponiveis():
        return ["amigurumi", "vestuario", "acessorio"]
    ##get foi utitlizado para pegar o tipo de produto que o usuario deseja criar e instanciar a classe correta ##
    @staticmethod
    def criar_produto(tipo, id, nome, descricao, preco_venda, tempo_producao):
        classe = ProdutoFactory._TIPOS.get(tipo.lower(), Produto)
        return classe(id, nome, descricao, preco_venda, tempo_producao)
