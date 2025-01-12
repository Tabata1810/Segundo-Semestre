# Definimos la clase Habitacion, que representará una habitación en el hotel.
class Habitacion:
    def __init__(self, numero, tipo, precio):
        """
        Inicializa los atributos de la habitación.
        :param numero: El número de la habitación.
        :param tipo: El tipo de habitación (simple, doble, suite).
        :param precio: El precio de la habitación por noche.
        """
        self.numero = numero  # Número de la habitación
        self.tipo = tipo  # Tipo de habitación (por ejemplo, 'simple', 'doble', 'suite')
        self.precio = precio  # Precio de la habitación
        self.ocupada = False  # Estado de ocupación, inicialmente la habitación no está ocupada.

    def ocupar(self):
        """Método para ocupar la habitación."""
        if not self.ocupada:
            self.ocupada = True
            print(f"La habitación {self.numero} ha sido ocupada.")
        else:
            print(f"La habitación {self.numero} ya está ocupada.")

    def liberar(self):
        """Método para liberar la habitación."""
        if self.ocupada:
            self.ocupada = False
            print(f"La habitación {self.numero} ha sido liberada.")
        else:
            print(f"La habitación {self.numero} ya está libre.")

    def __str__(self):
        """Método que define cómo se muestra la habitación cuando se imprime."""
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio} por noche"


# Clase que maneja las reservas de un cliente.
class Reserva:
    def __init__(self, cliente, habitacion, noches):
        """
        Inicializa la reserva con los datos del cliente, la habitación y la duración de la reserva.
        :param cliente: Nombre del cliente que hace la reserva.
        :param habitacion: Objeto de la clase Habitacion que se reserva.
        :param noches: Número de noches que se desea reservar.
        """
        self.cliente = cliente
        self.habitacion = habitacion
        self.noches = noches
        self.total = self.habitacion.precio * self.noches

    def mostrar_reserva(self):
        """Método para mostrar la información de la reserva."""
        print(f"Cliente: {self.cliente}")
        print(f"Reserva: {self.habitacion}")
        print(f"Duración: {self.noches} noches")
        print(f"Total: ${self.total}")

    def cancelar_reserva(self):
        """Método para cancelar la reserva y liberar la habitación."""
        print(f"Reserva cancelada para {self.cliente}.")
        self.habitacion.liberar()


# Clase que representa al hotel y gestiona las habitaciones y reservas.
class Hotel:
    def __init__(self, nombre):
        """
        Inicializa el hotel con un nombre y una lista de habitaciones vacías.
        :param nombre: Nombre del hotel.
        """
        self.nombre = nombre
        self.habitaciones = []  # Lista de habitaciones disponibles en el hotel.
        self.reservas = []  # Lista de reservas activas.

    def agregar_habitacion(self, habitacion):
        """Método para agregar una habitación al hotel."""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        """Método para mostrar las habitaciones disponibles."""
        disponibles = [h for h in self.habitaciones if not h.ocupada]
        if disponibles:
            print("Habitaciones disponibles:")
            for habitacion in disponibles:
                print(habitacion)
        else:
            print("No hay habitaciones disponibles.")

    def hacer_reserva(self, cliente, numero_habitacion, noches):
        """
        Método para realizar una reserva para un cliente.
        Si la habitación está disponible, se realiza la reserva.
        :param cliente: Nombre del cliente.
        :param numero_habitacion: El número de la habitación a reservar.
        :param noches: Número de noches que el cliente desea reservar.
        """
        # Buscar la habitación por su número.
        habitacion = next((h for h in self.habitaciones if h.numero == numero_habitacion), None)

        if habitacion and not habitacion.ocupada:
            habitacion.ocupar()
            reserva = Reserva(cliente, habitacion, noches)
            self.reservas.append(reserva)
            print(f"Reserva realizada para {cliente} en la habitación {numero_habitacion}.")
            reserva.mostrar_reserva()
        else:
            print(f"La habitación {numero_habitacion} no está disponible o no existe.")

    def cancelar_reserva(self, cliente):
        """Método para cancelar la reserva de un cliente."""
        reserva = next((r for r in self.reservas if r.cliente == cliente), None)
        if reserva:
            reserva.cancelar_reserva()
            self.reservas.remove(reserva)
        else:
            print(f"No se encontró una reserva para el cliente {cliente}.")


# Función principal para interactuar con el usuario
def menu():
    # Crear el hotel
    hotel = Hotel("Hotel Delux")

    # Agregar algunas habitaciones al hotel
    hotel.agregar_habitacion(Habitacion(1, "simple", 20))
    hotel.agregar_habitacion(Habitacion(2, "doble", 50))
    hotel.agregar_habitacion(Habitacion(3, "suite", 150))

    while True:
        print("\nBienvenido al Hotel Delux")
        print("1. Ver habitaciones disponibles")
        print("2. Hacer una reserva")
        print("3. Cancelar una reserva")
        print("4. Ver reservas actuales")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            hotel.mostrar_habitaciones_disponibles()

        elif opcion == "2":
            nombre_cliente = input("Ingrese su nombre: ")
            hotel.mostrar_habitaciones_disponibles()
            numero_habitacion = int(input("Ingrese el número de la habitación que desea reservar: "))
            noches = int(input("¿Cuántas noches desea reservar? "))
            hotel.hacer_reserva(nombre_cliente, numero_habitacion, noches)

        elif opcion == "3":
            nombre_cliente = input("Ingrese su nombre para cancelar la reserva: ")
            hotel.cancelar_reserva(nombre_cliente)

        elif opcion == "4":
            print("\nReservas actuales:")
            for reserva in hotel.reservas:
                reserva.mostrar_reserva()

        elif opcion == "5":
            print("Gracias por visitar el Hotel Delux. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida, por favor ingrese una opción entre 1 y 5.")


# Llamamos a la función principal para iniciar el programa.
if __name__ == "__main__":
    menu()
