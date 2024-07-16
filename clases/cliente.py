class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial_compras = []

    def actualizar_informacion(self, direccion = None, telefono = None):
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono

    def registrar_compra(self,compra):
        self.historial_compras.append(compra)

    def mostrar_informacion(self):
        for compra in self.historial_compras:
            productos = ", ".join([producto.nombre for producto in compra.lista_de_productos])
            print(f"Cliente: {self.nombre}, Direccion = {self.direccion}, Telefono = {self.telefono}, Fecha de Compra = {compra.fecha}, Productos = {productos}, Total = {compra.total}")