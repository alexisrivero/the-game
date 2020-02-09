class Embutido{
    nombre;
    constructor(nombre){
        if (nombre){
            this.nombre = nombre;
        }
    }
    descripcion (){
        console.log ("este embutido se llama: " + this.nombre);
    }
}
class Chorizo extends Embutido{
    color;
    peso;
    procedencia = "pindonga"
    constructor (peso, color, procedencia){
        super ("chorizo ");
        this.peso = peso;
        this.color = color;
        if (procedencia){
            this.procedencia = procedencia;
        }
    }
    descripcion(){
        console.log ("esto se llama: " + this.nombre);
        console.log("peso: " + this.peso);
        console.log ("color: " + this.color);
        console.log ("procedencia " + this.procedencia);
    }
}



let ch1 = new Chorizo (2, "azul", "the game");
ch1.descripcion();

