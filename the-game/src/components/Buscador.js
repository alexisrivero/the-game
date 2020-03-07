import React, { useState } from 'react';
import './Buscador.css';
import ListadoSugerenciaBuscador from './ListadoSugerenciaBuscador';

const Buscador = (props) => {
    const [mostrarSugerencia, setMostrarSugerencia] = useState(false);
    const [busqueda, setBusqueda] = useState("");
    let input_id = "buscador_" + props.nombre;

    let handleFocus = (event) => {
        if (event.target.value.trim().length > 1){
            setMostrarSugerencia(true);
        }
    }
    let handleBlur = (event) => {
        //setMostrarSugerencia(false);
    }
    let handleChange = (event) => {
        setBusqueda(event.target.value.trim().toLowerCase());
        if(event.target.value.trim().length > 1){
            setMostrarSugerencia(true);
        } else{
            setMostrarSugerencia(false);
        }
    }
    
    return (
        <div className="Buscador">
            <input id={input_id} name={input_id} onFocus={handleFocus} onBlur={handleBlur} onChange={handleChange} />
            {mostrarSugerencia && <ListadoSugerenciaBuscador busqueda={busqueda} tipo={props.tipo}  />}
        </div>
    )
}

export default Buscador