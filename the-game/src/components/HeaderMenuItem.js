import React, { useState, useEffect } from 'react';
import './HeaderMenuItem.css';

const HeaderMenuItem = (props) => {
    const [numeroClicks, setNumeroClicks] = useState(0);

    var handleClick = () => {
        setNumeroClicks(numeroClicks + 1);
    }

    var handleEffect = () => {
        if( numeroClicks % 2 == 0) {
            document.title = "cliqueaste " + (numeroClicks * 2) + " veces";
        } else {
            document.title = 'Impar';
        }
    }

    useEffect(handleEffect);

    let json_color = props.color;
    
    let color_class = "c-" + props.texto.toLowerCase();

    return (
        <li className="HeaderMenuItem">
            <button onClick={handleClick} className={color_class}>{props.texto}</button>
        </li>
    )
}

export default HeaderMenuItem
//agregar posibilidad de pasarle el color de fondo como atributo al boton la otra posibilidad puede ser quizas estableciendo clase en css