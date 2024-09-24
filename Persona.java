class Persona {
    private string nombre = "";
    private string apellido = ""

    public Persona(string nombre, string apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }

    public void setNombre(string nombre){
        this.nombre = nombre;
    }

    public string getNombre(){
        return this.nombre;
    }
}

class Estudiante extends Persona {
    
}