import os


class ArchivoTemporal:
    """
    Clase para gestionar un archivo temporal, con soporte para escritura y eliminación automática al finalizar.
    """

    def __init__(self, nombre_archivo):
        """
        Constructor de la clase. Crea un archivo temporal.
        :param nombre_archivo: Nombre del archivo temporal.
        """
        self.nombre_archivo = nombre_archivo
        print(f"Creando el archivo temporal: {self.nombre_archivo}")
        try:
            # Crear el archivo temporal y escribir una línea inicial
            with open(self.nombre_archivo, 'w') as archivo:
                archivo.write("Este es un archivo temporal.\n")
        except OSError as e:
            print(f"Error al crear el archivo {self.nombre_archivo}: {e}")
        else:
            print(f"Archivo {self.nombre_archivo} creado exitosamente.")

    def escribir_datos(self, datos):
        """
        Escribe datos adicionales en el archivo temporal.
        :param datos: Texto a escribir en el archivo.
        """
        try:
            with open(self.nombre_archivo, 'a') as archivo:
                archivo.write(datos + "\n")
        except OSError as e:
            print(f"Error al escribir en el archivo {self.nombre_archivo}: {e}")
        else:
            print(f"Datos escritos correctamente: {datos}")

    def leer_archivo(self):
        """
        Lee y muestra el contenido del archivo temporal.
        """
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
            print(f"Contenido de {self.nombre_archivo}:\n{contenido}")
        except OSError as e:
            print(f"Error al leer el archivo {self.nombre_archivo}: {e}")

    def __del__(self):
        """
        Destructor de la clase. Elimina el archivo temporal.
        """
        if os.path.exists(self.nombre_archivo):
            try:
                os.remove(self.nombre_archivo)
                print(f"El archivo temporal {self.nombre_archivo} ha sido eliminado.")
            except OSError as e:
                print(f"Error al eliminar el archivo {self.nombre_archivo}: {e}")
        else:
            print(f"El archivo temporal {self.nombre_archivo} ya no existe.")


if __name__ == "__main__":
    print("Bienvenido al programa de manejo de archivos temporales.")

    # Solicitar al usuario el nombre del archivo temporal
    nombre_archivo = input("Ingrese el nombre del archivo temporal (e.g., temporal.txt): ").strip()
    if not nombre_archivo:
        print("El nombre del archivo no puede estar vacío. Saliendo del programa.")
        exit(1)

    archivo = ArchivoTemporal(nombre_archivo)

    # Menú interactivo
    while True:
        print("\nOpciones:")
        print("1. Escribir datos en el archivo")
        print("2. Leer el contenido del archivo")
        print("3. Salir (el archivo será eliminado)")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            datos = input("Ingrese los datos que desea escribir en el archivo: ").strip()
            if datos:
                archivo.escribir_datos(datos)
            else:
                print("No se escribió nada. Intente nuevamente.")
        elif opcion == "2":
            archivo.leer_archivo()
        elif opcion == "3":
            print("Saliendo del programa. El archivo será eliminado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

    # El archivo se elimina automáticamente al salir del programa
