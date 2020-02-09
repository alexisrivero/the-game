var Chorizo = (lote, kilo, color) =>{
    this.lote = lote;
    this.kilo = kilo * 2;
    this.color = color;

    this.descripcion = var descripcion = () =>{
        return "este chorizo es del lote " + this.lote + ", pesa: " + this.kilo + ",de color: " + this.color;
    }
}
let ch1 = new Chorizo(1234, 5, "azul");
let ch2 = new Chorizo(89832, 1, "rojo");

console.log(ch1.descripcion());
console.log(ch2.descripcion());
