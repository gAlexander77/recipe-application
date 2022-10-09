import React from 'react';
import '../styles/components/RecipeCardStyle.css'

function RecipeCard({image,name,desc,rating}){

    return (
        <div className="RecipeCard">
            <div className="Container">
                <img className="Image" src={image}/>
                <h1>{name}</h1>
                <body>{desc}</body>
                <div>{rating}</div>
                <button className="btn btn-primary">View Recipe</button>
            </div>
        </div>
    );
}

export default RecipeCard;