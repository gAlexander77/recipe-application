import React from 'react';
import { BsXLg } from "react-icons/bs";

function RateRecipe(props){
    return(props.trigger)?(
        <div className="rate-recipe-popup">
            <div className="rate-recipe-inner">
                <BsXLg className="exit-rate-recipe" onClick={() => props.setTrigger(false)}/>
                <h1>Rate Recipe</h1>
            </div>
        </div>
    ):"";
}

export default RateRecipe;