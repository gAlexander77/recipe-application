import React from 'react';
import { ImStarFull, ImStarHalf , ImStarEmpty } from "react-icons/im";
import '../styles/components/RecipeCardStyle.css'

function RecipeCard({image,name,desc,rating}){

    const Stars = () => {
        if(rating > 4.5)
            return(<div className="star-container"><ImStarFull className="star"/><ImStarFull className="star"/><ImStarFull className="star"/><ImStarFull className="star"/><ImStarFull className="star"/></div>);
        else if(rating > 4.0)
            return(<div className="star-container"><ImStarFull className="star"/><ImStarFull className="star"/><ImStarFull className="star"/><ImStarFull className="star"/><ImStarHalf className="star"/></div>);    
        else if(rating > 3.5)
            return(<div className="star-container"><ImStarFull className="star"/><ImStarFull className="star"/><ImStarFull className="star"/><ImStarFull className="star"/><ImStarEmpty className="star"/></div>);
        else if(rating > 3.0)
            return(<div className="star-container"><ImStarFull className="star"/><ImStarFull className="star"/><ImStarFull className="star"/><ImStarHalf className="star"/><ImStarEmpty className="star"/></div>);
        else if(rating > 2.5)
            return(<div className="star-container"><ImStarFull className="star"/><ImStarFull className="star"/><ImStarFull className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/></div>);
        else if(rating > 2.0)
            return(<div className="star-container"><ImStarFull className="star"/><ImStarFull className="star"/><ImStarHalf className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/></div>);    
        else if(rating > 1.5)
            return(<div className="star-container"><ImStarFull className="star"/><ImStarFull className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/></div>);
        else if(rating > 1.0)
            return(<div className="star-container"><ImStarFull className="star"/><ImStarHalf className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/></div>);    
        else if(rating > 0.5)
            return(<div className="star-container"><ImStarFull className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/></div>);
        else if(rating > 0)
            return(<div className="star-container"><ImStarHalf className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/></div>);    
        else
            return(<div className="star-container"><ImStarEmpty className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/><ImStarEmpty className="star"/></div>);
    }

    return (
        <div className="RecipeCard">
            <img className="recipe-image" src={image}/>
            <h1 className="recipe-name">{name}</h1>
            <p className="recipe-desc">{desc}</p>
            <div className="recipe-rating"> Rating <Stars/> </div>
            <button className="view-recipe">View Recipe</button>
        </div>
    );
}

export default RecipeCard;