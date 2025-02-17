class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: ID de producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for p in self.productos.values():
                print(p)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()
    opciones = {
        "1": lambda: inventario.agregar_producto(Producto(
            input("Ingrese el ID del producto: "),
            input("Ingrese el nombre del producto: "),
            int(input("Ingrese la cantidad: ")),
            float(input("Ingrese el precio: "))
        )),
        "2": lambda: inventario.eliminar_producto(input("Ingrese el ID del producto a eliminar: ")),
        "3": lambda: inventario.actualizar_producto(
            input("Ingrese el ID del producto a actualizar: "),
            int(input("Nueva cantidad (deje vacío para omitir): ") or 0) or None,
            float(input("Nuevo precio (deje vacío para omitir): ") or 0) or None
        ),
        "4": lambda: inventario.buscar_por_nombre(input("Ingrese el nombre del producto a buscar: ")),
        "5": inventario.mostrar_productos,
        "6": exit
    }

    while True:
        print("\n===== Sistema de Gestión de Inventarios =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        opciones.get(opcion, lambda: print("Opción no válida. Intente de nuevo."))()


if __name__ == "__main__":
    menu()

