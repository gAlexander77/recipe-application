import React, {useEffect, useState, useRef} from 'react';
import { useLocation, useNavigate } from "react-router-dom";
import { motion } from 'framer-motion';
import axios from 'axios';
import NavigationBar from '../components/NavigationBar';
import DisplayStars from '../components/DisplayStars';
import RateRecipe from '../components/RateRecipe';
import Comments from '../components/Comments';
import '../styles/RecipeStyle.css';

import hostname from '../hostname';

function Recipe(){
    const location = useLocation();
    const recipeID = location.state;
    console.log("ID:"+recipeID);

    const [recipe, setRecipe] = useState([])
    const [ingredients, setIngredients ] = useState([]);
    
    const [rateRecipePopUp, setRateRecipePopUp] = useState(false);
    const [errorPopUp, setErrorPopUp] = useState(false);
    const rateRecipePopUpHandler = () => {
        if(localStorage.getItem('userType') === 'user')
        {
            setRateRecipePopUp(true);
            console.log(rateRecipePopUp);
        }
        else
        {
            setErrorPopUp(true);
            setTimeout(() =>{setErrorPopUp(false);},7000);
        }
    }


    function ErrorPopUp(){
        if(errorPopUp === true)
        {
            return(
                <div className="rating-error-popup-container">
                    <p className="rating-error-message">You must be logged in to rate this recipe</p>
                </div>
            );
        }
        else
        {
            return('');
        }
    }
    
    useEffect(()=>{
        axios.get(hostname+'/api/recipes/'+recipeID).then(res => {
        setRecipe(res.data.data)
        setIngredients(res.data.data.ingredients)
        }).catch(error => alert('API ERROR'));
    }, []);

    const text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec urna morbi enim in. Elementum quam justo dui, mattis proin sed dui quis. Nec tincidunt sagittis nibh volutpat, et. Scelerisque sit morbi purus fermentum.";

    let navigate = useRef(useNavigate());
    const [userType, setUserType] = useState(localStorage.getItem('userType'));

    useEffect(()=>{ 
        setUserType(localStorage.getItem('userType'));
        console.log(userType)
        if (userType === null){
            navigate.current('/login');
        }
    },[userType]);

    return(
        <div className="Recipe">
            <NavigationBar {...{userType}} className="navbar"/>
            <motion.div className="recipe-container"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            >
                <div className="info-container">
                    <div className="row-1"><ErrorPopUp/>
                    <h1 className="recipe-title">{recipe.name}</h1> 
                    <div className="rating-container">
                        <DisplayStars classname="rating-stars" rating={recipe.rating}/>
                        <button className="rate-recipe-btn" onClick={rateRecipePopUpHandler}>Rate Recipe</button>
                        
                    </div>
                    </div>
                    <img src={hostname+"/"+recipe.image} className="recipe-imagebox"/>                   
                    <h1 className="desc-title">Description</h1>
                    <p className="desc-textbox">{recipe.description}</p>
                    <h1 className="ingr-title">Ingredients</h1>
                    <ul className="ingr-list">
                        {ingredients.map((ingredient, index) =>{
                            return(
                                <li key={index}>{ingredient}</li>
                            );
                        })}
                    </ul>
                    <h1 className="inst-title">Instructions</h1>
                    <p className="inst-textbox">{recipe.instructions}</p>
                </div>
                <Comments recipeID={recipe.id}/>
            </motion.div>
            <RateRecipe recipeID={recipe.id} trigger={rateRecipePopUp} setTrigger={setRateRecipePopUp}/>
        </div>
    );   
}

export default Recipe;