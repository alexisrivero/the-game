import React from 'react';
import useAxios from 'axios-hooks';
import './HeaderMenu.css';
import HeaderMenuItem from './HeaderMenuItem';

const HeaderMenu = (props) => {
    const [{data, loading, error}, refetch] = useAxios("https://jonasjacek.github.io/colors/data.json");
    if (loading) {
        return(<p>Estamos cargando broder</p>);
    }
    if (error) {
        return (<p>error broder</p>);
    }

    let clases = 'HeaderMenu alineacion-' + props.alineacion;

    return (
        <div className={clases}>
            <ul>
                {data.map(((item,indice) =>
                    <HeaderMenuItem link={indice} texto={item.name} key={indice} color={item.hexString} />
                ))}
            </ul>
        </div>
    )
}

export default HeaderMenu