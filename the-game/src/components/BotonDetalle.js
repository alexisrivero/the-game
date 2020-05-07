import React from 'react';
import './BotonDetalle.css';

//acordarse de bindear la funcion al evento dentro del return, onEvento={funcionEvento}
const BotonDetalle = () => {
    let color = 'black';
    var handleClick = () => {
        window.alert("Detalles");
    }
    return (
        <p className="BotonDetalle">
            <button onClick={handleClick}>Detalles</button>
        </p>
    )
}
export default BotonDetalle