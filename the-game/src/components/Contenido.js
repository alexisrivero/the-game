import React from 'react';
import './Contenido.css';
import ListadoResultados from './ListadoResultados';
import BotonReservar from './BotonReservar';
import BotonDetalle from './BotonDetalle';

const Contenido = () => {
    return (
        <div className="Contenido">
            <ListadoResultados />
            <BotonDetalle />
        </div>
    )    
}


export default Contenido