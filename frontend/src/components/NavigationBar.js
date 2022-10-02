import React from 'react';
import { Link } from "react-router-dom";
import { FaHome } from "react-icons/fa";
import '../styles/components/NavigationBarStyle.css'

function NavigationBar({userType}){

    const User = () => {
        if (userType === 'user'){
            return(
                <div className="user-account">
                    <Link to="/account">
                    My Account
                    </Link>
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
            
            <Link to="/" className="icon-link">
                <FaHome className="icon"/>
            </Link>
            
            <User/>
        </div>
    );
}

export default NavigationBar;