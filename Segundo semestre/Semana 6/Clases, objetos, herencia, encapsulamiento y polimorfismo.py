# Clase base: Animal
class Animal:
    def __init__(self, nombre, edad):
        # Atributos de la clase base, encapsulados (privados)
        self.__nombre = nombre
        self.__edad = edad

    # Método getter para obtener el nombre
    def get_nombre(self):
        return self.__nombre

    # Método setter para modificar el nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Método getter para obtener la edad
    def get_edad(self):
        return self.__edad

    # Método setter para modificar la edad
    def set_edad(self, edad):
        if edad >= 0:  # Validación de edad
            self.__edad = edad
        else:
            print("La edad no puede ser negativa.")

    # Método de comportamiento común para todas las clases derivadas
    def hablar(self):
        return "El animal hace un sonido."


# Clase derivada: Perro (hereda de Animal)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, edad)
        self.__raza = raza

    # Método getter para obtener la raza
    def get_raza(self):
        return self.__raza

    # Método setter para modificar la raza
    def set_raza(self, raza):
        self.__raza = raza

    # Sobrescritura del método hablar (polimorfismo)
    def hablar(self):
        return f"{self.get_nombre()} (el perro) ladra."


# Clase derivada: Gato (hereda de Animal)
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, edad)
        self.__color = color

    # Método getter para obtener el color
    def get_color(self):
        return self.__color

    # Método setter para modificar el color
    def set_color(self, color):
        self.__color = color

    # Sobrescritura del método hablar (polimorfismo)
    def hablar(self):
        return f"{self.get_nombre()} (el gato) maúlla."


# Función para validar que la edad sea un número positivo
def validar_edad():
    while True:
        try:
            edad = int(input("Ingresa la edad del animal: "))
            if edad >= 0:
                return edad
            else:
                print("La edad no puede ser negativa. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido para la edad.")


# Función principal para interactuar con el usuario
def main():
    print("Bienvenido al programa de animales.\n")

    # Se asegura de que el tipo de animal sea válido
    while True:
        tipo_animal = input("¿Qué tipo de animal deseas crear? (Perro/Gato): ").strip().lower()
        if tipo_animal in ["perro", "gato"]:
            break
        else:
            print("Opción no válida. Por favor elige 'Perro' o 'Gato'.\n")

    nombre = input("Ingresa el nombre del animal: ").strip()

    edad = validar_edad()

    # Crear el animal correspondiente según la elección del usuario
    if tipo_animal == "perro":
        raza = input("Ingresa la raza del perro: ").strip()
        animal = Perro(nombre, edad, raza)
    elif tipo_animal == "gato":
        color = input("Ingresa el color del gato: ").strip()
        animal = Gato(nombre, edad, color)

    # Muestra la información del animal creado
    print("\nInformación del animal creado:")
    print(f"Nombre: {animal.get_nombre()}")
    print(f"Edad: {animal.get_edad()} años")

    if isinstance(animal, Perro):
        print(f"Raza: {animal.get_raza()}")
    elif isinstance(animal, Gato):
        print(f"Color: {animal.get_color()}")

    # Mostrar el sonido del animal
    print(f"Sonido: {animal.hablar()}")


# Llamar a la función principal para que el programa inicie
if __name__ == "__main__":
    main()