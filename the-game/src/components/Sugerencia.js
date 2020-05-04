import React from 'react';
import './Sugerencia.css';

const Sugerencia = (props) => {
    

    let thegame_1 = props.nombre.toLowerCase().replace(props.busqueda, props.busqueda);
    //if(props.nombre.toLowerCase().indexOf(props.busqueda) != -1){
        // la re concha de tu hermana
    //}

    let thegame_3 = props.nombre.slice(props.busqueda.length);
    let thegame_4 = props.nombre.toLowerCase().split(props.busqueda)[1];
    let thegame_6 = props.nombre.substring(props.busqueda.length);


    let busqueda_display = props.busqueda.charAt(0).toUpperCase() + props.busqueda.slice(1);

    let elotro_game = props.nombre.toLowerCase().includes(props.busqueda)
    console.log(elotro_game)

    let final_thegame = props.nombre.toLowerCase().split(props.busqueda);
    let pre_thegame = final_thegame[0];
    let post_thegame = thegame_4;


    console.log(post_thegame)

    return (<div className="Sugerencia">{pre_thegame}<span>{props.busqueda}</span>{post_thegame}</div>)
}


export default Sugerencia