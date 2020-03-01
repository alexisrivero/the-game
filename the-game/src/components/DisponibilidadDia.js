import React from 'react';
import './DisponibilidadDia.css';
import * as Constants from '../Constants';


const DisponibilidadDia = (props) => {
    let dia = Object.getOwnPropertyNames(props.disponibilidad)[0];
    let clase = 'DisponibilidadDia disponibilidad_'  + props.disponibilidad[dia];
    return(
        <li className={clase}>{dia}</li>
    )
}

export default DisponibilidadDia