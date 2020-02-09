let funcionConParametros = (naranja, marca) => {
    console.log("hay tantas naranjas " + naranja);
    console.log("hay tantas marcas " + marca);
}
funcionConParametros (3, "marca yea");
funcionConParametros(15, "marca game"); 

let chorizator = (kilo, color = "tuvieja", procedencia = "pinamar") => {
    console.log ("este chorizo pesa: " + kilo );
    console.log ("este chorizo es de color gamer" + color);
    console.log ("este chorizo viene de: " + procedencia);
}
chorizator (2, "azul");
chorizator (2);
chorizator (5, "la pampa");