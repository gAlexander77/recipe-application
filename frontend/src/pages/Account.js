import React, { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBar from '../components/NavigationBar';

function Account() {

    let navigate = useRef(useNavigate());
    const [userType, setUserType] = useState(localStorage.getItem('userType'));

    useEffect(()=>{ 
        setUserType(localStorage.getItem('userType'));
        if (userType !== 'user'){
            navigate.current('/login');
        }
    },[userType])

    return(
        <div className="Account">
            <NavigationBar {...{userType}}/>
            <h1>Account Info</h1>
            <h1>My Recipes</h1>
            <h1>Saved Recipes</h1>
        </div>
    );
}

export default Account;