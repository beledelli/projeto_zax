class Pedido:
    def __init__(self, numero, valor):
        self.numero = numero
        self.valor = valor

    def valor_entrega(self, motoboy):
        taxa_entrega = motoboy.taxa_entrega
        taxa_comissao = self.valor * motoboy.taxa_entrega * 0.01
        return taxa_entrega + taxa_comissao

class AtribuirPedidos:
    def __init__(self, motoboys, lojas):
        self.motoboys = motoboys
        self.lojas = lojas
        self.motoboy_pedidos = {motoboy: {"pedidos": [], "lojas": []} for motoboy in self.motoboys}

    def atribuir_pedidos(self):
        for loja in self.lojas:
            for pedido in loja.pedidos:
                motoboys_disponiveis = []
                for motoboy in self.motoboys:
                    if (loja.nome in motoboy.lojas_exclusivas) \
                            and (loja.nome not in self.motoboy_pedidos[motoboy]["lojas"]):
                        motoboys_disponiveis.append(motoboy)

                if not motoboys_disponiveis:
                    motoboys_disponiveis = self.motoboys

                motoboy_escolhido = min(motoboys_disponiveis, key=lambda x: len(x.pedidos))
                motoboy_escolhido.adicionar_pedido(pedido)

                self.motoboy_pedidos[motoboy_escolhido]["pedidos"].append(pedido)
                self.motoboy_pedidos[motoboy_escolhido]["lojas"].append(loja.nome)
                motoboy_escolhido.calcular_comissao()
