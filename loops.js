var matriz = [72, "tuvieja", 49, "chorizo"];
for (var elemento in matriz){
    console.log(elemento);
    console.log(matriz[elemento]);
}
console.log("este es el for in: ");
for (var elemento of matriz){
    console.log(elemento);
}
console.log ("este es el for of: ");
