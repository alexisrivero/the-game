import React from 'react';
import './Empresa.css';
import DatosEmpresa from './DatosEmpresa';



const Empresa = (props) => {

    return (
        <li className="Empresa">
            <DatosEmpresa empresa={props.empresa} />
        </li>
    )    
}

export default Empresa