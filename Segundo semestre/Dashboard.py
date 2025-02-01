import os

def mostrar_codigo(ruta_script):
    """Función para mostrar el contenido de un archivo dado su ruta."""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    """Función para mostrar un menú interactivo con las opciones disponibles."""
    # Define la ruta base donde se encuentra el Dashboard.py
    ruta_base = os.path.dirname(__file__)

    # Opciones basadas en las semanas de tu proyecto
    opciones = {
        '1': 'Semana 2/Semana2.py',
        '2': 'Semana 3/Programación Orientada a Objetos (POO).py',
        '3': 'Semana 3/Programación Tradicional.py',
        '4': 'Semana 4/Características de la Programación Orientada a Objetos.py',
        '5': 'Semana 5/Semana 5.py',
        '6': 'Semana 6/Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '7': 'Semana 7/Constructores y Destructores.py'
    }

    while True:
        print("\n===== Menú Principal - Tabata Cifuentes´s dashboard =====")
        # Imprime las opciones del menú
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")

        if eleccion == '0':
            print("Saliendo del Dashboard...")
            break
        elif eleccion in opciones:
            # Asegura que la ruta sea absoluta
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()