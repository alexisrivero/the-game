import React from 'react';
import Buscador from './Buscador';
import './BuscadorHeader.css';

const BuscadorHeader = () => {
    let handleSubmit = (event) => {
        event.preventDefault();
        console.log(event);
    }
    return (
        <div className="BuscadorHeader">
            <form onSubmit={handleSubmit}>
                <Buscador nombre="empresa" tipo="empresa" />
                <Buscador nombre="ciudad" tipo="ciudad" />
            </form>
        </div>
    )
}

export default BuscadorHeader