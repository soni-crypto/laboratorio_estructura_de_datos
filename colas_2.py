from collections import deque

class SistemaGestionPedidos:
    def __init__(self):
        self.cola_pedidos = deque()

    def agregar_pedido(self, pedido):
        self.cola_pedidos.append(pedido)
        print(f"Pedido agregado: {pedido}")

    def procesar_pedido(self):
        if len(self.cola_pedidos) > 0:
            pedido_procesado = self.cola_pedidos.popleft()
            print(f"Pedido procesado: {pedido_procesado}")
        else:
            print("No hay pedidos para procesar.")

    def mostrar_estado_cola(self):
        if len(self.cola_pedidos) > 0:
            print("Pedidos en cola:")
            for pedido in self.cola_pedidos:
                print(pedido)
        else:
            print("No hay pedidos en cola.")

# Ejemplo de uso
sistema_pedidos = SistemaGestionPedidos()

sistema_pedidos.agregar_pedido("Pedido 1")
sistema_pedidos.agregar_pedido("Pedido 2")
sistema_pedidos.agregar_pedido("Pedido 3")

sistema_pedidos.mostrar_estado_cola()

sistema_pedidos.procesar_pedido()
sistema_pedidos.procesar_pedido()

sistema_pedidos.mostrar_estado_cola()
