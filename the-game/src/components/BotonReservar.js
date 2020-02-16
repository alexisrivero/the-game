import React, {useState, useEffect} from 'react';

const BotonReservar = (props) => {
    const [numeroClicks, setNumeroClicks] = useState(0);
    const [nombre, setNombre] = useState('diego');

    var handleClick = () => {
        setNumeroClicks(numeroClicks + 1);
    }

    var handleEffect = () => {
        if( numeroClicks % 2 == 0) {
            document.title = "cliqueaste " + numeroClicks + " veces";
        } else {
            document.title = 'Impar';
        }
    }

    useEffect(handleEffect);

    return (
        <li className="HeaderMenuItem">
            <button onClick={handleClick}>{props.texto}</button>
        </li>
    )
}

export default BotonReservar