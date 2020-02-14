import React from 'react';
import './HeaderLogo.css';
import CIALOGO from './images/logo.jpg';

const HeaderLogo = () => {
    return (
        <div className="HeaderLogo">
            <a href="/">
                <img src={CIALOGO} alt="LOGO DE LA CIA"/>
            </a>
        </div>
    )
}

export default HeaderLogo