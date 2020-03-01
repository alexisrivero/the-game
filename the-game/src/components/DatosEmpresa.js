import React from 'react';
import './DatosEmpresa.css';
import LogoEmpresa from './LogoEmpresa';
import NombreEmpresa from './NombreEmpresa';
import DireccionEmpresa from './DireccionEmpresa';
import DescripcionEmpresa from './DescripcionEmpresa';
import PreviewDisponibilidadEmpresa from './PreviewDisponibilidadEmpresa';
import RatingEmpresa from './RatingEmpresa';
import BotonReservar from './BotonReservar';

const DatosEmpresa = (props) => {
    return (
        <div className="DatosEmpresa">
            <LogoEmpresa empresa={props.empresa} />
            <div className="wrapper-datos">
                <NombreEmpresa empresa={props.empresa} />
                <RatingEmpresa empresa={props.empresa} />
                <PreviewDisponibilidadEmpresa empresa={props.empresa}  />                
               <div className="la-cueca">
                    <BotonReservar />
                    <DescripcionEmpresa empresa={props.empresa} />
                    <DireccionEmpresa empresa={props.empresa} />
                </div>
            </div>
        </div>
    )
}

export default DatosEmpresa