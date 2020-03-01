import React from 'react';
import useAxios from 'axios-hooks';
import './PreviewDisponibilidadEmpresa.css';
import DisponibilidadDia from './DisponibilidadDia';
import * as Constants from '../Constants';

const PreviewDisponibilidadEmpresa = (props) => {
    return (
        <div className="PreviewDisponibilidadEmpresa">
            <ul>
                {props.empresa.disponibilidad.map(((item,indice) =>
                    <DisponibilidadDia disponibilidad={item} key={indice} />
                ))}
            </ul>
        </div>
    )
}

export default PreviewDisponibilidadEmpresa