import React from 'react';
import useAxios from 'axios-hooks';
import * as Constants from '../Constants';
import './ListadoSugerenciaBuscador.css';

const ListadoSugerenciaBuscador = (props) => {
    let classes = 'SugerenciaBuscador ';
    let listado_sugerencias = []
    let api_busqueda = "";
    if(props.tipo === "ciudad" ) {
        api_busqueda = Constants.URL_API_CIUDADES;
    } else if(props.tipo === "empresa") {
        api_busqueda = Constants.URL_API_EMPRESAS;
    }

    let url_definitiva = api_busqueda;
    const [{data, loading, error}] = useAxios(url_definitiva);

    if (loading) {
        return(<p>Estamos cargando broder</p>);
    }
    if (error) {
        return (<p>error broder</p>);
    }
    
    if (props.tipo === "ciudad") {
        for(var i = 0; i < data.length; i++) {
            console.log('Provincia ' + data[i].nombre + ', Ciudades: ' + data[i].ciudades.length);
            for(var j = 0; j < data[i].ciudades.length; j++) {
                if (data[i].ciudades[j] === undefined){
                    console.log('encontramos un thegame');
                } else {
                    let nombre_ciudad = data[i].ciudades[j].nombre;
                    if(nombre_ciudad.toLowerCase().startsWith(props.busqueda)) {
                        listado_sugerencias.push(nombre_ciudad + ', ' + data[i].nombre);
                    }
                }
            }
        }        
    } else if (props.tipo === "empresa") {
        for(var i = 0; i < data.length; i++) {
            console.log(data[i].nombre);
            if(data[i].nombre === undefined){
                console.log('encontramos un thegame')
            } else {
                let nombre_empresa = data[i].nombre;
                if(nombre_empresa.toLowerCase().startsWith(props.busqueda)){
                    listado_sugerencias.push(nombre_empresa);
                }
            }
        }
    }

    return (
        <div className={classes}>
            <ul>
                {listado_sugerencias.map(((item,indice) =>
                    <li key={indice}>{item}</li>
                ))}                
            </ul>
        </div>
    )
}

export default ListadoSugerenciaBuscador