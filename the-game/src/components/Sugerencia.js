import React from 'react';
import './Sugerencia.css';

const Sugerencia = (props) => {
    

    let thegame_1 = props.nombre.toLowerCase().replace(props.busqueda, props.busqueda);
    let thegame_3 = props.nombre.slice(props.busqueda.length);
    let thegame_4 = props.nombre.toLowerCase().split(props.busqueda)[1];
    let thegame_6 = props.nombre.substring(props.busqueda.length);

    let busqueda_display = props.busqueda.charAt(0).toUpperCase() + props.busqueda.slice(1);

    let elotro_game = props.nombre.toLowerCase().includes(props.busqueda)
    console.log(elotro_game)

    let pre_thegame = "";
    let post_thegame = thegame_1;

    console.log(post_thegame)

    return (<div className="Sugerencia">{pre_thegame}<span></span>{post_thegame}</div>)
}


export default Sugerencia