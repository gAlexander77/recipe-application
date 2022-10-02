import React, { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';

function Account() {

    let navigate = useRef(useNavigate());
    let userType = useRef(localStorage.getItem('userType'));

    useEffect(()=>{ 
        userType.current = localStorage.getItem('userType')
        if (userType ===null || 'guest'){
            navigate.current('/login');
        }
    },[])

    return(
        <div className="Account">
            <h1>Header</h1>
            <h1>Account Info</h1>
            <h1>My Recipes</h1>
            <h1>Saved Recipes</h1>
        </div>
    );
}

export default Account;