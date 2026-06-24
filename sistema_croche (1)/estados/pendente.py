from estados.estado_producao import EstadoProducao

class Pendente(EstadoProducao):

    def proximo_estado(self, pedido):
        from estados.em_producao import EmProducao
        pedido.estado = EmProducao()

    def nome(self):
        return "Pendente"