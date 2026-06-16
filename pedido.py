from datetime import date
 
class Producao:
    def __init__(self,id,produto, qntd_produzida):
        self.id = id
        self.produto = produto
        self.qntd_produzida = qntd_produzida

        self.data_inicio = None
        self.data_fim = None
        self.status = "pendente"

    def iniciar(self):
        self.data_inicio = date.today()
        self.status = "Em Produção"

    def finalizar(self):
        self.data_fim = date.today()
        self.status = "Finalizada"
