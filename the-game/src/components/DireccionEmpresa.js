import React from 'react';
import './DireccionEmpresa.css'

const DireccionEmpresa = (props) => {
    return (
        <div className="DireccionEmpresa">{props.empresa.direccion}</div>
    )
}



export default DireccionEmpresa