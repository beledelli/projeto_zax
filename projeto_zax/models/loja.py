class Loja:
    def __init__(self, nome, taxa_comissao):
        self.nome = nome
        self.taxa_comissao = taxa_comissao
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)
