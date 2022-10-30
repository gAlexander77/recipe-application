import React, {useState}from 'react';
import { motion } from 'framer-motion';
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
            <motion.div className="rate-recipe-inner"
            initial={{ opacity: 0, y: "300px" }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0 }}
            transition={{ opacity: 0.2, y: 0.3 }}
            >
                <BsXLg className="exit-rate-recipe" onClick={() => props.setTrigger(false)}/>
                <h1>Rate Recipe</h1>
                <div>
                    <button className="number-btn" onClick={()=>setRating(1)}>1</button>
                    <button className="number-btn" onClick={()=>setRating(2)}>2</button>
                    <button className="number-btn" onClick={()=>setRating(3)}>3</button>
                    <button className="number-btn" onClick={()=>setRating(4)}>4</button>
                    <button className="number-btn" onClick={()=>setRating(5)}>5</button>    
                </div>
                <p>{rating}/5 Stars</p>
                <button className="submit-rating-btn" onClick={rateRecipe}>Submit Rating</button>
            </motion.div>
        </div>
    ):"";
}

export default RateRecipe;