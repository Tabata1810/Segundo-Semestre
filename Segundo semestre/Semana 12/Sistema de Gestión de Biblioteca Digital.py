# Clase Libro: Representa un libro con título, autor, categoría y ISBN
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"'{self.titulo}' de {self.autor} (ISBN: {self.isbn}, Categoría: {self.categoria})"


# Clase Usuario: Representa a un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"

    def añadir_libro_prestado(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        return [libro.titulo for libro in self.libros_prestados]


# Clase Biblioteca: Gestiona los libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario de libros por ISBN
        self.usuarios = {}  # Diccionario de usuarios por ID

    def añadir_libro(self, libro):
        """Añade un libro a la biblioteca"""
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        """Quita un libro de la biblioteca por su ISBN"""
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"Libro con ISBN {isbn} no encontrado.")

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario en la biblioteca"""
        if usuario.id_usuario in self.usuarios:
            print(f"Ya existe un usuario con el ID {usuario.id_usuario}.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado exitosamente.")

    def dar_baja_usuario(self, id_usuario):
        """Da de baja a un usuario de la biblioteca"""
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        """Presta un libro a un usuario si está disponible"""
        if id_usuario not in self.usuarios:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return
        if isbn not in self.libros:
            print(f"Libro con ISBN {isbn} no encontrado.")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        usuario.añadir_libro_prestado(libro)
        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        """Devuelve un libro prestado por un usuario"""
        if id_usuario not in self.usuarios:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return
        if isbn not in self.libros:
            print(f"Libro con ISBN {isbn} no encontrado.")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        usuario.devolver_libro(libro)
        print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")

    def buscar_libro(self, criterio, valor):
        """Busca libros por título, autor o categoría"""
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self):
        """Muestra todos los libros prestados"""
        libros_prestados = []
        for usuario in self.usuarios.values():
            libros_prestados.extend(usuario.listar_libros_prestados())
        return libros_prestados


# Funciones auxiliares para la interacción con el usuario
def validar_isbn(isbn):
    """Valida si el ISBN tiene el formato correcto (10 o 13 caracteres numéricos)"""
    return isbn.isdigit() and (len(isbn) == 10 or len(isbn) == 13)


def validar_id_usuario(id_usuario, biblioteca):
    """Verifica que el ID del usuario no esté registrado"""
    if id_usuario in biblioteca.usuarios:
        return False
    return True


# Función para interactuar con el usuario y realizar acciones en la biblioteca
def interfaz_usuario():
    biblioteca = Biblioteca()

    while True:
        print("\n===== Bienvenido al sistema de gestión de la biblioteca digital =====")
        print("1. Registrar usuario")
        print("2. Añadir libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar libro")
        print("6. Listar libros prestados")
        print("7. Dar de baja usuario")
        print("8. Eliminar libro")
        print("9. Salir")

        opcion = input("Seleccione una opción (1-9): ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del usuario: ")
            id_usuario = input("Ingrese el ID del usuario: ")

            if not validar_id_usuario(id_usuario, biblioteca):
                print(f"El ID {id_usuario} ya está registrado.")
                continue

            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == '2':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")

            if not validar_isbn(isbn):
                print("El ISBN no es válido. Debe tener 10 o 13 caracteres numéricos.")
                continue

            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)

        elif opcion == '3':
            id_usuario = input("Ingrese el ID del usuario que desea tomar el libro: ")
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == '4':
            id_usuario = input("Ingrese el ID del usuario que desea devolver el libro: ")
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == '5':
            criterio = input("Buscar por (titulo/autor/categoria): ").lower()
            if criterio not in ['titulo', 'autor', 'categoria']:
                print("Criterio de búsqueda no válido.")
                continue
            valor = input(f"Ingrese el {criterio} a buscar: ")
            resultados = biblioteca.buscar_libro(criterio, valor)
            if resultados:
                print("\nLibros encontrados:")
                for libro in resultados:
                    print(libro)
            else:
                print(f"No se encontraron libros con {criterio} '{valor}'.")

        elif opcion == '6':
            libros_prestados = biblioteca.listar_libros_prestados()
            if libros_prestados:
                print("\nLibros prestados:")
                for libro in libros_prestados:
                    print(libro)
            else:
                print("No hay libros prestados actualmente.")

        elif opcion == '7':
            id_usuario = input("Ingrese el ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == '8':
            isbn = input("Ingrese el ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == '9':
            print("¡Gracias por usar el sistema de gestión de la biblioteca!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


# Iniciar la interfaz de usuario
if __name__ == "__main__":
    interfaz_usuario()

