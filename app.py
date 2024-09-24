from biblioteca import Biblioteca
from libro import Libro


libro1 = Libro("Cuando quiero llorar no lloro", "Gabriel Garcia Marquez")
libro2 = Libro("El Gran Gatsby", "Scott Fizgerald")
libro3 = Libro("100 Años de Soledad", "Gabriel Garcia Marquez")

biblioteca = Biblioteca("Antartica")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.mostrar_inventario()

biblioteca.agregar_libro(libro3)

biblioteca.mostrar_inventario()