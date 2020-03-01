import React from 'react';
import useAxios from 'axios-hooks';
import './HeaderMenu.css';
import HeaderMenuItem from './HeaderMenuItem';
import * as Constants from '../Constants';

const HeaderMenu = (props) => {

    let url_definitiva = ''

    if(props.url_api) {
        url_definitiva = props.url_api
    } else {
        url_definitiva = Constants.URL_API_COLORES;
    }    
    
    const [{data, loading, error}, refetch] = useAxios(url_definitiva);
    if (loading) {
        return(<p>Estamos cargando broder</p>);
    }
    if (error) {
        return (<p role='error-message'>error broder</p>);
    }

    let clases = 'HeaderMenu alineacion-' + props.alineacion;

    return (
        <div className={clases}>
            <ul role='menu'>
                {data.map(((item,indice) =>
                    <HeaderMenuItem link={indice} texto={item.name} key={indice} color={item.hexString} />
                ))}
            </ul>
        </div>
    )
}

export default HeaderMenu