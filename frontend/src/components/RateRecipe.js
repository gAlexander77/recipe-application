import React, {useState}from 'react';
import { BsXLg } from "react-icons/bs";
import '../styles/components/RateRecipeStyle.css';

function RateRecipe(props){
    const [rating, setRating] = useState(0);

    const rateRecipe = () => {
        console.log(rating);
        props.setTrigger(false);
    }

    return(props.trigger)?(
        <div className="rate-recipe-popup">
            <div className="rate-recipe-inner">
                <BsXLg className="exit-rate-recipe" onClick={() => props.setTrigger(false)}/>
                <h1>Rate Recipe</h1>
                <div>
                    <button onClick={()=>setRating(1)}>1</button>
                    <button onClick={()=>setRating(2)}>2</button>
                    <button onClick={()=>setRating(3)}>3</button>
                    <button onClick={()=>setRating(4)}>4</button>
                    <button onClick={()=>setRating(5)}>5</button>
                    <div>{rating}/5 Stars</div>
                </div>
                <button onClick={rateRecipe}>Submit Rating</button>
            </div>
        </div>
    ):"";
}

export default RateRecipe;