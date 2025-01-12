class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(f"{self.nombre}:")
        print(f"· Fuerza: {self.fuerza}")
        print(f"· Inteligencia: {self.inteligencia}")
        print(f"· Defensa: {self.defensa}")
        print(f"· Vida: {self.vida}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto.")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        daño = max(daño, 0)
        enemigo.vida -= daño
        print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}.")
        if enemigo.esta_vivo():
            print(f"Vida de {enemigo.nombre}: {enemigo.vida}")
        else:
            enemigo.morir()


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Espada de Hierro, daño 6. (2) Espada de Fuego, daño 9: "))
        if opcion == 1:
            self.espada = 6
        elif opcion == 2:
            self.espada = 9
        else:
            print("Número de arma incorrecto.")

    def atributos(self):
        super().atributos()
        print(f"· Espada: {self.espada}")

    def daño(self, enemigo):
        return (self.fuerza + self.espada) - enemigo.defensa


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print(f"· Libro Mágico: {self.libro}")

    def daño(self, enemigo):
        return (self.inteligencia * self.libro) - enemigo.defensa


class Arquero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, flechas):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.flechas = flechas  # Bonus de ataque

    def atributos(self):
        super().atributos()
        print(f"· Carcaj de Flechas: {self.flechas}")

    def daño(self, enemigo):
        return (self.fuerza * 1.5 + self.flechas) - enemigo.defensa


# Función principal para el combate
def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\nTurno {turno}")
        print(f">>> Acción de {jugador_1.nombre}:")
        jugador_1.atacar(jugador_2)
        if not jugador_2.esta_vivo():
            break
        print(f">>> Acción de {jugador_2.nombre}:")
        jugador_2.atacar(jugador_1)
        turno += 1

    if jugador_1.esta_vivo():
        print(f"\nHa ganado {jugador_1.nombre}")
    elif jugador_2.esta_vivo():
        print(f"\nHa ganado {jugador_2.nombre}")
    else:
        print("\nEmpate")


# Creación de nuevos personajes con diferentes valores
personaje_1 = Guerrero("Aragorn", 18, 8, 6, 120, 7)
personaje_2 = Mago("Gandalf", 6, 20, 5, 100, 3)
personaje_3 = Arquero("Legolas", 14, 10, 4, 110, 5)

# Mostrar atributos
personaje_1.atributos()
personaje_2.atributos()

# Realizar combate entre Guerrero y Mago
combate(personaje_1, personaje_2)

# Nuevo combate con el Arquero
print("\n- Nuevo combate entre Arquero y Guerrero -")
personaje_3.atributos()
combate(personaje_3, personaje_1)
