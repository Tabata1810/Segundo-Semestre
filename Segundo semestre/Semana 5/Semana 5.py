# Programa que realiza cálculos de áreas y conversiones de unidades.
# Funcionalidad: Permite calcular el área de diferentes figuras geométricas y convertir unidades de medida (metros a kilómetros y viceversa).
# Tipos de datos: Integer, float, string, boolean son utilizados adecuadamente.
# Identificadores: Se siguen las convenciones de snake_case.

import math


def calcular_area_circulo(radio):
    """
    Función para calcular el área de un círculo.
    Parámetros:
    radio (float): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    return math.pi * radio ** 2  # Fórmula para el área de un círculo


def calcular_area_rectangulo(base, altura):
    """
    Función para calcular el área de un rectángulo.
    Parámetros:
    base (float): La base del rectángulo.
    altura (float): La altura del rectángulo.

    Retorna:
    float: El área del rectángulo.
    """
    return base * altura  # Fórmula para el área de un rectángulo


def calcular_area_triangulo(base, altura):
    """
    Función para calcular el área de un triángulo.
    Parámetros:
    base (float): La base del triángulo.
    altura (float): La altura del triángulo.

    Retorna:
    float: El área del triángulo.
    """
    return 0.5 * base * altura  # Fórmula para el área de un triángulo


def convertir_metros_a_kilometros(metros):
    """
    Función para convertir metros a kilómetros.
    Parámetros:
    metros (float): La cantidad de metros.

    Retorna:
    float: La cantidad convertida en kilómetros.
    """
    return metros / 1000  # Conversión de metros a kilómetros


def convertir_kilometros_a_metros(kilometros):
    """
    Función para convertir kilómetros a metros.
    Parámetros:
    kilometros (float): La cantidad de kilómetros.

    Retorna:
    float: La cantidad convertida en metros.
    """
    return kilometros * 1000  # Conversión de kilómetros a metros


def obtener_entrada_numerica(prompt):
    """
    Función para obtener una entrada numérica del usuario.
    Si la entrada no es válida, repite hasta obtener un valor numérico válido.

    Parámetros:
    prompt (str): Mensaje que se muestra al usuario.

    Retorna:
    float: La entrada numérica válida proporcionada por el usuario.
    """
    while True:
        try:
            return float(input(prompt))  # Solicita la entrada y la convierte a flotante
        except ValueError:
            print(
                "Por favor, ingresa un valor numérico válido.")  # Manejo de error si el valor ingresado no es numérico


def main():
    """
    Función principal que permite al usuario elegir qué operación realizar.
    """
    print("¡Bienvenido al programa de cálculo de áreas y conversiones de unidades!")

    while True:
        # Menú de opciones
        opcion = input("¿Qué deseas hacer? (1: Calcular área, 2: Convertir unidades, 3: Salir): ")

        if opcion == "1":
            # Calcular área de figuras geométricas
            figura = input("¿De qué figura deseas calcular el área? (1: Círculo, 2: Rectángulo, 3: Triángulo): ")

            if figura == "1":
                radio = obtener_entrada_numerica("Introduce el radio del círculo: ")
                area = calcular_area_circulo(radio)
                print(f"El área del círculo es: {area:.2f} unidades cuadradas.")

            elif figura == "2":
                base = obtener_entrada_numerica("Introduce la base del rectángulo: ")
                altura = obtener_entrada_numerica("Introduce la altura del rectángulo: ")
                area = calcular_area_rectangulo(base, altura)
                print(f"El área del rectángulo es: {area:.2f} unidades cuadradas.")

            elif figura == "3":
                base = obtener_entrada_numerica("Introduce la base del triángulo: ")
                altura = obtener_entrada_numerica("Introduce la altura del triángulo: ")
                area = calcular_area_triangulo(base, altura)
                print(f"El área del triángulo es: {area:.2f} unidades cuadradas.")

            else:
                print("Opción no válida.")

        elif opcion == "2":
            # Convertir entre unidades
            convertir = input("¿Qué conversión deseas realizar? (1: Metros a kilómetros, 2: Kilómetros a metros): ")

            if convertir == "1":
                metros = obtener_entrada_numerica("Introduce la cantidad de metros: ")
                kilometros = convertir_metros_a_kilometros(metros)
                print(f"{metros} metros son {kilometros:.2f} kilómetros.")

            elif convertir == "2":
                kilometros = obtener_entrada_numerica("Introduce la cantidad de kilómetros: ")
                metros = convertir_kilometros_a_metros(kilometros)
                print(f"{kilometros} kilómetros son {metros:.2f} metros.")

            else:
                print("Opción no válida.")

        elif opcion == "3":
            # Salir del programa
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")


# Ejecutar el programa
if __name__ == "__main__":
    main()
