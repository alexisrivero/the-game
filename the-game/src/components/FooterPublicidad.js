import React from 'react';
import useAxios from 'axios-hooks';
import './FooterPublicidad.css';
import * as Constants from "../Constants";

const FooterPublicidad = (props) => {
    var url_definitiva = "";
    if (props.API_Url) {
        url_definitiva = props.API_Url;
    } else {
        url_definitiva = Constants.URL_API_PUBLICIDAD;
    }

    const [{data, loading, error}, refetch] = useAxios(url_definitiva);

    if(loading) {
        return(<p>Estamos cargando la publicidad...</p>)
    }

    if (error) {
        return(<p role='error-message'>Error: no se pudo contactar la API de publicidad</p>)
    }

    return(
        <div className="FooterPublicidad" role='publicidad'>
            <a href={data.publicidad.url}>
                <img src={data.publicidad.img_url} />
            </a>
        </div>
    )
};

export default FooterPublicidad