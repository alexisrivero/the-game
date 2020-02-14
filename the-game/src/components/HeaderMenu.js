import React from 'react';
import './HeaderMenu.css';
import HeaderMenuItem from './HeaderMenuItem';

const HeaderMenu = (props) => {

    var traerMenu = () => {

    }
    
    let clases = 'HeaderMenu alineacion-' + props.alineacion;

    return (
        <ul className={clases}>
            <HeaderMenuItem link="https://cia.net.ar" texto="LA CIA" />
            <HeaderMenuItem link="https://diego.com.ar" texto="diego" />
            <HeaderMenuItem link="https://trevisan.net" texto="trevisan" />
        </ul>
    )
}

export default HeaderMenu