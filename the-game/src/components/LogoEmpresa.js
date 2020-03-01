import React from 'react';
import './LogoEmpresa.css';

const LogoEmpresa = (props) => {
    return(
        <div className="LogoEmpresa">
            <img src={props.empresa.logo_url} />
        </div>
    )
}

export default LogoEmpresa