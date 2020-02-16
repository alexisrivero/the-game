import React, { useState, useEffect} from 'react';
import './BotonDetalle.css';

const BotonDetalle = () => {
    alert("Detalles")
//    var handleClick = () => {
//        setClick (onClick);
//    }


    return (
        <p className="BotonDetalle">
            <button onClick={BotonDetalle}>Detalles</button>
        </p>
    )
}
export default BotonDetalle