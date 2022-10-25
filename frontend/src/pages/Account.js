import React, { useEffect, useRef, useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import axios from 'axios';
import { BsXCircle, BsCaretLeftSquareFill, BsCaretRightSquareFill } from "react-icons/bs";
import { TbTrash } from "react-icons/tb";
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

    
    const [isDeleting, setIsDeleting] = useState(false);

    function AccountRecipeCard({image, name, id}) {

        const deleteRecipeHandler = () => {
            setRecipes(recipes.filter(recipe=>recipe.id !== id));
        }

        return (
            <div>
                <BsXCircle className={`${isDeleting ? "delete-recipe-btn ": "hidden"}`} onClick={deleteRecipeHandler}/>
                <BsXCircle className={`${isDeleting ? "hidden": "hide-delete-recipe-btn"}`}/>
                <div className="box-container">
                    <Link to={"/recipe/"+id} state={id} onClick={() => console.log("clicked "+id)}> 
                        <img src={image} className="box"></img>
                    </Link>
                    <p className="my-recipe-name">{name}</p>
                </div>
            </div>
        );
    }

    function MyRecipes() {
        return(
            <div className="my-recipes-container">
                <div className="row-container">
                    <div className="row-header">
                        <h1 className="row-title">My Recipes</h1>
                        <TbTrash className={`${isDeleting ? "trash-icon-active": "trash-icon"}`} onClick={()=> setIsDeleting(!isDeleting)}/>
                    </div>
                    <div className="recipe-row-container">
                        <BsCaretLeftSquareFill className="left-btn" id="slideRight"/>
                        <div className="recipe-row" id="container">    
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
                        <BsCaretRightSquareFill className="right-btn" id="slideLeft"/>
                    </div>    
                </div>
            </div>
        );
    }

    function AccountInfo() {
        return(
            <div className="account-information">
                <div className="circle">
                    <h1 className="letter">{username[0].toUpperCase()}</h1>
                </div>
                <h1 className="account-username">@{username}</h1>
                <button className="logout-btn" onClick={logout}>Logout</button>
            </div>
        );
    }

    return(
        <div className="Account">
            <div className="navbar">
                <NavigationBar {...{userType}}/>
            </div>
            <AccountInfo/>
            <MyRecipes/>
        </div>
    );
}

export default Account;