import React from 'react';
import './HeaderLogo.css';
import * as Constants from "../Constants";

const HeaderLogo = () => {
    return (
        <div className="HeaderLogo">
            <a href="/">
                <img src={Constants.LOGO_CIA} alt="LOGO DE LA CIA"/>
            </a>
        </div>
    )
}

export default HeaderLogo