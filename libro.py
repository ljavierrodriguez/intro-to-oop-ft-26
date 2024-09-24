class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_informacion(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}"
    

#libro = Libro("Cuando quiero llorar no lloro", "Gabriel Garcia Marquez")
#print(libro.mostrar_informacion())