from models.motoboy import Motoboy
from models.loja import Loja
from models.pedido import Pedido, AtribuirPedidos

class Main:

    def check_motoboy():
        motoboy_procurado = input("Digite o nome do motoboy: ")
        for motoboy in motoboys:
            if (motoboy.nome == motoboy_procurado):
                print(f"\nMotoboy: {motoboy.nome}")

                for i, pedido in enumerate(atribuidor.motoboy_pedidos[motoboy]["pedidos"]):
                    print(f"Pedido {i + 1} da {atribuidor.motoboy_pedidos[motoboy]['lojas'][i]}")
                    print(f"Comissão a ser ganha: R${pedido.valor_entrega(motoboy):.2f}")

                total_pedidos = len(atribuidor.motoboy_pedidos[motoboy]["pedidos"])
                total_ganho = sum(pedido.valor_entrega(motoboy) for pedido in atribuidor.motoboy_pedidos[motoboy]["pedidos"])

                print(f"\nTotal Pedidos: {total_pedidos} pedidos")
                print(f"Total Ganho: R${total_ganho:.2f}")
                break
        else:
            print("Motoboy não encontrado!")
            print("Motoboys cadastrados:")
            for motoboy in motoboys:
                print(f"Motoboy: {motoboy.nome}")
            Main.check_motoboy()
    
    def check_all():
        for motoboy in motoboys:
            print(f"\nMotoboy: {motoboy.nome}")

            for i, pedido in enumerate(atribuidor.motoboy_pedidos[motoboy]["pedidos"]):
                print(f"Pedido {i + 1} da {atribuidor.motoboy_pedidos[motoboy]['lojas'][i]}")
                print(f"Comissão a ser ganha: R${pedido.valor_entrega(motoboy):.2f}")

            total_pedidos = len(atribuidor.motoboy_pedidos[motoboy]["pedidos"])
            total_ganho = sum(pedido.valor_entrega(motoboy) for pedido in atribuidor.motoboy_pedidos[motoboy]["pedidos"])

            print(f"\nTotal Pedidos: {total_pedidos} pedidos")
            print(f"Total Ganho: R${total_ganho:.2f}")

if __name__ == "__main__":

    motoboy1 = Motoboy(nome="Moto 1", taxa_entrega=2)
    motoboy2 = Motoboy(nome="Moto 2", taxa_entrega=2)
    motoboy3 = Motoboy(nome="Moto 3", taxa_entrega=2)
    motoboy4 = Motoboy(nome="Moto 4", taxa_entrega=2, lojas_exclusivas=["Loja 1"])
    motoboy5 = Motoboy(nome="Moto 5", taxa_entrega=3)
    # motoboy5 = Motoboy(nome="Moto 5", taxa_entrega=3, lojas_exclusivas=["Loja 1"])

    loja1 = Loja(nome="Loja 1", taxa_comissao=5)
    loja2 = Loja(nome="Loja 2", taxa_comissao=5)
    loja3 = Loja(nome="Loja 3", taxa_comissao=15)

    pedidos_loja1 = [
        Pedido(numero=1, valor=50),
        Pedido(numero=2, valor=50),
        Pedido(numero=3, valor=50)
    ]
    pedidos_loja2 = [
        Pedido(numero=1, valor=50),
        Pedido(numero=2, valor=50),
        Pedido(numero=3, valor=50),
        Pedido(numero=4, valor=50)
    ]
    pedidos_loja3 = [
        Pedido(numero=1, valor=50),
        Pedido(numero=2, valor=50),
        Pedido(numero=3, valor=100)
    ]

    loja1.pedidos.extend(pedidos_loja1)
    loja2.pedidos.extend(pedidos_loja2)
    loja3.pedidos.extend(pedidos_loja3)

    motoboys = [motoboy1, motoboy2, motoboy3, motoboy4, motoboy5]
    lojas = [loja1, loja2, loja3]

    atribuidor = AtribuirPedidos(motoboys, lojas)
    atribuidor.atribuir_pedidos()

    while True:
        escolha = input("Deseja verificar um motoboy específico? (S/N): ").upper()
        if escolha == "S":
            Main.check_motoboy()
        elif escolha == "N":
            break
        else:
            print("Opção inválida. Por favor, escolha 'S' para Sim ou 'N' para Não.")

    while True:
        escolha = input("Deseja verificar todos os motoboys? (S/N): ").upper()
        if escolha == "S":
            Main.check_all()
        elif escolha == "N":
            break
        else:
            print("Opção inválida. Por favor, escolha 'S' para Sim ou 'N' para Não.")
