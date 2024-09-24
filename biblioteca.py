class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_inventario(self):
        print(f"Mostrando catalogo de libros de la biblioteca {self.nombre}:")
        print("-------------------------------------------------------------")
        if len(self.libros) > 0:
            for libro in self.libros:
                print(libro.mostrar_informacion())
                print("-------------------------------------------------------------")
        else:
            print("Catalogo de libros vacios")


#biblioteca = Biblioteca("Antartica")
#biblioteca.mostrar_inventario()