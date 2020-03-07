import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faStar, faStarHalfAlt ,faStarAndCrescent} from '@fortawesome/free-solid-svg-icons'
import { faStar as faStarEmpty } from '@fortawesome/free-regular-svg-icons'
import './RatingEmpresa.css';


//cuando hay un thegame, preguntarme siempre que carajo estoy haciendo
// qué es rating empresa?
// es un componente que muestra la puntuacion que los usuarios le asignan a una empres determinada

const RatingEmpresa = (props) => {

    //calculo las estrellas enteras
    let estrellas = [];
    let numero_estrellas = Math.floor(props.empresa.rating);
    for(var i = 0; i < numero_estrellas; i++) {
        estrellas.push(false);
    }

    // calculo si hay media estrella
    let media_estrella = false;
    if(!Number.isInteger(props.empresa.rating)) {
        media_estrella = true;
    }

    //calculo las estrellas enteras vacías
    let estrellas_vacias = [];
    let numero_estrellas_vacias = 5 - Math.round(props.empresa.rating);
    for (var i = 0; i < numero_estrellas_vacias; i++) {
        estrellas_vacias.push(false)
    }

    return (
        <div className="RatingEmpresa">
            {/* loopeo las estrellas e imprimo un ícono de fontawesome por cada una */}
            {estrellas.map(((item, indice) =>
                <FontAwesomeIcon icon={faStar} key={indice} />
            ))}

            {/* chequeo si hay media estrella y si es verdadero la imprimo */}
            {media_estrella && <FontAwesomeIcon icon={faStarHalfAlt} /> }

            {/*loopeo las estrellas vacias e imprimo un ícono de fontawesome por cada una */}
            {estrellas_vacias.map(((item, indice) =>
                <FontAwesomeIcon icon={faStarEmpty} key={indice} />
            ))}

        </div>
    );
};

export default RatingEmpresa