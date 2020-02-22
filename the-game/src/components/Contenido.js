import React from 'react';
import './Contenido.css';
import ListadoResultados from './ListadoResultados';
import BotonReservar from './BotonReservar';
import BotonDetalle from './BotonDetalle';
import DatosEmpresa from './DatosEmpresa';

const Contenido = () => {
    return (
        <div className="Contenido">
            <ListadoResultados />
            <BotonReservar />
            <BotonDetalle />
            <DatosEmpresa />
        </div>
    )    
}


export default Contenido