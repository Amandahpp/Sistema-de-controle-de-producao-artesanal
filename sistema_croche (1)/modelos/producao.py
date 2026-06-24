from estados.pendente import Pendente


class Producao:
    ###aqui eu criei a classe producao para poder registrar a producao de um produto e poder alterar o estado da producao ##

    def __init__(self, id, produto, quantidade_produzida):
        self.id = id
        self.produto = produto
        self.quantidade_produzida = quantidade_produzida
        self.data_inicio = None
        self.data_fim = None
        self.estado = Pendente()
        #None significa que a produção ainda não começou, e Pendente é o estado inicial da produção.
    
    def iniciar(self):
        from datetime import date
        self.data_inicio = date.today()
        self.alterar_estado()
        #today() retorna a data atual, que é atribuída à data_inicio da produção. Em seguida, o método alterar_estado() é chamado
    
    def finalizar(self):
        from datetime import date
        self.data_fim = date.today()
        self.alterar_estado()

    def alterar_estado(self):
        self.estado.proximo_estado(self)

    def mostrar_estado(self):
        return self.estado.nome()

    #str(self) é um método especial que retorna uma representação em string do objeto. Aqui, ele retorna uma string formatada com o id da produção, o nome do produto, a quantidade produzida e o estado atual da produção.#
    def __str__(self):
        return (
            f"Produção {self.id} - "
            f"{self.produto.nome} - "
            f"Qtd: {self.quantidade_produzida} - "
            f"Estado: {self.mostrar_estado()}"
        )
