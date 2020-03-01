import React from 'react';
import './NombreEmpresa.css';

const NombreEmpresa = (props) => {
    return(
        <div className="NombreEmpresa">{props.empresa.nombre}</div>
    )
}

export default NombreEmpresa