import React from 'react';
import './Contenido.css';
import ListadoResultados from './ListadoResultados';
import ItemResultados from './ItemResultado';
import BotonReservar from './BotonReservar';
import BotonDetalle from './BotonDetalle';


const Contenido = () => {
    return (
        <div classname="Contenido">
            <ListadoResultados />
        </div>
    )    
}


export default Contenido