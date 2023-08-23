class Motoboy:
    def __init__(self, nome, taxa_entrega, lojas_exclusivas=None):
        self.nome = nome
        self.taxa_entrega = taxa_entrega
        self.lojas_exclusivas = lojas_exclusivas if lojas_exclusivas else []
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def calcular_comissao(self):
        comissao = 0
        for pedido in self.pedidos:
            valor_entrega = pedido.valor_entrega(self)
            comissao += valor_entrega
        return comissao
