import React from 'react';
import './DatosEmpresa.css';
import LogoEmpresa from './LogoEmpresa';
import NombreEmpresa from './NombreEmpresa';
import DireccionEmpresa from './DireccionEmpresa';

const DatosEmpresa = () => {
    return (
        <div className="DatosEmpresa">
            <LogoEmpresa />
            <NombreEmpresa />
            <DireccionEmpresa />
            <ul> Somos una empresa boliviana destacada en hacer the games</ul>
        </div>
    )
}

export default DatosEmpresa