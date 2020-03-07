import React from 'react';
import './Header.css';
import HeaderMenu from './HeaderMenu';
import BuscadorHeader from './BuscadorHeader';
import HeaderLogo from './HeaderLogo';

const Header = () => {
    return (
        <div className="Header">
            <HeaderLogo />
            <BuscadorHeader />
            <HeaderMenu alineacion="derecha" />
        </div>
    )
}

export default Header