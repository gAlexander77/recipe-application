import React, {useEffect} from 'react';
import { useLocation } from "react-router-dom"

function Recipe(){
    const location = useLocation();
    const recipeID = location.state;
    return(
        <div className="Recipe">
            <h1>Image {recipeID}</h1>
            <h1>Recipe Name</h1>
            <h1>Recipe Rating</h1>
            <h1>Recipe Description</h1>
            <h1>Recipe Ingredient</h1>
            <h1>Recipe Directions</h1>
            <button>Download Recipe</button>
            <button>Rate Recipe</button>
        </div>
    );   
}

export default Recipe;