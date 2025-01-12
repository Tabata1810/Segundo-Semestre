# Programa para calcular el promedio semanal de temperaturas usando programación tradicional.

def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas diarias y las devuelve en una lista.
    """
    temperaturas = []
    print("Ingrese las temperaturas diarias:")
    for i in range(7):  # Una semana tiene 7 días
        while True:
            try:
                temp = float(input(f"Día {i + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Calcula y devuelve el promedio de una lista de temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)

def main():
    """
    Función principal para coordinar la entrada de datos y el cálculo del promedio.
    """
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()