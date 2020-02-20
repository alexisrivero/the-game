import React from 'react';
import './Header.css';
import * as Constants from "../Constants";
import HeaderMenu from './HeaderMenu';
import HeaderLogo from './HeaderLogo';

const Header = () => {
    return (
        <div className="Header">
           <HeaderMenu alineacion="derecha" />
           <HeaderLogo />
        </div>
    )
}

export default Header