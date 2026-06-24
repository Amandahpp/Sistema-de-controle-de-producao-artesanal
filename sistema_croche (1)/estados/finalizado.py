from estados.estado_producao import EstadoProducao

class Finalizado(EstadoProducao):

    def proximo_estado(self, pedido):
        print("Pedido já finalizado.")

    def nome(self):
        return "Finalizado"