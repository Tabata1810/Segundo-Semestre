import json


class Producto:
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad: int):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio: float):
        self.precio = nuevo_precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self, archivo_datos: str = "Almacen.json"):
        self.productos = {}
        self.archivo_datos = archivo_datos
        self.cargar_desde_archivo()

    def agregar_producto(self, producto: Producto):
        if producto.id_producto in self.productos:
            print("Error: El ID del producto ya existe.")
            return
        self.productos[producto.id_producto] = producto
        self.guardar_en_archivo()
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto: str):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto: str, cantidad: int = None, precio: float = None):
        producto = self.productos.get(id_producto)
        if producto:
            if cantidad is not None:
                producto.actualizar_cantidad(cantidad)
            if precio is not None:
                producto.actualizar_precio(precio)
            self.guardar_en_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre: str):
        return [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_en_archivo(self):
        with open(self.archivo_datos, "w") as f:
            json.dump({k: vars(v) for k, v in self.productos.items()}, f, indent=4)

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo_datos, "r") as f:
                datos = json.load(f)
                self.productos = {k: Producto(**v) for k, v in datos.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}


def menu():
    inventario = Inventario()
    opciones = {
        "1": "Agregar producto",
        "2": "Eliminar producto",
        "3": "Actualizar producto",
        "4": "Buscar producto por nombre",
        "5": "Mostrar inventario",
        "6": "Salir"
    }

    while True:
        print("\n===== MENÚ DE INVENTARIO =====")
        for key, value in opciones.items():
            print(f"{key}. {value}")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            id_producto = input("ID: ").strip()
            nombre = input("Nombre: ").strip()
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ").strip()
            cantidad = input("Nueva cantidad (dejar vacío si no se cambia): ").strip()
            precio = input("Nuevo precio (dejar vacío si no se cambia): ").strip()
            try:
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ").strip()
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("Producto no encontrado.")
        elif opcion == "5":
            inventario.mostrar_inventario()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
