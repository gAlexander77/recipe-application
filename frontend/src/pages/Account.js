import React, { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import NavigationBar from '../components/NavigationBar';
import '../styles/AccountStyle.css';

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
            <div className="navbar">
                <NavigationBar {...{userType}}/>
            </div>
            <div className="account-information">
                <div className="circle"></div>
                <h1 className="account-username">Username</h1>
                <button className="btn">Settings</button>
            </div>
            <div className="saved-recipes-container">
                <div className="row-container">
                    <h1 className="row-title">Saved Recipes</h1>
                    <div className="recipe-row">
                        <div className="box"></div>
                        <div className="box"></div>
                        <div className="box"></div>
                        <div className="box"></div>
                        <div className="box"></div>
                        <div className="box"></div>
                        <div className="box"></div>
                        <div className="box"></div>
                    </div>
                </div>
            </div>
            <div className="my-recipes-container">
                <div className="row-container">
                    <h1 className="row-title">My Recipes</h1>
                    <div className="recipe-row">
                        <div className="box"></div>
                        <div className="box"></div>
                        <div className="box"></div>
                        <div className="box"></div>
                        <div className="box"></div>
                        <div className="box"></div>
                        <div className="box"></div>
                        <div className="box"></div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Account;