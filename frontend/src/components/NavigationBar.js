import React from 'react';
import {Link } from "react-router-dom";
import '../styles/components/NavigationBarStyle.css'

function NavigationBar({userType}){

    const User = () => {
        if (userType === 'user'){
            return(
                <div className="user-account">
                    <h1>My Account</h1>
                </div>
            );
        }
        else{
            return(
                <div className="user-account">
                    <Link to="/login">
                    Create Account
                    </Link>
                </div>    
            );
        }
    
    }

    return (
        <div className="NavigationBar">
            <User/>
        </div>
    );
}

export default NavigationBar;