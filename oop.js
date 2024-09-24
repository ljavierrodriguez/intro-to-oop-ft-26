class Persona {
    constructor(nombre = "", apellido = ""){
        //console.log("Instanciando la clase Persona")
        this._nombre = nombre;
        this._apellido = apellido
    }

    quienSoy(){
        return `${this._nombre} ${this._apellido}`
    }
}

let persona = new Persona() 
console.log(persona.quienSoy())

let persona2 = new Persona("John", "Doe") 
console.log(persona2.quienSoy())


class Estudiante extends Persona {
    constructor(nombre, apellido, facultad){
        super(nombre, apellido)
        this._facultad = facultad
        //console.log("Instanciando la clase Estudiante")
    }

    quienSoy(){
        return `Soy ${this._nombre} ${this._apellido} de la facultad de: ${this._facultad}`
    }
}

let estudiante = new Estudiante("Jane", "Doe", "Medicina")
console.log(estudiante.quienSoy())