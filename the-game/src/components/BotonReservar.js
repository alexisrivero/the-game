import React, { useState, useEffect} from 'react';
import './BotonReservar.css';

const BotonReservar = () => {
    var handleClick = () => {
        window.alert("Confirmar Reserva");
    }
    return (
        <p className="BotonReservar">
            <button onClick={handleClick}>Reservar</button>
        </p>
    )
}
export default BotonReservar