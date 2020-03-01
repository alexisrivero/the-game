import React from 'react';
import './DescripcionEmpresa.css';

const DescripcionEmpresa = (props) => {
    return(
        <div className="DescripcionEmpresa">{props.empresa.descripcion}</div>
    )
}

export default DescripcionEmpresa