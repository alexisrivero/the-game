import React from 'react';
import useAxios from 'axios-hooks';
import * as Constants from '../Constants';
import './ListadoResultados.css';
import Empresa from './Empresa';
import DatosEmpresa from './DatosEmpresa';


const ListadoResultados = (props) => {

    let url_definitiva = ''

    if(props.url_api) {
        url_definitiva = props.url_api
    } else {
        url_definitiva = Constants.URL_API_EMPRESAS;
    }

    const [{data, loading, error}, refetch] = useAxios(url_definitiva);

    if (loading) {
        return(<p>Estamos cargando broder</p>);
    }
    if (error) {
        return (<p>error broder</p>);
    }

    return(
        <div className="ListadoResultados">
            <h1>Listado de resultados</h1>
            <ul>
                {data.map(((item,indice) =>
                    <DatosEmpresa empresa={item} key={indice} />
                ))}
            </ul>
        </div>
    )
}

export default ListadoResultados