import React from 'react';
import '../styles/components/RecipeCardStyle.css'

function RecipeCard({image,name,desc,rating}){

    return (
        <div className="RecipeCard">
            <img className="recipe-image" src={image}/>
            <h1 className="recipe-name">{name}</h1>
            <p className="recipe-desc">{desc}</p>
            <div className="recipe-rating">Rating: {rating}</div>
            <button className="view-recipe">View Recipe</button>
        </div>
    );
}

export default RecipeCard;