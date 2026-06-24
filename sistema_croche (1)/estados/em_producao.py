from estados.estado_producao import EstadoProducao

class EmProducao(EstadoProducao):

    def proximo_estado(self, pedido):
        from estados.finalizado import Finalizado
        pedido.estado = Finalizado()

    def nome(self):
        return "Em Produção"