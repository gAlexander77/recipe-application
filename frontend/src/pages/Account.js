import React, { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import NavigationBar from '../components/NavigationBar';
import '../styles/AccountStyle.css';

import hostname from '../hostname';

function Account() {

    let navigate = useRef(useNavigate());
    const [userType, setUserType] = useState(localStorage.getItem('userType'));

    const [username, setUsername] = useState('username');

    useEffect(()=>{ 
        setUserType(localStorage.getItem('userType'));
        if (userType !== 'user'){
            navigate.current('/login');
        }
    },[userType])

    const [recipes, setRecipes] = useState([])
    /* Test Mock API */
    useEffect(()=>{
        axios.get(hostname+'/recipes').then(res => {
        setRecipes(res.data)
        }).catch(error => alert('API ERROR'));
    }, []);

    const logout = () => {
        localStorage.removeItem('userType');
        localStorage.removeItem('userID');
        localStorage.removeItem('username');
        setUserType(localStorage.getItem('userType'));        
    }

    function AccountRecipeCard({image, name, id}) {
        return (
            <div>
                <div>DELETE</div>
                <img src={image} className="box">
                </img>
                <p>{name} {id}</p>
            </div>
        );
    }

    return(
        <div className="Account">
            <div className="navbar">
                <NavigationBar {...{userType}}/>
            </div>
            
            <div className="account-information">
                <div className="circle">
                </div>
                <h1 className="account-username">{username}</h1>
                <button className="btn" onClick={logout}>Logout</button>
            </div>

            <div className="saved-recipes-container">
                <div className="row-container">
                    <h1 className="row-title">Saved Recipes</h1>
                    <div className="recipe-row">
                        {recipes.map((recipe,index) =>{
                            return(
                                <AccountRecipeCard
                                key = {index}
                                id = {recipe.id}
                                image={recipe.image} 
                                name={recipe.recipe_name} 
                                />
                            );
                        })}
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