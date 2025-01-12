# Clase para representar la información diaria del clima
class ClimaDiario:
    def __init__(self, temperatura):
        """
        Inicializa un objeto con la temperatura del día.
        """
        self.__temperatura = temperatura  # Atributo privado

    def obtener_temperatura(self):
        """
        Método para obtener la temperatura del día.
        """
        return self.__temperatura

    def establecer_temperatura(self, temperatura):
        """
        Método para establecer la temperatura del día.
        """
        if isinstance(temperatura, (int, float)):  # Validar que la temperatura sea numérica
            self.__temperatura = temperatura
        else:
            raise ValueError("La temperatura debe ser un número.")

# Clase para manejar la información del clima semanal
class ClimaSemanal:
    def __init__(self):
        """
        Inicializa la lista de clima semanal vacía.
        """
        self.__clima_semanal = []  # Atributo privado

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas de cada día de la semana.
        """
        print("Ingrese las temperaturas diarias para la semana:")
        for i in range(7):
            while True:
                try:
                    temp = float(input(f"Día {i + 1}: "))
                    clima_diario = ClimaDiario(temp)  # Crear un objeto ClimaDiario para cada día
                    self.__clima_semanal.append(clima_diario)  # Añadirlo a la lista
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

    def calcular_promedio(self):
        """
        Método para calcular el promedio de las temperaturas semanales.
        """
        suma = sum(clima.obtener_temperatura() for clima in self.__clima_semanal)
        return suma / len(self.__clima_semanal)

def main():
    """
    Función principal para coordinar las operaciones.
    """
    clima_semanal = ClimaSemanal()  # Crear un objeto de la clase ClimaSemanal
    clima_semanal.ingresar_temperaturas()
    promedio = clima_semanal.calcular_promedio()
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
