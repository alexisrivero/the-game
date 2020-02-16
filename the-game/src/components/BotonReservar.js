import React, { useState, useEffect} from 'react';
import './BotonReservar.css';

const BotonReservar = () => {
    alert("Confirmar Reserva")
    return (
        <p className="BotonReservar">
            <button onClick={BotonReservar}>Reservar</button>
        </p>
    )
}
export default BotonReservar