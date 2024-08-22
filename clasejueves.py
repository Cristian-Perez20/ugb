# Define la clase Libro para representar los libros con título y autor.
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# Define la clase Seccion para manejar las secciones de la biblioteca, que contienen libros.
class Seccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # Inicializa una lista vacía de libros.

    def agregar_libro(self, libro):
        self.libros.append(libro)  # Agrega un libro a la lista de libros.

# Define la clase Biblioteca para gestionar secciones y listas de lectura.
class Biblioteca:
    def __init__(self):
        self.secciones = {}  # Inicializa un diccionario vacío para las secciones.
        self.lista_lectura = []  # Inicializa una lista vacía para la lista de lectura.

    def agregar_seccion(self, seccion):
        self.secciones[seccion.nombre] = seccion  # Agrega una sección al diccionario.

    def agregar_libro_a_seccion(self, nombre_seccion, libro):
        # Añade un libro a una sección específica.
        if nombre_seccion in self.secciones:
            self.secciones[nombre_seccion].agregar_libro(libro)
        else:
            print(f"Sección '{nombre_seccion}' no encontrada.")  # Mensaje de error si la sección no existe.

    def mostrar_secciones(self):
        # Muestra todas las secciones disponibles.
        for i, seccion in enumerate(self.secciones.values()):
            print(f"{i + 1}. {seccion.nombre}")

    def mostrar_libros(self, nombre_seccion):
        # Muestra todos los libros de una sección específica.
        seccion = self.secciones.get(nombre_seccion)
        if seccion:
            for i, libro in enumerate(seccion.libros):
                print(f"{i + 1}. '{libro.titulo}' por {libro.autor}")
        else:
            print(f"Sección '{nombre_seccion}' no encontrada.")  # Mensaje de error si la sección no existe.

    def agregar_libro_a_lista_lectura(self, libro):
        self.lista_lectura.append(libro)  # Añade un libro a la lista de lectura.

    def mostrar_lista_lectura(self):
        # Muestra todos los libros en la lista de lectura.
        if not self.lista_lectura:
            print("No hay libros en la lista de lectura.")
        else:
            for libro in self.lista_lectura:
                print(f"'{libro.titulo}' por {libro.autor}")

# Función principal que maneja la lógica del programa.
def main():
    biblioteca = Biblioteca()

    # Define las secciones de la biblioteca.
    secciones = ["Ficción", "No Ficción", "Ciencia", "Historia", "Biografía"]
    for nombre_seccion in secciones:
        biblioteca.agregar_seccion(Seccion(nombre_seccion))

    # Define los libros disponibles.
    libros = [
        Libro("Cien años de soledad", "Gabriel García Márquez"),
        Libro("Sapiens", "Yuval Noah Harari"),
        Libro("Breve historia del tiempo", "Stephen Hawking"),
        Libro("El origen de las especies", "Charles Darwin"),
        Libro("El diario de Ana Frank", "Ana Frank")
    ]

    # Asocia libros con sus respectivas secciones.
    libros_por_seccion = {
        "Ficción": ["Cien años de soledad"],
        "No Ficción": ["Sapiens", "Breve historia del tiempo", "El origen de las especies"],
        "Historia": ["El diario de Ana Frank"],
        "Ciencia": ["Breve historia del tiempo", "El origen de las especies"],
        "Biografía": ["El diario de Ana Frank"]
    }

    # Añade los libros a las secciones correspondientes.
    for libro in libros:
        for nombre_seccion, titulos_libros in libros_por_seccion.items():
            if libro.titulo in titulos_libros:
                biblioteca.agregar_libro_a_seccion(nombre_seccion, libro)

    # Menú interactivo para el usuario.
    while True:
        print("\n1. Agregar libro a la lista de lectura")
        print("2. Ver lista de lectura")
        print("3. Salir")
        print("-------------------------------------------------")
        opcion = input("Selecciona una opción: ")
        print("-------------------------------------------------")
        if opcion == '1':
            print("Secciones disponibles:")
            biblioteca.mostrar_secciones()
            indice_seccion = int(input("Ingrese el número de la sección: ")) - 1
            nombre_seccion = secciones[indice_seccion]
            print(f"Libros disponibles en la sección {nombre_seccion}:")
            biblioteca.mostrar_libros(nombre_seccion)
            indice_libro = int(input("Ingrese el número del libro: ")) - 1
            libro = biblioteca.secciones[nombre_seccion].libros[indice_libro]
            biblioteca.agregar_libro_a_lista_lectura(libro)
            print(f"Libro '{libro.titulo}' agregado a la lista de lectura.")

        elif opcion == '2':
            biblioteca.mostrar_lista_lectura()

        elif opcion == '3':
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")  # Mensaje para opciones no válidas.

# Ejecuta la función principal si el script es ejecutado directamente.
if __name__ == "__main__":
    main()