import React from 'react';
import './Contenido.css';
import ListadoResultados from './ListadoResultados';
import ItemResultados from './ItemResultado';
import BotonReservar from './BotonReservar';
import BotonDetalle from './BotonDetalle';

const Contenido = () => {
    return (
        <div className="Contenido">
            <ListadoResultados />
            <BotonReservar />
            <BotonDetalle />
        </div>
    )    
}


export default Contenido