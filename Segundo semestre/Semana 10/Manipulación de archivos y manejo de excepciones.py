import os

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def from_string(data):
        nombre, cantidad, precio = data.strip().split(',')
        return Producto(nombre, int(cantidad), float(precio))

class Inventario:
    ARCHIVO = "inventario.txt"

    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        if not os.path.exists(self.ARCHIVO):
            open(self.ARCHIVO, 'w').close()
            return
        try:
            with open(self.ARCHIVO, "r") as archivo:
                self.productos = {p.nombre: p for p in map(Producto.from_string, archivo)}
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al leer el archivo: {e}")

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO, "w") as archivo:
                archivo.writelines(f"{p}\n" for p in self.productos.values())
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al escribir en el archivo: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        if nombre in self.productos:
            print("El producto ya existe. Use la opción de actualización.")
        else:
            self.productos[nombre] = Producto(nombre, cantidad, precio)
            self.guardar_en_archivo()
            print("Producto agregado correctamente.")

    def actualizar_producto(self, nombre, cantidad, precio):
        if nombre in self.productos:
            self.productos[nombre].cantidad = cantidad
            self.productos[nombre].precio = precio
            self.guardar_en_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("El producto no existe.")

    def eliminar_producto(self, nombre):
        if self.productos.pop(nombre, None):
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("El producto no existe.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\nInventario Actual:")
            print("-" * 30)
            for producto in self.productos.values():
                print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
            print("-" * 30)

if __name__ == "__main__":
    inventario = Inventario()
    while True:
        print("\n===== Gestión de Inventario =====")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            nombre = input("Nombre del producto: ").strip()
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(nombre, cantidad, precio)
        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ").strip()
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

