import React, {useEffect, useState, useRef} from 'react';
import { useLocation, useNavigate } from "react-router-dom";
import axios from 'axios';
import NavigationBar from '../components/NavigationBar';
import DisplayStars from '../components/DisplayStars';
import RateRecipe from '../components/RateRecipe';
import '../styles/RecipeStyle.css';

function Recipe(){
    const location = useLocation();
    const recipeID = location.state;

    const [recipe, setRecipe] = useState([])

    const [rateRecipePopUp, setRateRecipePopUp] = useState(false);
    const rateRecipePopUpHandler = () => {
        setRateRecipePopUp(true)
        console.log(rateRecipePopUp)
    }
    
    /* Test Mock API */
    useEffect(()=>{
        axios.get('https://f3fad6f8-6516-4627-a8dd-ac467a4107cf.mock.pstmn.io/recipes/'+recipeID).then(res => {
        setRecipe(res.data)
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
            <div className="recipe-container">
                <img src={recipe.image} className="recipe-imagebox"/>
                <div className="rating-container">
                    <DisplayStars rating={recipe.rating}/>
                    <button onClick={rateRecipePopUpHandler}>Rate Recipe</button>
                </div>
                <div className="info-container">
                    <h1 className="recipe-title">{recipe.recipe_name}</h1>
                    <h1 className="desc-title">Description</h1>
                    <p className="desc-textbox">{recipe.description}</p>
                    <h1 className="ingr-title">Ingredients</h1>
                    <ul className="ingr-list">
                        <li>Ingredient 1</li>
                        <li>Ingredient 2</li>
                        <li>Ingredient 3</li>
                        <li>Ingredient 4</li>
                        <li>Ingredient 5</li>
                    </ul>
                    <h1 className="inst-title">Instructions</h1>
                    <p className="inst-textbox">{recipe.instructions}</p>
                </div>
                <button>Download Recipe</button>
                <button>Save Recipe</button>
            </div>
            <RateRecipe trigger={rateRecipePopUp} setTrigger={setRateRecipePopUp}/>
        </div>
    );   
}

export default Recipe;