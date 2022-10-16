import React, {useEffect, useState, useRef} from 'react';
import { useLocation, useNavigate } from "react-router-dom";
import { ImStarFull, ImStarHalf , ImStarEmpty } from "react-icons/im";
import NavigationBar from '../components/NavigationBar';
import '../styles/RecipeStyle.css';

function Recipe(){
    const location = useLocation();
    const recipeID = location.state;

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
                <div className="recipe-imagebox"><h1>Image {recipeID}</h1></div>
                <div className="rating-container"><ImStarFull/><ImStarFull/><ImStarFull/><ImStarFull/><ImStarFull/></div>
                <div className="info-container">
                    <h1>Recipe Name</h1>
                    <h1>Description</h1>
                    <p className="desc-textbox">{text}</p>
                    <h1>Ingredient</h1>
                    <ul>
                        <li>Ingredient 1</li>
                        <li>Ingredient 2</li>
                        <li>Ingredient 3</li>
                        <li>Ingredient 4</li>
                        <li>Ingredient 5</li>
                    </ul>
                    <h1>Instructions</h1>
                    <p className="inst-textbox">{text}</p>
                </div>
                <button>Download Recipe</button>
                <button>Save Recipe</button>
                <button>Rate Recipe</button>
            </div>
        </div>
    );   
}

export default Recipe;