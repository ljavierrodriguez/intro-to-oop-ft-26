class Persona:
    def __init__(self, nombre = "", apellido = ""):
        print("Instanciando la clase Persona")
        self.nombre = nombre
        self.apellido = apellido

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def quien_soy(self):
        return f"{self.nombre} {self.apellido}"


persona = Persona()
print(persona.quien_soy())

persona2 = Persona("John", "Doe")
print(persona2.quien_soy())

class Estudiante(Persona):
    def __init__(self, nombre, apellido, facultad):
        super().__init__(nombre, apellido)
        self.__facultad = facultad

    def quien_soy(self):
        return f"Soy {self.nombre} {self.apellido} de la facultad de: {self.__facultad}"


estudiante = Estudiante("Jane", "Doe", "Medicina")
print(estudiante.quien_soy())