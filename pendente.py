from estado_producao import EstadoPedido

class Pendente(EstadoPedido):

    def proximo_estado(self, pedido):
        from em_producao import EmProducao
        pedido.estado = EmProducao()

    def nome(self):
        return "Pendente"